"""
Section processor module for ProfileMeister
Handles processing of individual sections
"""

import time
from api_client import cached_generate_content, rate_answer
from html_generator import save_section, load_section, validate_html, repair_html

def process_section_in_parallel(section, documents, persona, analysis_specs, output_format, profile_folder, refinement_iterations=1):
    """Process a single section for parallel execution with HTML output"""
    section_num = section["number"]
    section_title = section["title"]
    section_specs = section["specs"]
    
    # Get elapsed time function from project timing
    try:
        from profile_meister import get_elapsed_time
    except ImportError:
        def get_elapsed_time():
            return f"{time.time():.1f}s"
    
    print(f"\n{get_elapsed_time()} Section {section_num}: GENERATING AND REFINING {section_title}")
    
    # Check if we already have a refined version of this section saved
    existing_refined_content = load_section(profile_folder, f"{section_num}_refined")
    
    if existing_refined_content:
        section_content = existing_refined_content
        print(f"{get_elapsed_time()} Section {section_num}: Loaded previously refined section")
        return section_num, section_content
    
    # Add timeout protection for the overall section processing
    section_start_time = time.time()
    section_timeout = 600  # 10 minutes per section maximum
    
    # Create section-specific instruction with improved HTML guidance
    section_instruction = f"""
    Please create section {section_num}: {section_title} for a company profile.

    Here is the specification for this section:
    {section_specs}

    Focus exclusively on this section. Provide comprehensive and detailed information 
    following the analysis specifications below:

    <analysis_specs>
    {analysis_specs}
    </analysis_specs>

    CRITICAL HTML REQUIREMENTS:
    You MUST follow this exact HTML structure:

    <div class="section" id="section-{section_num}">
      <h2>{section_num}. {section_title}</h2>
      
      <!-- For paragraphs use: -->
      <p>Your paragraph text here</p>
      
      <!-- For lists use: -->
      <ul>
        <li>First item</li>
        <li>Second item</li>
      </ul>
      
      <!-- For tables use this EXACT structure: -->
      <table class="data-table">
        <thead>
          <tr>
            <th>Header 1</th>
            <th>Header 2</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Data 1</td>
            <td>Data 2</td>
          </tr>
        </tbody>
      </table>
      
      <!-- Always end with this closing div tag: -->
    </div>

    IMPORTANT RULES:
    1. NEVER use unclosed or self-closing tags except for <br/> which must include the forward slash.
    2. EVERY opening tag must have a matching closing tag in the correct order.
    3. Tables MUST include both <thead> and <tbody> sections.
    4. All paragraphs must be wrapped in <p> tags.
    5. Think of this as writing code, where syntax must be perfect.
    """
    
    try:
        # Check for timeout
        if time.time() - section_start_time > section_timeout:
            raise TimeoutError(f"Section {section_num} processing exceeded timeout limit of {section_timeout} seconds")
            
        # Generate initial content for this section
        print(f"{get_elapsed_time()} Section {section_num}: Generating initial content")
        # Create a copy of documents for this section
        section_docs = documents.copy()
        prompt = f"{persona} {section_instruction} {output_format}"
        section_docs.append(prompt)
        
        # Import models here to avoid circular imports
        from api_client import create_insight_model, create_fact_model
        insight_model = create_insight_model()
        
        # Generate content with your model - add more detailed error handling
        print(f"{get_elapsed_time()} Section {section_num}: Starting API call for initial content")
        try:
            # Add individual timeout for initial API call
            section_response = cached_generate_content(insight_model, section_docs, section_num, timeout=240)  # Longer timeout for initial generation
            print(f"{get_elapsed_time()} Section {section_num}: API call completed successfully")
            section_content = section_response.text
        except Exception as e:
            print(f"{get_elapsed_time()} Section {section_num}: API call failed: {str(e)}")
            # Create a fallback minimal section
            section_content = f'''
            <div class="section" id="section-{section_num}">
              <h2>{section_num}. {section_title}</h2>
              <p>Error generating content: {str(e)}</p>
              <p>This section could not be automatically generated. Please review the specifications and try again:</p>
              <pre>{section_specs}</pre>
            </div>
            '''
            # Skip further processing
            return section_num, section_content

        # Apply HTML repair right after generation
        print(f"{get_elapsed_time()} Section {section_num}: Repairing HTML")
        section_content = repair_html(section_content, section_num, section_title)
        print(f"{get_elapsed_time()} Section {section_num}: HTML repair completed")
        
        # Add HTML validation
        if not validate_html(section_content):
            print(f"{get_elapsed_time()} Section {section_num}: Warning - Invalid HTML even after repair")
        
        # Check for timeout again
        if time.time() - section_start_time > section_timeout:
            raise TimeoutError(f"Section {section_num} processing exceeded timeout")
        
        print(f"{get_elapsed_time()} Section {section_num}: Initial generation complete")
        
        # Rate the initial content - pass the HTML content for rating
        try:
            print(f"{get_elapsed_time()} Section {section_num}: Rating initial content")
            initial_section_rating = rate_answer(section_instruction, section_content)
            initial_section_rating_percent = initial_section_rating * 100
            print(f"{get_elapsed_time()} Section {section_num}: INITIAL RATING: {initial_section_rating_percent:.0f}%")
        except Exception as e:
            print(f"{get_elapsed_time()} Section {section_num}: Rating failed: {str(e)}")
            initial_section_rating = 0.7  # Default rating if rating fails
            
        # Save the initial content
        save_section(profile_folder, section_num, section_content)
        print(f"{get_elapsed_time()} Section {section_num}: Saved initial section")
        
        # Initialize best tracking with the initial rating
        best_section_score = initial_section_rating
        best_section_content = section_content
        
        # Only proceed with refinement if iterations > 0
        if refinement_iterations > 0:
            print(f"\n{get_elapsed_time()} Section {section_num}: BEGINNING REFINEMENT")
            
            # Import fact critique functions
            from fact_refinement import get_fact_critique, fact_improvement_response
            
            # First, do fact-checking refinement
            try:
                # Check for timeout
                if time.time() - section_start_time > section_timeout:
                    raise TimeoutError(f"Section {section_num} processing exceeded timeout")
                
                print(f"{get_elapsed_time()} Section {section_num}: Performing fact critique")
                fact_critique_response, fact_critique_text = get_fact_critique(section_instruction, section_content)
                
                print(f"{get_elapsed_time()} Section {section_num}: Applying fact improvements")
                fact_improvement_response, fact_improved_content = fact_improvement_response(
                    section_instruction, section_content, fact_critique_text
                )
                
                # Apply HTML repair right after fact improvement
                fact_improved_content = repair_html(fact_improved_content, section_num, section_title)
                
                # Rate the fact-improved content
                fact_improved_rating = rate_answer(section_instruction, fact_improved_content)
                fact_improved_rating_percent = fact_improved_rating * 100
                print(f"{get_elapsed_time()} Section {section_num}: FACT-IMPROVED RATING: {fact_improved_rating_percent:.0f}%")
                
                # Update best content if improved
                if fact_improved_rating > best_section_score:
                    best_section_score = fact_improved_rating
                    best_section_content = fact_improved_content
                    print(f"{get_elapsed_time()} Section {section_num}: Fact improvements increased score")
                
            except Exception as e:
                print(f"{get_elapsed_time()} Section {section_num}: Fact refinement failed: {str(e)}")
                # Continue with best content so far
            
            # Next, do insight refinement
            try:
                # Import insight refinement functions
                from insight_refinement import get_insight_critique, insight_improvement_response
                
                # Check for timeout
                if time.time() - section_start_time > section_timeout:
                    raise TimeoutError(f"Section {section_num} processing exceeded timeout")
                
                print(f"{get_elapsed_time()} Section {section_num}: Performing insight critique")
                insight_critique_response, insight_critique_text = get_insight_critique(section_instruction, best_section_content)
                
                print(f"{get_elapsed_time()} Section {section_num}: Applying insight improvements")
                insight_improvement_response, insight_improved_content = insight_improvement_response(
                    section_instruction, best_section_content, insight_critique_text
                )
                
                # Apply HTML repair right after insight improvement
                insight_improved_content = repair_html(insight_improved_content, section_num, section_title)
                
                # Rate the insight-improved content
                insight_improved_rating = rate_answer(section_instruction, insight_improved_content)
                insight_improved_rating_percent = insight_improved_rating * 100
                print(f"{get_elapsed_time()} Section {section_num}: INSIGHT-IMPROVED RATING: {insight_improved_rating_percent:.0f}%")
                
                # Update best content if improved
                if insight_improved_rating > best_section_score:
                    best_section_score = insight_improved_rating
                    best_section_content = insight_improved_content
                    print(f"{get_elapsed_time()} Section {section_num}: Insight improvements increased score")
                
            except Exception as e:
                print(f"{get_elapsed_time()} Section {section_num}: Insight refinement failed: {str(e)}")
                # Continue with best content so far

        # Ensure best content has proper HTML structure before saving
        best_section_content = repair_html(best_section_content, section_num, section_title)
        
        # Save the final version as a refined section
        save_section(profile_folder, f"{section_num}_refined", best_section_content)
        print(f"{get_elapsed_time()} Section {section_num}: Saved refined section with score: {best_section_score * 100:.0f}%")
        return section_num, best_section_content
        
    except TimeoutError as e:
        # Handle timeout explicitly
        print(f"{get_elapsed_time()} Section {section_num}: TIMEOUT - {str(e)}")
        error_content = f'''
        <div class="section" id="section-{section_num}">
          <h2>{section_num}. {section_title}</h2>
          <p class="error">ERROR: Processing timed out for section {section_num}</p>
          <p>The system took too long to generate this section. Please try again with simplified requirements.</p>
        </div>
        '''
        return section_num, error_content
    except Exception as e:
        # Handle any other exceptions
        print(f"{get_elapsed_time()} Section {section_num}: ERROR - {str(e)}")
        error_content = f'''
        <div class="section" id="section-{section_num}">
          <h2>{section_num}. {section_title}</h2>
          <p class="error">ERROR: Could not generate section {section_num}: {str(e)}</p>
        </div>
        '''
        return section_num, error_content
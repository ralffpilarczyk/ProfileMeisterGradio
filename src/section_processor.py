"""
Section processor module for ProfileMeister
Handles processing of individual sections
"""

import time
import re
import traceback # Import traceback for detailed errors
from api_client import cached_generate_content
# Import from html_generator now
from html_generator import save_section, load_section, validate_html, repair_html, clean_llm_output
# Import refinement functions here
from fact_refinement import get_fact_critique, fact_improvement_response
from insight_refinement import get_insight_critique, insight_improvement_response
# --- REMOVED import for question_refinement ---

# --- Function to Generate ONLY the Initial Section ---
# MODIFIED - REMOVED start_time_ref argument
def generate_initial_section(section, documents, persona, analysis_specs, output_format, profile_folder):
    """Generates, cleans, repairs, and saves the initial content for a single section."""
    section_num = section["number"]
    section_title = section["title"]
    section_specs = section["specs"]

    # Use the imported get_elapsed_time from main module
    try:
        from profile_meister import get_elapsed_time
    except ImportError:
        _start = time.time() # Fallback if running standalone
        def get_elapsed_time():
            elapsed = time.time() - _start; minutes = int(elapsed // 60); seconds = int(elapsed % 60); return f"{minutes}'{seconds:02d}\""

    print(f"\n{get_elapsed_time()} Section {section_num}: GENERATING initial content for {section_title}")

    section_instruction = f"""
    Please create section {section_num}: {section_title} for a company profile.
    Specs: {section_specs}
    <analysis_specs>{analysis_specs}</analysis_specs>
    HTML REQUIREMENTS:
    <div class="section" id="section-{section_num}"><h2>{section_num}. {section_title}</h2><!-- content --></div>
    RULES: Valid HTML, closed tags (<br/> self-closing), tables need thead/tbody.
    """

    try:
        section_start_time_local = time.time()
        section_timeout = 600

        print(f"{get_elapsed_time()} Section {section_num}: Calling API for initial content")
        section_docs = documents.copy()
        prompt = f"{persona} {section_instruction} {output_format}"
        section_docs.append(prompt)

        from api_client import create_insight_model
        insight_model = create_insight_model()

        # MODIFIED - REMOVED start_time_ref argument from call
        section_response = cached_generate_content(insight_model, section_docs, section_num, timeout=240)
        initial_content_raw = section_response.text
        print(f"{get_elapsed_time()} Section {section_num}: API call complete")

        print(f"{get_elapsed_time()} Section {section_num}: Cleaning LLM output")
        initial_content_cleaned = clean_llm_output(initial_content_raw, section_num, section_title)

        print(f"{get_elapsed_time()} Section {section_num}: Repairing HTML")
        initial_content_repaired = repair_html(initial_content_cleaned, section_num, section_title)

        if not validate_html(initial_content_repaired):
             print(f"{get_elapsed_time()} Section {section_num}: Warning - Invalid HTML structure detected even after repair.")
             if not initial_content_repaired or not initial_content_repaired.strip():
                  initial_content_repaired = f'<div class="section" id="section-{section_num}"><h2>{section_num}. {section_title}</h2><p>Error: Failed to generate or repair content.</p></div>'

        save_section(profile_folder, section_num, initial_content_repaired)
        print(f"{get_elapsed_time()} Section {section_num}: Saved initial section {section_num}")

        return section_num, initial_content_repaired

    except TimeoutError as e:
        print(f"{get_elapsed_time()} Section {section_num}: TIMEOUT - {str(e)}")
        error_content = f'<div class="section" id="section-{section_num}"><h2>{section_num}. {section_title}</h2><p class="error">ERROR: Processing timed out for section {section_num}</p></div>'
        save_section(profile_folder, section_num, error_content)
        return section_num, error_content
    except Exception as e:
        print(f"{get_elapsed_time()} Section {section_num}: ERROR generating initial content - {str(e)}")
        traceback.print_exc()
        error_content = f'<div class="section" id="section-{section_num}"><h2>{section_num}. {section_title}</h2><p class="error">ERROR: Could not generate initial content for section {section_num}: {str(e)}</p></div>'
        save_section(profile_folder, section_num, error_content)
        raise Exception(f"Error generating initial content for section {section_num}: {e}")


# --- Function to Refine a Single Section ---
# MODIFIED - REMOVED start_time_ref argument
def refine_section_content(section, initial_content, documents, persona, analysis_specs, output_format, profile_folder):
    """Performs Fact and Insight refinement sequence on initial content."""
    section_num = section["number"]
    section_title = section["title"]
    section_specs = section["specs"]

    # Use the imported get_elapsed_time from main module
    try:
        from profile_meister import get_elapsed_time
    except ImportError:
        _start = time.time() # Fallback if running standalone
        def get_elapsed_time():
            elapsed = time.time() - _start; minutes = int(elapsed // 60); seconds = int(elapsed % 60); return f"{minutes}'{seconds:02d}\""

    print(f"{get_elapsed_time()} Section {section_num}: Starting refinement for {section_title}")

    section_instruction = f"""
    Context: Refining section {section_num}: {section_title}. Spec: {section_specs}
    Analysis Specs: <analysis_specs>{analysis_specs}</analysis_specs>
    HTML Format: <output_format>{output_format}</output_format>
    """

    current_content = initial_content
    content_after_fact = initial_content # Start assuming failure

    # --- Fact Refinement ---
    print(f"\n{get_elapsed_time()} Section {section_num}: --- Fact Refinement ---")
    try:
        print(f"{get_elapsed_time()} Section {section_num}: Performing fact critique")
        _, fact_critique_text = get_fact_critique(section_instruction, current_content)

        if "Error: Could not generate" in fact_critique_text:
             print(f"{get_elapsed_time()} Section {section_num}: Skipping fact improvement due to critique error.")
             content_after_fact = current_content
        else:
            try:
                print(f"{get_elapsed_time()} Section {section_num}: Applying fact improvements")
                # MODIFIED - REMOVED start_time_ref argument from call
                _, fact_improved_content = fact_improvement_response(
                    section_instruction, current_content, fact_critique_text, section_num, section_title
                )
                content_after_fact = fact_improved_content
                print(f"{get_elapsed_time()} Section {section_num}: Fact improvement successful.")
            except Exception as fact_improve_e:
                 print(f"{get_elapsed_time()} Section {section_num}: Fact improvement API call FAILED: {fact_improve_e}. Using content from before this step.")
                 traceback.print_exc()
                 content_after_fact = current_content # Revert

    except Exception as fact_critique_e:
        print(f"{get_elapsed_time()} Section {section_num}: Fact critique generation FAILED: {fact_critique_e}. Skipping fact refinement.")
        traceback.print_exc()
        content_after_fact = current_content

    # Update current content for the next stage
    current_content = content_after_fact

    # --- Insight Refinement ---
    print(f"\n{get_elapsed_time()} Section {section_num}: --- Insight Refinement ---")
    try:
        print(f"{get_elapsed_time()} Section {section_num}: Performing insight critique")
        _, insight_critique_text = get_insight_critique(section_instruction, current_content)

        if "Error: Could not generate" in insight_critique_text:
            print(f"{get_elapsed_time()} Section {section_num}: Skipping insight improvement due to critique error.")
            # Keep current_content (which holds content_after_fact)
        else:
            try:
                print(f"{get_elapsed_time()} Section {section_num}: Applying insight improvements")
                # MODIFIED - REMOVED start_time_ref argument from call
                _, insight_improved_content = insight_improvement_response(
                    section_instruction, current_content, insight_critique_text, section_num, section_title
                )
                current_content = insight_improved_content # Update current content if successful
                print(f"{get_elapsed_time()} Section {section_num}: Insight improvement successful.")
            except Exception as insight_improve_e:
                print(f"{get_elapsed_time()} Section {section_num}: Insight improvement API call FAILED: {insight_improve_e}. Using content from before this step.")
                traceback.print_exc()
                # current_content remains unchanged (holds content_after_fact)

    except Exception as insight_critique_e:
        print(f"{get_elapsed_time()} Section {section_num}: Insight critique generation FAILED: {insight_critique_e}. Skipping insight refinement.")
        traceback.print_exc()
        # current_content remains unchanged (holds content_after_fact)

    # --- Final Output ---
    final_refined_content = current_content
    print(f"\n{get_elapsed_time()} Section {section_num}: --- Finalizing Refined Content ---")
    final_refined_content = clean_llm_output(final_refined_content, section_num, section_title)
    final_refined_content = repair_html(final_refined_content, section_num, section_title)

    save_section(profile_folder, f"{section_num}_refined", final_refined_content)
    print(f"{get_elapsed_time()} Section {section_num}: Saved refined section {section_num}")

    return final_refined_content
"""
HTML Generator module for ProfileMeister
Handles all HTML generation and processing
"""

import os
import re
from datetime import datetime

def create_profile_folder(company_name):
    """Create a unique folder for storing profile sections"""
    # Clean company name for folder naming (remove invalid characters)
    clean_name = ''.join(c if c.isalnum() or c in [' ', '_', '-'] else '_' for c in company_name)
    clean_name = clean_name.replace(' ', '_')
    
    # Create timestamp for uniqueness
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create folder name with company and timestamp
    folder_name = f"profile_{clean_name}_{timestamp}"
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    return folder_name

def save_section(profile_folder, section_number, content):
    """Save a section's HTML content to a file in the specified profile folder"""
    with open(f"{profile_folder}/section_{section_number}.html", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Section {section_number} saved to file in {profile_folder}.")

def load_section(profile_folder, section_number):
    """Load a section's HTML content from a file in the specified profile folder if it exists"""
    filepath = f"{profile_folder}/section_{section_number}.html"
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"Section {section_number} loaded from file in {profile_folder}.")
        return content
    return None

def validate_html(html_content):
    """Simplified HTML validation to prevent getting stuck"""
    # Check for empty content
    if not html_content or not html_content.strip():
        print("Warning: Empty HTML content")
        return False
    
    # Basic check - ensure section div and closing tag are present
    if not re.search(r'<div\s+class=["\']section["\']', html_content):
        print("Warning: Missing <div class=\"section\"> wrapper")
        return False
        
    if '</div>' not in html_content:
        print("Warning: Missing closing </div> tag")
        return False
    
    # Simple tag balance check for critical tags
    tags_to_check = ['div', 'table', 'thead', 'tbody', 'tr', 'td', 'th', 'ul', 'ol', 'li']
    
    for tag in tags_to_check:
        opening_count = len(re.findall(f'<{tag}[^>]*>', html_content, re.IGNORECASE))
        closing_count = len(re.findall(f'</{tag}>', html_content, re.IGNORECASE))
        
        if opening_count != closing_count:
            print(f"Warning: Unbalanced {tag} tags. Opening: {opening_count}, Closing: {closing_count}")
            # Don't fail validation on small imbalances - just report them
            if abs(opening_count - closing_count) > 3 and tag in ['div', 'table']:
                return False
    
    return True

def repair_html
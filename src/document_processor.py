"""
Document processing module for ProfileMeister
Handles document upload and preprocessing
"""

import os
import base64
import tkinter as tk
from tkinter import filedialog

def upload_documents():
    """
    Open a file dialog to select PDF files
    Returns a dictionary of filename: content pairs
    """
    # Create and hide the root window
    root = tk.Tk()
    root.withdraw()
    
    # Open file dialog
    files = filedialog.askopenfilenames(
        title='Select PDF files',
        filetypes=[('PDF files', '*.pdf')]
    )
    
    # Create a dictionary similar to files.upload() return format
    uploaded = {}
    for file_path in files:
        with open(file_path, 'rb') as file:
            filename = os.path.basename(file_path)  # Get just the filename
            uploaded[filename] = file.read()
    
    # Print info about uploaded files
    for fn in uploaded.keys():
        print('User uploaded file "{name}" with length {length} bytes'.format(
            name=fn, length=len(uploaded[fn])))
    
    return uploaded

def load_document_content(uploaded):
    """
    Process uploaded documents and convert to format needed for API
    Returns a list of document dictionaries
    """
    documents = []
    
    for fn in uploaded.keys():
        file_content = uploaded[fn]
        encoded_content = base64.standard_b64encode(file_content).decode("utf-8")

        # Add each document as a dictionary to the documents list
        documents.append({
            'mime_type': 'application/pdf',
            'data': encoded_content
        })
    
    return documents

def extract_text_from_html(html_content):
    """Extract plain text from HTML content"""
    import re
    # Simple HTML tag removal - for more complex HTML, consider using BeautifulSoup
    plain_text = re.sub(r'<[^>]+>', ' ', html_content)
    # Normalize whitespace
    plain_text = re.sub(r'\s+', ' ', plain_text).strip()
    return plain_text
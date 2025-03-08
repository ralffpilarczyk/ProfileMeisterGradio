# ProfileMeister

AI-powered company profile generator that analyzes PDF documents using Google's Gemini API.

## Features
- Analyzes company PDFs to extract key information
- Generates comprehensive company profiles with 20 structured sections
- Creates interactive HTML output with expandable sections

## Setup
1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Add your Google API key to a `.env` file: `GOOGLE_API_KEY=your_key_here`

## Usage
Run from the src directory:

cd src
python profile_meister.py

Then select PDF files when prompted.

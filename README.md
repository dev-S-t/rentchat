# Rental Agreement Assistant Chatbot

A simple Gemini-powered chatbot that assists users with Rental Agreement Complexity questions specific to their region.

## Features

- Answers questions about rental agreements
- Requests region information if not specified
- Provides up-to-date information relevant to the user's location
- Simple command-line interface

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv env
   ```
3. Activate the virtual environment:
   - Windows: `.\env\Scripts\Activate.ps1` (PowerShell) or `.\env\Scripts\activate.bat` (Command Prompt)
   - Linux/Mac: `source env/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Get a Gemini API key from Google AI Studio (https://makersuite.google.com/)
6. Add your API key to the `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the chatbot:
```
python gemini_wrapper.py
```

Commands:
- Type `exit` to quit the application
- Type `reset` to clear the chat history

## Testing

Run the tests:
```
python -m unittest test_wrapper.py
``` 
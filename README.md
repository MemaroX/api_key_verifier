# API Key Verifier

A simple Python tool to verify the validity of Google Gemini API keys by attempting a content generation call.

## Features

- Prompts for API key input.
- Lists available Gemini models for your key.
- Attempts to generate content using `gemini-1.5-flash-latest` to confirm key functionality.
- Provides clear success or failure messages.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MemaroX/api_key_verifier.git
    cd api_key_verifier
    ```

2.  **Install dependencies:**
    ```bash
    pip install .
    ```

## Usage

Run the script and enter your API key when prompted:

```bash
python -m api_key_verifier.main
```

## Security Note

This tool takes the API key as a one-time input and does not store it persistently. For production applications, always manage API keys securely using environment variables or dedicated secret management solutions.

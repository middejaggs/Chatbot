# Chatbot

A simple command-line AI chatbot powered by OpenAI. The program keeps the conversation in memory while it is running, so you can ask follow-up questions naturally.

## Features

- Interactive terminal chat loop
- Conversation context is preserved during the session
- Configurable OpenAI model
- Secure API-key configuration through environment variables
- Clear commands for help and quitting
- Friendly handling of common configuration and API errors

## Requirements

- Python 3.9 or newer
- An OpenAI API key
- Internet access while the chatbot is running

> **Important:** Never commit your real API key to GitHub. Treat it like a password.

## Installation

1. Clone this repository and enter its directory:

   ```bash
   git clone https://github.com/middejaggs/Chatbot.git
   cd Chatbot
   ```

2. Create and activate a virtual environment (recommended):

   **macOS/Linux**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows PowerShell**

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Create a local environment file:

   **macOS/Linux**

   ```bash
   cp .env.example .env
   ```

   **Windows PowerShell**

   ```powershell
   Copy-Item .env.example .env
   ```

5. Open `.env` and replace the placeholder with your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

## Run the chatbot

With the virtual environment activated, run:

```bash
python chatbot.py
```

You can also provide the API key through your shell instead of using `.env`:

```bash
OPENAI_API_KEY="your_api_key_here" python chatbot.py
```

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
python chatbot.py
```

## Chat commands

- `/help` — show available commands
- `/reset` — clear the current conversation and start over
- `/quit` or `/exit` — close the chatbot

Press `Ctrl+C` to stop the program at any time.

## Project structure

```text
.
├── chatbot.py       # Main command-line chatbot
├── requirements.txt # Python dependencies
├── .env.example     # Environment-variable template
├��─ .gitignore       # Files excluded from Git
└── README.md        # Project documentation
```

## Configuration

The following environment variables are supported:

| Variable | Required | Default | Description |
| --- | --- | --- | --- |
| `OPENAI_API_KEY` | Yes | — | Your OpenAI API key |
| `OPENAI_MODEL` | No | `gpt-4o-mini` | Model used for responses |
| `CHATBOT_SYSTEM_PROMPT` | No | Built-in prompt | Instructions that define the assistant's behavior |

## Troubleshooting

### `OPENAI_API_KEY is not set`

Make sure `.env` exists, contains a valid key, and that you are running the command from the project directory. You can also export the key directly in your terminal.

### Authentication or quota errors

Confirm that the API key is correct and that the associated OpenAI account has available API access or quota.

### Module-not-found errors

Activate the virtual environment and install the dependencies again:

```bash
pip install -r requirements.txt
```

## Security

- Keep `.env` private; it is ignored by Git.
- Do not paste API keys into source code.
- If a key is accidentally exposed, revoke it and create a replacement immediately.

## License

No license has been selected for this project yet. Add a license before distributing the code publicly.

"""A small interactive command-line chatbot powered by OpenAI."""

from __future__ import annotations

import os
import sys
from typing import NoReturn

from dotenv import load_dotenv
from openai import APIConnectionError, APIError, AuthenticationError, OpenAI, RateLimitError


DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_SYSTEM_PROMPT = (
    "You are a helpful, clear, and friendly assistant. "
    "If you are unsure about something, say so instead of inventing an answer."
)


def get_required_setting(name: str) -> str:
    """Return a required environment variable or exit with a useful message."""
    value = os.getenv(name, "").strip()
    if not value:
        print(
            f"Error: {name} is not set. Copy .env.example to .env and add your value.",
            file=sys.stderr,
        )
        raise SystemExit(1)
    return value


def print_help() -> None:
    """Print the commands supported by the chat loop."""
    print("Commands: /help, /reset, /quit, /exit")


def create_client() -> OpenAI:
    """Create an OpenAI client using the local environment configuration."""
    return OpenAI(api_key=get_required_setting("OPENAI_API_KEY"))


def ask(client: OpenAI, messages: list[dict[str, str]], model: str) -> str:
    """Send the conversation to OpenAI and return the generated text."""
    response = client.responses.create(model=model, input=messages)
    return response.output_text.strip()


def main() -> NoReturn:
    """Start the interactive chatbot."""
    load_dotenv()
    client = create_client()
    model = os.getenv("OPENAI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    system_prompt = os.getenv("CHATBOT_SYSTEM_PROMPT", DEFAULT_SYSTEM_PROMPT).strip()
    messages: list[dict[str, str]] = [
        {"role": "system", "content": system_prompt}
    ]

    print("Chatbot is ready. Type /help for commands or /quit to exit.")
    print(f"Model: {model}\n")

    while True:
        try:
            user_message = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            raise SystemExit(0)

        if not user_message:
            continue
        if user_message.lower() in {"/quit", "/exit"}:
            print("Goodbye!")
            raise SystemExit(0)
        if user_message.lower() == "/help":
            print_help()
            continue
        if user_message.lower() == "/reset":
            messages = [{"role": "system", "content": system_prompt}]
            print("Conversation reset.\n")
            continue

        messages.append({"role": "user", "content": user_message})
        try:
            answer = ask(client, messages, model)
        except AuthenticationError:
            print("Error: OpenAI rejected the API key. Check OPENAI_API_KEY.\n")
            messages.pop()
            continue
        except RateLimitError:
            print("Error: rate limit or account quota reached. Try again later.\n")
            messages.pop()
            continue
        except APIConnectionError:
            print("Error: could not connect to OpenAI. Check your internet connection.\n")
            messages.pop()
            continue
        except APIError as error:
            print(f"OpenAI API error: {error}\n")
            messages.pop()
            continue

        messages.append({"role": "assistant", "content": answer})
        print(f"Assistant: {answer}\n")


if __name__ == "__main__":
    main()

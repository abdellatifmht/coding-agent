import json
import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function


def main() -> None:
    """
    Entry point for the AI coding agent chatbot application.

    Loads the OpenRouter API key from environment variables, parses
    command-line arguments for the user prompt and verbosity flag,
    and initiates the content generation loop.

    Command-line Arguments:
        user_prompt (str): The user's prompt to send to the AI model.
        --verbose: Optional flag to enable detailed output including
            token usage and function call results.

    Raises:
        RuntimeError: If the OPENROUTER_API_KEY environment variable
            is not set or if the API response is malformed.

    Examples:
        $ python main.py "Write a hello world program"
        Response:
        Here is a hello world program...

        $ python main.py "List files" --verbose
        User prompt: List files
        Prompt tokens: 150
        Response tokens: 200
    """

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables.")


    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(client: OpenAI, messages: list, verbose: bool) -> None:
    """
    Generates content by interacting with the OpenRouter AI model in a loop,
    handling tool calls and accumulating conversation messages.

    Sends messages to the model, processes any tool calls returned by
    the model, appends results to the conversation, and prints the
    final response when no more tool calls are needed.

    Args:
        client: An initialized OpenAI client configured for OpenRouter.
        messages: A list of conversation messages (dicts with role/content).
        verbose: If True, prints detailed token usage and function call results.

    Raises:
        RuntimeError: If the API response is malformed or a function call
            returns no content.
        SystemExit: If the maximum number of iterations (20) is reached
            without a final response.

    Examples:
        >>> generate_content(client, messages, verbose=False)
        Response:
        Here is the answer...
    """

    completed = False
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )
        if not response.usage:
            raise RuntimeError("API response appears to be malformed")

        if verbose:
            print("Prompt tokens:", response.usage.prompt_tokens)
            print("Response tokens:", response.usage.completion_tokens)

        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, verbose)
                if not result_message["content"]:
                    raise RuntimeError("Function call returned no content")
                messages.append(result_message)
                if verbose:
                    print(f"-> {result_message['content']}")
        else:
            print("Response:")
            print(response.choices[0].message.content)
            completed = True
            break

    if not completed:
        print("Error: Maximum number of iterations (20) reached without a final response.")
        exit(1)


if __name__ == "__main__":
    main()

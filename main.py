import argparse
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt


def generate_content(client, messages):
    response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages, # type: ignore
    tools=available_functions,
    )
    return response


load_dotenv()

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
verbose = args.verbose

api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("Not able to get the api key")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
]

max_iterate = 25
for _ in range(max_iterate):
    response = generate_content(client, messages)

    if not response.usage:
            raise RuntimeError("probably a failed API request")

    # if verbose:
    #     print("User prompt:", messages[0]["content"])
    #     print("Prompt tokens:", response.usage.prompt_tokens)
    #     print("Response tokens:", response.usage.completion_tokens)

    message = response.choices[0].message
    messages.append(message)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose)

            if not result_message['content']:
                raise RuntimeError("the result_message has no content property")
            if verbose:
                print(f"-> {result_message['content']}")

            messages.append(result_message)

    else:
        print("Final response:")
        print(response.choices[0].message.content)
        break
else:
    print(f"It seems like the agent couldn't do what was asked in {max_iterate} iterations.")
    sys.exit(1)
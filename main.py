import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI


def generate_content(client, messages):
    response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages # type: ignore
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
        {"role": "user", "content": args.user_prompt},
        {"role": "user", "content": args.user_prompt},
]

response = generate_content(client, messages)

if not response.usage:
        raise RuntimeError("probably a failed API request")
if verbose:
    print("User prompt:", messages[0]["content"])
    print("Prompt tokens:", response.usage.prompt_tokens)
    print("Response tokens:", response.usage.completion_tokens)

print("Response:")
print(response.choices[0].message.content)

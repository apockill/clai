from argparse import ArgumentParser

from .api import initialize_api
from .message_creation import create_message_context


def main() -> None:
    parser = ArgumentParser("CLAI- your own command line AI!")
    parser.add_argument("prompt", type=str, nargs="+")
    parser.add_argument("-m", "--model", default="gpt-3.5-turbo")
    args = parser.parse_args()

    openai = initialize_api()

    prompt = " ".join(args.prompt)
    response = openai.ChatCompletion.create(
        model=args.model,
        messages=create_message_context(prompt),
    )

    best_response = response["choices"][0]["message"]["content"]
    print(best_response)

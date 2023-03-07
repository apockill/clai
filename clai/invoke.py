from argparse import ArgumentParser

from .api import initialize_api
from .behavior_context import MESSAGE_CONTEXT


def invoke() -> None:
    parser = ArgumentParser("CLAI- your own command line AI!")
    parser.add_argument("prompt", type=str, nargs="+")
    parser.add_argument("-e", "--engine", default="")
    args = parser.parse_args()

    openai = initialize_api()

    prompt = " ".join(args.prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[*MESSAGE_CONTEXT, {"role": "user", "content": prompt}],
    )

    best_response = response["choices"][0]["message"]["content"]
    print(best_response.strip())

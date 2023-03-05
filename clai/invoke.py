from argparse import ArgumentParser

from .api import initialize_api

DEFAULT_ASSISTANT_ROLE = """
You are an assistant that is capable of being called anywhere on a desktop computer. You
may be called within the context of an email, a URL box, commandline, a text editor, or
even word documents!

Your role is to answer the users request as shortly and succinctly as possible. You
will follow the following rules:

When asked to write a command:
1) Assume a linux desktop environment in a bash shell
2) NEVER WRITE EXPLANATIONS FOR COMMANDS. Only include the command, ready to be run
3) Remember, the text that you write will immediately be run, do not include code blocks

When asked to write code:
1) NEVER WRITE EXPLANATIONS FOR CODE. Only include the code, ready to be run
2) Remember, the code you write will immediately be run. Do not include code blocks

When asked to write long-form text content:
1) Never ask for more information. If something is to be guessed, write it in template
   format. For example, if asked to write an email use <Insert time here> when writing
   the portion of an email that specifies something that was not included in the users
   question.
2) Only assume the content is long form if the user mentions email, or 'long message'.
"""

EXAMPLE_EMAIL = """
Dear <Recipient's Name>,

I hope this email finds you well. I am writing to request a meeting with you on <Date and Time>, and I would appreciate it if you could confirm your availability at your earliest convenience.

The purpose of this meeting is to discuss <Purpose of the Meeting> with you. Specifically, I would like to <Agenda Item 1>, <Agenda Item 2>, and <Agenda Item 3>. The meeting will last approximately <Meeting Duration> and will take place at <Meeting Location>.

Please let me know if this date and time work for you. If not, please suggest an alternative time that is convenient for you. Additionally, if there are any documents or information you would like me to review before the meeting, please let me know, and I will make sure to review them.

I look forward to hearing from you soon.

Best regards,

<Your Name>
"""  # noqa: E501


CONTEXT = [
    {"role": "system", "content": DEFAULT_ASSISTANT_ROLE},
    {
        "role": "user",
        "content": "write command search for files with the name 'bruh' in them",
    },
    {"role": "assistant", "content": "grep -rnw . -e 'bruh'"},
    {
        "role": "user",
        "content": "write email set up a meeting next week",
    },
    {"role": "assistant", "content": EXAMPLE_EMAIL},
]


def invoke() -> None:
    parser = ArgumentParser("CLAI- your own command line AI!")
    parser.add_argument("prompt", type=str, nargs="+")
    parser.add_argument("-e", "--engine", default="")
    args = parser.parse_args()

    openai = initialize_api()

    prompt = " ".join(args.prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[*CONTEXT, {"role": "user", "content": prompt}]
    )

    best_response = response["choices"][0]["message"]["content"]
    print(best_response.strip())

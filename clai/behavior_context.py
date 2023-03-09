from dataclasses import dataclass
from typing import Literal, Union

from clai.ocr_drivers import WindowContext

USER_PROMPT_FORMAT = """
User Prompt:
```
{user_prompt}
```
"""
OCR_EXTRACTION_FORMAT = """
Active Window Title: {active_window_title}

Active Window OCR Extracted Text (RAW):
------ OCR DATA START ------
```
{ocr_text}
```
------ OCR DATA END ------

{user_prompt}

Please answer "User Prompt" using the raw OCR text as context to the message.
"""


@dataclass
class Prompt:
    context: WindowContext
    prompt: str

    def __str__(self) -> str:
        """Serialize the Prompt with differing formats, depending on whether window
        content was available

        :return: The window context and prompt in a standardized format
        """
        """."""
        user_prompt = USER_PROMPT_FORMAT.format(user_prompt=self.prompt.strip())
        if self.context.clean_screen_text and self.context.active_window_name:
            return OCR_EXTRACTION_FORMAT.format(
                active_window_title=self.context.active_window_name.strip(),
                ocr_text=self.context.clean_screen_text.strip(),
                user_prompt=user_prompt.strip(),
            )
        return user_prompt.strip()


@dataclass
class Message:
    role: Literal["system", "user", "assistant"]
    content: Union[Prompt, str]

    def to_api(self) -> dict[str, str]:
        """To OpenAPI format"""
        if isinstance(self.content, str) and self.role == "user":
            raise RuntimeError("The user message must be of type Prompt!")

        return {"role": self.role, "content": str(self.content)}


_DEFAULT_ASSISTANT_ROLE = """
You are an assistant that is capable of being called anywhere on a desktop computer. You
may be called within the context of an email, a URL box, commandline, a text editor, or
even word documents!

Your role is to answer the users request as shortly and succinctly as possible. You
will follow the following rules:

When asked to write long-form text content:
1) Never ask for more information. If something is to be guessed, write it in template
   format. For example, if asked to write an email use <Insert time here> when writing
   the portion of an email that specifies something that was not included in the users
   question.
2) Only assume the content is long form if the user mentions email, or 'long message'.

When asked to write a command, code, formulas, or any one-line response task:
1) NEVER WRITE EXPLANATIONS! Only include the command/code/etc, ready to be run
2) NEVER WRITE USAGE INSTRUCTIONS! Do not explain how to use the command/code/formulas.
3) NEVER WRITE NOTES ABOUT THE IMPLEMENTATION!
   Do not explain what it does or it's limitations.
4) Remember, the text that you write will immediately be run, do not include code blocks
5) If there is something that requires user input, such as a cell in a sheet or a
   variable from the user, write it inside of brackets, like this: <INPUT DESCRIBER>,
   where the insides of the bracket have an example of what is needed to be filled in.
6) Assume a linux desktop environment in a bash shell. Use freely available unix tools.

You will receive OCR context and window title names, for some prompts. They are very 
noisy, use best-effort when reading them.
"""
_EXAMPLE_EMAIL = """
Dear <Recipient's Name>,

I hope this email finds you well. I am writing to request a meeting with you on <Date and Time>, and I would appreciate it if you could confirm your availability at your earliest convenience.

The purpose of this meeting is to discuss <Purpose of the Meeting> with you. Specifically, I would like to <Agenda Item 1>, <Agenda Item 2>, and <Agenda Item 3>. The meeting will last approximately <Meeting Duration> and will take place at <Meeting Location>.

Please let me know if this date and time work for you. If not, please suggest an alternative time that is convenient for you. Additionally, if there are any documents or information you would like me to review before the meeting, please let me know, and I will make sure to review them.

I look forward to hearing from you soon.

Best regards,

<Your Name>
"""  # noqa: E501
_EXAMPLE_REGEX = '=IFERROR(REGEXEXTRACT(<INPUT CELL HERE>, "[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,4}");"")'  # noqa
_EXAMPLE_PYTHON = """
def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
"""
_EXAMPLE_GOOGLE_SHEETS = '=IFERROR(REGEXEXTRACT(<INPUT CELL HERE>, "[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,4}");"")'  # noqa
_EXAMPLE_BASH_COMMAND = "grep -rnw . -e 'bruh'"

MESSAGE_CONTEXT: list[Message] = [
    Message(role="system", content=_DEFAULT_ASSISTANT_ROLE),
    Message(
        role="user",
        content=Prompt(
            WindowContext(),
            prompt="commandline search for files with the name 'bruh' in them",
        ),
    ),
    Message(role="assistant", content=_EXAMPLE_BASH_COMMAND),
    Message(
        role="user",
        content=Prompt(
            context=WindowContext(), prompt="email set up a meeting next week"
        ),
    ),
    Message(role="assistant", content=_EXAMPLE_EMAIL),
    Message(
        role="user",
        content=Prompt(
            context=WindowContext(),
            prompt="google sheets formula extracts an email from string of text",
        ),
    ),
    Message(role="assistant", content=_EXAMPLE_GOOGLE_SHEETS),
    Message(
        role="user",
        content=Prompt(
            context=WindowContext(),
            prompt="google sheets formula extracts an email from string of text",
        ),
    ),
    Message(role="assistant", content=_EXAMPLE_REGEX),
    Message(
        role="user",
        content=Prompt(
            context=WindowContext(),
            prompt="python fibonacci function in form of a generator",
        ),
    ),
    Message(role="assistant", content=_EXAMPLE_PYTHON),
]

__all__ = ["MESSAGE_CONTEXT", "Message", "Prompt"]

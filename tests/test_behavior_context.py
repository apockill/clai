from clai.behavior_context import MESSAGE_CONTEXT, Message, Prompt
from clai.ocr_drivers import WindowContext

from .ocr_drivers.test_base_driver import _CLEAN_OCR_EXAMPLE, _RAW_OCR_EXAMPLE

_RAW_USER_PROMPT = "  hello I am a user prompt     "
_CLEAN_USER_PROMPT = "hello I am a user prompt"

_RAW_WINDOW_NAME = "  Gnome Terminal\n  "
_CLEAN_WINDOW_NAME = "Gnome Terminal"

EXAMPLE_USER_MESSAGE_NO_CONTEXT = Message(
    role="user", content=Prompt(context=WindowContext(), prompt=_RAW_USER_PROMPT)
)
EXPECTED_USER_MESSAGE_NO_CONTEXT = f"""
User Prompt:
```
{_CLEAN_USER_PROMPT}
```
""".strip()

EXAMPLE_USER_MESSAGE_WITH_CONTEXT = Message(
    role="user",
    content=Prompt(
        context=WindowContext(
            raw_screen_text=_RAW_OCR_EXAMPLE, active_window_name=_RAW_WINDOW_NAME
        ),
        prompt=_RAW_USER_PROMPT,
    ),
)
EXPECTED_USER_MESSAGE_WITH_CONTEXT = f"""
Active Window Title: {_CLEAN_WINDOW_NAME}

Active Window OCR Extracted Text (RAW):
------ OCR DATA START ------
```
{_CLEAN_OCR_EXAMPLE}
```
------ OCR DATA END ------

User Prompt:
```
{_CLEAN_USER_PROMPT}
```

Please answer "User Prompt" using the raw OCR text as context to the message.
"""

EXAMPLE_ASSISTANT_MESSAGE = Message(role="assistant", content="Hey whats up I'm an AI")


def test_no_context_message() -> None:
    expected = {"role": "user", "content": EXPECTED_USER_MESSAGE_NO_CONTEXT}
    assert EXAMPLE_USER_MESSAGE_NO_CONTEXT.to_api() == expected


def test_with_context_message() -> None:
    expected = {"role": "user", "content": EXPECTED_USER_MESSAGE_WITH_CONTEXT}
    assert EXAMPLE_USER_MESSAGE_WITH_CONTEXT.to_api() == expected


def test_assistant_message() -> None:
    expected = {"role": "assistant", "content": "Hey whats up I'm an AI"}
    assert EXAMPLE_ASSISTANT_MESSAGE.to_api() == expected


def test_behavior_context_format() -> None:
    """Validate the MESSAGE_CONTEXT alternates between 'user' and 'assistant', ending
    on 'assistant'"""
    assert MESSAGE_CONTEXT[0].role == "system", "The first role must always be system"

    for i, message in enumerate(MESSAGE_CONTEXT[1:]):
        expected_role = "user" if i % 2 == 0 else "assistant"
        assert message.role == expected_role

        if expected_role == "assistant":
            assert isinstance(message.content, str)
        else:
            assert isinstance(message.content, Prompt)

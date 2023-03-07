from clai.behavior_context import MESSAGE_CONTEXT


def test_behavior_context_format() -> None:
    """Validate the MESSAGE_CONTEXT alternates between 'user' and 'assistant', ending
    on 'assistant'"""
    assert (
        MESSAGE_CONTEXT[0]["role"] == "system"
    ), "The first role must always be system"

    for i, message in enumerate(MESSAGE_CONTEXT[1:]):
        expected_role = "user" if i % 2 == 0 else "assistant"
        assert message["role"] == expected_role

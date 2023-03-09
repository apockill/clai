# flake8: noqa
from clai.ocr_drivers import WindowContext

_RAW_OCR_EXAMPLE = """
test

            test   



iasjaslkdj123
alsklkajd  sadjl 12lkj
        laksjdlk124
"""
_CLEAN_OCR_EXAMPLE = """
iasjaslkdj123
alsklkajd  sadjl 12lkj
laksjdlk124
""".strip()


def test_window_context() -> None:
    """Test the text cleaning functionality of the WindowContext"""
    # Test null case
    context = WindowContext(raw_screen_text=None, active_window_name=None)
    assert context.clean_screen_text is None

    context = WindowContext(raw_screen_text=_RAW_OCR_EXAMPLE)
    assert context.clean_screen_text == _CLEAN_OCR_EXAMPLE

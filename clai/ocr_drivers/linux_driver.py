import pyautogui
import pytesseract
import pywinctl
from PIL.Image import Image

from .base_driver import BaseOCRDriver, WindowContext


class LinuxOCRDriver(BaseOCRDriver):
    def extract_context(self) -> WindowContext:
        screenshot = self._extract_active_window_screenshot()

        # Perform OCR and clean up the text
        raw_ocr_text = pytesseract.image_to_string(screenshot)

        return WindowContext(
            raw_screen_text=raw_ocr_text,
            active_window_name=pywinctl.getActiveWindowTitle(),  # type: ignore
        )

    def _extract_active_window_screenshot(self) -> Image:
        # Get the active window object
        active_window = pywinctl.getActiveWindow()  # type: ignore
        region = (
            active_window.left,
            active_window.top,
            active_window.width,
            active_window.height,
        )

        # Take a screenshot of the active window
        screenshot = pyautogui.screenshot(region=region)
        return screenshot

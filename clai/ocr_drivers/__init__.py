from .base_driver import BaseOCRDriver, WindowContext
from .linux_driver import LinuxOCRDriver


def get_driver() -> BaseOCRDriver:
    """In the future, we can return other OS compatible OCR solutions here"""
    return LinuxOCRDriver()

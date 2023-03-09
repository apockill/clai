from .base_driver import BaseOCRDriver, WindowContext


def get_driver() -> BaseOCRDriver:
    """In the future, we can return other OS compatible OCR solutions here"""
    from .linux_driver import LinuxOCRDriver

    return LinuxOCRDriver()

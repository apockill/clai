from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

_MIN_CHARACTERS_PER_LINE = 10


@dataclass
class WindowContext:
    raw_screen_text: Optional[str] = None
    """If the driver supports it, the text extracted from the active window will be
    filled here."""

    active_window_name: Optional[str] = None
    """If the driver supports it, the current active window name will be filled here."""

    @property
    def clean_screen_text(self) -> Optional[str]:
        if not self.raw_screen_text:
            return None

        lines: list[str] = self.raw_screen_text.split("\n")
        clean_lines = []
        for line in lines:
            line = line.strip()
            if len(line) > _MIN_CHARACTERS_PER_LINE:
                clean_lines.append(line)

        clean_text = "\n".join(clean_lines)
        return clean_text


class BaseOCRDriver(ABC):
    """This base class can be used to standardize the interface for future OS's"""

    @abstractmethod
    def extract_context(self) -> WindowContext:
        """A method to extract the current useful context from the in-focus window"""
        pass

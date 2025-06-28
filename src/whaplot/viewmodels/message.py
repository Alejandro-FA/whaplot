from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass(frozen=True, kw_only=True)
class Message:
    """Message class."""

    author: str
    timestamp: datetime
    content: str
    attachment: Optional[Path] = None

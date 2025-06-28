from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, kw_only=True)
class ApplicationConfig:
    chat_files: list[Path]

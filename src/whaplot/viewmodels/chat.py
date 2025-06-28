from dataclasses import dataclass
from typing import Optional
from whaplot.viewmodels.message import Message


@dataclass(frozen=True, kw_only=True)
class Chat:
    """Chat class."""

    name: Optional[str] = None
    messages: list[Message]

    def participants(self) -> set[str]:
        """Return the set of participants of the chat."""
        return {message.author for message in self.messages}

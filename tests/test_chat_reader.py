import pathlib
from whaplot.io.chat_reader import ChatReader
from whaplot.viewmodels.chat import Chat
from whaplot.viewmodels.message import Message
import pytest
from datetime import datetime

class TestChatReader:
    @pytest.fixture
    def chat(self) -> pathlib.Path:
        return pathlib.Path(__file__).parent / "resources" / "chat.txt"

    def __expected_output(self) -> Chat:
        return Chat(
            messages=[
                Message(
                    author="Hogwarts class ✨",
                    timestamp=datetime(2025, 30, 1, 16, 55, 39),
                    content="Messages and calls are end-to-end encrypted. Only people in this chat can read, listen to, or share them.",
                ),
                Message(
                    author="Harry Potter",
                    timestamp=datetime(2025, 30, 1, 16, 55, 39),
                    content="Harry Potter created this group",
                ),
                Message(
                    author="Hogwarts class ✨",
                    timestamp=datetime(2025, 30, 1, 16, 55, 41),
                    content="Harry Potter added you",
                ),
                Message(
                    author="Harry Potter",
                    timestamp=datetime(2025, 30, 1, 16, 58, 26),
                    content="",
                    attachment=pathlib.Path("00001317-AUDIO-2025-30-01-00-00-00.opus"),
                ),
                Message(
                    author="Harry Potter",
                    timestamp=datetime(2025, 30, 1, 17, 1, 55),
                    content=(
                        "I want to share a link with you:\n\n\n"
                        "How to pet a dragon: https://www.example.com/"
                    ),
                ),
                Message(
                    author="Hermione 🧙‍♀️",
                    timestamp=datetime(2025, 30, 1, 17, 5, 4),
                    content="Hi 😋",
                ),
                Message(
                    author="Hermione 🧙‍♀️",
                    timestamp=datetime(2025, 30, 1, 17, 44, 11),
                    content="",
                    attachment=pathlib.Path("00000000-STICKER-2025-30-01-00-00-00.webp"),
                ),
                Message(
                    author="Ron :)",
                    timestamp=datetime(2025, 30, 1, 18, 25, 21),
                    content="When do you want to meet to study?",
                    attachment=pathlib.Path("00001383-A_guide_to_dragons.pdf"),
                ),
                Message(
                    author="Ron :)",
                    timestamp=datetime(2025, 30, 1, 19, 51, 37),
                    content=(
                        "*Study date*\n"
                        "Ron: Tomorrow morning\n"
                    ),
                ),
            ]
        )

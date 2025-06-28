from pathlib import Path
from datetime import datetime
from whaplot.viewmodels.chat import Chat
import logging


class ChatReader:
    __FALLBACK_DATETIME_FORMAT = "%x, %X"
    __UNICODE_LEFT_TO_RIGHT_MARK = "\u200e"
    __LOGGER = logging.getLogger()

    def __init__(self, datetime_format: str = __FALLBACK_DATETIME_FORMAT) -> None:
        self.__datetime_format: str = datetime_format

    def read(self, chat_file: Path) -> Chat:
        extension: str = chat_file.suffix
        if extension == ".txt":
            return self.__from_txt(chat_file)
        if extension == ".zip":
            return self.__from_zip(chat_file)
        raise ValueError(f"Unsupported file format: {extension}")

    def __from_txt(self, chat_file: Path) -> Chat:
        with chat_file.open() as file:
            lines = file.readlines()
            raise NotImplementedError("from_txt method not implemented")

    def __from_zip(self, chat_file: Path) -> Chat:
        raise NotImplementedError("from_zip method not implemented")

    def __parse_timestamp(self, timestamp: str) -> datetime:
        try:
            return datetime.strptime(timestamp, self.__datetime_format)
        except ValueError:
            ChatReader.__LOGGER.warning(
                f"Could not parse timestamp with format '{self.__datetime_format}': {timestamp}"
            )
            try:
                return datetime.strptime(timestamp, ChatReader.__FALLBACK_DATETIME_FORMAT)
            except ValueError as e:
                ChatReader.__LOGGER.error(
                    "Could not parse timestamp with fallback format "
                    f"'{ChatReader.__FALLBACK_DATETIME_FORMAT}': {timestamp}"
                )
                raise ValueError(f"Could not parse timestamp: {timestamp}") from e

    @staticmethod
    def __remove_left_to_right_mark(text: str) -> str:
        return text.replace(ChatReader.__UNICODE_LEFT_TO_RIGHT_MARK, "")

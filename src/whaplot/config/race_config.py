from dataclasses import dataclass
from enum import Enum

from whaplot.config.application_config import ApplicationConfig


class RaceMetric(Enum):
    MESSAGE_COUNT = ("messages",)
    CHARACTER_COUNT = ("characters",)
    WORD_COUNT = ("words",)


@dataclass(frozen=True, kw_only=True)
class RaceConfig(ApplicationConfig):
    metric: RaceMetric

import enum
import random
from dataclasses import dataclass

from .read_csv import read_csv


@dataclass
class Career:
    career: str
    career_type: str
    workplace: str
    pack: str


_CAREERS: list[Career] = []


def load() -> None:
    filename = "careers.csv"
    for row in read_csv(filename):
        _CAREERS.append(Career(**row))


def pick(nr_choices: int) -> list[str]:
    """Pick a number of traits."""
    choices = random.choices(_CAREERS, k=nr_choices)
    return list(t.career for t in choices)

import enum
import random
from dataclasses import dataclass

from .read_csv import read_csv


@dataclass
class Aspiration:
    aspiration: str
    pack: str


_ASPIRATIONS: list[Aspiration] = []


def load() -> None:
    filename = "aspirations.csv"
    for row in read_csv(filename):
        _ASPIRATIONS.append(Aspiration(**row))


def pick(nr_choices: int) -> list[str]:
    """Pick a number of traits."""
    choices = random.choices(_ASPIRATIONS, k=nr_choices)
    return list(t.aspiration for t in choices)

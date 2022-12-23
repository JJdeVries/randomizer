import enum
import random
from dataclasses import dataclass

from .read_csv import read_csv


@dataclass
class Death:
    death: str
    pack: str


_DEATHS: list[Death] = []


def load() -> None:
    filename = "deaths.csv"
    for row in read_csv(filename):
        _DEATHS.append(Death(**row))


def pick(nr_choices: int) -> list[str]:
    """Pick a number of deaths."""
    choices = random.choices(_DEATHS, k=nr_choices)
    return list(t.death for t in choices)

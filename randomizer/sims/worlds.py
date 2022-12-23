import enum
import random
from dataclasses import dataclass

from .read_csv import read_csv


@dataclass
class World:
    neighbourhood: str
    residential_lot: str
    world: str
    pack: str


_WORLDS: list[World] = []


def load() -> None:
    filename = "worlds.csv"
    for row in read_csv(filename):
        _WORLDS.append(World(**row))


def pick(nr_choices: int) -> list[str]:
    """Pick a number of worlds."""
    choices = random.choices(_WORLDS, k=nr_choices)
    return list(t.world for t in choices)

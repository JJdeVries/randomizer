import enum
import random
from dataclasses import dataclass

from .read_csv import read_csv


@dataclass
class Trait:
    trait: str
    trait_type: str
    pack: str


_TRAITS: list[Trait] = []


def load() -> None:
    filename = "traits.csv"
    for row in read_csv(filename):
        _TRAITS.append(Trait(**row))


def pick(nr_choices: int) -> list[str]:
    """Pick a number of traits."""
    choices = random.choices(_TRAITS, k=nr_choices)
    return list(t.trait for t in choices)

import enum
import random
from dataclasses import dataclass

from .read_csv import read_csv


@dataclass
class Skill:
    skill: str
    skill_type: str
    pack: str


_SKILLS: list[Skill] = []


def load() -> None:
    filename = "skills.csv"
    for row in read_csv(filename):
        _SKILLS.append(Skill(**row))


def pick(nr_choices: int) -> list[str]:
    """Pick a number of traits."""
    choices = random.choices(_SKILLS, k=nr_choices)
    return list(t.skill for t in choices)

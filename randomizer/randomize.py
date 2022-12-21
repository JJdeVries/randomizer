from pathlib import Path
import random

_OPTIONS: dict[str, list[str]] = {"careers": [], "skills": [], "aspirations": []}


def initialize():
    global _OPTIONS
    files = {"skills": "skills.txt"}

    for output, filename in files.items():
        with open(Path(__file__).parent.resolve() / filename) as f:
            _OPTIONS[output] = f.readlines()


def __pick(options: list[str]) -> str:
    if not options:
        return ""

    randint = random.randint(0, len(options) - 1)
    return options[randint].strip()


def get_skill() -> str:
    return __pick(_OPTIONS["skills"])


def get_aspiration() -> str:
    return __pick(_OPTIONS["aspirations"])


def get_career() -> str:
    return __pick(_OPTIONS["careers"])

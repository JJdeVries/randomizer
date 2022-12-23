import enum
import random
from pathlib import Path


class Types(str, enum.Enum):
    Trait = "trait"
    Career = "career"
    Aspiration = "aspiration"
    Skill = "skill"


_OPTIONS: dict[Types, list[str]] = {
    Types.Trait: [],
    Types.Career: [],
    Types.Aspiration: [],
    Types.Skill: [],
}


def initialize():
    global _OPTIONS
    files = {
        Types.Skill: "skills.txt",
        Types.Trait: "traits.txt",
        Types.Career: "careers.txt",
        Types.Aspiration: "aspirations.txt",
    }

    for output, filename in files.items():
        with open(Path(__file__).parent.resolve() / filename) as f:
            _OPTIONS[output] = f.readlines()


def __pick(options: list[str]) -> str:
    if not options:
        return ""

    randint = random.randint(0, len(options) - 1)
    return options[randint].strip()


def get(random_type: Types) -> str:
    return __pick(_OPTIONS[random_type])

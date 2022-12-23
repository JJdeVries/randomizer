from . import aspirations, careers, deaths, skills, traits
from .types import Types

__all__ = ["Types", "traits", "careers"]


def initialize() -> None:
    traits.load()
    careers.load()
    aspirations.load()
    skills.load()
    deaths.load()


def pick(sims_type: Types, nr_choices: int) -> list[str]:
    if sims_type is Types.Trait:
        return traits.pick(nr_choices)
    if sims_type is Types.Career:
        return careers.pick(nr_choices)
    if sims_type is Types.Aspiration:
        return aspirations.pick(nr_choices)
    if sims_type is Types.Skill:
        return skills.pick(nr_choices)
    if sims_type is Types.Death:
        return deaths.pick(nr_choices)
    return [""]

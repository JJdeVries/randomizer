""" The module with all the specified ids used for the Dash application."""
import enum


class _BaseDashId(str, enum.Enum):
    pass


@enum.unique
class GenerateId(_BaseDashId):
    """The ids for scraping data."""

    Generate = "-generate-"

    OutputButton = "-output-button-"
    OutputTooltip = "-output-tooltip-"

    TraitOutput = "-trait-output-"
    TraitDropdown = "-trait-dropdown-"

    CareerOutput = "-career-output-"
    CareerDropdown = "-career-dropdown-"

    AspirationOutput = "-aspiration-output-"
    AspirationDropdown = "-aspiration-dropdown-"

    SkillOutput = "-skill-output-"
    SkillDropdown = "-skill-dropdown-"

    DeathOutput = "-death-output-"
    DeathCheck = "-death-checkbox-"

    WorldOutput = "-world-output-"
    WorldCheck = "-world-checkbox-"

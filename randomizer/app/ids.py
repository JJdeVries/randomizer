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

    TraitsOutput = "-traits-output-"
    TraitsDropdown = "-traits-dropdown-"

    CareersOutput = "-careers-output-"
    CareersDropdown = "-careers-dropdown-"

    AspirationsOutput = "-aspirations-output-"
    AspirationsDropdown = "-aspirations-dropdown-"

    SkillsOutput = "-skills-output-"
    SkillsDropdown = "-skills-dropdown-"

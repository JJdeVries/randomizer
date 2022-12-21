""" The module with all the specified ids used for the Dash application."""
import enum


class _BaseDashId(str, enum.Enum):
    pass


@enum.unique
class GenerateId(_BaseDashId):
    """The ids for scraping data."""

    Generate = "-generate-"

    TraitsOutput = "-traits-output-"
    TraitsDropdown = "-traits-dropdown-"
    TraitsOutputButton = "-traits-output-button-"

    AspirationsOutput = "-aspirations-output-"
    AspirationsDropdown = "-aspirations-dropdown-"

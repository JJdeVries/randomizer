import dash
import dash_bootstrap_components as dbc
from randomizer import randomize

from .. import ids

_BUTTON_COUNTER = 0


def _generate_button(random_type: randomize.Types) -> dbc.Col:
    global _BUTTON_COUNTER

    new_id = {
        "id": ids.GenerateId.OutputButton,
        "index": _BUTTON_COUNTER,
        "type": random_type,
    }
    button_text = randomize.get(random_type)

    new_col = dbc.Col(
        [
            dash.html.Div(
                [
                    dbc.Button(
                        id=new_id, children=button_text, outline=True, color="secondary"
                    ),
                    dbc.Tooltip(
                        children=button_text,
                        id={
                            "id": ids.GenerateId.OutputTooltip,
                            "index": _BUTTON_COUNTER,
                        },
                        target=new_id,
                        placement="bottom",
                    ),
                ],
                className="d-grid",
            )
        ]
    )

    _BUTTON_COUNTER += 1
    return new_col


def _generate(nr: int, random_type: randomize.Types) -> list[dbc.Col]:
    ret_val = []
    for _ in range(nr):
        ret_val.append(_generate_button(random_type))
    return ret_val


@dash.callback(
    dash.Output(ids.GenerateId.TraitsOutput, "children"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
    dash.State(ids.GenerateId.TraitsDropdown, "value"),
)
def generate_traits(_generate_clicks: int, nr_values_str: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    return _generate(nr_values, randomize.Types.Trait)


@dash.callback(
    dash.Output(ids.GenerateId.CareersOutput, "children"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
    dash.State(ids.GenerateId.CareersDropdown, "value"),
)
def generate_careers(_generate_clicks: int, nr_values_str: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    return _generate(nr_values, randomize.Types.Career)


@dash.callback(
    dash.Output(ids.GenerateId.AspirationsOutput, "children"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
    dash.State(ids.GenerateId.AspirationsDropdown, "value"),
)
def generate_aspirations(_generate_clicks: int, nr_values_str: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    return _generate(nr_values, randomize.Types.Aspiration)


@dash.callback(
    dash.Output(ids.GenerateId.SkillsOutput, "children"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
    dash.State(ids.GenerateId.SkillsDropdown, "value"),
)
def generate_skills(_generate_clicks: int, nr_values_str: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    return _generate(nr_values, randomize.Types.Skill)

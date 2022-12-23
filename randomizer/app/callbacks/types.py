import dash
import dash_bootstrap_components as dbc
from randomizer import randomize, sims

from .. import ids

_BUTTON_COUNTER = 0


def _generate_button(button_text: str, random_type: sims.Types) -> dbc.Col:
    global _BUTTON_COUNTER

    new_id = {
        "id": ids.GenerateId.OutputButton,
        "index": _BUTTON_COUNTER,
        "type": random_type,
    }

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


@dash.callback(
    dash.Output(ids.GenerateId.TraitOutput, "children"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
    dash.State(ids.GenerateId.TraitDropdown, "value"),
)
def generate_traits(_generate_clicks: int, nr_values_str: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    ret_list = []
    for i in sims.pick(sims.Types.Trait, nr_values):
        ret_list.append(_generate_button(i, sims.Types.Trait))
    return ret_list


@dash.callback(
    dash.Output(ids.GenerateId.CareerOutput, "children"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
    dash.State(ids.GenerateId.CareerDropdown, "value"),
)
def generate_careers(_generate_clicks: int, nr_values_str: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    ret_list = []
    for i in sims.pick(sims.Types.Career, nr_values):
        ret_list.append(_generate_button(i, sims.Types.Career))
    return ret_list


@dash.callback(
    dash.Output(ids.GenerateId.AspirationOutput, "children"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
    dash.State(ids.GenerateId.AspirationDropdown, "value"),
)
def generate_aspirations(_generate_clicks: int, nr_values_str: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    ret_list = []
    for i in sims.pick(sims.Types.Aspiration, nr_values):
        ret_list.append(_generate_button(i, sims.Types.Aspiration))
    return ret_list


@dash.callback(
    dash.Output(ids.GenerateId.SkillOutput, "children"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
    dash.State(ids.GenerateId.SkillDropdown, "value"),
)
def generate_skills(_generate_clicks: int, nr_values_str: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    ret_list = []
    for i in sims.pick(sims.Types.Skill, nr_values):
        ret_list.append(_generate_button(i, sims.Types.Skill))
    return ret_list


@dash.callback(
    dash.Output(ids.GenerateId.DeathOutput, "children"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
    dash.State(ids.GenerateId.DeathCheck, "value"),
)
def generate_deaths(_generate_clicks: int, nr_values_str: str) -> list[dbc.Col]:
    ret_list = []
    for i in sims.pick(sims.Types.Skill, 1):
        ret_list.append(_generate_button(i, sims.Types.Death))
    return ret_list

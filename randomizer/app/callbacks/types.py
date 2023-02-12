import dash
import dash_bootstrap_components as dbc
from randomizer import randomize, sims

from .. import ids

_BUTTON_COUNTER = 0


def _generate_button(
    button_text: str, random_type: sims.Types, disabled=False
) -> dbc.Col:
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
                        id=new_id,
                        children=button_text,
                        outline=True,
                        color="secondary",
                        disabled=disabled,
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
    dash.Input(ids.GenerateId.TraitDropdown, "value"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
)
def generate_traits(nr_values_str: str, _n_clicks: int) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    ret_list = []
    for i in sims.pick(sims.Types.Trait, nr_values):
        ret_list.append(_generate_button(i, sims.Types.Trait))
    return ret_list


@dash.callback(
    dash.Output(ids.GenerateId.CareerOutput, "children"),
    dash.Input(ids.GenerateId.CareerDropdown, "value"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
)
def generate_careers(nr_values_str: str, _n_clicks: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    ret_list = []
    for i in sims.pick(sims.Types.Career, nr_values):
        ret_list.append(_generate_button(i, sims.Types.Career))
    return ret_list


@dash.callback(
    dash.Output(ids.GenerateId.AspirationOutput, "children"),
    dash.Input(ids.GenerateId.AspirationDropdown, "value"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
)
def generate_aspirations(nr_values_str: str, _n_clicks: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    ret_list = []
    for i in sims.pick(sims.Types.Aspiration, nr_values):
        ret_list.append(_generate_button(i, sims.Types.Aspiration))
    return ret_list


@dash.callback(
    dash.Output(ids.GenerateId.SkillOutput, "children"),
    dash.Input(ids.GenerateId.SkillDropdown, "value"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
)
def generate_skills(nr_values_str: str, _n_clicks: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)
    ret_list = []
    for i in sims.pick(sims.Types.Skill, nr_values):
        ret_list.append(_generate_button(i, sims.Types.Skill))
    return ret_list


@dash.callback(
    dash.Output(ids.GenerateId.DeathOutput, "children"),
    dash.Input(ids.GenerateId.DeathCheck, "value"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
)
def generate_deaths(enabled: bool, _n_clicks: str) -> list[dbc.Col]:
    if not enabled:
        return [_generate_button("--", sims.Types.Death, True)]
    return [_generate_button(sims.pick(sims.Types.Death, 1)[0], sims.Types.Death)]


@dash.callback(
    dash.Output(ids.GenerateId.WorldOutput, "children"),
    dash.Input(ids.GenerateId.WorldCheck, "value"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
)
def generate_deaths(enabled: bool, _n_clicks: str) -> list[dbc.Col]:
    if not enabled:
        return [_generate_button("--", sims.Types.World, True)]
    return [_generate_button(sims.pick(sims.Types.World, 1)[0], sims.Types.World)]

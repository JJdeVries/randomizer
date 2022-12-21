import dash
import dash_bootstrap_components as dbc

from . import ids
from randomizer import randomize

_COUNTERS = {"traits": 0}


@dash.callback(
    dash.Output(ids.GenerateId.TraitsOutput, "children"),
    dash.Input(ids.GenerateId.Generate, "n_clicks"),
    dash.State(ids.GenerateId.TraitsDropdown, "value"),
)
def _generate_traits(_generate_clicks: int, nr_values_str: str) -> list[dbc.Col]:
    nr_values = int(nr_values_str)

    ret_val = []
    for i in range(nr_values):
        skill = randomize.get_skill()

        ret_val.append(
            dbc.Col(
                [
                    dash.html.Div(
                        [
                            dbc.Button(
                                id={
                                    "type": ids.GenerateId.TraitsOutputButton,
                                    "index": _COUNTERS["traits"],
                                },
                                children=skill,
                                outline=True,
                                color="primary",
                            ),
                            dbc.Tooltip(
                                skill,
                                target=f"-skill-output-{skill}-{i}-",
                                placement="bottom",
                            ),
                        ],
                        className="d-grid",
                    )
                ]
            )
        )

        _COUNTERS["traits"] += 1

    return ret_val


@dash.callback(
    dash.Output(
        {"type": ids.GenerateId.TraitsOutputButton, "index": dash.MATCH}, "children"
    ),
    dash.Input(
        {"type": ids.GenerateId.TraitsOutputButton, "index": dash.MATCH}, "n_clicks"
    ),
    dash.State(
        {"type": ids.GenerateId.TraitsOutputButton, "index": dash.MATCH}, "children"
    ),
)
def _generate_new_trait(_n_clicks: int, current):
    # Let's maximize 10 tries to avoid deadlocks
    for _ in range(10):
        new_skill = randomize.get_skill()
        if new_skill != current:
            break
    return new_skill

from typing import Any

import dash
from randomizer import randomize, sims

from .. import ids


@dash.callback(
    dash.Output(
        {"id": ids.GenerateId.OutputButton, "index": dash.MATCH, "type": dash.MATCH},
        "children",
    ),
    dash.Input(
        {"id": ids.GenerateId.OutputButton, "index": dash.MATCH, "type": dash.MATCH},
        "n_clicks",
    ),
    dash.State(
        {"id": ids.GenerateId.OutputButton, "index": dash.ALL, "type": dash.MATCH},
        "children",
    ),
)
def generate_new(
    _btn_n_clicks: int, all_vals: list[str]
) -> str | dash._callback.NoUpdate:
    # Let's maximize 10 tries to avoid deadlocks
    if not dash.callback_context.triggered_id:
        return dash.no_update

    picking = ""
    for _ in range(10):
        picking = sims.pick(sims.Types(dash.callback_context.triggered_id["type"]), 1)[
            0
        ]
        if picking not in all_vals:
            break
    return picking


@dash.callback(
    dash.Output({"id": ids.GenerateId.OutputTooltip, "index": dash.MATCH}, "children"),
    dash.Input({"id": ids.GenerateId.OutputButton, "index": dash.MATCH}, "children"),
)
def update_tooltip(new_tooltip: str) -> str:
    return new_tooltip

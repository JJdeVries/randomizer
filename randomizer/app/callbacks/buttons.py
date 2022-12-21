import dash
from randomizer import randomize

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
        {"id": ids.GenerateId.OutputButton, "index": dash.MATCH, "type": dash.MATCH},
        "children",
    ),
)
def generate_new(n_clicks: int, current):
    # Let's maximize 10 tries to avoid deadlocks
    if not n_clicks or not dash.callback_context.triggered_id:
        return current

    new_value = ""
    for _ in range(10):
        new_value = randomize.get(dash.callback_context.triggered_id["type"])
        if new_value != current:
            break
    return new_value


@dash.callback(
    dash.Output({"id": ids.GenerateId.OutputTooltip, "index": dash.MATCH}, "children"),
    dash.Input({"id": ids.GenerateId.OutputButton, "index": dash.MATCH}, "children"),
)
def update_tooltip(new_tooltip: str):
    return new_tooltip

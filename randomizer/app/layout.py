"""Dash app callbacks for the index/home page."""
import dash_bootstrap_components as dbc
from dash import dcc, html

from .ids import GenerateId

_TYPES = ["traits", "aspirations"]


def _get_dropdown_id(gen_type: str) -> GenerateId:
    dropid = f"-{gen_type}-dropdown-"
    return GenerateId(dropid)


def _get_output_id(gen_type: str) -> GenerateId:
    dropid = f"-{gen_type}-output-"
    return GenerateId(dropid)


def _get_new_row(row_type: str) -> dbc.Row:
    return dbc.Row(
        [
            dbc.Col(
                [
                    dcc.Dropdown(
                        options=[str(i) for i in range(1, 10)],
                        value="1",
                        id=_get_dropdown_id(row_type),
                        clearable=False,
                    )
                ],
                width=1,
            ),
            dbc.Col(
                [html.B(row_type.capitalize())], width=2, style={"textAlign": "center"}
            ),
            dbc.Col(
                [
                    dbc.Container(
                        [
                            dbc.Row(
                                children=[
                                    dbc.Col(
                                        dbc.Input(
                                            readonly=True, placeholder="", type="text"
                                        ),
                                    ),
                                ],
                                id=_get_output_id(row_type),
                            )
                        ],
                        fluid=True,
                    )
                ]
            ),
        ],
        align="center",
        className="mb-3",
    )


def get_layout() -> html.Div:
    """Get the layout of the stockwatch dash application."""
    return html.Div(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Container(
                [
                    dbc.Row(
                        dbc.Col(
                            [
                                dbc.Button(
                                    "GENERATE",
                                    GenerateId.Generate,
                                    size="lg",
                                    style={
                                        "height": "3em",
                                        "color": "white",
                                        "fontSize": "45px",
                                        "backgroundColor": "#4b7a34",
                                    },
                                )
                            ],
                            class_name="d-grid gap-2",
                        )
                    ),
                    dbc.Row(
                        dbc.Col(
                            [
                                dbc.Container(
                                    [_get_new_row(i) for i in _TYPES]
                                    + [
                                        dbc.Row(dbc.Col(html.Br())),
                                        dbc.Row(dbc.Col(html.Br())),
                                    ],
                                    style={"margin": "1.5em"},
                                    fluid=True,
                                ),
                            ]
                        ),
                    ),
                ],
                style={"backgroundColor": "white"},
                className="g-0",
            ),
        ],
    )

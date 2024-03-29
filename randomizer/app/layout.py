"""Dash app callbacks for the index/home page."""
import dash_bootstrap_components as dbc
from dash import dcc, html
from randomizer.sims import Types

from .ids import GenerateId


def _get_dropdown_id(gen_type: Types) -> GenerateId:
    dropid = f"-{gen_type.value}-dropdown-"
    return GenerateId(dropid)


def _get_output_id(gen_type: Types) -> GenerateId:
    dropid = f"-{gen_type.value}-output-"
    return GenerateId(dropid)


def _get_checkbox_id(gen_type: Types) -> GenerateId:
    dropid = f"-{gen_type.value}-checkbox-"
    return GenerateId(dropid)


def _get_dropdown(row_type: Types) -> dcc.Dropdown:
    return dcc.Dropdown(
        options=[str(i) for i in range(1, 10)],
        value="1",
        id=_get_dropdown_id(row_type),
        clearable=False,
    )


def _get_checkbox(row_type: Types) -> dbc.Checklist:
    return dbc.Checklist(
        id=_get_checkbox_id(row_type),
        value=[1],
        options=[
            {
                "label": "",
                "value": 1,
            }
        ],
        input_checked_style={
            "backgroundColor": "var(--bs-tertiary)",
            "borderColor": "var(--bs-tertiary)",
        },
        style={"float": "right", "boxShadow": "0 0 0 .25rem var(--bs-gray-200);"},
    )


def _get_new_row(row_type: Types, add_dropdown: bool) -> dbc.Row:
    return dbc.Row(
        [
            dbc.Col(
                [
                    _get_dropdown(row_type)
                    if add_dropdown
                    else _get_checkbox(row_type),
                ],
                width=1,
            ),
            dbc.Col([html.B(row_type.capitalize())], width=1),
            dbc.Col(
                [
                    dbc.Container(
                        [dbc.Row(children=[], id=_get_output_id(row_type))], fluid=True
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
                                        "boxShadow": "none",
                                        "borderRadius": "0",
                                    },
                                    color="primary",
                                )
                            ],
                            class_name="d-grid gap-2",
                        )
                    ),
                    dbc.Row(
                        dbc.Col(
                            [
                                dbc.Container(
                                    [
                                        _get_new_row(Types.Trait, True),
                                        _get_new_row(Types.Career, True),
                                        _get_new_row(Types.Aspiration, True),
                                        _get_new_row(Types.Skill, True),
                                        dbc.Row(dbc.Col(html.Br())),
                                        _get_new_row(Types.Death, False),
                                        _get_new_row(Types.World, False),
                                    ],
                                    style={"margin": "1.5em"},
                                    fluid=True,
                                )
                            ]
                        )
                    ),
                ],
                style={"backgroundColor": "white"},
                className="g-0",
            ),
        ],
        className="bg-primary",
    )

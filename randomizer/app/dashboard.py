"""This module provides a dashboard for analysis of share portfolios.

The dashboard is defined by connecting widgets, events, etc. as defined in layout
to methods provided by analysis and use_cases.

This package has a clean architecture. This module should not contain any business- or
application logic, nor any adapters.
"""
import dash_bootstrap_components as dbc
from dash import Dash

from . import callbacks
from .layout import get_layout


def run_blocking() -> None:
    """Run the dash application."""
    app = Dash(__name__, prevent_initial_callbacks=True)

    app.layout = get_layout()

    app.run_server(debug=True)

import base64
import numpy as np
from datetime import date
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_table

from App.dashApp.chemograph.layouts.visualizations.visualization import *


# -----------------------------------------------------------------------------
# TAB 1 - BODY
# -----------------------------------------------------------------------------


TAB_1_BODY = [
    html.Div(
        children=[
            # Map: Study Area & Stations.
            TAB1_BODY_CONTENT1
        ],
        className="row justify-content-center",
        style={
            "height": "390px",
            "margin-bottom": "10px"
        }
    ),
    html.Div(
        children=[
            html.Div(
                children=[
                    # Table: Geographic Information of Stations.
                    TAB1_BODY_CONTENT2
                ],
                className="w-100 h-100 px-4"
            )

        ],
        className="row justify-content-center"
    )
]

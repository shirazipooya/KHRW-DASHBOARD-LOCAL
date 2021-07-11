import dash_html_components as html
import dash_dangerously_set_inner_html
from App.dashApp.precipitation.layouts.tabs.tab import *


# -----------------------------------------------------------------------------
# Tab Pan
# -----------------------------------------------------------------------------

TAB_PAN = html.Div(
    children=[

        # Nav Tabs ------------------------------------------------------------

        dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
            """
                    <ul class="nav nav-tabs mt-1" role="tablist">
                        <li class="nav-item">
                            <a class="nav-link active" data-toggle="tab" href="#Home">خانه</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-toggle="tab" href="#Tab_1">اتصال به پایگاه داده</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-toggle="tab" href="#Tab_2">تحلیل ایستگاهی داده‌های بارش</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-toggle="tab" href="#Tab_3">تحلیل منطقه‌ای داده‌های بارش</a>
                        </li>
                    </ul>
            """
        ),

        # Tab Panes -----------------------------------------------------------

        html.Div(
            children=[
                html.Div(
                    children=[
                        "HOME"
                    ],
                    className="tab-pane fade",
                    id="Home"
                ),
                html.Div(
                    children=[
                        TAB_1
                    ],
                    className="tab-pane fade",
                    id="Tab_1"
                ),
                html.Div(
                    children=[
                        TAB_2
                    ],
                    className="tab-pane active",
                    id="Tab_2"
                ),
                html.Div(
                    children=[
                        TAB_3
                    ],
                    className="tab-pane fade",
                    id="Tab_3"
                ),
            ],
            className="tab-content"
        )
    ],
    className="tabbable"
)


# -----------------------------------------------------------------------------
# Main Layout
# -----------------------------------------------------------------------------


def SERVER_MAIN_LAYOUT(TAB_PAN=TAB_PAN):
    MAIN_LAYOUT = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        children=[
                            TAB_PAN
                        ],
                        className="col"
                    )
                ],
                className="row"
            )
        ],
        className="container-fluid"
    )
    return MAIN_LAYOUT


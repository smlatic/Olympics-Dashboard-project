from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
from Load_data import Load_data

from plotly_graphs import General
from plotly_graphs import Finland




# Loat the dataset

Load_data.load()

Finland.initialize()

olympic_data = Load_data.olympic_data

# initialize dash app
app = Dash(name=__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



##############################################################################################################

##############################################################################################################

# Define layouts for each page
layout1 = html.Div(
    [
        html.H3(
            children="Male Female contestants in various countries",
            style={"textAlign": "center", "color": "#636EFA"},
        ),
        dcc.Graph(id="noc-graph", figure={})
    ]
)

layout2 = html.Div(
    [
        html.H3(children="graf 2", style={"textAlign": "center", "color": "#636EFA"}),
        dcc.Graph(
            id="rpdr_graph2",
            figure=Finland.graphfig(),
        ),
    ]
)





# Simple side bar
# https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/


# the style arguments for the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "32rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and add some padding.
CONTENT_STYLE = {
    "margin-left": "32rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# define sidebar section of HTML
sidebar = html.Div(
    [
        # html.H2("Drag Race: Plotly Dashboard", className="display-4"),
        html.Img(
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Olympic_rings_without_rims.svg/1200px-Olympic_rings_without_rims.svg.png",
            style={'height':'25%'}),
        html.Hr(),
        html.P("Olympic Games stats", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("General", href="/", active="exact"),
                dbc.NavLink("Finland", href="/page-1", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

# Define content section of HTML
content = html.Div(id="page-content", style=CONTENT_STYLE)


# INDEX LAYOUT
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# INDEX CALLBACKS
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return layout1
    elif pathname == "/page-1":
        return layout2

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P("The pathname {pathname} was not recognised..."),
        ]
    )


# # Callback function for page layout 1
# @app.callback(
#     Output(component_id="noc-graph", component_property="figure"),
#     Input(component_id="noc-dropdown", component_property="value"),
# )
# def update_graph(selected_noc):
#     filtered_noc = olympic_data[olympic_data["NOC"] == selected_noc]
#     pie_fig = px.pie(
#         filtered_noc,
#         names="Sex",
#         title=f"Percentages of Female/Male Athletes in {selected_noc}",
#     )
#     return pie_fig


# Run local server
if __name__ == "__main__":
    app.run_server(debug=True)
    app.run_server(port=8050)

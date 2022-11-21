# Import Libraries
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


# Loat the dataset
olympicdata = pd.read_csv("Data/athlete_events.csv")


# Create the Dash app
# app = Dash(__name__)


# initialize dash app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


# Render deployment
server= app.server



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
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Finnish_Olympic_Committee_logo.svg/220px-Finnish_Olympic_Committee_logo.svg.png"
        ),
        html.Hr(),
        html.P("Analysis of Finland in the Olympic Games", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Season Rankings", href="/", active="exact"),
                dbc.NavLink("Winners", href="/page-1", active="exact"),
                dbc.NavLink("Medals", href="/page-2", active="exact"),
                dbc.NavLink("Yada yada", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

# Define content section of HTML
content = html.Div(id="page-content", style=CONTENT_STYLE)


##############################################################################################################

##############################################################################################################

# Define layouts for each page
layout1 = html.Div(
    [
        html.H3(
            children="Male Female contestants in various countries",
            style={"textAlign": "center", "color": "#636EFA"},
        ),
        dcc.Dropdown(
            id="noc-dropdown",
            clearable=False,
            value="FIN",  # Preselection
            options=[{"label": i, "value": i} for i in olympicdata["NOC"].unique()],
            style={"width": "75%", "margin": "auto"},
        ),
        dcc.Graph(id="noc-graph", figure={}),
    ]
)

layout2 = html.Div(
    [
        html.H3(children="graf 2", style={"textAlign": "center", "color": "#636EFA"}),
        dcc.Graph(id="rpdr_graph2", figure=px.histogram(olympicdata, x="Age", color_discrete_sequence = ['blue'], title="Age distribution")),
    ]
)

layout3 = html.Div(
    [
        html.H3(children="Graf 3", style={"textAlign": "center", "color": "#636EFA"}),
        dcc.Graph(id="rpdr_graph3", figure={}),
    ]
)

layout4 = html.Div(
    [
        html.H3(children="Graf 4", style={"textAlign": "center", "color": "#636EFA"}),
        dcc.Graph(id="rpdr_graph4", figure={}),
    ]
)


##############################################################################################################
##############################################################################################################

# INDEX LAYOUT
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# INDEX CALLBACKS
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return layout1
    elif pathname == "/page-1":
        return layout2, layout2
    elif pathname == "/page-2":
        return layout3
    elif pathname == "/page-3":
        return layout4

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P("The pathname {pathname} was not recognised..."),
        ]
    )


##############################################################################################################


# -------------Origin

# Set up app layout
# app.layout = html.Div(
#     children=[
#         html.H1(children="Olympics Dashboard"),
#         dcc.Dropdown(
#             id="noc-dropdown",
#             options=[{"label": i, "value": i} for i in olympicdata["NOC"].unique()],
#             value="FIN", # den som visas först
#         ),
#         dcc.Graph(id="age-graph"),
#     ]
# )
# -----Origin


##############################################################################################################
##############################################################################################################

# Callback function for page layout 1
@app.callback(
    Output(component_id="noc-graph", component_property="figure"),
    Input(component_id="noc-dropdown", component_property="value"),
)
def update_graph(selected_noc):
    filtered_noc = olympicdata[olympicdata["NOC"] == selected_noc]
    pie_fig = px.pie(
        filtered_noc,
        names="Sex",
        title=f"Percentages of Female/Male Athletes in {selected_noc}",
    )
    return pie_fig


##############################################################################################################
##############################################################################################################


# # Run local server
# if __name__ == "__main__":
#     # app.run_server(debug=True)
#     app.run_server(port=8050)

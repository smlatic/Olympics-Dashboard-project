# Import Libraries
import dash
from dash import Dash, html, dcc

from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


# Loat the dataset
olympicdata = pd.read_csv("Data/athlete_events.csv")


# Create the Dash app
app = Dash(__name__)


# Set up app layout
app.layout = html.Div(
    children=[
        html.H1(children="Olympics Dashboard"),
        dcc.Dropdown(
            id="noc-dropdown",
            options=[{"label": i, "value": i} for i in olympicdata["NOC"].unique()],
            value="FIN", # den som visas först
        ),
        dcc.Graph(id="age-graph"),
    ]
)


# Callback funtion
@app.callback(
    Output(component_id="age-graph", component_property="figure"),
    Input(component_id="noc-dropdown", component_property="value")
)

def update_graph(selected_noc):
    filtered_noc = olympicdata[olympicdata["NOC"] == selected_noc]
    pie_fig = px.pie(filtered_noc, names="Sex", title=f"Percentages of Female/Male Athletes in {selected_noc}")
    return pie_fig





# Run local server
if __name__ == "__main__":
  # app.run_server(debug=True)
    app.run_server(port=8050)

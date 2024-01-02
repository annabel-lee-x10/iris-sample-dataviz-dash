import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the Iris dataset
df = px.data.iris()

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Simple Data Visualization Dashboard"),

    # Pie Chart
    dcc.Graph(
        id='pie-chart',
        figure=px.pie(df, names='species', title='Pie Chart')
    ),

    # Line Chart
    dcc.Graph(
        id='line-chart',
        figure=px.line(df, x='sepal_width', y='sepal_length', title='Line Chart')
    ),

    # Stacked Bar Chart
    dcc.Graph(
        id='stacked-bar-chart',
        figure=px.bar(df, x='species', y='sepal_width', color='species', title='Stacked Bar Chart')
    ),

    # Data Table
    html.Div([
        dcc.Graph(
            id='data-table',
            figure=px.scatter(df, x='sepal_width', y='sepal_length', title='Scatter Plot')
        ),
        dcc.Graph(
            id='scatter-plot',
            figure=px.scatter(df, x='sepal_width', y='sepal_length', title='Scatter Plot')
        ),
    ]),

])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

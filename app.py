import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import seaborn as sns
import pandas as pd

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    # Row 1
    html.Div([
        # Pie Chart
        dcc.Graph(id='pie-chart', className='col', style={'width': '50%'}),
        # Scatter Plot
        dcc.Graph(id='scatter-plot', className='col', style={'width': '50%'}),
    ], className='row'),

    # Row 2
    html.Div([
        # Stacked Bar Chart
        dcc.Graph(id='stacked-bar-chart', className='col', style={'width': '50%'}),
        # Line Chart
        dcc.Graph(id='line-chart', className='col', style={'width': '50%'}),
    ], className='row'),

    # Row 3
    html.Div([
        # Data Table
        dcc.Graph(id='data-table', className='col', style={'width': '100%'}),
    ], className='row'),
])

# Define callback functions to update charts based on user input
@app.callback(
    Output('pie-chart', 'figure'),
    Output('scatter-plot', 'figure'),
    Output('stacked-bar-chart', 'figure'),
    Output('line-chart', 'figure'),
    Output('data-table', 'figure'),
    Input('pie-chart', 'hoverData'),
    Input('scatter-plot', 'hoverData'),
    Input('stacked-bar-chart', 'hoverData'),
    Input('line-chart', 'hoverData'),
)
def update_charts(pie_hover, scatter_hover, stacked_bar_hover, line_hover):
    # Define functions to create individual charts
    def create_pie_chart():
        fig = px.pie(iris, names='species', title='Pie Chart', hole=0.3, labels={'species': 'Species'})
        return fig

    def create_scatter_plot():
        fig = px.scatter(iris, x='sepal_width', y='sepal_length', color='species', title='Scatter Plot',
                         labels={'sepal_width': 'Sepal Width', 'sepal_length': 'Sepal Length'})
        return fig

    def create_stacked_bar_chart():
        fig = px.bar(iris, x='species', y='sepal_width', color='species', title='Stacked Bar Chart',
                     labels={'sepal_width': 'Sepal Width'})
        return fig

    def create_line_chart():
        fig = px.line(iris, x='species', y='sepal_width', color='species', title='Line Chart',
                      labels={'sepal_width': 'Sepal Width'})
        return fig

    def create_data_table():
        fig = px.scatter(iris, x='sepal_width', y='sepal_length', color='species', title='Data Table',
                         labels={'sepal_width': 'Sepal Width', 'sepal_length': 'Sepal Length'})
        return fig

    # Call the appropriate function based on the input
    pie_chart = create_pie_chart()
    scatter_plot = create_scatter_plot()
    stacked_bar_chart = create_stacked_bar_chart()
    line_chart = create_line_chart()
    data_table = create_data_table()

    return pie_chart, scatter_plot, stacked_bar_chart, line_chart, data_table

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

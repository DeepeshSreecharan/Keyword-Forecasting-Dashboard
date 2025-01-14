import time

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, Input, Output, dcc, html
from prophet import Prophet
from pytrends.request import TrendReq

# Set pandas option to avoid downcasting warning
pd.set_option('future.no_silent_downcasting', True)

# Initialize Dash app
app = Dash(__name__)

# Initialize Pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define the list of keywords to analyze
keywords = ['Data Analyst', 'Java', 'AI']

# Define regions for analysis
regions = ['US', 'GB', 'IN', 'BR']  # Example regions

# Initialize dictionaries to store dataframes
dataframes_by_time = {}
dataframes_by_region = {}

# Loop through each keyword and region
for keyword in keywords:
    dataframes_by_time[keyword] = {}
    dataframes_by_region[keyword] = {}
    for region in regions:
        try:
            # Build the payload with the current keyword and region
            pytrends.build_payload([keyword], cat=0, timeframe='today 12-m', geo=region, gprop='')

            # Retrieve Interest Over Time
            interest_over_time_df = pytrends.interest_over_time()
            if not interest_over_time_df.empty:
                # Apply infer_objects() to handle dtype issues
                interest_over_time_df = interest_over_time_df.infer_objects(copy=False).fillna(False)
                dataframes_by_time[keyword][region] = interest_over_time_df

                # Store data for regional analysis
                dataframes_by_region[keyword][region] = interest_over_time_df.iloc[-1][keyword]  # Store latest interest score

            else:
                print(f"No interest over time data found for {keyword} in {region}.")

            # Introduce a delay to prevent rate limiting
            time.sleep(5)

        except Exception as e:
            print(f"An error occurred for keyword '{keyword}' in region '{region}': {e}")

# Dash Layout
app.layout = html.Div([
    html.H1("Keyword Trend Analysis"),
    
    html.Div([
        html.Label("Select Region:"),
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': region, 'value': region} for region in regions],
            value=regions[0]  # Default selection
        )
    ], style={'margin-bottom': '20px'}),
    
    html.Div([
        dcc.Graph(id='trend-graph'),
    ])
])

# Callback to update graph based on region selection
@app.callback(
    Output('trend-graph', 'figure'),
    Input('region-dropdown', 'value')
)
def update_graph(selected_region):
    fig = go.Figure()
    for keyword in keywords:
        if selected_region in dataframes_by_time[keyword]:
            df = dataframes_by_time[keyword][selected_region]
            fig.add_trace(go.Scatter(
                x=df.index,
                y=df[keyword],
                mode='lines',
                name=keyword
            ))
    fig.update_layout(
        title=f'Trends Over Time in {selected_region}',
        xaxis_title='Date',
        yaxis_title='Interest',
        template='plotly'
    )
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

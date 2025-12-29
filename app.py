from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

app = Dash(__name__)

app.layout = html.Div(style={
    'backgroundColor': '#f8f9fa',
    'fontFamily': 'Segoe UI, sans-serif',
    'padding': '40px',
    'minHeight': '100vh'
}, children=[

    html.H1(
        children='Soul Foods Pink Morsel Sales Analysis',
        style={
            'textAlign': 'center',
            'color': '#2c3e50',
            'fontWeight': 'bold',
            'marginBottom': '30px'
        }
    ),

    html.Div(style={
        'backgroundColor': '#ffffff',
        'padding': '20px',
        'borderRadius': '10px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
        'marginBottom': '20px',
        'textAlign': 'center'
    }, children=[
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '15px'}),
        dcc.RadioItems(
            id='region-picker',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True,
            style={'display': 'inline-block'}
        ),
    ]),

    html.Div(style={
        'backgroundColor': '#ffffff',
        'padding': '20px',
        'borderRadius': '10px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
    }, children=[
        dcc.Graph(id='sales-line-chart')
    ])
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(selected_region):
    # Filter selection
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Sales Trend: {selected_region.capitalize()} Region",
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales ($)",
        transition_duration=500
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)
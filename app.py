from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 1. දත්ත කියවීම සහ පිළිවෙළට සැකසීම
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

# 2. Dash App එක ආරම්භ කිරීම
app = Dash(__name__)

# 3. App එකේ Layout එක (පෙනුම) සැකසීම
app.layout = html.Div(style={
    'backgroundColor': '#f8f9fa',
    'fontFamily': 'Segoe UI, sans-serif',
    'padding': '40px',
    'minHeight': '100vh'
}, children=[

    # Title - CSS Styling ඇතුළත් කර ඇත
    html.H1(
        children='Soul Foods Pink Morsel Sales Analysis',
        style={
            'textAlign': 'center',
            'color': '#2c3e50',
            'fontWeight': 'bold',
            'marginBottom': '30px'
        }
    ),

    # Radio Buttons - ප්‍රදේශය තෝරා ගැනීමට
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
            value='all',  # Default value එක ලෙස 'all' තබා ඇත
            inline=True,
            style={'display': 'inline-block'}
        ),
    ]),

    # Graph - ප්‍රස්ථාරය දර්ශනය වන ස්ථානය
    html.Div(style={
        'backgroundColor': '#ffffff',
        'padding': '20px',
        'borderRadius': '10px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
    }, children=[
        dcc.Graph(id='sales-line-chart')
    ])
])


# 4. Callback Function - Radio Button එක අනුව ප්‍රස්ථාරය වෙනස් කිරීම
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

    # නව ප්‍රස්ථාරය නිර්මාණය කිරීම
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
        transition_duration=500  # වෙනස් වන විට සිදුවන animation එක
    )

    return fig


# 5. App එක Run කිරීම
if __name__ == '__main__':
    app.run(debug=True)
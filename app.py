from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

app = Dash(__name__)

fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Analysis")

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales ($)",
)

app.layout = html.Div(style={'textAlign': 'center', 'fontFamily': 'Arial'}, children=[

    html.H1(
        children='Soul Foods Pink Morsel Sales Visualiser',
        style={'color': '#2c3e50', 'marginTop': '20px'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
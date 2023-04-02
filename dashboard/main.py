from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from database.functions import get_month_count, get_month_count_by_users

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
    html.H1("GEOREPORT"),
    dcc.Graph(id="report_count", style={'width': '800px', 'height': '500px'}),
    html.P("Выбор типа графика:"),
    dcc.Dropdown(
        id="ticker",
        options=["Общее число", "По пользователям"],
        value="Общее число",
        clearable=False,
        style={'width': '800px', 'height': '30px'}
    )])
])


@app.callback(
    Output("report_count", "figure"),
    Input("ticker", "value"))
def report_count(ticker):
    if ticker == "Общее число":
        df = get_month_count()
        fig = px.line(df, x='Месяц', y='Общее число протоколов', title="Выданные протоколы")
        return fig
    elif ticker == "По пользователям":
        df = get_month_count_by_users()
        fig = px.line(df, x='Месяц', y=df.columns[1:], title="Выданные протоколы")
        return fig


app.run_server(debug=True)

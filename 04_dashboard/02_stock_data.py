import dash
from dash import  dcc
from dash import html

import plotly.graph_objects as go

def fetch_data(company='AMZN'):
  """pobiera dane spolek z serwisu stooq"""
  import pandas_datareader.data as web
  return web.DataReader(name=company, data_source='stooq')

df = fetch_data()
df.reset_index(inplace=True)

df = df[df.Date>'2023-01-01']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H2(children='Amazon shares value on stock!'),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x=df.Date,
                    y=df.Close,
                    mode='lines',
                    fill='tozeroy',
                    name='Amazon'
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=500,
                title_text='Amazon share price chart',
                showlegend=True
            )
        )
    ),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=df.Date,
                    y=df.Volume,
                    name='Wolumen'

                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=300,
                title_text='Volumen chart',
                showlegend=True
            )
        )
    )
])


if __name__ ==  '__main__':
    app.run_server(debug=True)

# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:11:56 2018

@author: n34873
"""

import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)
server = app.server
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

df_csv = pd.read_csv('https://raw.githubusercontent.com/enracol/deploydash-kike-csv/master/Prueba_csv_2.csv')

app.layout = html.Div(children=[

        html.Label('Year'),
        html.Div(dcc.Slider(
            id='year-slider',
            min=df_csv['Year'].min(),
            max=df_csv['Year'].max(),
            value=df_csv['Year'].min(),
            step=None,
            marks={str(year): str(year) for year in df_csv['Year'].unique()},
         )),          
            
        html.Div(id='example-graph-csv'),
        
    ])   

@app.callback(Output('example-graph-csv','children'),[Input('year-slider','value')])

def update_graph(selected_year):
    
    #df_csv = pd.read_csv('C:\\Users\\N34873\\Desktop\\Prueba_csv_2.csv')
    fecha=selected_year
    dff=df_csv[df_csv['Year']==fecha]
    
    #Selecionar solo lo sdatos con 'Year' igual a fecha
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': dff.Precio,'y': dff.Value,'type': 'line','name': 'tttt'},
            ],
            'layout': {
                'title': 'Year {}'.format(fecha)
            }
        }
    )
            
if __name__ == '__main__':
    app.run_server()
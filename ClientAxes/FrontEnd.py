#Trevor O'Hearn
#8/28/20
#FrontEnd.py
#Front end to take inputs from user about new client axes
#Dependencies: Python3, Dash, sqlite3
#notes: You can use MySQLWorkbench to view database created in sqlite3

#plotly for visuals
#import plotly.graph_objects as go #or plotly.express as px
#import plotly.express as px #or plotly.graph_objects as go

#Dash runs the background server to take the inputs
import dash
import dash_core_components as dcc
import dash_html_components as html
#used for events to use change page
#from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([ #main container
    #top
    html.Div([html.H2('Client Requested Axes',
                style={
                    'font-size' : '20px',
                    'padding-left' : '25%',
                    'padding-right' : '25%',
                    'text-align' : 'center'
                        }
                    )
    ], style={
      'background-color' : '#011f4b',
      'padding' : '10px',
      'z-index' : '1',
      'top' : '0px',
      'left' : '0px',
      'width' : '100%'
    }),
    #middle
    #container to hold all inputs
    html.Div([
        #name of client
        html.H3('Name of Client'),
        dcc.Input(id='clientName', type='text', value='name here', debounce=True),
        #market
        #html.H3('Market'),
        #dcc.Input(id='market', type='text', value='market', debounce=True),
        #rating he is looking into
        html.H3('Rating'),
        dcc.Input(id='rating', type='text', value='BBB', debounce=True),
        #yield he is l
        html.H3('Yield'),
        dcc.Input(id='yield', type='number', value=0, debounce=True),
        #maturity
        html.H3('Maturity'),
        dcc.Input(id='maturity', type='number', value=27, debounce=True),
        #sector
        html.H3('Sector'),
        dcc.Input(id='sector', type='text', value='type sector', debounce=True),
        #Go button
        html.H3('Go!'),
        html.Button('Submit', id='bnt_submit')

    ], style={
          'margin-left' : '200px',
          'background-color' : '#6497b1',
          'padding' : '5%'
        }),


    #bottom
    html.Div([
            html.P('this is the bottom')],

            style={'padding' : '1em',
                    'background-color' : '#005b96'}
            )


], style={
        'background-color' : '#b3cde0'
})

app.run_server(debug=True)

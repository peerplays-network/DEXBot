import sys
import threading

from dexbot.config import Config
from dexbot.controllers.main_controller import MainController
from dexbot.views.worker_list import MainView
# Todo: Remove extra and order things around here
from bitshares.bitshares import Account
from dexbot.orderengines.bitshares_engine import BitsharesOrderEngine

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from PyQt5.QtWidgets import QApplication

import math


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        # Init config
        config = Config()

        # Init main controller
        self.main_controller = MainController(config)

        # Init main view
        self.main_view = MainView(self.main_controller)

        # Show main view
        self.main_view.show()


def main():
    app = App(sys.argv)
    sys.exit(app.exec_())


def server():
    """ Server to provide statistical visualization of a worker
    """
    # Fixme: Include this file in the project instead of loading from external source
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    dash_app.layout = html.Div(id='wrapper', style={'height': '80vh'}, children=[
        html.H1(children='Staggered Orders Overview'),
        html.H2(children='A mountain based visualisation of (base asset/quote asset)'),
        # Fixme: Button's layout is inherited in some bad way because it looks good in browser
        html.Button(id='button', n_clicks=0, children='Switch'),
        html.Div(id='output-graph'),

        # Represents the URL bar, doesn't render anything
        dcc.Location(id='url', refresh=False)

    ])

    @dash_app.callback(Output('output-graph', 'children'),
                       [Input('button', 'n_clicks'),
                        Input('url','pathname')])
    def display_page(n_clicks,pathname):

        # Todo: the if pathname part needs to be moved into another function but that causes errors
        if pathname:
            # Add readable spaces to worker name if there are any
            pathname = pathname.replace("%20", " ")

            # Split the path so that the names can be extracted
            pathname = pathname.split('/')

            account_name = pathname[1]
            worker_name = pathname[2]

            # Create Bitshares Account instance using the account name
            account = Account(account_name)

            # Todo: This config stuff needs to be adjusted
            config = Config()
            worker_config = config
            # print(worker_config.workers_data)

            worker_market = worker_config.workers_data[worker_name]['market']
            worker_market = worker_market.split('/')

            base_asset = worker_market[1]
            quote_asset = worker_market[0]

            df = pd.DataFrame({'label':[],
                               'price':[],
                               'order_size':[],
                               'current_orders':[],
                               'initial_orders':[],
                               'bar_colors_current':[],
                               'bar_colors_initial':[]})


            df, cp = get_orders(df,account,base_asset)

            # Fixme: is it necessary to append this in the Pandas dataframe? If yes, do it in get_orders
            ticks = [i for i in range(len(df['price'].tolist()))]
            text = [str(i) for i in df['price'].tolist()]

            # Todo: change 'current' stuff once update on db is done
            current_orders = {} # placeholder so program doesn't crash
            bar_colors_current = [] # placeholder so program doesn't crash

            # Get half of all orders to determine range for y-axis
            half = df['order_size'].head(int(len(df['order_size'])*(50/100))).tolist()

            if n_clicks is 0 or n_clicks % 2 == 0: # check whether the number of clicks is an even number, if so, vertical view
                figure_dict = {}
                data = [go.Bar(x=[i for i in range(len(df['price'].tolist()))],
                               y=list(current_orders.values()),name='Current',
                               marker=go.bar.Marker(color=bar_colors_current)),
                        go.Bar(x=[i for i in range(len(df['price'].tolist()))],
                               y=df['order_size'].tolist(),name='Initial',
                               marker=go.bar.Marker(color=df['bar_colors_initial'].tolist()),
                               orientation='v')]
                figure_dict['data'] = data
                xaxis_dict = {'title':quote_asset + '/' + base_asset,
                              'zerolinecolor':'rgba(153,153,153,0.2)','tickvals':ticks,
                              'ticktext':text,'showticklabels':False}
                yaxis_dict = {'title':'Order size','gridcolor':'rgba(153,153,153,0.2)',
                              'range':[half[0],half[-1]]}

                figure = get_figure(figure_dict,xaxis_dict,yaxis_dict)

                return figure

            elif n_clicks % 2 != 0: # check whether the number of clicks isn't an even number, if so, horizontal view
                figure_dict = {}
                data = [go.Bar(x=list(current_orders.values()),
                               y=[i for i in range(len(df['price'].tolist()))],name='Current',
                               marker=go.bar.Marker(color=bar_colors_current)),
                        go.Bar(x=df['order_size'].tolist(),
                               y=[i for i in range(len(df['price'].tolist()))],name='Initial',
                               marker=go.bar.Marker(color=df['bar_colors_initial'].tolist()),
                               orientation='h')]
                figure_dict['data'] = data
                xaxis_dict = {'title':'Order size','gridcolor':'rgba(153,153,153,0.2)',
                              'range':[half[0],half[-1]]}
                yaxis_dict = {'title':quote_asset + '/' + base_asset,'zerolinecolor':'rgba(153,153,153,0.2)',
                              'tickvals':ticks,'ticktext':text,'showticklabels':False}

                figure = get_figure(figure_dict,xaxis_dict,yaxis_dict)

                return figure


    def get_orders(df,account,base_asset):

        # Todo: create an if-statement to check whether the order is a current_order or initial_order
        for order in account.openorders:
            if order['for_sale']['symbol'] == base_asset: # if the asset that you sell is equal to base asset, it's a buy order
                df = df.append({'label':'buy',
                                'price':round(order['price'],3),
                                'order_size':float(order['base']['amount']*order['price']),
                                'bar_colors_initial':'rgba(58, 98, 87, 0.5)'},ignore_index=True)

            else: # otherwise it's a sell order
                price = round(float(order['quote']['amount'])/float(order['base']['amount']),3)

                df = df.append({'label':'sell',
                                'price':price,
                                'order_size':float(order['base']['amount']*order['price']),
                                'bar_colors_initial':'rgba(230, 0, 0, 0.5)'},ignore_index=True)

        # set label (sell or buy) as the row's index and ignore duplicate labels
        df = df.set_index('label',verify_integrity=False)

        # get lowest sell and highest buy from unsorted DataFrame
        sell_price = df.loc[['sell'],['price']].iloc[0]['price'] # sell_price
        buy_price = df.loc[['buy'],['price']].iloc[0]['price'] # buy_price

        sell_order_size = df.loc[['sell'],['order_size']].iloc[0]['order_size']
        buy_order_size = df.loc[['buy'],['order_size']].iloc[0]['order_size']

        # calculate center price (same for market_center_price) and center order size
        cp = round(buy_price * math.sqrt(sell_price / buy_price),3)
        cp_order_size = round(buy_order_size * math.sqrt(sell_order_size / buy_order_size),3)

        # append cp, cp_order_size and belonging color to the DataFrame
        df = df.append({'price':cp,'order_size':cp_order_size,
                        'bar_colors_initial':'rgba(217,217,217,0.5)'},ignore_index=True)

        # sort values in dataframe by price to get mountain type datastructure
        df = df.sort_values(by=['price'])

        # Todo: this may be needed in case the update of storing orders in db is done
        # initial_orders = {}
        # current_orders = {}
        # for x, y in zip(price_list, order_size):
        #     initial_orders[round(x, 3)] = y
        #     # current_dict[round(x, 3)] = z

        return df, cp


    def get_figure(figure_dict,xaxis_dict,yaxis_dict):
        data = figure_dict['data']
        return dcc.Graph(
            id='my-figure',
            figure=go.Figure(
                data=data,
                layout=go.Layout(
                    autosize=True,
                    xaxis=xaxis_dict,
                    yaxis=yaxis_dict,
                    barmode='stack',
                    plot_bgcolor='rgb(21,43,42)',
                    paper_bgcolor='rgb(21,43,42)',
                    font={
                        'color': 'white'
                    },
                    showlegend=False
                )
            ),
            config={
                'displayModeBar': False
            },
            style={'height': '100%', 'width': '80vw', 'display': 'inline-block'}
        )

    dash_app.run_server()


# Run Dash app on separate thread
# Todo: This could be possibly improved by moving most of the Dash related stuff out of this file
server_thread = threading.Thread(target=server)
server_thread.daemon = True
server_thread.start()

if __name__ == '__main__':
    main()

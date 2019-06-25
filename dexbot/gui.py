import sys
import threading

from dexbot.config import Config
from dexbot.controllers.main_controller import MainController
from dexbot.views.worker_list import MainView
from dexbot.controllers.wallet_controller import WalletController
from dexbot.views.unlock_wallet import UnlockWalletView
from dexbot.views.create_wallet import CreateWalletView
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
from bitshares import BitShares


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        config = Config()
        bitshares_instance = BitShares(config['node'], num_retries=-1, expiration=60)

        # Wallet unlock
        unlock_ctrl = WalletController(bitshares_instance)
        if unlock_ctrl.wallet_created():
            unlock_view = UnlockWalletView(unlock_ctrl)
        else:
            unlock_view = CreateWalletView(unlock_ctrl)

        if unlock_view.exec_():
            bitshares_instance = unlock_ctrl.bitshares
            self.main_ctrl = MainController(bitshares_instance, config)
            self.main_view = MainView(self.main_ctrl)
            self.main_view.show()
        else:
            sys.exit()


def main():
    app = App(sys.argv)
    sys.exit(app.exec_())


def server():
    """ Server to provide statistical visualization of a worker
    """
    # Todo: Change to use data from Bitshares
    df = pd.read_csv('test.csv',
                     usecols=['Price', 'Mountain_neutral_view', 'Current'])
    # Fixme: Include this file in the project instead of loading from external source
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    dash_app.layout = html.Div(id='wrapper', style={'height': '80vh', 'width': '100vh'}, children=[
        # Represents the URL bar, doesn't render anything
        dcc.Location(id='url', refresh=False),

        html.H1(children='Staggered Orders Overview'),
        html.H2(children='A mountain based visualisation of (base asset/quote asset)'),
        html.Div(id='output-figure'),
        dcc.Input(id='input1', type='text'),  # Price
        dcc.Input(id='input2', type='text'),  # Order size
        html.Button(id='submit-button', n_clicks=0, children='Submit')

    ])

    @dash_app.callback(
        dash.dependencies.Output('wrapper', 'children'),
        [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname):
        """ This is called on every page load and URL change.
            # Todo: this can be changed to only retrieve data of the worker
            # Todo: Add documentation
            :param pathname: URL of the worker
            :return:
        """

        if pathname:
            # Add readable spaces to worker name if there are any
            pathname = pathname.replace("%20", " ")

            # Split the path so that the names can be extracted
            pathname = pathname.split('/')

            account_name = pathname[1]
            worker_name = pathname[2]

            # Create Bitshares Account instance using the account name
            account = Account(account_name)
            # Todo: Get's all open orders for this account
            # print(account.openorders)

            # Return updated figure
            return html.Div(id='wrapper', style={'height': '80vh', 'width': '100vh'}, children=[
                html.H1(children='Staggered Orders Overview for {}'.format(worker_name)),
                html.H2(children='A mountain based visualisation of (base asset/quote asset)'),
                html.Div(id='output-figure'),
                dcc.Input(id='input1', type='text'),  # Price
                dcc.Input(id='input2', type='text'),  # Order size
                html.Button(id='submit-button', n_clicks=0, children='Submit')

            ])

        # Return empty div
        return html.Div()

    @dash_app.callback(Output('output-figure', 'children'),
                       [Input('submit-button', 'n_clicks')],
                       [State('input1', 'value'),
                        State('input2', 'value')])
    def update_figure(n_clicks, input1, input2):
        """ Todo: Add documentation

            :param n_clicks:
            :param input1:
            :param input2:
            :return:
        """
        bar_background_colors_initial = []
        bar_background_colors_current = []

        initial_dict = {}
        current_dict = {}
        for x, y, z in zip(df.Price, df.Mountain_neutral_view, df.Current):
            initial_dict[round(x, 3)] = y
            current_dict[round(x, 3)] = z

        if input1 is not None:  # NEEDS TO BE ADDED: if not input1 == ''
            input_price = float(input1)
            if input_price in list(initial_dict.keys()):
                current_dict[input_price] += float(input2)
                initial_dict[input_price] -= float(input2)
            else:
                print('error')

        for item in initial_dict:
            item = round(item, 3)
            if item < 1:
                bar_background_colors_initial.append('rgba(58, 98, 87, 0.5)')
                bar_background_colors_current.append('rgba(51, 204, 51, 0.9)')
            else:
                if item == 1:
                    bar_background_colors_initial.append('rgba(217,217,217,0.5)')
                    bar_background_colors_current.append('rgba(242,242,242,0.9)')
                else:
                    bar_background_colors_initial.append('rgba(230, 0, 0, 0.5)')
                    bar_background_colors_current.append('rgba(255, 0, 0, 0.9)')

        print(list(current_dict.values()))

        data = [
            go.Bar(
                x=[i for i in range(len(list(df.Price)))],  # Length of the dict (len(dict))
                y=list(current_dict.values()),  # All values from current_dict
                name='Buy',
                marker=go.bar.Marker(
                    color=bar_background_colors_current
                )
            ),
            go.Bar(
                x=[i for i in range(len(list(df.Price)))],  # Length of the dict
                y=list(initial_dict.values()),  # All values from mountain_dict
                name='Sell',
                marker=go.bar.Marker(
                    color=bar_background_colors_initial
                )
            )
        ]

        return dcc.Graph(
            id='my-figure',
            figure=go.Figure(
                data=data,
                layout=go.Layout(
                    autosize=True,
                    xaxis=dict(
                        title='BTS/USD',
                        zerolinecolor='rgba(153,153,153,0.2)'
                    ),
                    yaxis=dict(
                        title='Order size',
                        gridcolor='rgba(153,153,153,0.2)'
                    ),
                    barmode='stack',
                    plot_bgcolor='rgb(21,43,42)',
                    paper_bgcolor='rgb(21,43,42)',
                    font={
                        'color': 'white'
                    }
                )
            ),
            style={'height': '100%', 'width': '60vw', 'display': 'inline-block'}
        )

    dash_app.run_server()


# Run Dash app on separate thread
# Todo: This could be possibly improved by moving most of the Dash related stuff out of this file
server_thread = threading.Thread(target=server)
server_thread.daemon = True
server_thread.start()

if __name__ == '__main__':
    main()

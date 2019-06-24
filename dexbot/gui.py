import sys
import threading

from dexbot.config import Config
from dexbot.controllers.main_controller import MainController
from dexbot.views.worker_list import MainView
from dexbot.controllers.wallet_controller import WalletController
from dexbot.views.unlock_wallet import UnlockWalletView
from dexbot.views.create_wallet import CreateWalletView

import dash
import dash_core_components as dcc
import dash_html_components as html

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
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    dash_app.layout = html.Div(children=[
        html.H1(children='DEXBot Dash app'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Some random test data'
                }
            }
        )
    ])

    # Todo: Remove debug
    dash_app.run_server(debug=True)


server_thread = threading.Thread(target=server)
server_thread.daemon = True
server_thread.start()

if __name__ == '__main__':
    main()

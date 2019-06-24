import os
import importlib

from dexbot.controllers.worker_details_controller import WorkerDetailsController
from dexbot.helper import get_user_data_directory
from dexbot.views.ui.worker_details_window_ui import Ui_details_dialog
from dexbot.views.ui.tabs.graph_tab_ui import Ui_Graph_Tab
from dexbot.views.ui.tabs.table_tab_ui import Ui_Table_Tab
from dexbot.views.ui.tabs.text_tab_ui import Ui_Text_Tab
from dexbot.views.ui.tabs.web_tab import WebTab

from PyQt5.QtWidgets import QWidget, QDialog


class WorkerDetailsView(QDialog, Ui_details_dialog, Ui_Graph_Tab, Ui_Table_Tab, Ui_Text_Tab, WebTab):

    def __init__(self, worker_name, config):
        super().__init__()

        self.config = config['workers'].get(worker_name)

        # Initialize view controller
        self.controller = WorkerDetailsController(self, worker_name, self.config)

        self.setupUi(self)

        # Add worker's name to the dialog title
        self.setWindowTitle("DEXBot - {} details".format(worker_name))

        # Get strategy class from the config
        strategy_class = getattr(importlib.import_module(self.config.get('module')), 'Strategy')

        # DetailElements that are used to configure worker's detail view
        details = strategy_class.configure_details()

        # Initialize other data to the dialog
        self.controller.initialize_worker_data()

        # Add custom tabs
        self.add_tabs(details)

        # Dialog controls
        self.button_box.rejected.connect(self.reject)

    def add_tabs(self, details):
        # Add tabs to the details view
        for detail in details:
            widget = QWidget(self)

            if detail.type == 'graph':
                widget = self.add_graph_tab(detail, widget)
            elif detail.type == 'table':
                widget = self.add_table_tab(detail, widget)
            elif detail.type == 'text':
                widget = self.add_text_tab(detail, widget)
            elif detail.type == 'web':
                widget = self.add_web_tab(widget)

            self.tabs_widget.addTab(widget, detail.name)

    def add_web_tab(self, widget):
        """ Creates a web view to details. Opens URL inside the tab.
            Todo: Add documentation
            Fixme: Get a better way to load the per worker data, unless data is behind url + worker_data or something.
                   For now it only opens the default page for sake of testing.

            :param widget:
            :return:
        """

        tab = WebTab()
        url = 'http://127.0.0.1:8050/'
        tab.setup_ui(widget, url)

        return widget

    def add_graph_tab(self, detail, widget):
        tab = Ui_Graph_Tab()
        tab.setupUi(widget)
        tab.graph_wrap.setTitle(detail.title)

        if detail.file:
            file = os.path.join(get_user_data_directory(), 'graphs', detail.file)
            tab.table = self.controller.add_graph(tab, file)

        return widget

    def add_table_tab(self, detail, widget):
        tab = Ui_Table_Tab()
        tab.setupUi(widget)
        tab.table_wrap.setTitle(detail.title)

        if detail.file:
            file = os.path.join(get_user_data_directory(), 'data', detail.file)
            tab.table = self.controller.populate_table_from_csv(tab, file)

        return widget

    def add_text_tab(self, detail, widget):
        tab = Ui_Text_Tab()
        tab.setupUi(widget)
        tab.text_wrap.setTitle(detail.title)

        if detail.file:
            file = os.path.join(get_user_data_directory(), 'logs', detail.file)
            tab.text = self.controller.populate_text_from_file(tab, file)

        return widget

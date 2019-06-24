from PyQt5.QtCore import QMetaObject, QUrl
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox
from PyQt5.QtWebEngineWidgets import QWebEngineView


class WebTab(object):

    def __init__(self):
        self.verticalLayout = None
        self.graph_wrap = None
        self.web_view = QWebEngineView()

    def setup_ui(self, web_tab, url):
        web_tab.setObjectName("Graph_Tab")
        web_tab.resize(800, 600)

        self.verticalLayout = QVBoxLayout(web_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graph_wrap = QGroupBox(web_tab)
        self.graph_wrap.setTitle("")

        self.web_view.load(QUrl(url))

        self.verticalLayout.addWidget(self.web_view)

        QMetaObject.connectSlotsByName(web_tab)



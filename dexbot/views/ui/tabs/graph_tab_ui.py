# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/laptech/pbsa/DEXBot/dexbot/views/ui/tabs/graph_tab.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Graph_Tab(object):
    def setupUi(self, Graph_Tab):
        Graph_Tab.setObjectName("Graph_Tab")
        Graph_Tab.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Graph_Tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graph_wrap = QtWidgets.QGroupBox(Graph_Tab)
        self.graph_wrap.setTitle("")
        self.graph_wrap.setObjectName("graph_wrap")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.graph_wrap)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graph = QtWidgets.QTextEdit(self.graph_wrap)
        self.graph.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graph.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graph.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.graph.setObjectName("graph")
        self.verticalLayout_2.addWidget(self.graph)
        self.status_label = QtWidgets.QLabel(self.graph_wrap)
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.verticalLayout_2.addWidget(self.status_label)
        self.verticalLayout.addWidget(self.graph_wrap)

        self.retranslateUi(Graph_Tab)
        QtCore.QMetaObject.connectSlotsByName(Graph_Tab)

    def retranslateUi(self, Graph_Tab):
        _translate = QtCore.QCoreApplication.translate
        Graph_Tab.setWindowTitle(_translate("Graph_Tab", "Form"))


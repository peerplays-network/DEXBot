# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jacko/Desktop/DEXBot/dexbot/dexbot/views/ui/tabs/table_tab.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Table_Tab(object):
    def setupUi(self, Table_Tab):
        Table_Tab.setObjectName("Table_Tab")
        Table_Tab.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Table_Tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_wrap = QtWidgets.QGroupBox(Table_Tab)
        self.table_wrap.setTitle("")
        self.table_wrap.setObjectName("table_wrap")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.table_wrap)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.table = QtWidgets.QTableWidget(self.table_wrap)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setGridStyle(QtCore.Qt.SolidLine)
        self.table.setRowCount(0)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.horizontalHeader().setDefaultSectionSize(120)
        self.verticalLayout_5.addWidget(self.table)
        self.status_label = QtWidgets.QLabel(self.table_wrap)
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.verticalLayout_5.addWidget(self.status_label)
        self.verticalLayout.addWidget(self.table_wrap)

        self.retranslateUi(Table_Tab)
        QtCore.QMetaObject.connectSlotsByName(Table_Tab)

    def retranslateUi(self, Table_Tab):
        _translate = QtCore.QCoreApplication.translate
        Table_Tab.setWindowTitle(_translate("Table_Tab", "Form"))
        self.table.setSortingEnabled(True)


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/laptech/pbsa/DEXBot/dexbot/views/ui/tabs/text_tab.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Text_Tab(object):
    def setupUi(self, Text_Tab):
        Text_Tab.setObjectName("Text_Tab")
        Text_Tab.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Text_Tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_wrap = QtWidgets.QGroupBox(Text_Tab)
        self.text_wrap.setTitle("")
        self.text_wrap.setObjectName("text_wrap")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.text_wrap)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.text = QtWidgets.QPlainTextEdit(self.text_wrap)
        self.text.setObjectName("text")
        self.verticalLayout_15.addWidget(self.text)
        self.status_label = QtWidgets.QLabel(self.text_wrap)
        self.status_label.setEnabled(True)
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.verticalLayout_15.addWidget(self.status_label)
        self.verticalLayout.addWidget(self.text_wrap)

        self.retranslateUi(Text_Tab)
        QtCore.QMetaObject.connectSlotsByName(Text_Tab)

    def retranslateUi(self, Text_Tab):
        _translate = QtCore.QCoreApplication.translate
        Text_Tab.setWindowTitle(_translate("Text_Tab", "Form"))


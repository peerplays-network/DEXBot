# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/laptech/pbsa/DEXBot/dexbot/views/ui/edit_worker_window.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(428, 365)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.strategy_label = QtWidgets.QLabel(self.groupBox)
        self.strategy_label.setMinimumSize(QtCore.QSize(120, 0))
        self.strategy_label.setMaximumSize(QtCore.QSize(120, 16777215))
        self.strategy_label.setObjectName("strategy_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.strategy_label)
        self.strategy_input = QtWidgets.QComboBox(self.groupBox)
        self.strategy_input.setObjectName("strategy_input")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.strategy_input)
        self.worker_name_label = QtWidgets.QLabel(self.groupBox)
        self.worker_name_label.setMinimumSize(QtCore.QSize(120, 0))
        self.worker_name_label.setMaximumSize(QtCore.QSize(120, 16777215))
        self.worker_name_label.setObjectName("worker_name_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.worker_name_label)
        self.worker_name_input = QtWidgets.QLineEdit(self.groupBox)
        self.worker_name_input.setObjectName("worker_name_input")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.worker_name_input)
        self.quote_asset_input = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quote_asset_input.sizePolicy().hasHeightForWidth())
        self.quote_asset_input.setSizePolicy(sizePolicy)
        self.quote_asset_input.setMaximumSize(QtCore.QSize(145, 16777215))
        self.quote_asset_input.setObjectName("quote_asset_input")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.quote_asset_input)
        self.base_asset_wrap = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.base_asset_wrap.sizePolicy().hasHeightForWidth())
        self.base_asset_wrap.setSizePolicy(sizePolicy)
        self.base_asset_wrap.setMinimumSize(QtCore.QSize(120, 0))
        self.base_asset_wrap.setMaximumSize(QtCore.QSize(120, 16777215))
        self.base_asset_wrap.setObjectName("base_asset_wrap")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.base_asset_wrap)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.base_asset_label = QtWidgets.QLabel(self.base_asset_wrap)
        self.base_asset_label.setMinimumSize(QtCore.QSize(0, 0))
        self.base_asset_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.base_asset_label.setObjectName("base_asset_label")
        self.horizontalLayout.addWidget(self.base_asset_label)
        self.base_asset_tooltip = QtWidgets.QLabel(self.base_asset_wrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.base_asset_tooltip.sizePolicy().hasHeightForWidth())
        self.base_asset_tooltip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.base_asset_tooltip.setFont(font)
        self.base_asset_tooltip.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.base_asset_tooltip.setObjectName("base_asset_tooltip")
        self.horizontalLayout.addWidget(self.base_asset_tooltip)
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.base_asset_wrap)
        self.quote_asset_wrap = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quote_asset_wrap.sizePolicy().hasHeightForWidth())
        self.quote_asset_wrap.setSizePolicy(sizePolicy)
        self.quote_asset_wrap.setMinimumSize(QtCore.QSize(120, 0))
        self.quote_asset_wrap.setMaximumSize(QtCore.QSize(120, 16777215))
        self.quote_asset_wrap.setObjectName("quote_asset_wrap")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.quote_asset_wrap)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.quote_asset_label = QtWidgets.QLabel(self.quote_asset_wrap)
        self.quote_asset_label.setMinimumSize(QtCore.QSize(0, 0))
        self.quote_asset_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.quote_asset_label.setObjectName("quote_asset_label")
        self.horizontalLayout_3.addWidget(self.quote_asset_label)
        self.quote_asset_tooltip = QtWidgets.QLabel(self.quote_asset_wrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quote_asset_tooltip.sizePolicy().hasHeightForWidth())
        self.quote_asset_tooltip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.quote_asset_tooltip.setFont(font)
        self.quote_asset_tooltip.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.quote_asset_tooltip.setObjectName("quote_asset_tooltip")
        self.horizontalLayout_3.addWidget(self.quote_asset_tooltip)
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.quote_asset_wrap)
        self.fee_asset_wrap = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fee_asset_wrap.sizePolicy().hasHeightForWidth())
        self.fee_asset_wrap.setSizePolicy(sizePolicy)
        self.fee_asset_wrap.setMinimumSize(QtCore.QSize(120, 0))
        self.fee_asset_wrap.setMaximumSize(QtCore.QSize(120, 16777215))
        self.fee_asset_wrap.setObjectName("fee_asset_wrap")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fee_asset_wrap)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fee_asset_label = QtWidgets.QLabel(self.fee_asset_wrap)
        self.fee_asset_label.setMinimumSize(QtCore.QSize(0, 0))
        self.fee_asset_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fee_asset_label.setObjectName("fee_asset_label")
        self.horizontalLayout_5.addWidget(self.fee_asset_label)
        self.fee_asset_tooltip = QtWidgets.QLabel(self.fee_asset_wrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fee_asset_tooltip.sizePolicy().hasHeightForWidth())
        self.fee_asset_tooltip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fee_asset_tooltip.setFont(font)
        self.fee_asset_tooltip.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.fee_asset_tooltip.setObjectName("fee_asset_tooltip")
        self.horizontalLayout_5.addWidget(self.fee_asset_tooltip)
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.fee_asset_wrap)
        self.fee_asset_input = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fee_asset_input.sizePolicy().hasHeightForWidth())
        self.fee_asset_input.setSizePolicy(sizePolicy)
        self.fee_asset_input.setMinimumSize(QtCore.QSize(145, 0))
        self.fee_asset_input.setMaximumSize(QtCore.QSize(80, 16777215))
        self.fee_asset_input.setObjectName("fee_asset_input")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.fee_asset_input)
        self.base_asset_input = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.base_asset_input.sizePolicy().hasHeightForWidth())
        self.base_asset_input.setSizePolicy(sizePolicy)
        self.base_asset_input.setMinimumSize(QtCore.QSize(145, 0))
        self.base_asset_input.setMaximumSize(QtCore.QSize(145, 16777215))
        self.base_asset_input.setObjectName("base_asset_input")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.base_asset_input)
        self.operational_quote_wrap = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operational_quote_wrap.sizePolicy().hasHeightForWidth())
        self.operational_quote_wrap.setSizePolicy(sizePolicy)
        self.operational_quote_wrap.setMinimumSize(QtCore.QSize(120, 0))
        self.operational_quote_wrap.setMaximumSize(QtCore.QSize(120, 16777215))
        self.operational_quote_wrap.setObjectName("operational_quote_wrap")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.operational_quote_wrap)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.operational_quote_label = QtWidgets.QLabel(self.operational_quote_wrap)
        self.operational_quote_label.setMinimumSize(QtCore.QSize(0, 0))
        self.operational_quote_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.operational_quote_label.setObjectName("operational_quote_label")
        self.horizontalLayout_6.addWidget(self.operational_quote_label)
        self.operational_quote_tooltip = QtWidgets.QLabel(self.operational_quote_wrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operational_quote_tooltip.sizePolicy().hasHeightForWidth())
        self.operational_quote_tooltip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.operational_quote_tooltip.setFont(font)
        self.operational_quote_tooltip.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.operational_quote_tooltip.setObjectName("operational_quote_tooltip")
        self.horizontalLayout_6.addWidget(self.operational_quote_tooltip)
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.operational_quote_wrap)
        self.operational_base_wrap = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operational_base_wrap.sizePolicy().hasHeightForWidth())
        self.operational_base_wrap.setSizePolicy(sizePolicy)
        self.operational_base_wrap.setMinimumSize(QtCore.QSize(120, 0))
        self.operational_base_wrap.setMaximumSize(QtCore.QSize(120, 16777215))
        self.operational_base_wrap.setObjectName("operational_base_wrap")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.operational_base_wrap)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.operational_base_label = QtWidgets.QLabel(self.operational_base_wrap)
        self.operational_base_label.setMinimumSize(QtCore.QSize(0, 0))
        self.operational_base_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.operational_base_label.setObjectName("operational_base_label")
        self.horizontalLayout_7.addWidget(self.operational_base_label)
        self.operational_base_tooltip = QtWidgets.QLabel(self.operational_base_wrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operational_base_tooltip.sizePolicy().hasHeightForWidth())
        self.operational_base_tooltip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.operational_base_tooltip.setFont(font)
        self.operational_base_tooltip.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.operational_base_tooltip.setObjectName("operational_base_tooltip")
        self.horizontalLayout_7.addWidget(self.operational_base_tooltip)
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.operational_base_wrap)
        self.operational_percent_quote_input = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.operational_percent_quote_input.setMinimumSize(QtCore.QSize(145, 0))
        self.operational_percent_quote_input.setMaximumSize(QtCore.QSize(80, 16777215))
        self.operational_percent_quote_input.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.operational_percent_quote_input.setMouseTracking(True)
        self.operational_percent_quote_input.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.operational_percent_quote_input.setPrefix("")
        self.operational_percent_quote_input.setMaximum(100.0)
        self.operational_percent_quote_input.setSingleStep(1.0)
        self.operational_percent_quote_input.setObjectName("operational_percent_quote_input")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.operational_percent_quote_input)
        self.operational_percent_base_input = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.operational_percent_base_input.setMinimumSize(QtCore.QSize(145, 0))
        self.operational_percent_base_input.setMaximumSize(QtCore.QSize(80, 16777215))
        self.operational_percent_base_input.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.operational_percent_base_input.setMouseTracking(True)
        self.operational_percent_base_input.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.operational_percent_base_input.setPrefix("")
        self.operational_percent_base_input.setMaximum(100.0)
        self.operational_percent_base_input.setSingleStep(1.0)
        self.operational_percent_base_input.setObjectName("operational_percent_base_input")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.operational_percent_base_input)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout_2.setObjectName("formLayout_2")
        self.account_label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_label.sizePolicy().hasHeightForWidth())
        self.account_label.setSizePolicy(sizePolicy)
        self.account_label.setMinimumSize(QtCore.QSize(120, 0))
        self.account_label.setMaximumSize(QtCore.QSize(120, 16777215))
        self.account_label.setObjectName("account_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.account_label)
        self.account_name = QtWidgets.QLabel(self.groupBox_2)
        self.account_name.setText("")
        self.account_name.setObjectName("account_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_name)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.strategy_container = QtWidgets.QVBoxLayout(self.widget_2)
        self.strategy_container.setContentsMargins(0, 0, 0, 0)
        self.strategy_container.setObjectName("strategy_container")
        self.verticalLayout.addWidget(self.widget_2)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.remove_button = QtWidgets.QPushButton(self.widget)
        self.remove_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_button.setStyleSheet(" QPushButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #eb9994, stop: 1 #cc2522);\n"
"    min-width: 80px;\n"
"    min-height: 23px;\n"
"    color: #fff;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #ed9f9c, stop: 1 #db4240);\n"
" }\n"
"")
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout_2.addWidget(self.remove_button)
        spacerItem1 = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cancel_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.save_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_2.addWidget(self.save_button)
        self.verticalLayout.addWidget(self.widget)
        self.strategy_label.setBuddy(self.strategy_input)
        self.worker_name_label.setBuddy(self.worker_name_input)
        self.quote_asset_label.setBuddy(self.quote_asset_input)
        self.fee_asset_label.setBuddy(self.quote_asset_input)
        self.operational_quote_label.setBuddy(self.quote_asset_input)
        self.operational_base_label.setBuddy(self.quote_asset_input)

        self.retranslateUi(Dialog)
        self.strategy_input.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DEXBot - Edit Worker"))
        self.groupBox.setTitle(_translate("Dialog", "Worker Details"))
        self.strategy_label.setText(_translate("Dialog", "Strategy"))
        self.worker_name_label.setText(_translate("Dialog", "Worker Name"))
        self.base_asset_label.setText(_translate("Dialog", "Base Asset"))
        self.base_asset_tooltip.setToolTip(_translate("Dialog", "Asset to be used as unit of measure"))
        self.base_asset_tooltip.setText(_translate("Dialog", "?"))
        self.quote_asset_label.setText(_translate("Dialog", "Quote Asset"))
        self.quote_asset_tooltip.setToolTip(_translate("Dialog", "Asset to be bought and sold"))
        self.quote_asset_tooltip.setText(_translate("Dialog", "?"))
        self.fee_asset_label.setText(_translate("Dialog", "Fee asset"))
        self.fee_asset_tooltip.setToolTip(_translate("Dialog", "Asset to be used to pay transaction fees"))
        self.fee_asset_tooltip.setText(_translate("Dialog", "?"))
        self.fee_asset_input.setText(_translate("Dialog", "BTS"))
        self.operational_quote_label.setText(_translate("Dialog", "Operational QUOTE"))
        self.operational_quote_tooltip.setToolTip(_translate("Dialog", "Max % of QUOTE asset available to this worker, 0 - auto"))
        self.operational_quote_tooltip.setText(_translate("Dialog", "?"))
        self.operational_base_label.setText(_translate("Dialog", "Operational BASE"))
        self.operational_base_tooltip.setToolTip(_translate("Dialog", "Max % of BASE asset available to this worker, 0 - auto"))
        self.operational_base_tooltip.setText(_translate("Dialog", "?"))
        self.operational_percent_quote_input.setSuffix(_translate("Dialog", "%"))
        self.operational_percent_base_input.setSuffix(_translate("Dialog", "%"))
        self.groupBox_2.setTitle(_translate("Dialog", "Bitshares Account Details"))
        self.account_label.setText(_translate("Dialog", "Account"))
        self.remove_button.setText(_translate("Dialog", "Delete"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.save_button.setText(_translate("Dialog", "Save"))


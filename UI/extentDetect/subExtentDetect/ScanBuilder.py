# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScanBuilder.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScanBuildWiget(object):
    def setupUi(self, ScanBuildWiget):
        ScanBuildWiget.setObjectName("ScanBuildWiget")
        ScanBuildWiget.resize(495, 532)
        self.scrollArea = QtWidgets.QScrollArea(ScanBuildWiget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 471, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 469, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.te_html = Browser(self.scrollAreaWidgetContents)
        self.te_html.setGeometry(QtCore.QRect(0, 0, 471, 281))
        self.te_html.setObjectName("te_html")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(ScanBuildWiget)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 310, 471, 211))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 469, 209))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.te_res = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.te_res.setGeometry(QtCore.QRect(0, 0, 481, 211))
        self.te_res.setObjectName("te_res")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pb_back = QtWidgets.QPushButton(ScanBuildWiget)
        self.pb_back.setGeometry(QtCore.QRect(10, 0, 471, 28))
        self.pb_back.setObjectName("pb_back")

        self.retranslateUi(ScanBuildWiget)
        QtCore.QMetaObject.connectSlotsByName(ScanBuildWiget)

    def retranslateUi(self, ScanBuildWiget):
        _translate = QtCore.QCoreApplication.translate
        ScanBuildWiget.setWindowTitle(_translate("ScanBuildWiget", "Form"))
        self.pb_back.setText(_translate("ScanBuildWiget", "返回"))

from UI.ToolWidget.Browser import Browser

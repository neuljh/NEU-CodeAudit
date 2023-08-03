# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlawFinder.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FlawFinderWidget(object):
    def setupUi(self, FlawFinderWidget):
        FlawFinderWidget.setObjectName("FlawFinderWidget")
        FlawFinderWidget.resize(507, 541)
        self.scrollArea = QtWidgets.QScrollArea(FlawFinderWidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 491, 521))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.te_flawfinder = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.te_flawfinder.setGeometry(QtCore.QRect(0, 0, 491, 521))
        self.te_flawfinder.setObjectName("te_flawfinder")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(FlawFinderWidget)
        QtCore.QMetaObject.connectSlotsByName(FlawFinderWidget)

    def retranslateUi(self, FlawFinderWidget):
        _translate = QtCore.QCoreApplication.translate
        FlawFinderWidget.setWindowTitle(_translate("FlawFinderWidget", "Form"))


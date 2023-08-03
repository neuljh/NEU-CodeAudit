# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddDialog(object):
    def setupUi(self, AddDialog):
        AddDialog.setObjectName("AddDialog")
        AddDialog.resize(588, 426)
        AddDialog.setWhatsThis("")
        self.label = QtWidgets.QLabel(AddDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 31))
        self.label.setObjectName("label")
        self.FunctionNameText = QtWidgets.QTextEdit(AddDialog)
        self.FunctionNameText.setGeometry(QtCore.QRect(30, 60, 521, 41))
        self.FunctionNameText.setToolTip("")
        self.FunctionNameText.setStatusTip("")
        self.FunctionNameText.setObjectName("FunctionNameText")
        self.RiskLevelText = QtWidgets.QTextEdit(AddDialog)
        self.RiskLevelText.setGeometry(QtCore.QRect(30, 150, 521, 41))
        self.RiskLevelText.setObjectName("RiskLevelText")
        self.label_2 = QtWidgets.QLabel(AddDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 141, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 141, 31))
        self.label_3.setObjectName("label_3")
        self.SolutionText = QtWidgets.QPlainTextEdit(AddDialog)
        self.SolutionText.setGeometry(QtCore.QRect(30, 240, 521, 101))
        self.SolutionText.setObjectName("SolutionText")
        self.CancelPushButton = QtWidgets.QPushButton(AddDialog)
        self.CancelPushButton.setGeometry(QtCore.QRect(340, 367, 93, 41))
        self.CancelPushButton.setObjectName("CancelPushButton")
        self.AddPushButton = QtWidgets.QPushButton(AddDialog)
        self.AddPushButton.setGeometry(QtCore.QRect(460, 367, 93, 41))
        self.AddPushButton.setObjectName("AddPushButton")

        self.retranslateUi(AddDialog)
        QtCore.QMetaObject.connectSlotsByName(AddDialog)

    def retranslateUi(self, AddDialog):
        _translate = QtCore.QCoreApplication.translate
        AddDialog.setWindowTitle(_translate("AddDialog", "Dialog"))
        self.label.setText(_translate("AddDialog", "FunctionName"))
        self.FunctionNameText.setWhatsThis(_translate("AddDialog", "String"))
        self.FunctionNameText.setPlaceholderText(_translate("AddDialog", "String"))
        self.RiskLevelText.setPlaceholderText(_translate("AddDialog", "String"))
        self.label_2.setText(_translate("AddDialog", "RiskLevel"))
        self.label_3.setText(_translate("AddDialog", "Solution"))
        self.SolutionText.setPlaceholderText(_translate("AddDialog", "String"))
        self.CancelPushButton.setText(_translate("AddDialog", "取消"))
        self.AddPushButton.setText(_translate("AddDialog", "添加"))


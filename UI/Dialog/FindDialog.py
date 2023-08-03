# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FindDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FindDialog(object):
    def setupUi(self, FindDialog):
        FindDialog.setObjectName("FindDialog")
        FindDialog.resize(634, 158)
        self.label = QtWidgets.QLabel(FindDialog)
        self.label.setGeometry(QtCore.QRect(10, 45, 81, 31))
        self.label.setObjectName("label")
        self.FindPushButton = QtWidgets.QPushButton(FindDialog)
        self.FindPushButton.setGeometry(QtCore.QRect(350, 40, 121, 41))
        self.FindPushButton.setObjectName("FindPushButton")
        self.ReCheckBox = QtWidgets.QCheckBox(FindDialog)
        self.ReCheckBox.setGeometry(QtCore.QRect(110, 110, 141, 19))
        self.ReCheckBox.setObjectName("ReCheckBox")
        self.IgonreCheckBox = QtWidgets.QCheckBox(FindDialog)
        self.IgonreCheckBox.setGeometry(QtCore.QRect(270, 110, 111, 19))
        self.IgonreCheckBox.setObjectName("IgonreCheckBox")
        self.FindLineEdit = QtWidgets.QLineEdit(FindDialog)
        self.FindLineEdit.setGeometry(QtCore.QRect(110, 40, 221, 41))
        self.FindLineEdit.setObjectName("FindLineEdit")
        self.FindNextPushButton = QtWidgets.QPushButton(FindDialog)
        self.FindNextPushButton.setGeometry(QtCore.QRect(490, 40, 121, 41))
        self.FindNextPushButton.setObjectName("FindNextPushButton")
        self.number = QtWidgets.QLabel(FindDialog)
        self.number.setGeometry(QtCore.QRect(250, 20, 72, 15))
        self.number.setText("")
        self.number.setObjectName("number")

        self.retranslateUi(FindDialog)
        QtCore.QMetaObject.connectSlotsByName(FindDialog)

    def retranslateUi(self, FindDialog):
        _translate = QtCore.QCoreApplication.translate
        FindDialog.setWindowTitle(_translate("FindDialog", "Dialog"))
        self.label.setText(_translate("FindDialog", "查找字符串："))
        self.FindPushButton.setText(_translate("FindDialog", "查找全部"))
        self.ReCheckBox.setText(_translate("FindDialog", "支持正则表达式"))
        self.IgonreCheckBox.setText(_translate("FindDialog", "忽略大小写"))
        self.FindNextPushButton.setText(_translate("FindDialog", "查找下一个"))


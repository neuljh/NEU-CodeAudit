# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuzzWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Fuzz(object):
    def setupUi(self, Fuzz):
        Fuzz.setObjectName("Fuzz")
        Fuzz.resize(1327, 847)
        self.StringFuzzTableWidget = QtWidgets.QTableWidget(Fuzz)
        self.StringFuzzTableWidget.setGeometry(QtCore.QRect(460, 100, 401, 721))
        self.StringFuzzTableWidget.setStyleSheet("QTableWidget::horizontalHeader {\n"
"    background-color: #98b4d5;\n"
"}\n"
"")
        self.StringFuzzTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.StringFuzzTableWidget.setObjectName("StringFuzzTableWidget")
        self.StringFuzzTableWidget.setColumnCount(3)
        self.StringFuzzTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.StringFuzzTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.StringFuzzTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.StringFuzzTableWidget.setHorizontalHeaderItem(2, item)
        self.StringFuzzTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.DeletePushButton = QtWidgets.QPushButton(Fuzz)
        self.DeletePushButton.setGeometry(QtCore.QRect(1150, 30, 111, 41))
        self.DeletePushButton.setObjectName("DeletePushButton")
        self.RunPushButton = QtWidgets.QPushButton(Fuzz)
        self.RunPushButton.setGeometry(QtCore.QRect(240, 30, 111, 41))
        self.RunPushButton.setObjectName("RunPushButton")
        self.IntFuzzTableWidget = QtWidgets.QTableWidget(Fuzz)
        self.IntFuzzTableWidget.setGeometry(QtCore.QRect(30, 100, 401, 721))
        self.IntFuzzTableWidget.setStyleSheet("QTableWidget::horizontalHeader {\n"
"    background-color: #98b4d5;\n"
"}\n"
"")
        self.IntFuzzTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.IntFuzzTableWidget.setObjectName("IntFuzzTableWidget")
        self.IntFuzzTableWidget.setColumnCount(3)
        self.IntFuzzTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.IntFuzzTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.IntFuzzTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.IntFuzzTableWidget.setHorizontalHeaderItem(2, item)
        self.IntFuzzTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.ByteFuzzTableWidget = QtWidgets.QTableWidget(Fuzz)
        self.ByteFuzzTableWidget.setGeometry(QtCore.QRect(890, 100, 401, 721))
        self.ByteFuzzTableWidget.setStyleSheet("QTableWidget::horizontalHeader {\n"
"    background-color: #98b4d5;\n"
"}\n"
"")
        self.ByteFuzzTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.ByteFuzzTableWidget.setObjectName("ByteFuzzTableWidget")
        self.ByteFuzzTableWidget.setColumnCount(3)
        self.ByteFuzzTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ByteFuzzTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ByteFuzzTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ByteFuzzTableWidget.setHorizontalHeaderItem(2, item)
        self.ByteFuzzTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.comboBox = QtWidgets.QComboBox(Fuzz)
        self.comboBox.setGeometry(QtCore.QRect(90, 30, 111, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Fuzz)
        QtCore.QMetaObject.connectSlotsByName(Fuzz)

    def retranslateUi(self, Fuzz):
        _translate = QtCore.QCoreApplication.translate
        Fuzz.setWindowTitle(_translate("Fuzz", "Form"))
        item = self.StringFuzzTableWidget.horizontalHeaderItem(0)
        item.setWhatsThis(_translate("Fuzz", "QCheckBox"))
        item = self.StringFuzzTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Fuzz", "id"))
        item = self.StringFuzzTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Fuzz", "FuzzRandomString"))
        self.DeletePushButton.setText(_translate("Fuzz", "删除"))
        self.RunPushButton.setText(_translate("Fuzz", "生成"))
        item = self.IntFuzzTableWidget.horizontalHeaderItem(0)
        item.setWhatsThis(_translate("Fuzz", "QCheckBox"))
        item = self.IntFuzzTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Fuzz", "id"))
        item = self.IntFuzzTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Fuzz", "FuzzRandomInteger"))
        item = self.ByteFuzzTableWidget.horizontalHeaderItem(0)
        item.setWhatsThis(_translate("Fuzz", "QCheckBox"))
        item = self.ByteFuzzTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Fuzz", "id"))
        item = self.ByteFuzzTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Fuzz", "FuzzRandomByte"))
        self.comboBox.setItemText(0, _translate("Fuzz", "String"))
        self.comboBox.setItemText(1, _translate("Fuzz", "Integer"))
        self.comboBox.setItemText(2, _translate("Fuzz", "Byte"))


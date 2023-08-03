# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manageRiskFunctionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManageRiskFunction(object):
    def setupUi(self, ManageRiskFunction):
        ManageRiskFunction.setObjectName("ManageRiskFunction")
        ManageRiskFunction.resize(1333, 860)
        self.tabWidget = QtWidgets.QTabWidget(ManageRiskFunction)
        self.tabWidget.setGeometry(QtCore.QRect(14, 29, 1291, 831))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.AllRiskFuncTableWidget = QtWidgets.QTableWidget(self.tab)
        self.AllRiskFuncTableWidget.setGeometry(QtCore.QRect(10, 90, 1261, 681))
        self.AllRiskFuncTableWidget.setStyleSheet("QTableWidget::horizontalHeader {\n"
"    background-color: #98b4d5;\n"
"}\n"
"")
        self.AllRiskFuncTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.AllRiskFuncTableWidget.setObjectName("AllRiskFuncTableWidget")
        self.AllRiskFuncTableWidget.setColumnCount(4)
        self.AllRiskFuncTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.AllRiskFuncTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.AllRiskFuncTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.AllRiskFuncTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.AllRiskFuncTableWidget.setHorizontalHeaderItem(3, item)
        self.AllRiskFuncTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.AddPushButton = QtWidgets.QPushButton(self.tab)
        self.AddPushButton.setGeometry(QtCore.QRect(50, 30, 111, 41))
        self.AddPushButton.setObjectName("AddPushButton")
        self.DeletePushButton = QtWidgets.QPushButton(self.tab)
        self.DeletePushButton.setGeometry(QtCore.QRect(200, 30, 111, 41))
        self.DeletePushButton.setObjectName("DeletePushButton")
        self.FindPushButton = QtWidgets.QPushButton(self.tab)
        self.FindPushButton.setGeometry(QtCore.QRect(1090, 30, 111, 41))
        self.FindPushButton.setObjectName("FindPushButton")
        self.FindTextEdit = QtWidgets.QTextEdit(self.tab)
        self.FindTextEdit.setGeometry(QtCore.QRect(420, 30, 621, 41))
        self.FindTextEdit.setObjectName("FindTextEdit")
        self.picLable = QtWidgets.QLabel(self.tab)
        self.picLable.setGeometry(QtCore.QRect(380, 30, 41, 41))
        self.picLable.setText("")
        self.picLable.setObjectName("picLable")
        self.picLable2 = ClickableLabel(self.tab)
        self.picLable2.setGeometry(QtCore.QRect(1000, 30, 41, 41))
        self.picLable2.setText("")
        self.picLable2.setObjectName("picLable2")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(ManageRiskFunction)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ManageRiskFunction)

    def retranslateUi(self, ManageRiskFunction):
        _translate = QtCore.QCoreApplication.translate
        ManageRiskFunction.setWindowTitle(_translate("ManageRiskFunction", "Form"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(0)
        item.setWhatsThis(_translate("ManageRiskFunction", "QCheckBox"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ManageRiskFunction", "FunctionName"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ManageRiskFunction", "RiskLevel"))
        item = self.AllRiskFuncTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ManageRiskFunction", "Solution"))
        self.AddPushButton.setText(_translate("ManageRiskFunction", "新增"))
        self.DeletePushButton.setText(_translate("ManageRiskFunction", "删除"))
        self.FindPushButton.setText(_translate("ManageRiskFunction", "查找"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ManageRiskFunction", "风险函数管理"))

from UI.ToolWidget.ClickableLabel import ClickableLabel

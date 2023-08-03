# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extentWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_extent(object):
    def setupUi(self, extent):
        extent.setObjectName("extent")
        extent.resize(1342, 860)
        extent.setStyleSheet("/* 设置ComboBox字体大小为16 */\n"
"QComboBox {\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"/* 设置PushButton中设定的菜单字体大小为16 */\n"
"QPushButton::menu {\n"
"    font-size: 16px;\n"
"}\n"
"QTabWidget::tab {\n"
"    font-size: 16px;\n"
"}")
        self.commentTabWidget = QtWidgets.QTabWidget(extent)
        self.commentTabWidget.setGeometry(QtCore.QRect(280, 20, 1041, 821))
        self.commentTabWidget.setTabsClosable(True)
        self.commentTabWidget.setMovable(True)
        self.commentTabWidget.setObjectName("commentTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAcceptDrops(False)
        self.tab.setObjectName("tab")
        self.picLable = QtWidgets.QLabel(self.tab)
        self.picLable.setGeometry(QtCore.QRect(38, 110, 961, 401))
        self.picLable.setStyleSheet("QLabel {\n"
"    font-size: 30px; \n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.picLable.setText("")
        self.picLable.setObjectName("picLable")
        self.OpenPushButton = QtWidgets.QPushButton(self.tab)
        self.OpenPushButton.setGeometry(QtCore.QRect(360, 480, 311, 51))
        self.OpenPushButton.setObjectName("OpenPushButton")
        self.commentTabWidget.addTab(self.tab, "")
        self.ChooseActionPushButton = codeAuditMenuButton(extent)
        self.ChooseActionPushButton.setGeometry(QtCore.QRect(20, 30, 241, 41))
        self.ChooseActionPushButton.setObjectName("ChooseActionPushButton")
        self.scrollArea = QtWidgets.QScrollArea(extent)
        self.scrollArea.setGeometry(QtCore.QRect(20, 90, 241, 751))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 239, 749))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.treeView = QtWidgets.QTreeView(self.scrollAreaWidgetContents)
        self.treeView.setGeometry(QtCore.QRect(0, 40, 241, 781))
        self.treeView.setObjectName("treeView")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 16))
        self.label.setObjectName("label")
        self.ChooseComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.ChooseComboBox.setGeometry(QtCore.QRect(120, 10, 111, 22))
        self.ChooseComboBox.setObjectName("ChooseComboBox")
        self.ChooseComboBox.addItem("")
        self.ChooseComboBox.addItem("")
        self.ChooseComboBox.addItem("")
        self.ChooseComboBox.addItem("")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(extent)
        self.commentTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(extent)

    def retranslateUi(self, extent):
        _translate = QtCore.QCoreApplication.translate
        extent.setWindowTitle(_translate("extent", "Form"))
        self.OpenPushButton.setText(_translate("extent", "打开文件夹"))
        self.commentTabWidget.setTabText(self.commentTabWidget.indexOf(self.tab), _translate("extent", "开始"))
        self.ChooseActionPushButton.setText(_translate("extent", "选择"))
        self.label.setText(_translate("extent", "文件目录"))
        self.ChooseComboBox.setItemText(0, _translate("extent", "*"))
        self.ChooseComboBox.setItemText(1, _translate("extent", "*.c"))
        self.ChooseComboBox.setItemText(2, _translate("extent", "*.h"))
        self.ChooseComboBox.setItemText(3, _translate("extent", "*.c,*.h"))

from UI.ToolWidget.codeAuditMenuButton import codeAuditMenuButton

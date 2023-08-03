# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'codeAuditWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CodeAudit(object):
    def setupUi(self, CodeAudit):
        CodeAudit.setObjectName("CodeAudit")
        CodeAudit.resize(1330, 859)
        CodeAudit.setStyleSheet("/* 设置ComboBox字体大小为16 */\n"
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
        self.scrollArea = QtWidgets.QScrollArea(CodeAudit)
        self.scrollArea.setGeometry(QtCore.QRect(20, 90, 281, 751))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 749))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.treeView = QtWidgets.QTreeView(self.scrollAreaWidgetContents)
        self.treeView.setGeometry(QtCore.QRect(0, 40, 281, 781))
        self.treeView.setObjectName("treeView")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 16))
        self.label.setObjectName("label")
        self.ChooseComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.ChooseComboBox.setGeometry(QtCore.QRect(150, 10, 111, 22))
        self.ChooseComboBox.setObjectName("ChooseComboBox")
        self.ChooseComboBox.addItem("")
        self.ChooseComboBox.addItem("")
        self.ChooseComboBox.addItem("")
        self.ChooseComboBox.addItem("")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.commentTabWidget = QtWidgets.QTabWidget(CodeAudit)
        self.commentTabWidget.setGeometry(QtCore.QRect(330, 20, 971, 821))
        self.commentTabWidget.setStyleSheet("QTabWidget::tab {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.commentTabWidget.setTabsClosable(True)
        self.commentTabWidget.setMovable(True)
        self.commentTabWidget.setObjectName("commentTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAcceptDrops(False)
        self.tab.setObjectName("tab")
        self.picLable = QtWidgets.QLabel(self.tab)
        self.picLable.setGeometry(QtCore.QRect(0, 130, 961, 401))
        self.picLable.setStyleSheet("QLabel {\n"
"    font-size: 30px; \n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.picLable.setText("")
        self.picLable.setObjectName("picLable")
        self.OpenPushButton = QtWidgets.QPushButton(self.tab)
        self.OpenPushButton.setGeometry(QtCore.QRect(322, 500, 311, 51))
        self.OpenPushButton.setObjectName("OpenPushButton")
        self.commentTabWidget.addTab(self.tab, "")
        self.ChooseActionPushButton = codeAuditMenuButton(CodeAudit)
        self.ChooseActionPushButton.setGeometry(QtCore.QRect(20, 30, 281, 41))
        self.ChooseActionPushButton.setObjectName("ChooseActionPushButton")

        self.retranslateUi(CodeAudit)
        self.commentTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CodeAudit)

    def retranslateUi(self, CodeAudit):
        _translate = QtCore.QCoreApplication.translate
        CodeAudit.setWindowTitle(_translate("CodeAudit", "Form"))
        self.label.setText(_translate("CodeAudit", "文件目录"))
        self.ChooseComboBox.setItemText(0, _translate("CodeAudit", "*"))
        self.ChooseComboBox.setItemText(1, _translate("CodeAudit", "*.c"))
        self.ChooseComboBox.setItemText(2, _translate("CodeAudit", "*.h"))
        self.ChooseComboBox.setItemText(3, _translate("CodeAudit", "*.c,*.h"))
        self.OpenPushButton.setText(_translate("CodeAudit", "打开文件夹"))
        self.commentTabWidget.setTabText(self.commentTabWidget.indexOf(self.tab), _translate("CodeAudit", "开始"))
        self.ChooseActionPushButton.setText(_translate("CodeAudit", "选择"))

from UI.ToolWidget.codeAuditMenuButton import codeAuditMenuButton

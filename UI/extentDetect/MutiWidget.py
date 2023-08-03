# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MutiWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MutiWidget(object):
    def setupUi(self, MutiWidget):
        MutiWidget.setObjectName("MutiWidget")
        MutiWidget.resize(1038, 820)
        self.scrollArea = QtWidgets.QScrollArea(MutiWidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 501, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 499, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.CodeEditor = NewCodeEditor(self.scrollAreaWidgetContents)
        self.CodeEditor.setGeometry(QtCore.QRect(-10, 0, 511, 551))
        self.CodeEditor.setStyleSheet("QTextEdit{\n"
"    background-color: #ffffff\n"
"}")
        self.CodeEditor.setObjectName("CodeEditor")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.detectWidget = QtWidgets.QTabWidget(MutiWidget)
        self.detectWidget.setGeometry(QtCore.QRect(520, 50, 501, 561))
        self.detectWidget.setTabsClosable(True)
        self.detectWidget.setObjectName("detectWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pb_detect_start = detectMenuButton(self.tab_3)
        self.pb_detect_start.setGeometry(QtCore.QRect(100, 350, 251, 51))
        self.pb_detect_start.setStyleSheet("QPushButton::menu {\n"
"    font-size: 14px;\n"
"}")
        self.pb_detect_start.setObjectName("pb_detect_start")
        self.picLable = QtWidgets.QLabel(self.tab_3)
        self.picLable.setGeometry(QtCore.QRect(10, 60, 471, 291))
        self.picLable.setStyleSheet("QLabel {\n"
"    font-size: 30px; \n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.picLable.setText("")
        self.picLable.setObjectName("picLable")
        self.detectWidget.addTab(self.tab_3, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(MutiWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 501, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_format = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pb_format.setStyleSheet("QPushButton::menu {\n"
"    font-size: 13px;\n"
"}")
        self.pb_format.setObjectName("pb_format")
        self.horizontalLayout.addWidget(self.pb_format)
        self.pb_compile = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pb_compile.setStyleSheet("QPushButton::menu {\n"
"    font-size: 13px;\n"
"}")
        self.pb_compile.setObjectName("pb_compile")
        self.horizontalLayout.addWidget(self.pb_compile)
        self.pb_run = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pb_run.setStyleSheet("QPushButton::menu {\n"
"    font-size: 13px;\n"
"}")
        self.pb_run.setObjectName("pb_run")
        self.horizontalLayout.addWidget(self.pb_run)
        self.pb_detect = detectMenuButton(self.horizontalLayoutWidget)
        self.pb_detect.setStyleSheet("QPushButton::menu {\n"
"    font-size: 13px;\n"
"}")
        self.pb_detect.setObjectName("pb_detect")
        self.horizontalLayout.addWidget(self.pb_detect)
        self.pushButton = ProjectMenuButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.LogAndCmd = QtWidgets.QTabWidget(MutiWidget)
        self.LogAndCmd.setGeometry(QtCore.QRect(0, 620, 1021, 171))
        self.LogAndCmd.setObjectName("LogAndCmd")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 1021, 151))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1019, 149))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.te_log = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.te_log.setGeometry(QtCore.QRect(0, 0, 1011, 141))
        self.te_log.setObjectName("te_log")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.LogAndCmd.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_3.setGeometry(QtCore.QRect(0, 0, 1021, 141))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1019, 139))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.te_cmd = CmdTextEdit(self.scrollAreaWidgetContents_3)
        self.te_cmd.setGeometry(QtCore.QRect(0, 0, 1021, 141))
        self.te_cmd.setObjectName("te_cmd")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.LogAndCmd.addTab(self.tab_2, "")
        self.pb_generate_2 = QtWidgets.QPushButton(MutiWidget)
        self.pb_generate_2.setGeometry(QtCore.QRect(858, 20, 161, 28))
        self.pb_generate_2.setStyleSheet("QPushButton::menu {\n"
"    font-size: 13px;\n"
"}")
        self.pb_generate_2.setObjectName("pb_generate_2")

        self.retranslateUi(MutiWidget)
        self.detectWidget.setCurrentIndex(0)
        self.LogAndCmd.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MutiWidget)

    def retranslateUi(self, MutiWidget):
        _translate = QtCore.QCoreApplication.translate
        MutiWidget.setWindowTitle(_translate("MutiWidget", "Form"))
        self.pb_detect_start.setText(_translate("MutiWidget", "选择静态检测工具"))
        self.detectWidget.setTabText(self.detectWidget.indexOf(self.tab_3), _translate("MutiWidget", "开始"))
        self.pb_format.setText(_translate("MutiWidget", "规范代码格式"))
        self.pb_compile.setText(_translate("MutiWidget", "编译"))
        self.pb_run.setText(_translate("MutiWidget", "运行"))
        self.pb_detect.setText(_translate("MutiWidget", "静态检测"))
        self.pushButton.setText(_translate("MutiWidget", "项目"))
        self.LogAndCmd.setTabText(self.LogAndCmd.indexOf(self.tab), _translate("MutiWidget", "Log Information"))
        self.LogAndCmd.setTabText(self.LogAndCmd.indexOf(self.tab_2), _translate("MutiWidget", "CMD"))
        self.pb_generate_2.setText(_translate("MutiWidget", "生成审计报告"))

from UI.ToolWidget.ProjectMenuButton import ProjectMenuButton
from UI.ToolWidget.CmdTextEditor import CmdTextEdit
from UI.ToolWidget.NewCodeEditor import NewCodeEditor
from UI.ToolWidget.detectMenuButton import detectMenuButton

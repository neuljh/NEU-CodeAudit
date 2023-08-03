# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(1487, 869)
        menu.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"}\n"
"QLabel {\n"
"    font-size: 15px; \n"
"}\n"
"\n"
"/* 设置ComboBox字体大小为16 */\n"
"QComboBox {\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"/* 设置PushButton中设定的菜单字体大小为16 */\n"
"QPushButton::menu {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.widget = QtWidgets.QWidget(menu)
        self.widget.setGeometry(QtCore.QRect(10, 0, 131, 611))
        self.widget.setObjectName("widget")
        self.ExitPushButton = QtWidgets.QPushButton(self.widget)
        self.ExitPushButton.setGeometry(QtCore.QRect(0, 550, 131, 61))
        self.ExitPushButton.setObjectName("ExitPushButton")
        self.Page3pushButton = QtWidgets.QPushButton(self.widget)
        self.Page3pushButton.setGeometry(QtCore.QRect(0, 440, 131, 61))
        self.Page3pushButton.setObjectName("Page3pushButton")
        self.Page2pushButton = QtWidgets.QPushButton(self.widget)
        self.Page2pushButton.setGeometry(QtCore.QRect(0, 330, 131, 61))
        self.Page2pushButton.setObjectName("Page2pushButton")
        self.Page1pushButton = QtWidgets.QPushButton(self.widget)
        self.Page1pushButton.setGeometry(QtCore.QRect(0, 220, 131, 61))
        self.Page1pushButton.setObjectName("Page1pushButton")
        self.picLable = QtWidgets.QLabel(self.widget)
        self.picLable.setGeometry(QtCore.QRect(1, 4, 131, 121))
        self.picLable.setText("")
        self.picLable.setObjectName("picLable")
        self.ChangeStackedWidget = QtWidgets.QStackedWidget(menu)
        self.ChangeStackedWidget.setGeometry(QtCore.QRect(150, 9, 1321, 841))
        self.ChangeStackedWidget.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"}\n"
"QLabel {\n"
"    font-size: 15px; \n"
"}\n"
"\n"
"/* 设置ComboBox字体大小为16 */\n"
"QComboBox {\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"/* 设置PushButton中设定的菜单字体大小为16 */\n"
"QPushButton::menu {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.ChangeStackedWidget.setObjectName("ChangeStackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.ChangeStackedWidget.addWidget(self.page1)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.picLable2 = QtWidgets.QLabel(self.page)
        self.picLable2.setGeometry(QtCore.QRect(80, 70, 1231, 671))
        self.picLable2.setText("")
        self.picLable2.setObjectName("picLable2")
        self.ChangeStackedWidget.addWidget(self.page)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.ChangeStackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.ChangeStackedWidget.addWidget(self.page3)
        self.HidePushButton = QtWidgets.QPushButton(menu)
        self.HidePushButton.setGeometry(QtCore.QRect(0, 820, 31, 31))
        self.HidePushButton.setObjectName("HidePushButton")

        self.retranslateUi(menu)
        self.ChangeStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Form"))
        self.ExitPushButton.setText(_translate("menu", "退出"))
        self.Page3pushButton.setText(_translate("menu", "扩展应用"))
        self.Page2pushButton.setText(_translate("menu", "审计管理"))
        self.Page1pushButton.setText(_translate("menu", "代码审计"))
        self.HidePushButton.setText(_translate("menu", "<"))


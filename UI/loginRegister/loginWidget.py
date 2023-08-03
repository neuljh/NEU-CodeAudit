# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1038, 521)
        Login.setStyleSheet("")
        self.LoginButton = QtWidgets.QPushButton(Login)
        self.LoginButton.setGeometry(QtCore.QRect(692, 350, 301, 41))
        self.LoginButton.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"}")
        self.LoginButton.setObjectName("LoginButton")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(691, 54, 291, 41))
        self.label.setStyleSheet("QLabel {\n"
"    font-size: 30px; \n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(690, 140, 301, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.UserNameEdit = QtWidgets.QLineEdit(self.frame)
        self.UserNameEdit.setGeometry(QtCore.QRect(90, 10, 191, 31))
        self.UserNameEdit.setStyleSheet("QLineEdit{\n"
"    font-size: 15px; \n"
"}")
        self.UserNameEdit.setObjectName("UserNameEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 0, 61, 51))
        self.label_2.setStyleSheet("QLabel {\n"
"    font-size: 15px; \n"
"    qproperty-alignment: AlignCenter;\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.picLable1 = QtWidgets.QLabel(self.frame)
        self.picLable1.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.picLable1.setText("")
        self.picLable1.setObjectName("picLable1")
        self.frame_2 = QtWidgets.QFrame(Login)
        self.frame_2.setGeometry(QtCore.QRect(690, 220, 301, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.PassWordEdit = QtWidgets.QLineEdit(self.frame_2)
        self.PassWordEdit.setGeometry(QtCore.QRect(90, 10, 191, 31))
        self.PassWordEdit.setObjectName("PassWordEdit")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 51, 31))
        self.label_3.setStyleSheet("QLabel {\n"
"    font-size: 15px; \n"
"}")
        self.label_3.setObjectName("label_3")
        self.picLable2 = QtWidgets.QLabel(self.frame_2)
        self.picLable2.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.picLable2.setText("")
        self.picLable2.setObjectName("picLable2")
        self.RegisterButton = QtWidgets.QPushButton(Login)
        self.RegisterButton.setGeometry(QtCore.QRect(690, 420, 301, 41))
        self.RegisterButton.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"}")
        self.RegisterButton.setObjectName("RegisterButton")
        self.RememberPwcheckBox = QtWidgets.QCheckBox(Login)
        self.RememberPwcheckBox.setGeometry(QtCore.QRect(690, 290, 101, 31))
        self.RememberPwcheckBox.setStyleSheet("QCheckBox{\n"
"    font-size: 14px; \n"
"}")
        self.RememberPwcheckBox.setObjectName("RememberPwcheckBox")
        self.ForgetPwButton = QtWidgets.QPushButton(Login)
        self.ForgetPwButton.setGeometry(QtCore.QRect(900, 290, 93, 31))
        self.ForgetPwButton.setStyleSheet("QPushButton {\n"
"    font-size: 13px;\n"
"}\n"
"")
        self.ForgetPwButton.setObjectName("ForgetPwButton")
        self.picLable3 = QtWidgets.QLabel(Login)
        self.picLable3.setGeometry(QtCore.QRect(1, 4, 631, 511))
        self.picLable3.setText("")
        self.picLable3.setObjectName("picLable3")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.LoginButton.setText(_translate("Login", "登陆"))
        self.label.setText(_translate("Login", "NeuCodeAudit"))
        self.label_2.setText(_translate("Login", "用户名"))
        self.label_3.setText(_translate("Login", " 密码"))
        self.RegisterButton.setText(_translate("Login", "注册"))
        self.RememberPwcheckBox.setText(_translate("Login", "记住密码"))
        self.ForgetPwButton.setText(_translate("Login", "找回密码"))


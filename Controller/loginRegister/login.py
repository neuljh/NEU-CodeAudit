from PyQt5.QtCore import QFile, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *
from qtpy import QtCore

from Data.leanCloud import UserQuery
from UI.loginRegister.loginWidget import Ui_Login
from Controller.loginRegister.register import MainRegistWindow

from Controller.mainWindow.menu import Menu

import sys
import configparser
import os
from Data.crypto import *

from qt_material import apply_stylesheet

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

global UserName
UserP = {}  # 定义一个存储密码账号的元组

class MainLoginWindow(QWidget, Ui_Login):
    def __init__(self, parent=None):
        super(MainLoginWindow, self).__init__(parent)
        self.re = MainRegistWindow()  # 这边一定要加self
        self.mainWin = Menu()
        self.setupUi(self)

        self.account = ""
        self.passwd = ""
        self.filePath = os.path.dirname(os.path.dirname(os.getcwd()))+"\\Data\\user.ini"

        self.initUi()

    def initUi(self):

        self.setWindowIcon(QIcon(os.path.dirname(os.path.dirname(os.getcwd()))+"\\UI\\picture\\all.ico"))
        self.setWindowTitle("NeuCodeAudit")

        pixmap1 = QPixmap(os.path.dirname(os.path.dirname(os.getcwd()))+"\\UI\\picture\\user-line.png")
        pixmap2 = QPixmap(os.path.dirname(os.path.dirname(os.getcwd()))+"\\UI\\picture\\key-2-line.png")
        pixmap3 = QPixmap(os.path.dirname(os.path.dirname(os.getcwd()))+"\\UI\\picture\\picLogin1.jpg")
        pixmap3 = pixmap3.scaled(850, 800, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.picLable1.setPixmap(pixmap1)
        self.picLable2.setPixmap(pixmap2)
        self.picLable3.setPixmap(pixmap3)
        self.picLable3.setAlignment(Qt.AlignCenter)

        self.IsRememberUser()
        self.UserNameEdit.setFocus()
        self.UserNameEdit.setPlaceholderText("请输入账号")
        self.PassWordEdit.setPlaceholderText("请输入密码")
        self.PassWordEdit.setEchoMode(QLineEdit.Password)  # 密码隐藏

        self.RegisterButton.clicked.connect(self.regist_button)  # 跳转到注册页面
        self.re.SuccessReg.connect(self.Success_Regist)  # 注册成功跳转回来
        self.re.ReturnLogin.connect(self.Return_Login)  # 返回 跳转回来
        self.LoginButton.clicked.connect(self.login_button)  # 登录

    """设置记住密码"""
    def IsRememberUser(self):
        print(self.filePath)
        config = configparser.ConfigParser()
        file = config.read(self.filePath)  # 读取密码账户的配置文件
        print(self.filePath)
        config_dict = config.defaults()  # 返回包含实例范围默认值的字典
        self.account = config_dict['user_name']  # 获取账号信息
        self.UserNameEdit.setText(self.account)  # 写入账号上面
        if config_dict['remember'] == 'True':
            self.passwd = config_dict['password']
            self.PassWordEdit.setText(self.passwd)
            self.RememberPwcheckBox.setChecked(True)
        else:
            self.RememberPwcheckBox.setChecked(False)

    """设置配置文件格式"""
    def config_ini(self):
        self.account = self.UserNameEdit.text()
        self.passwd = self.PassWordEdit.text()
        config = configparser.ConfigParser()
        if self.RememberPwcheckBox.isChecked():
            config["DEFAULT"] = {
                "user_name": self.account,
                "password": self.passwd,
                "remember": self.RememberPwcheckBox.isChecked()
            }
        else:
            config["DEFAULT"] = {
                "user_name": self.account,
                "password": "",
                "remember": self.RememberPwcheckBox.isChecked()
            }
        with open(self.filePath, 'w') as configfile:
            config.write(configfile)
        print(self.account, self.passwd)

    # 注册
    def regist_button(self):
        # 载入数据库
        # self.sql = Oper_Mysql()
        # self.sql.ZSGC_Mysql()
        self.re.show()
        self.close()

    # 登录
    def login_button(self):

        Login_UserName = self.UserNameEdit.text()
        Login_Passwd = self.PassWordEdit.text()

        if Login_UserName.strip() == '' or Login_Passwd.strip() == '':
            QMessageBox.information(self, "error", "请输入用户名和密码！")
        else:
            self.config_ini()  # 加载用户密码配置文件
            query_Passwd = UserQuery(Login_UserName)
            if query_Passwd == None:
                QMessageBox.information(self, "waining", "该账号不存在！", QMessageBox.Ok)
                return False
            else:
                if checkPasswd(Login_Passwd, query_Passwd):  # 登陆成功
                    mess = QMessageBox(self)
                    mess.setWindowTitle("成功")
                    mess.setText("登录成功！")
                    mess.setStandardButtons(QMessageBox.Ok)
                    mess.button(QMessageBox.Ok).animateClick(1000)  # 弹框定时关闭
                    mess.exec_()
                    self.mainWin.show()
                    self.close()  # 关闭 LoginWin
                    return True
                else:
                    QMessageBox.information(self, "error!", "密码错误！", QMessageBox.Ok)
                    return False

    # 成功注册
    def Success_Regist(self):
        self.show()
        self.re.close()

    # 返回
    def Return_Login(self):
        self.show()
        self.re.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    LoginWin = MainLoginWindow()

    path = os.path.dirname(os.path.dirname(os.getcwd()))+"\\UI\\theme_set\\my_theme.xml"

    # setup stylesheet
    apply_stylesheet(app, theme=path)
    # apply_stylesheet(app, theme='light_cyan_500.xml', invert_secondary=True)

    LoginWin.show()
    sys.exit(app.exec())


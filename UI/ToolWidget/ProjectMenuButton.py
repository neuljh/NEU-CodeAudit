# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ProjectMenuButton(QPushButton):
    def __init__(self, parent):
        super(ProjectMenuButton, self).__init__(parent)
        self.parent = parent
        self.createContextMenu()

        self.menu_visible = False  # 菜单是否可见

        # 连接鼠标悬停事件
        self.setMouseTracking(True)

    def createContextMenu(self):
        # 创建右键菜单
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.showContextMenu)

        # 创建QMenu
        self.contextMenu = QMenu(self)
        self.actionA = self.contextMenu.addAction('项目编译')
        self.actionB = self.contextMenu.addAction('项目ClangChecker扫描')
        self.actionC = self.contextMenu.addAction('项目CppChecker扫描')
        self.actionD = self.contextMenu.addAction('项目内存泄漏检测')
        # 将动作与处理函数相关联
        # self.actionA.triggered.connect(self.parent.hello)
        # self.actionB.triggered.connect(self.parent.show_find_dialog)
        # self.actionC.triggered.connect(self.parent.show_save_dialog)
        # self.actionD.triggered.connect(self.parent.show_save_another_dialog)
        # self.actionE.triggered.connect(self.parent.show_save_dialog)
        # self.actionF.triggered.connect(self.parent.show_save_another_dialog)

    def showContextMenu(self, pos):
        self.contextMenu.exec_(self.mapToGlobal(pos))

    def mousePressEvent(self, event):
        # 鼠标按下
        # print("mousePressEvent")
        QPushButton.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        # 鼠标松开
        # print("mouseReleaseEvent")
        QPushButton.mouseReleaseEvent(self, event)

    def enterEvent(self, event):
        if not self.menu_visible:
            self.menu_visible = True
            self.showContextMenu(QPoint(0, self.height()))

    def leaveEvent(self, event):
        if self.menu_visible:
            self.menu_visible = False
            self.contextMenu.hide()
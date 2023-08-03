from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

global temp
temp = 0


class UIFunction(QWidget):
    widthChanged = pyqtSignal(int)  # 创建一个信号

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.menu_visible = False
        self.sign = self.parent.HidePushButton.text()

    def MeauFunction(self):
        self.sign = self.parent.HidePushButton.text()
        if self.sign == ">":
            TarGet = self.parent.widget
            animation = QPropertyAnimation(TarGet)
            animation.setTargetObject(TarGet)
            animation.setPropertyName(b"geometry")
            animation.setStartValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
                                          TarGet.geometry().width(),
                                          TarGet.geometry().height()))
            animation.setEndValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
                                        0,
                                        TarGet.geometry().height()))

            animation.setDuration(200)
            animation.start()

            stackedWidget = self.parent.ChangeStackedWidget
            stackedWidget.setGeometry(QRect(stackedWidget.geometry().x() - 131,
                                            stackedWidget.geometry().y(),
                                            stackedWidget.geometry().width(),
                                            stackedWidget.geometry().height()))

            # current_width = self.parent().width()
            # new_width = current_width - 131
            # self.parent().resize(new_width, self.parent().height())
            self.widthChanged.emit(-131)  # 发送信号

        elif self.sign == "<":
            TarGet = self.parent.widget
            animation = QPropertyAnimation(TarGet)
            animation.setTargetObject(TarGet)
            animation.setPropertyName(b"geometry")
            animation.setStartValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
                                          TarGet.geometry().width(),
                                          TarGet.geometry().height()))
            animation.setEndValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
                                            131,
                                            941))
            # animation.setEndValue(QRect(TarGet.geometry().x(), TarGet.geometry().y(),
            #                             TarGet.geometry().width(),
            #                             TarGet.geometry().height()))
            animation.setDuration(200)
            animation.start()

            stackedWidget = self.parent.ChangeStackedWidget
            stackedWidget.setGeometry(QRect(stackedWidget.geometry().x() + 131,
                                            stackedWidget.geometry().y(),
                                            stackedWidget.geometry().width(),
                                            stackedWidget.geometry().height()))

            # current_width = self.parent().width()
            # new_width = current_width + 131
            # self.parent().resize(new_width, self.parent().height())
            self.widthChanged.emit(131)  # 发送信号

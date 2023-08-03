from PyQt5.QtCore import pyqtSignal, Qt, QRect
from PyQt5.QtWidgets import QHeaderView, QStyleOptionButton, QStyle


class CheckBoxHeader(QHeaderView):
    clicked = pyqtSignal(int, bool)  # 关键点自定义信号槽，传入了2个参数记录当前选中状态
    _x_offset = 3
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, column_indices, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.setSectionResizeMode(QHeaderView.Stretch)
        self.setSectionsClickable(True)

        if isinstance(column_indices, list) or isinstance(column_indices, tuple):
            self.column_indices = column_indices
        elif isinstance(column_indices, int):
            self.column_indices = [column_indices]
        else:
            raise RuntimeError('column_indices must be a list, tuple or integer')

        self.isChecked = {}
        for column in self.column_indices:
            self.isChecked[column] = 0

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()
        self._y_offset = int((rect.height() - self._width) / 2.)
        if logicalIndex in self.column_indices:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isChecked[logicalIndex] == 2:
                option.state |= QStyle.State_NoChange
            elif self.isChecked[logicalIndex]:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def updateCheckState(self, index, state):
        '''
        记录每个点击checkbox 状态及序号存入dict
        :param index:
        :param state:
        :return:
        '''
        self.isChecked[index] = state
        self.viewport().update()

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 <= index < self.count():
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isChecked[index] == 1:
                    self.isChecked[index] = 0
                else:
                    self.isChecked[index] = 1
                self.clicked.emit(index, self.isChecked[index])
                self.viewport().update()
            else:
                super(CheckBoxHeader, self).mousePressEvent(event)
        else:
            super(CheckBoxHeader, self).mousePressEvent(event)
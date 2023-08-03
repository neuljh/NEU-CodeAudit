import os

from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QTextCursor, QColor, QTextCharFormat, QIcon
from PyQt5.QtWidgets import QTextEdit

from UI.Dialog.FindDialog import *
from UI.Main import *


class FindDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.ui = Ui_FindDialog()
        self.ui.setupUi(self)

        self.initUI()

        self.sign = True
        self.current_index = 0  # 当前匹配字符串的索引位置
        self.cursor = None
        self.previous_cursor = None
        self.plain_text_edit = None
        self.connectSignalsSlots()

    def unhighlight_text(self):
        if self.plain_text_edit is not None:
            self.plain_text_edit.setExtraSelections([])

    def closeEvent(self, event):
        if self.previous_cursor is not None:
            format = self.previous_cursor.blockFormat()
            format.setBackground(QColor("#FFFFFF"))
            self.previous_cursor.setBlockFormat(format)
            # 将光标设置为初始位置
            self.previous_cursor.movePosition(QTextCursor.StartOfBlock)
            self.previous_cursor.setPosition(self.previous_cursor.position() + len(self.previous_cursor.block().text()),
                                             QTextCursor.KeepAnchor)
        self.unhighlight_text()
        # 调用父类的 closeEvent 方法继续执行默认的关闭操作
        super().closeEvent(event)

    def initUI(self):
        self.setWindowTitle("查找")
        self.setWindowIcon(QIcon(os.path.dirname(os.path.dirname(os.getcwd()))+"\\UI\\picture\\all.ico"))

        self.ui.ReCheckBox.setChecked(False)
        self.ui.ReCheckBox.setEnabled(True)
        self.ui.IgonreCheckBox.setChecked(True)
        self.ui.IgonreCheckBox.setEnabled(False)

    def connectSignalsSlots(self):
        self.ui.FindPushButton.clicked.connect(self.find_text)
        self.ui.FindNextPushButton.clicked.connect(self.find_text_onebyone)

    def find_text(self):
        search_text = self.ui.FindLineEdit.text()
        if search_text:
            main_window = self.parent
            if isinstance(main_window, QtWidgets.QWidget):
                text_edit = main_window.findChild(QTextEdit, 'commentCodeEditor')
                self.plain_text_edit = text_edit
                self.highlight_text(text_edit, search_text)

    def highlight_text(self, plain_text_edit, search_text):
        # cursor = plain_text_edit.textCursor()
        format = QTextCharFormat()
        format.setBackground(QColor("#92acdc"))
        extra_selections = []
        plain_text_edit.moveCursor(QTextCursor.Start)
        cursor = plain_text_edit.textCursor()
        while cursor.hasComplexSelection() or cursor.atEnd() == False:
            is_ReCheck = self.ui.ReCheckBox.isChecked()
            if is_ReCheck:
                # cursor = plain_text_edit.document().find(search_text, cursor)
                regex = QRegularExpression(search_text)
                cursor = plain_text_edit.document().find(regex, cursor)
            else:
                cursor = plain_text_edit.document().find(search_text, cursor)
            if cursor.isNull() == False:
                selection = QTextEdit.ExtraSelection()
                selection.format = format
                selection.cursor = QTextCursor(cursor)
                extra_selections.append(selection)
            else:
                break
        plain_text_edit.setExtraSelections(extra_selections)

    def find_text_onebyone(self):
        if self.sign:
            self.find_text()
            self.sign = False
        main_window = self.parent
        if isinstance(main_window, QtWidgets.QWidget):
            text_edit = main_window.findChild(QTextEdit, 'commentCodeEditor')
            selections = text_edit.extraSelections()
            if self.current_index == len(selections):
                self.current_index = 0  # 若已到达最后一个匹配字符串，则从第一个开始

            if self.current_index < len(selections):
                self.cursor = QTextCursor(selections[self.current_index].cursor)
                text_edit.setTextCursor(self.cursor)

                # 设置行的格式
                format = self.cursor.blockFormat()
                format.setBackground(QColor("#92cedc"))
                self.cursor.setBlockFormat(format)
                # 将光标设置为初始位置
                self.cursor.movePosition(QTextCursor.StartOfBlock)
                self.cursor.setPosition(self.cursor.position() + len(self.cursor.block().text()), QTextCursor.KeepAnchor)
                line_number = self.cursor.blockNumber()

                if self.current_index >= 0 and self.previous_cursor is not None:
                    # self.previous_cursor = QTextCursor(selections[self.current_index - 1].cursor)
                    pre_line_number = self.previous_cursor.blockNumber()
                    if line_number != pre_line_number:
                        # 设置行的格式
                        format = self.previous_cursor.blockFormat()
                        format.setBackground(QColor("#FFFFFF"))
                        self.previous_cursor.setBlockFormat(format)
                        # 将光标设置为初始位置
                        self.previous_cursor.movePosition(QTextCursor.StartOfBlock)
                        self.previous_cursor.setPosition(self.previous_cursor.position() + len(self.previous_cursor.block().text()),
                                                    QTextCursor.KeepAnchor)

                self.previous_cursor = self.cursor
                # 滚动到显示匹配字符串的行
                text_edit.ensureCursorVisible()

                self.ui.label.setText(f"{self.current_index + 1}/{len(selections)}")
                self.current_index += 1

import subprocess

from PyQt5.QtCore import pyqtSignal, Qt, QThread
from PyQt5.QtWidgets import QTextEdit

class CmdTextEdit(QTextEdit):
    commandEntered = pyqtSignal(str)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            all_command = self.toPlainText().split('\n')
            command = all_command[-1].split(">")[-1].strip()
            print('all')
            print(all_command)
            print('command')
            print(command)
            self.commandEntered.emit(command)
            self.clear()
        else:
            super().keyPressEvent(event)
from PyQt5.QtWidgets import QApplication, QTextBrowser
from PyQt5.QtCore import QUrl, QFileInfo
from PyQt5.QtGui import QTextCursor
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager
from Utils import *

class Browser(QTextBrowser):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOpenLinks(False)  # 禁用默认的链接打开行为
        self.anchorClicked.connect(self.handleAnchorClicked)
        self.basepath = None
        self.stack = []  # 历史记录栈

    def handleAnchorClicked(self, url):
        file_path = QUrl.fromPercentEncoding(url.toString().encode())
        if self.basepath is not None:
            path = self.basepath+'/'+file_path
            self.openLocalFile(path.replace('#EndPath', ''))
        else:
            print(f"File path not exist: {self.basepath}")


    def openLocalFile(self, file_path):
        file_info = QFileInfo(file_path)
        if file_info.exists() and file_info.isFile():
            content = open_with_encodings(file_path)
            self.stack.append(file_path)
            self.setHtml(content)
        else:
            print(f"File does not exist: {file_path}")

    def get_base_path(self, path):
        self.basepath = path

    def goBack(self):
        print(self.stack)
        if self.stack:
            previous_URL = self.stack.pop()
            print(self.stack)
            print(previous_URL)
            content = open_with_encodings(self.stack[-1])
            self.setHtml(content)
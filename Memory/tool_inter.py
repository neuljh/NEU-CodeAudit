from PyQt5.QtWidgets import QApplication, QTextBrowser
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QTextCursor
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager

class Browser(QTextBrowser):
    def __init__(self):
        super().__init__()
        self.setOpenLinks(False)  # 禁用默认的链接打开行为
        self.anchorClicked.connect(self.handleAnchorClicked)
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.handleNetworkReply)

    def setHtmlContent(self, html):
        self.setHtml(html)

    def handleAnchorClicked(self, url):
        request = QNetworkRequest(url)
        self.network_manager.get(request)

    def handleNetworkReply(self, reply):
        if reply.error():
            print("Error: ", reply.errorString())
        else:
            data = reply.readAll()
            text = str(data, 'utf-8')  # 假设页面编码为UTF-8
            self.setHtmlContent(text)

# 示例用法
app = QApplication([])
browser = Browser()
html_content = '<a href="https://fanyi.youdao.com/index.html#/">点击跳转到示例网站</a>'
browser.setHtmlContent(html_content)
browser.show()
app.exec_()

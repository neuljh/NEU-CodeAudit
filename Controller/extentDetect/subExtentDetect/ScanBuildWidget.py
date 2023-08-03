
from PyQt5 import QtWidgets

from UI.extentDetect.subExtentDetect.ScanBuilder import Ui_ScanBuildWiget


class ScanBuilder_Widget(QtWidgets.QWidget, Ui_ScanBuildWiget):
    def __init__(self, parent=None):
        super(ScanBuilder_Widget, self).__init__(parent)
        self.setupUi(self)
        self.pb_back.clicked.connect(self.te_html.goBack)

    def set_scanBuilder_res(self, res, html, path, report_file):
        self.te_res.setPlainText(res)
        self.te_html.setHtml(html)
        self.te_html.get_base_path(path)
        self.te_html.stack.append(report_file)


from PyQt5 import QtWidgets

from UI.extentDetect.subExtentDetect.FlawFinder import Ui_FlawFinderWidget


class FlawFinder_Widget(QtWidgets.QWidget, Ui_FlawFinderWidget):
    def __init__(self, parent=None):
        super(FlawFinder_Widget, self).__init__(parent)
        self.setupUi(self)


    def set_flawfinder_res(self, res):
        self.te_flawfinder.setPlainText(res)

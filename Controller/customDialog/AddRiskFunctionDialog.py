from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QTextCursor, QColor, QTextCharFormat, QIcon
from PyQt5.QtWidgets import QTextEdit, QMessageBox

from UI.Dialog.AddDialog import *
from Data.leanCloud import *


class AddRiskFunctionDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.ui = Ui_AddDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("添加风险函数")
        self.setWindowIcon(QIcon(os.path.dirname(os.path.dirname(os.getcwd()))+"\\UI\\picture\\all.ico"))

        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.ui.AddPushButton.clicked.connect(self.add_function)
        self.ui.CancelPushButton.clicked.connect(self.close_dialog)

    def add_function(self):
        functionName = self.ui.FunctionNameText.toPlainText()
        riskLevel = self.ui.RiskLevelText.toPlainText()
        solution = self.ui.SolutionText.toPlainText()
        if addRiskFunction(functionName, riskLevel, solution):
            QMessageBox.information(self.parent, "成功", "添加成功!")
            self.ui.FunctionNameText.setText("")
            self.ui.RiskLevelText.setText("")
            self.ui.SolutionText.setText("")
            # 更新当前table
            self.parent.set_RiskFunction_table()

    def close_dialog(self):
        self.reject()
        # 更新当前table
        self.parent.set_RiskFunction_table()
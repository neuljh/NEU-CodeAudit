from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QMessageBox
from qtpy import QtWidgets

from Controller.customDialog.AddRiskFunctionDialog import AddRiskFunctionDialog
from Controller.manage.fuzz import fuzz_Widget
from UI.manage.manageRiskFunctionWidget import Ui_ManageRiskFunction

from Data.leanCloud import *
from UI.ToolWidget.CheckBoxHeader import *

class manageRiskFunction_Widget(QtWidgets.QWidget, Ui_ManageRiskFunction):
    def __init__(self, parent=None):
        super(manageRiskFunction_Widget, self).__init__(parent)
        self.setupUi(self)

        self.addDialog = None
        self.header = None
        self.fuzzWidget = None

        self.InitUI()
        self.Init_RiskFunction_table()
        self.connectSignalsSlots()

    def InitUI(self):
        pixmap1 = QPixmap(os.path.dirname(os.path.dirname(os.getcwd())) + "\\UI\\picture\\search-line.png")
        pixmap2 = QPixmap(os.path.dirname(os.path.dirname(os.getcwd())) + "\\UI\\picture\\close-circle-line.png")

        self.picLable.setPixmap(pixmap1)
        self.picLable2.setPixmap(pixmap2)

        self.fuzzWidget = fuzz_Widget()
        self.tabWidget.addTab(self.fuzzWidget, "fuzz漏洞字符库管理")
        # 修改选项卡宽度
        tabBar = self.tabWidget.tabBar()
        tabBar.setMinimumWidth(1300)


    def Get_RiskFunction_Data(self):
        riskFunction_dict = getRiskFunction()
        riskFunction_list = [[item[key] for key in item.keys()] for item in riskFunction_dict]
        return riskFunction_list

    def Init_RiskFunction_table(self):
        # 首列复选框
        column_indices = [0]
        self.header = CheckBoxHeader(column_indices, Qt.Horizontal)
        self.AllRiskFuncTableWidget.setHorizontalHeader(self.header)
        self.header.clicked.connect(self.updateModel)
        self.AllRiskFuncTableWidget.itemChanged.connect(self.modelChanged)

        self.set_RiskFunction_table()

        # 调整列宽度
        self.AllRiskFuncTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # 设置Fixed，固定列宽度
        self.AllRiskFuncTableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.AllRiskFuncTableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)

        # 设置宽度
        self.AllRiskFuncTableWidget.setColumnWidth(1, 200)
        self.AllRiskFuncTableWidget.setColumnWidth(2, 200)

        self.AllRiskFuncTableWidget.setAlternatingRowColors(True) # 开启交替行颜色
        # 设置交替行的颜色
        style = "QTableWidget{												    \
                                background-color: white;			\
                                alternate-background-color: #cedcf8;	\
                                     }"
        self.AllRiskFuncTableWidget.setStyleSheet(style)

    def set_RiskFunction_table(self):
        # set数据
        # 设置表格的行数和列数
        data = self.Get_RiskFunction_Data()
        num_rows = len(data)
        num_columns = 4
        self.AllRiskFuncTableWidget.setRowCount(num_rows)
        self.AllRiskFuncTableWidget.setColumnCount(num_columns)

        for i in range(num_rows):
            # 第一列放复选框
            checkbox = QCheckBox()
            self.AllRiskFuncTableWidget.setCellWidget(i, 0, checkbox)

            # 将数据放入表格中的第二、第三、第四列
            for j in range(1, num_columns):
                item = QTableWidgetItem()
                item.setText(data[i][j - 1])
                self.AllRiskFuncTableWidget.setItem(i, j, item)

        # 居中显示
        for i in range(num_rows):
            for j in range(1, num_columns - 1):
                item = self.AllRiskFuncTableWidget.item(i, j)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def updateModel(self, index, state):
        for i in range(self.AllRiskFuncTableWidget.rowCount()):
            checkbox = self.AllRiskFuncTableWidget.cellWidget(i, index)
            if isinstance(checkbox, QCheckBox):
                checkbox.setChecked(state)

    def modelChanged(self):
        for i in range(self.AllRiskFuncTableWidget.columnCount()):
            checked = 0
            unchecked = 0
            for j in range(self.AllRiskFuncTableWidget.rowCount()):
                checkbox = self.AllRiskFuncTableWidget.cellWidget(j, 0)
                if isinstance(checkbox, QCheckBox):
                    if checkbox.isChecked():
                        checked += 1
                    else:
                        unchecked += 1

            if checked and unchecked:
                self.header.updateCheckState(i, 2)
            elif checked:
                self.header.updateCheckState(i, 1)
            else:
                self.header.updateCheckState(i, 0)

    def delete_et(self):
        self.FindTextEdit.setText("")

    def connectSignalsSlots(self):
        self.AddPushButton.clicked.connect(self.add_RiskFunction)
        self.DeletePushButton.clicked.connect(self.delete_RiskFunction)
        self.FindPushButton.clicked.connect(self.query_RiskFunction)
        self.picLable2.clicked.connect(self.delete_et)

    def add_RiskFunction(self):
        self.addDialog = AddRiskFunctionDialog(self)
        self.addDialog.show()

    def delete_RiskFunction(self):
        checked_name_list = []
        for row in range(self.AllRiskFuncTableWidget.rowCount()):
            checkbox_item = self.AllRiskFuncTableWidget.cellWidget(row, 0)
            if checkbox_item.isChecked():
                value_item = self.AllRiskFuncTableWidget.item(row, 1)
                value = value_item.text()
                checked_name_list.append(value)
        for functionName in checked_name_list:
            deleteRiskFunction(functionName)

        QMessageBox.information(self, "Success", "删除成功!")
        # 更新当前table
        self.set_RiskFunction_table()

    def query_RiskFunction(self):
        find = self.FindTextEdit.toPlainText()

        if not find:
            # 更新当前table
            self.set_RiskFunction_table()
            # 将所有行设置为不隐藏
            for row in range(self.AllRiskFuncTableWidget.rowCount()):
                self.AllRiskFuncTableWidget.setRowHidden(row, False)
            return

        # 遍历所有行
        for row in range(self.AllRiskFuncTableWidget.rowCount()):
            found = False
            # 遍历当前行的所有列
            for col in range(1, 4):
                item = self.AllRiskFuncTableWidget.item(row, col)
                if item.text().strip().find(find) != -1:
                    found = True
                    break

            # 隐藏或显示行
            if found:
                self.AllRiskFuncTableWidget.setRowHidden(row, False)
            else:
                self.AllRiskFuncTableWidget.setRowHidden(row, True)



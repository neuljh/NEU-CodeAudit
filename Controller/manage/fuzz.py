from functools import partial

from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QMessageBox
from qtpy import QtWidgets

from UI.ToolWidget.CheckBoxHeader import *
from UI.manage.fuzzWidget import Ui_Fuzz

from Tool.FUZZ import *

class fuzz_Widget(QtWidgets.QWidget, Ui_Fuzz):
    def __init__(self, parent=None):
        super(fuzz_Widget, self).__init__(parent)
        self.setupUi(self)

        self.addDialog = None
        self.header = None

        self.InitUI()

        self.connectSignalsSlots()

    def InitUI(self):
        self.Init_fuzz_table(self.StringFuzzTableWidget)
        self.Init_fuzz_table(self.IntFuzzTableWidget)
        self.Init_fuzz_table(self.ByteFuzzTableWidget)

        self.set_all_fuzz_Data()

    def set_all_fuzz_Data(self):
        fuzz_dict1 = getStringFuzz()
        fuzz_list1 = [[item[key] for key in item.keys()] for item in fuzz_dict1]
        self.set_Fuzz_table(self.StringFuzzTableWidget, fuzz_list1)

        fuzz_dict2 = getIntFuzz()
        fuzz_list2 = [[item[key] for key in item.keys()] for item in fuzz_dict2]
        self.set_Fuzz_table(self.IntFuzzTableWidget, fuzz_list2)

        fuzz_dict3 = getByteFuzz()
        fuzz_list3 = [[item[key] for key in item.keys()] for item in fuzz_dict3]
        self.set_Fuzz_table(self.ByteFuzzTableWidget, fuzz_list3)

    def Init_fuzz_table(self, table):
        # 首列复选框
        column_indices = [0]
        self.header = CheckBoxHeader(column_indices, Qt.Horizontal)
        table.setHorizontalHeader(self.header)
        self.header.clicked.connect(partial(self.updateModel, table))
        table.itemChanged.connect(lambda: self.modelChanged(table))

        self.set_all_fuzz_Data()

        # 隐藏垂直表头，即行号
        table.verticalHeader().setVisible(False)

        # 调整列宽度
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        table.setAlternatingRowColors(True) # 开启交替行颜色
        # 设置交替行的颜色
        style = "QTableWidget{												    \
                                background-color: white;			\
                                alternate-background-color: #cedcf8;	\
                                     }"
        table.setStyleSheet(style)

    def set_Fuzz_table(self, table, data):
        # set数据
        # 设置表格的行数和列数
        num_rows = len(data)
        num_columns = 3
        table.setRowCount(num_rows)
        table.setColumnCount(num_columns)

        for i in range(num_rows):
            # 第一列放复选框
            checkbox = QCheckBox()
            table.setCellWidget(i, 0, checkbox)

            # 将数据放入表格中的第二列
            item = QTableWidgetItem()
            item.setText(str(data[i][0]))
            table.setItem(i, 1, item)

            item = QTableWidgetItem()
            item.setText(data[i][1])
            table.setItem(i, 2, item)

        # 居中显示
        for i in range(num_rows):
            for j in range(1, num_columns):
                item = table.item(i, j)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def updateModel(self, table, index, state):
        for i in range(table.rowCount()):
            checkbox = table.cellWidget(i, index)
            if isinstance(checkbox, QCheckBox):
                checkbox.setChecked(state)

    def modelChanged(self, table):
        for i in range(table.columnCount()):
            checked = 0
            unchecked = 0
            for j in range(table.rowCount()):
                checkbox = table.cellWidget(j, 0)
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

    def connectSignalsSlots(self):
        self.RunPushButton.clicked.connect(self.run_Fuzz)
        self.DeletePushButton.clicked.connect(self.delete_Fuzz)

    def run_Fuzz(self):
        fuzz = Fuzz()
        # 根据索引获取当前的下拉框内容
        index = self.comboBox.currentIndex()
        if index == 0:
            fuzz.generate_string()
        elif index == 1:
            fuzz.generate_int()
        elif index == 2:
            fuzz.generate_byte()
        # 更新当前table
        self.set_all_fuzz_Data()
        return

    def delete_Fuzz(self):
        sign = 1
        for table in [self.StringFuzzTableWidget, self.IntFuzzTableWidget, self.ByteFuzzTableWidget]:
            self.delete_fortable(table, sign)
            sign += 1

        QMessageBox.information(self, "Success", "删除成功!")

        # 更新当前table
        self.set_all_fuzz_Data()

    def delete_fortable(self, table, sign):
        checked_name_list = []
        for row in range(table.rowCount()):
            checkbox_item = table.cellWidget(row, 0)
            if checkbox_item.isChecked():
                value_item = table.item(row, 1)
                value = int(value_item.text())
                checked_name_list.append(value)
        for id in checked_name_list:
            if sign == 1:
                deleteFuzz1(id)
            elif sign == 2:
                deleteFuzz2(id)
            elif sign == 3:
                deleteFuzz3(id)



"""
@FileName：drmemoryWidget.py
@Description:
@Time：2023/7/17 10:05
@user: 20324
"""
from PyQt5 import  QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from UI.extentDetect.subExtentDetect.drmemoryWidget import Ui_Form


class Drmemory_Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        # self.file_path =filePath
        self.setupUi(self)
    #     self.connectSignalsSlots()
    #     self.show_information()
    #
    # def connectSignalsSlots(self):
    #
    #     return

    def show_information(self, errors, errors_summery):
        # c_file_path = self.file_path
        # tool_memory = ToolMemoryChecker(c_file_path)
        # tool_memory.run_cl_compile()
        # tool_memory.run()
        # errors,errors_summery=tool_memory.extract_memory_leaks()
        self.textEdit.setText("\n".join(errors))
        self.write_to_table(errors_summery)

    def write_to_table(self,list):
        # 创建一个 QStandardItemModel 对象
        model = QStandardItemModel()
        # 设置表头的列名字
        column_names = ["Kind", "Unique", "Sum", "Size"]
        model.setHorizontalHeaderLabels(column_names)

        # 将数据添加到模型中
        for row_index, row_data in enumerate(list):
            for col_index, cell_data in enumerate(row_data):
                item = QStandardItem(str(cell_data))
                model.setItem(row_index, col_index, item)

        # 将模型设置给 QTableView 组件
        self.tableView.setModel(model)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = drmemory_Widget(r'D:\project_code\pythonproject\CodeAuditing\\test_c\\graph.c')
#     win.show()
#     sys.exit(app.exec())

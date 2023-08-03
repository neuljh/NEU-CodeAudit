# import os
# from UI.Main import *
# import sys
# from fileTree import FileTree
# def file_tree_clicked():
#     treeview = ui.treeView
#     code_text = ui.plainTextEdit
#     # 策略双击槽函数
#     index = treeview.currentIndex()
#     model = index.model()  # 请注意这里可以获得model的对象
#     item_path = model.filePath(index)
#     if not os.path.isdir(item_path):
#         try:
#             with open(item_path, 'r', encoding='gbk') as file:
#                 file_content = file.read()
#                 # print(file_content)  # 在这里可以使用文件内容进行进一步的处理
#                 code_text.setPlainText(file_content)
#         except FileNotFoundError:
#             print("文件不存在")
#         except IOError:
#             print("无法读取文件")
#
# def set_file_tree(ui):
#     model = QtWidgets.QFileSystemModel()
#     model.setRootPath(QtCore.QDir.rootPath())
#     model.setReadOnly(False)
#     treeview = ui.treeView
#     treeview.setModel(model)
#     treeview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#     treeview.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
#     treeview.setHeaderHidden(True)
#     treeview.hideColumn(1)
#     treeview.hideColumn(2)
#     treeview.hideColumn(3)
#     #信号  槽部分
#     treeview.doubleClicked.connect(file_tree_clicked)
#
#
# def Groove_signal():
#     """
#     @description: 消息  槽的连接
#     @Time：2023/7/11 || 10:00 ||20324
#     """
#     ui.action.triggered.connect(lambda: file_node.open_folder_dialog(ui)) #打开文件夹操作
#     ui.comboBox.activated.connect(lambda: file_node.display_filtered_files(ui))
#
# def Property_fun():
#     """
#     @description: 控件初始化
#     @Time：2023/7/11 || 10:00 ||20324
#     """
#     ui.comboBox.setVisible(False)
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     file_node = FileTree()#文件树操作对象
#     #
#     Groove_signal()  #槽函数与消息连接封装
#     Property_fun()
#     set_file_tree(ui)
#     #
#     MainWindow.show()
#     sys.exit(app.exec_())
#
#

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QTextCharFormat, QColor, QTextCursor
from PyQt5.QtWidgets import QTextEdit

from Controller.customDialog.FindDialogController import set_search_dialog
from Tool.fileTree import FileTree

from UI.ToolWidget.CodeEditor import *
from UI.Dialog.FindDialog import *

from Utils import *


def set_c_file_tableview(header_files, macro_definitions, variable_names, function_declarations):
    tableview = ui.tableView
    # 创建数据模型
    model = QStandardItemModel()
    # 设置列名称
    column_names = ['Name', 'Type', 'Line']
    model.setHorizontalHeaderLabels(column_names)

    # 添加数据
    datas = []

    for item in header_files:
        data = []
        data.append(item)
        data.append(header_file_str)
        data.append('\\')
        datas.append(data)
    for item in macro_definitions:
        data = []
        data.append(item)
        data.append(macro_definitions_str)
        data.append('\\')
        datas.append(data)
    for item in variable_names:
        data = []
        data.append(item[0])
        data.append(item[1])
        data.append(str(item[2]))
        datas.append(data)
    for item in function_declarations:
        data = []
        data.append(item[0])
        data.append(item[1])
        data.append(str(item[2]))
        datas.append(data)

    for row in datas:
        item_row = []
        for item in row:
            item_cell = QStandardItem(item)
            item_cell.setEditable(False)  # 设置单元格不可编辑
            item_row.append(item_cell)
        model.appendRow(item_row)

    tableview.setModel(model)
    # 设置双击事件
    tableview.doubleClicked.connect(tableview_double_clicked)


def tableview_double_clicked(index):
    tableview = ui.tableView
    pte_content = ui.pte_content
    code_text_new = ui.textEdit
    if index.isValid():
        index_row = index.row()
        index_column = index.column()
        value = index.data()
        print(f"Double clicked on item: row={index_row}, column={index_column}, item={value}")
        pte_content.setPlainText(value)

        # 获取行数据
        model = tableview.model()
        data = []
        for column in range(model.columnCount()):
            item = model.index(index_row, column).data(Qt.DisplayRole)
            data.append(item)
        line = data[2]
        # print(data)

        if index_column == 0:
            search_text = value
            cursor = code_text_new.textCursor()
            format = QTextCharFormat()
            format.setBackground(QColor("yellow"))

            extra_selections = []
            code_text_new.moveCursor(QTextCursor.Start)

            while cursor.hasComplexSelection() or cursor.atEnd() == False:
                cursor = code_text_new.document().find(search_text, cursor)

                if cursor.isNull() == False:
                    target_number = cursor.block().blockNumber() + 1
                    if str(target_number) == line:
                        selection = QTextEdit.ExtraSelection()
                        selection.format = format
                        selection.cursor = QTextCursor(cursor)
                        extra_selections.append(selection)
                else:
                    break
            code_text_new.setExtraSelections(extra_selections)
        elif(line!='\\'):
            target_text = data[0]
            # 获取总行数
            total_lines = code_text_new.document().blockCount()
            # 设置高亮格式
            format = QTextCharFormat()
            format.setBackground(QColor("yellow"))
            # 添加高亮选择
            extra_selections = []

            if int(line) <= total_lines:
                target_line = int(line) - 1
                block = code_text_new.document().findBlockByLineNumber(target_line)
                if block.isValid():
                    # 获取目标行的文本
                    line_text = block.text()
                    # 在目标行中查找目标字符串的位置
                    index = line_text.find(target_text)
                    while index != -1:
                        # 创建额外选择并设置高亮
                        cursor = QTextCursor(block)
                        cursor.setPosition(block.position() + index)
                        cursor.setPosition(block.position() + index + len(target_text), QTextCursor.KeepAnchor)
                        selection = QTextEdit.ExtraSelection()
                        selection.format = format
                        selection.cursor = cursor
                        extra_selections.append(selection)
                        # 在目标行中继续查找下一个目标字符串的位置
                        index = line_text.find(target_text, index + len(target_text))

            code_text_new.setExtraSelections(extra_selections)






"""
    创建一个查找对话框，并对在plaintext中查找到的字符串高亮处理。
"""
#
# def file_tree_clicked():
#     treeview = ui.treeView
#     textEdit = ui.textEdit
#     # textEdit.setStyleSheet("background-color: #000000;")
#     # 策略双击槽函数
#     index = treeview.currentIndex()
#     model = index.model()  # 请注意这里可以获得model的对象
#     item_path = model.filePath(index)
#     if not os.path.isdir(item_path) and check_extension(item_path):
#         try:
#             with open(item_path, 'r', encoding='gbk') as file:
#                 file_content = file.read()
#                 # print(file_content)  # 在这里可以使用文件内容进行进一步的处理
#
#                 # print(code_text.toPlainText())
#                 getdata = Getdata(item_path)
#                 getdata.get_file_info_pre()
#                 getdata.get_local_info()
#                 file_content, header_files, macro_definitions, variable_names, function_declarations = getdata.get_all_local_data()
#                 set_c_file_tableview(header_files, macro_definitions, variable_names, function_declarations)
#
#                 """
#                 还没有颜色
#                 """
#                 lexer = get_lexer_by_name('c')
#                 formatter = HtmlFormatter(style='xcode')
#                 # 获取样式定义并嵌入到 HTML 代码中
#                 css_style = formatter.get_style_defs('.highlight')
#                 highlighted_code = highlight(file_content, lexer, formatter)
#                 html_code = f'<style>{css_style}</style>{highlighted_code}'
#                 textEdit.setHtml(html_code)
#         except FileNotFoundError:
#             print("文件不存在")
#         except IOError:
#             print("无法读取文件")
def file_tree_clicked():

    treeview = ui.treeView
    code_text = ui.plainTextEdit
    # 策略双击槽函数
    index = treeview.currentIndex()
    model=ui.treeView.model()
    clicked_item = model.itemFromIndex(index) #获取当前节点
    # model.folder_path
    name = clicked_item.text() #获取当前节点存储的内容，也就是文件名字

    path = name
    parent_index = index.parent()
    while parent_index.isValid():
        parent_item = treeview.model().itemFromIndex(parent_index)
        parent_name = parent_item.text()
        path = parent_name + '/' + path  # 使用斜杠分隔路径部分
        parent_index = parent_index.parent()
    item_path=path

    if not os.path.isdir(item_path):
        try:
            with open(item_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                # print(file_content)  # 在这里可以使用文件内容进行进一步的处理
                code_text.setPlainText(file_content)
        except FileNotFoundError:
            print("文件不存在")
        except IOError:
            print("无法读取文件")


def set_file_tree(ui):
    model = QtWidgets.QFileSystemModel()
    model.setRootPath(QtCore.QDir.rootPath())
    model.setReadOnly(False)
    treeview = ui.treeView
    treeview.setModel(model)
    treeview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    treeview.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
    treeview.setHeaderHidden(True)
    treeview.hideColumn(1)
    treeview.hideColumn(2)
    treeview.hideColumn(3)
    treeview.doubleClicked.connect(file_tree_clicked)

def Groove_signal():
    """
    @description: 消息  槽的连接
    @Time：2023/7/11 || 10:00 ||20324
    """
    ui.action.triggered.connect(lambda: file_node.open_folder_dialog()) #打开文件夹操作
    ui.comboBox.activated.connect(lambda: file_node.display_filtered_files())

def Property_fun():
    """
    @description: 控件初始化
    @Time：2023/7/11 || 10:00 ||20324
    """
    ui.comboBox.setVisible(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    file_node = FileTree(ui)  # 文件树操作对象
    Groove_signal()  #槽函数与消息连接封装
    Property_fun()
    set_file_tree(ui)
    set_search_dialog(ui, MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())








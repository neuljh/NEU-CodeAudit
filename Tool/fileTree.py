"""
@FileName：fileTree.py
@Description:
@Time：2023/7/10 15:28
@user: 20324
"""
import fnmatch
from PyQt5 import QtWidgets
import Tool.crawler
from Tool.crawler import File
from editor.database import crawler_database
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from Utils import *
import multiprocessing

default_folder_path=r'D:\project_code\pythonproject\CodeAuditing\test_c'
def is_c_or_h_file(file_path):
    # 判断文件是否为C文件或头文件
    return file_path.endswith('.c') or file_path.endswith('.h')

def File_get(file_path):
    file_obj=File(file_path)
    file_obj.parse_c_file()
    # db=crawler_database() 数据库存储
    # db.add_file(file_obj)
    element_list=[]
    for function in file_obj.fun_list:
        element_list.append('fun:'+function.name)
    for struct in file_obj.struct_list:
        element_list.append('struct:'+struct.name)
    for gobal_var in file_obj.var_list:
        element_list.append('var:'+gobal_var.name)
    for macro in file_obj.macro_list:
        element_list.append('macro:'+macro.name)
    return element_list


def index_get_path(ui):
    treeview = ui.treeView
    index = treeview.currentIndex()
    model = ui.treeView.model()
    path = model.itemFromIndex(index).text()
    parent_index = index.parent()
    while parent_index.isValid():  # 向上层遍历获取路径
        parent_name = treeview.model().itemFromIndex(parent_index).text()
        path = parent_name + '/' + path  # 使用斜杠分隔路径部分
        parent_index = parent_index.parent()
    item_path = path
    if os.path.isfile(item_path):
        file_obj = File(item_path)
        file_obj.parse_c_file()
        return item_path,file_obj
    else:   #不是文件,分离最后一部分,并获取其中的对象
        item_path,element=os.path.split(path)
        e_type=element.split(':')[0]  #对应的类
        e_name = element.split(':')[1]# 真实的名字
        file_obj=File(item_path)
        file_obj.parse_c_file()
        if e_type=='fun':
            for fun_obj in file_obj.fun_list:
                if fun_obj.name==e_name:
                    return item_path,fun_obj
        elif e_type=='struct':
            for fun_obj in file_obj.struct_list:
                if fun_obj.name == e_name:
                    return item_path, fun_obj
        elif e_type=='var':
            for fun_obj in file_obj.var_list:
                if fun_obj.name == e_name:
                    return item_path, fun_obj
        elif e_type=='macro':
            for fun_obj in file_obj.macro_list:
                if fun_obj.name == e_name:
                    return item_path, fun_obj
        exit(f'指定的类型{e_type}，名字{e_name}不存在')

def from_index_get_path(treeview):
    index = treeview.currentIndex()
    model = treeview.model()
    path = model.itemFromIndex(index).text()
    parent_index = index.parent()
    while parent_index.isValid():  # 向上层遍历获取路径
        parent_name = treeview.model().itemFromIndex(parent_index).text()
        path = parent_name + '/' + path  # 使用斜杠分隔路径部分
        parent_index = parent_index.parent()
    item_path = path
    if os.path.isfile(item_path):
        file_obj = File(item_path)
        file_obj.parse_c_file()
        return item_path,file_obj
    else:   #不是文件,分离最后一部分,并获取其中的对象
        item_path,element=os.path.split(path)
        e_type=element.split(':')[0]  #对应的类
        e_name = element.split(':')[1]# 真实的名字
        file_obj=File(item_path)
        file_obj.parse_c_file()
        if e_type=='fun':
            for fun_obj in file_obj.fun_list:
                if fun_obj.name==e_name:
                    return item_path,fun_obj
        elif e_type=='struct':
            for fun_obj in file_obj.struct_list:
                if fun_obj.name == e_name:
                    return item_path, fun_obj
        elif e_type=='var':
            for fun_obj in file_obj.var_list:
                if fun_obj.name == e_name:
                    return item_path, fun_obj
        elif e_type=='macro':
            for fun_obj in file_obj.macro_list:
                if fun_obj.name == e_name:
                    return item_path, fun_obj
        exit(f'指定的类型{e_type}，名字{e_name}不存在')


class FileTree:
    def __init__(self, parent):
        self.folder_path = ""
        self.parent = parent
        self.tree_view = parent.treeView  # 显示存储结构
        self.ChooseComboBox = parent.ChooseComboBox
        self.tree_model = QStandardItemModel()  # 存储的数据结构
        self.root_item = QStandardItem()

    def open_folder_dialog(self):

        folder_dialog = QtWidgets.QFileDialog()
        folder_path = folder_dialog.getExistingDirectory(self.parent.treeView, "选择文件夹",
                                                         default_folder_path)
        if not folder_path:
            return
        self.tree_model.clear()  # 清空现有的模型数据
        self.folder_path = folder_path
        self.ChooseComboBox.setVisible(True)
        # 添加根节点
        root_item = QStandardItem(folder_path)
        self.root_item=root_item
        self.tree_model.appendRow(root_item)
        # 遍历文件夹并添加到根节点
        self.add_folder_to_node(folder_path, root_item)
        self.tree_view.setModel(self.tree_model)
        self.tree_view.expandToDepth(0)

    def add_folder_to_node(self, folder_path, parent_item):#添加文件夹
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isdir(file_path):
                folder_item = QStandardItem(file_name)
                parent_item.appendRow(folder_item)
                self.add_folder_to_node(file_path, folder_item)

            elif os.path.isfile(file_path) and is_c_or_h_file(file_path):
                file_item = QStandardItem(file_name)
                parent_item.appendRow(file_item)
                self.add_element_to_node(file_path, file_item)

    def add_element_to_node(self, file_path, parent_item):
        elements = File_get(file_path)
        for element in elements:
            function_item = QStandardItem(element)
            parent_item.appendRow(function_item)

    def display_filtered_files(self):
        folder_path=self.folder_path
        self.tree_model.clear()  # 清空现有的模型数据
        # 添加根节点
        root_item = QStandardItem(folder_path)
        self.tree_model.appendRow(root_item)
        # 遍历文件夹并添加到根节点
        self.add_folder_to_node(folder_path, root_item)
        self.tree_view.setModel(self.tree_model)
        root_item = self.tree_model.item(0)  # 获取根节点
        if root_item:       # 遍历文件树，设置显示/隐藏属性
            self.remove_filtered_files(root_item)

        self.tree_view.expandToDepth(0)

    def remove_filtered_files(self, parent_item):
        for row in reversed(range(parent_item.rowCount())):
            item = parent_item.child(row)
            file_path = os.path.join(self.folder_path, item.text())
            if is_c_or_h_file(file_path):  # c或者h文件,不会遍历其子节点
                if not self.is_file_match_filter(file_path):
                    parent_item.removeRow(row)
            elif item.hasChildren():  # 不是元素节点，但是不是c或者h文件
                self.remove_filtered_files(item)
                if item.rowCount() == 0:  # 节点为空删除
                    parent_item.removeRow(row)
            else:  # 一般文件
                if not self.is_file_match_filter(file_path):
                    parent_item.removeRow(row)

    def is_file_match_filter(self, file_path): #匹配筛选条件
        filter_list = self.ChooseComboBox.currentText().split(',')  # 获取当前选择的过滤规则
        file_name = os.path.basename(file_path)
        return any(fnmatch.fnmatch(file_name, filter_pattern) for filter_pattern in filter_list)

    def get_element_line(self):
        item_path,element=index_get_path(self.ui)
        if not isinstance(element, Tool.crawler.File):
            # print(element.name,element.line)
            return element.name,element.line,item_path


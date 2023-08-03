import sys

from PyQt5.QtWidgets import QTabBar
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QFileDialog

from UI.Main import Ui_codeAudit
from Controller.codeAudit.commentWidget import comment_Widget
from Tool.fileTree import *
from Controller.customDialog.FindDialogController import FindDialog

from Utils import *


class codeAudit(QtWidgets.QWidget, Ui_codeAudit):
    def __init__(self, parent=None):
        super(codeAudit, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

        self.file_path = ''
        self.datas = []

        self.fileTree = FileTree(self)
        self.set_file_tree()

        self.commentWidget = None
        self.findDialog = None
        self.connectSignalsSlots()

    def initUI(self):
        self.ChooseComboBox.setVisible(False)
        # 设置第一个Tab为不可删除
        tab_bar = self.commentTabWidget.tabBar()
        tab_bar.setTabButton(0, QTabBar.RightSide, None)

    def tabClose(self, index):
        self.commentTabWidget.removeTab(index)

    def openAction_click(self):
        # 获取现有的 tab 数量
        tab_count = self.commentTabWidget.count()

        # 从最后一个 tab 开始删除，直到只剩下第一个 tab
        for index in range(tab_count - 1, 0, -1):
            self.commentTabWidget.removeTab(index)

        self.fileTree.open_folder_dialog()

    def get_selected_items(self, model):
        self.datas.clear()
        selected_indexes = self.treeView.selectedIndexes()
        for index in selected_indexes:
            selected_file_path = model.filePath(index)
            selected_file_name = index.data()
            selected_file_directory = os.path.dirname(selected_file_path)
            self.datas.append(selected_file_path)
            self.datas.append(selected_file_name)
            self.datas.append(selected_file_directory)

    def show_save_another_dialog(self):
        if isinstance(self.treeView.model(), QtGui.QStandardItemModel):
            selected_file_path = from_index_get_path(self.treeView)[0]
            selected_file_name = os.path.basename(selected_file_path)
            selected_file_directory = os.path.dirname(selected_file_path)

            file_content = self.commentWidget.get_code_text()
            save_file_dir = selected_file_directory
            print(save_file_dir)
            save_path, _ = QFileDialog.getSaveFileName(None, "另存为", selected_file_directory + '/' + 'untitle.c',
                                                       "All Files (*);;C Files (*.c);;C header Files (*.h)")
            if save_path:
                # 打开文件并写入内容
                with open(save_path, 'w') as file:
                    file.write(file_content)
                # 在这里可以执行保存文件的操作，比如将文件保存到 save_path 路径下
                print("保存路径:", save_path)

    def show_save_dialog(self):
        if isinstance(self.treeView.model(), QtGui.QStandardItemModel):
            selected_file_path = from_index_get_path(self.treeView)[0]
            selected_file_name = os.path.basename(selected_file_path)
            selected_file_directory = os.path.dirname(selected_file_path)
            file_content = self.commentWidget.get_code_text()
            save_file_dir = selected_file_path
            print(save_file_dir)

            if save_file_dir:
                # 打开文件并写入内容
                with open(save_file_dir, 'w') as file:
                    file.write(file_content)
                # 在这里可以执行保存文件的操作，比如将文件保存到 save_path 路径下
                print("保存路径:", save_file_dir)

    def connectSignalsSlots(self):
        self.treeView.doubleClicked.connect(self.file_tree_clicked)
        self.openAction.triggered.connect(self.openAction_click)  # 打开文件夹操作
        self.ChooseComboBox.activated.connect(self.fileTree.display_filtered_files)
        self.findAction.triggered.connect(self.show_find_dialog)
        self.saveAction.triggered.connect(lambda: self.show_save_dialog())
        self.saveAsAction.triggered.connect(lambda: self.show_save_another_dialog())
        self.commentTabWidget.tabCloseRequested.connect(self.tabClose)


    def show_find_dialog(self):
        # commentWidget = comment_Widget()
        # self.commentTabWidget.addTab(commentWidget, item_path)
        #
        # self.commentWidget = commentWidget  # 添加该行

        self.findDialog = FindDialog(self.commentWidget)
        self.findDialog.show()

    def file_tree_clicked(self):
        model = self.treeView.model()
        if isinstance(model, QtWidgets.QFileSystemModel):
            index = self.treeView.currentIndex()
            item_path = index.model().filePath(index)
        elif isinstance(model, QtGui.QStandardItemModel):
            # 策略双击槽函数
            item_path = index_get_path(self)[0]

        if not os.path.isdir(item_path):
            self.add_CommentWidget(item_path)
            try:
                file_content=open_with_encodings(item_path)

                self.commentWidget.set_open_text(item_path)

            except FileNotFoundError:
                print("文件不存在")
            except IOError:
                print("无法读取文件")

    def add_CommentWidget(self, item_path):
        file_name = os.path.basename(item_path)

        # 检查是否已存在相同路径的tab
        for index in range(self.commentTabWidget.count()):
            tab_widget = self.commentTabWidget.widget(index)
            if tab_widget.property("FilePath") == item_path:
                # 切换到已存在的tab
                self.commentTabWidget.setCurrentWidget(tab_widget)
                return

        # 不存在相同路径的tab，新增tab
        commentWidget = comment_Widget()
        self.commentTabWidget.addTab(commentWidget, file_name)
        commentWidget.setProperty("FilePath", item_path)

        self.commentWidget = commentWidget
        self.commentTabWidget.setCurrentWidget(commentWidget)

    def set_file_tree(self):
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(QtCore.QDir.rootPath())
        model.setReadOnly(False)
        self.treeView.setModel(model)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.treeView.setHeaderHidden(True)
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = codeAudit()
    win.show()
    sys.exit(app.exec())
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QProcess, Qt
from PyQt5.QtGui import QTextCursor, QPixmap
from PyQt5.QtWidgets import QTabBar
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from Controller.extentDetect.subExtentDetect.FlawfinderWidget import FlawFinder_Widget
from Controller.extentDetect.subExtentDetect.drmemoryWidget import Drmemory_Widget
from Controller.extentDetect.subExtentDetect.ScanBuildWidget import ScanBuilder_Widget

from Data import *
from Data.getdata import *
import Memory
from Memory.compile import compile_project
from Memory.project_tool import *
from Memory.tool_memory import ToolMemoryChecker
from UI.extentDetect.MutiWidget import Ui_MutiWidget
from Memory.tool_Clang import *
from Memory.tool_flawfinder import *
from Memory.tool_cppchecker import *
from Utils import *
from Controller.report.test import *


class mutiComment_Widget(QtWidgets.QWidget, Ui_MutiWidget):
    def __init__(self, parent=None):
        super(mutiComment_Widget, self).__init__(parent)

        self.setupUi(self)
        self.file_path = None
        self.tool_clang = None
        self.tool_flawfinder = None
        self.tool_cppchecker = None
        self.tool_memory = None

        self.flawfinderWidget = None
        self.drmemory_Widget = None
        self.scanBuilderWidget = None

        self.process = QProcess()
        self.cmd()

        self.initUI()
        self.connectSignalsSlots()

    def initUI(self):
        # 设置第一个Tab为不可删除
        tab_bar = self.detectWidget.tabBar()
        tab_bar.setTabButton(0, QTabBar.RightSide, None)

        pixmap = QPixmap(os.path.dirname(os.path.dirname(os.getcwd())) + "\\UI\\picture\\waitpic (3).png")
        pixmap = pixmap.scaled(800, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.picLable.setPixmap(pixmap)

    def tabClose(self, index):
        self.detectWidget.removeTab(index)

    def connectSignalsSlots(self):
        self.te_cmd.commandEntered.connect(self.execute_command)
        self.detectWidget.tabCloseRequested.connect(self.tabClose)
        # 将动作与处理函数相关联
        self.pb_detect_start.actionA.triggered.connect(lambda: self.run_flawfinder_scan())
        self.pb_detect_start.actionB.triggered.connect(lambda: self.run_clang_tidy_scan())
        self.pb_detect_start.actionC.triggered.connect(lambda: self.run_clang_checker_scan())
        self.pb_detect_start.actionD.triggered.connect(lambda: self.run_clang_scan_build_scan())
        self.pb_detect_start.actionE.triggered.connect(lambda: self.run_cppchecker_scan())
        self.pb_detect_start.actionF.triggered.connect(lambda: self.run_code_evaluation())


    def cmd(self):
        self.te_cmd.setReadOnly(False)
        # 创建 QProcess 对象
        self.process.setProgram("cmd")
        # self.process.setWorkingDirectory("C:\\Users")
        # self.process.setProcessChannelMode(QProcess.MergedChannels)  # 将标准输出和标准错误合并
        # self.process.readyRead.connect(self.update_cmd)
        self.process.readyReadStandardOutput.connect(self.update_cmd)
        self.process.readyReadStandardError.connect(self.update_cmd)
        self.process.start("cmd")

    def update_cmd(self):
        while self.process.bytesAvailable():
            # 读取命令提示符的输出并将其追加到 QTextEdit 中
            # output = self.process.readAll().data()
            output = self.process.readAllStandardOutput().data()
            error = self.process.readAllStandardError().data()
            print(output)
            print(error)
            text = ""
            if output:
                try:
                    text = output.decode("utf-8")
                except UnicodeDecodeError:
                    text = output.decode("gbk", errors="replace")
                print(text)
                self.te_cmd.moveCursor(QTextCursor.End)
                self.te_cmd.insertPlainText(text)
                self.te_cmd.moveCursor(QTextCursor.End)
            if error:
                try:
                    text = error.decode("utf-8")
                except UnicodeDecodeError:
                    text = error.decode("gbk", errors="replace")
                print(text)
                self.te_cmd.moveCursor(QTextCursor.End)
                self.te_cmd.insertPlainText(text)
                self.te_cmd.moveCursor(QTextCursor.End)

    def execute_command(self, command):
        QtCore.QTimer.singleShot(100, lambda: self.process.write(f"{command}\n".encode()))
        self.process.waitForBytesWritten()  # 等待写入完成，确保命令被发送

    def init_tools(self, item_path):
        self.file_path = item_path
        self.tool_clang = ToolClang(self.file_path, get_available_llvm_path(llvm_path))
        self.tool_flawfinder = ToolFlawfinder(self.file_path)
        self.tool_cppchecker = ToolCppChecker(self.file_path)
        self.tool_memory = ToolMemoryChecker(self.file_path)

        self.pb_compile.clicked.connect(lambda: self.compile_code())
        self.pb_format.clicked.connect(lambda: self.format_code(item_path))
        self.pb_run.clicked.connect(lambda: self.run_code())
        self.pb_generate_2.clicked.connect(lambda: self.get_report(item_path))
        # 将动作与处理函数相关联
        self.pb_detect.actionA.triggered.connect(lambda: self.run_flawfinder_scan())
        self.pb_detect.actionB.triggered.connect(lambda: self.run_clang_tidy_scan())
        self.pb_detect.actionC.triggered.connect(lambda: self.run_clang_checker_scan())
        self.pb_detect.actionD.triggered.connect(lambda: self.run_clang_scan_build_scan())
        self.pb_detect.actionE.triggered.connect(lambda: self.run_cppchecker_scan())
        self.pb_detect.actionF.triggered.connect(lambda: self.run_code_evaluation())
        self.pb_detect.actionG.triggered.connect(lambda: self.run_memory_detect())
        #项目按钮的槽函数
        # self.actionA = self.contextMenu.addAction('项目编译')
        # self.actionB = self.contextMenu.addAction('项目ClangChecker扫描')
        # self.actionC = self.contextMenu.addAction('项目CppChecker扫描')
        # self.actionD = self.contextMenu.addAction('项目内存泄漏检测')
        self.pushButton.actionA.triggered.connect(lambda: compile_project(self.file_path))
        self.pushButton.actionB.triggered.connect(lambda: self.project_clangcheck())
        self.pushButton.actionC.triggered.connect(lambda: self.project_cppcheck())
        self.pushButton.actionD.triggered.connect(lambda: self.run_memory_detect())
    # def on_pushButton1_clicked(self):
    #     self.stackedWidget.setCurrentIndex(0)
    #
    # def on_pushButton2_clicked(self):
    #     self.stackedWidget.setCurrentIndex(1)
    def project_clangcheck(self):
        self.add_CommentWidget("project_clangcheck")
        output=clangcheck(self.file_path)
        self.flawfinderWidget.te_flawfinder.setText(output)
    def project_cppcheck(self):
        self.add_CommentWidget("project_cppcheck")
        output = cppcheck(self.file_path)
        self.flawfinderWidget.te_flawfinder.setText(output)
    def project_drmemory(self):
        self.add_CommentWidget("project_drmemory")
        output = drmemory(self.file_path)
        self.flawfinderWidget.te_flawfinder.setText(output)

    # 新增tab
    def add_CommentWidget(self, name):

        # 检查是否已存在相同路径的tab
        for index in range(self.detectWidget.count()):
            tab_widget = self.detectWidget.widget(index)
            if tab_widget.property("name") == name:
                # 切换到已存在的tab
                self.detectWidget.setCurrentWidget(tab_widget)
                return

        if name == '内存泄漏检测':
            # 不存在相同路径的tab，新增tab
            drmemory_Widget = Drmemory_Widget()
            self.detectWidget.addTab(drmemory_Widget, name)
            drmemory_Widget.setProperty("name", name)
            self.drmemory_Widget = drmemory_Widget
            self.detectWidget.setCurrentWidget(drmemory_Widget)
        elif name == 'ClangScanBuild扫描':
            # 不存在相同路径的tab，新增tab
            scanBuilderWidget = ScanBuilder_Widget()
            self.detectWidget.addTab(scanBuilderWidget, name)
            scanBuilderWidget.setProperty("name", name)
            self.scanBuilderWidget = scanBuilderWidget
            self.detectWidget.setCurrentWidget(scanBuilderWidget)
        else:
            # 不存在相同路径的tab，新增tab
            flawfinderWidget = FlawFinder_Widget()
            self.detectWidget.addTab(flawfinderWidget, name)
            flawfinderWidget.setProperty("name", name)
            self.flawfinderWidget = flawfinderWidget
            self.detectWidget.setCurrentWidget(flawfinderWidget)

    def run_memory_detect(self):
        self.add_CommentWidget("内存泄漏检测")
        # self.tool_memory.run_cl_compile()
        self.tool_memory.run()
        errors, errors_summery = self.tool_memory.extract_memory_leaks()
        self.drmemory_Widget.show_information(errors, errors_summery)


    #此部分的所有检测还未实现对应组件，因此仅仅是运行
    def run_flawfinder_scan(self):
        self.add_CommentWidget("FlawFinder扫描")

        self.tool_flawfinder.run()
        self.tool_flawfinder.get_data()
        self.tool_flawfinder.get_graph_base_data()
        print(self.tool_flawfinder.result_text)
        # ...
        message = 'STDOUT:\n' + self.tool_flawfinder.result_text
        self.flawfinderWidget.te_flawfinder.setText(message)


    def run_clang_tidy_scan(self):
        self.add_CommentWidget("ClangTidy扫描")
        self.tool_clang.run_static_scan()
        message = 'STDOUT:\n' + self.tool_clang.static_scan_output + '\nSTDERR:\n' + self.tool_clang.static_scan_error
        self.flawfinderWidget.te_flawfinder.setText(message)

    def run_clang_checker_scan(self):
        self.add_CommentWidget("ClangChecker扫描")
        self.tool_clang.run_static_scan_strict()
        message = 'STDOUT:\n' + self.tool_clang.static_scan_strict_output + '\nSTDERR:\n' + self.tool_clang.static_scan_strict_error
        self.flawfinderWidget.te_flawfinder.setText(message)

    #展示较为复杂
    def run_clang_scan_build_scan(self):
        self.add_CommentWidget("ClangScanBuild扫描")
        self.tool_clang.run_static_scan_report()
        message = 'STDOUT:\n' + self.tool_clang.static_scan_report_output + '\nSTDERR:\n' + self.tool_clang.static_scan_report_output
        pre_path = get_debug_database()
        report_file = pre_path + '\index.html'
        print('report_file: ')
        print(report_file)
        file_content = open_with_encodings(report_file)
        print('file_content: ')
        print(file_content)
        self.scanBuilderWidget.set_scanBuilder_res(message, file_content, pre_path, report_file)


    def run_cppchecker_scan(self):
        self.add_CommentWidget("CppChecker扫描")
        self.tool_cppchecker.run_scan()
        message = 'STDOUT:\n' + self.tool_cppchecker.output + '\nSTDERR:\n' + self.tool_cppchecker.error
        self.flawfinderWidget.te_flawfinder.setText(message)

    def run_code_evaluation(self):
        self.add_CommentWidget("Clang代码质量检测")
        self.tool_clang.run_code_quality_evaluation()
        message = 'STDOUT:\n' + self.tool_clang.code_evaluation_output + '\nSTDERR:\n' + self.tool_clang.code_evaluation_error
        self.flawfinderWidget.te_flawfinder.setText(message)

    def run_code(self):
        self.tool_clang.run_exec()
        message = 'STDOUT: ' + self.tool_clang.run_output+'\n'+'STDERR: '+self.tool_clang.run_error
        self.te_log.setPlainText(message)

    def compile_code(self):
        self.tool_clang.run_compile()
        message = 'STDOUT: ' + self.tool_clang.compile_output+'\n'+'STDERR: '+self.tool_clang.compile_error
        self.te_log.setPlainText(message)

    def format_code(self, item_path):
        file_content0 = self.CodeEditor.toPlainText()
        with open(item_path, "w") as file:
            file.write(file_content0)
        self.tool_clang.format_code()
        file_content = open_with_encodings(item_path)
        if file_content is not None:
            message = 'STDOUT: ' + self.tool_clang.format_output+'\n'+'STDERR: '+self.tool_clang.format_error
            self.te_log.setPlainText(message)
            # 设置editor中的内容
            file_content = file_content + '\n' + '//' + item_path
            lexer = get_lexer_by_name('c')
            formatter = HtmlFormatter(style='xcode')
            # 获取样式定义并嵌入到 HTML 代码中
            css_style = formatter.get_style_defs('.highlight')
            highlighted_code = highlight(file_content, lexer, formatter)
            html_code = f'<style>{css_style}</style>{highlighted_code}'
            self.CodeEditor.setHtml(html_code)



    def get_file_path(self):
        item_path = self.CodeEditor.toPlainText().splitlines()[-1].replace('//', '').replace(' ', '')
        return item_path

    def muti_set_open_text(self, item_path):
        getdata = Getdata(item_path)
        getdata.get_file_info_pre()
        getdata.get_local_info()
        file_content, header_files, macro_definitions, variable_names, function_declarations = getdata.get_all_local_data()

        # 设置editor中的内容
        file_content = file_content + '\n' + '//' + item_path
        lexer = get_lexer_by_name('c')
        formatter = HtmlFormatter(style='xcode')
        # 获取样式定义并嵌入到 HTML 代码中
        css_style = formatter.get_style_defs('.highlight')
        highlighted_code = highlight(file_content, lexer, formatter)
        html_code = f'<style>{css_style}</style>{highlighted_code}'
        self.CodeEditor.setHtml(html_code)

        self.init_tools(item_path)

    def muti_get_code_text(self):
        return self.CodeEditor.toPlainText()

    def get_report(self, file_path):
        get_report(file_path)






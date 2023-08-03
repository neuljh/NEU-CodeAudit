from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtWidgets import QTextEdit, QHeaderView
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

from Data.leanCloud import *
from UI.codeAudit.commentWidget import Ui_comment
from Data.getdata import Getdata
from UI.ToolWidget.NewCodeEditor import *

from Tool.fileTree import *
from Utils import *


class comment_Widget(QtWidgets.QWidget, Ui_comment):
    def __init__(self, parent=None):
        super(comment_Widget, self).__init__(parent)
        self.setupUi(self)

        self.current_index = 0
        self.pre_cursor = None
        self.cursor = None
        self.current_line = -1
        self.pre_line = -1

        self.risk_current_index = 0
        self.risk_pre_cursor = None
        self.risk_cursor = None
        self.risk_current_line = -1
        self.risk_pre_line = -1

        self.initUI()
        self.connectSignalsSlots()

    def initUI(self):
        self.stackedWidget.setCurrentIndex(0)

        # 设置行宽
        self.ShowDefineTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ShowRiskFunctionTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置交替行的颜色
        style = "QTableWidget{												    \
                                        background-color: #a6c0f0;			\
                                        alternate-background-color: white;	\
                                             }"
        self.ShowDefineTableView.setAlternatingRowColors(True)  # 开启交替行颜色
        self.ShowDefineTableView.setStyleSheet(style)
        self.ShowRiskFunctionTableView.setAlternatingRowColors(True)  # 开启交替行颜色
        self.ShowRiskFunctionTableView.setStyleSheet(style)

    def connectSignalsSlots(self):
        self.FunctionPushButton.clicked.connect(self.on_pushButton1_clicked)
        self.RiskFunctionPushButton.clicked.connect(self.on_pushButton2_clicked)
        # 设置双击事件
        self.ShowDefineTableView.doubleClicked.connect(self. c_file_tableview_double_clicked)
        self.ShowDefineTableView.clicked.connect(self.c_file_tableview_clicked)
        self.ShowRiskFunctionTableView.doubleClicked.connect(self.riskFunction_tableview_double_clicked)

        self.commentCodeEditor.doubleClicked.connect(self.on_text_double_clicked)
        self.commentCodeEditor.clicked.connect(self.on_text_clicked)

    def on_pushButton1_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def on_pushButton2_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def find_related_text(self, selected_text):
        self.FunctionMesShowTextEdit.setPlainText('')
        item_path = self.commentCodeEditor.toPlainText().splitlines()[-1].replace('//', '').replace(' ','')
        print(item_path)
        file_obj = File(item_path)
        file_obj.parse_c_file()
        show_text = ''
        sign = True
        for function in file_obj.fun_list:
            if sign:
                show_text = show_text+ item_path + ': '
                sign = False
            for variable in function.local_variables:
                if selected_text == variable.name:
                    # print(True)
                    show_text = show_text +  '[' + 'Function: ' + str(function.line) + ',' + function.name + ']' + '[' + 'Variables: '+ str(variable.line) + ',' + variable.name+']'
                    show_text = show_text + '\n'
        sign = True
        for macro in file_obj.macro_list:
            if sign:
                show_text = show_text+ item_path + ': '
                sign = False
            if macro.name == selected_text:
                show_text = show_text  + '[' + 'Macro: ' + str(macro.line) + ',' + macro.name + '=' + macro.value + ']'
                show_text = show_text + '\n'
        sign = True
        for include in file_obj.include_list:
            if sign:
                show_text = show_text+ item_path + ': '
                sign = False
            if selected_text == include.name:
                show_text = show_text  + '[' + 'Included file: ' + str(include.line) + ',' + include.name + ']'
                show_text = show_text + '\n'
        sign = True
        for struct in file_obj.struct_list:
            if sign:
                show_text = show_text+ item_path + ': '
                sign = False
            if selected_text == struct.name:
                show_text = show_text  + '[' + 'Struct: ' + str(struct.line) + ',' + struct.name + ']'+ '[' + 'Fields: '
                for field in struct.fields:
                    show_text = show_text + field[0] + '=' + field[1] + ' '
                show_text = show_text + ']\n'
        sign = True
        for variable in file_obj.var_list:
            if sign:
                show_text = show_text+ item_path + ': '
                sign = False
            if selected_text == variable.name:
                show_text = show_text  + '[' + 'Variable: ' + str(variable.line) + ',' + variable.name + ']'
                show_text = show_text + '\n'
        print(show_text)
        self.FunctionMesShowTextEdit.setPlainText(show_text)


    @pyqtSlot(str)
    def on_text_double_clicked(self, selected_text):
        # 在双击事件发生时执行的操作
        print("双击选中的文本：", selected_text)
        self.find_related_text(selected_text)

    @pyqtSlot(str)
    def on_text_clicked(self, selected_text):
        # 在单击事件发生时执行的操作
        print("单击选中的文本：", selected_text)
        self.find_related_text(selected_text)

    def set_c_file_tableview(self, header_files, macro_definitions, variable_names, function_declarations):
        # 创建数据模型
        model = QStandardItemModel()
        # 设置列名称
        column_names = ['Name', 'Type', 'Line']
        model.setHorizontalHeaderLabels(column_names)

        # 添加数据
        datas = []

        for item in header_files:
            data = []
            data.append(item[0])
            data.append(header_file_str)
            data.append(str(item[1]))
            datas.append(data)
        for item in macro_definitions:
            data = []
            data.append(item[0])
            data.append(macro_definitions_str)
            data.append(str(item[1]))
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

        self.ShowDefineTableView.setModel(model)

    def set_RiskFunction_tableview(self, risk_function_data):
        # 创建数据模型
        model = QStandardItemModel()
        # 设置列名称
        column_names = ['FunctionName', 'RiskLevel', 'Solution', 'Line']
        model.setHorizontalHeaderLabels(column_names)

        datas = [[item['FunctionName'], item['RiskLevel'], item['Solution'], ', '.join(map(str, item['Lines']))] for
                 item in risk_function_data]
        print(datas)

        for row in datas:
            item_row = []
            for item in row:
                item_cell = QStandardItem(item)
                item_cell.setEditable(False)  # 设置单元格不可编辑
                item_row.append(item_cell)
            model.appendRow(item_row)

        self.ShowRiskFunctionTableView.setModel(model)

    def c_file_tableview_clicked(self, index):
        if self.pre_cursor is not None:
            # 设置行的格式
            format = self.pre_cursor.blockFormat()
            format.setBackground(QColor("#FFFFFF"))
            self.pre_cursor.setBlockFormat(format)
            # 将光标设置为初始位置
            self.pre_cursor.movePosition(QTextCursor.StartOfBlock)
            self.pre_cursor.setPosition(self.pre_cursor.position() + len(self.pre_cursor.block().text()),
                                        QTextCursor.KeepAnchor)

    def c_file_tableview_double_clicked(self, index):
        tableview = self.ShowDefineTableView
        pte_content = self.ShowTextEdit
        code_text_new = self.commentCodeEditor
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
            self.current_line = line
            print(data)
            # 找到所有匹配字符并存储
            search_text = data[0]
            # cursor = code_text_new.textCursor()
            format = QTextCharFormat()
            format.setBackground(QColor("#92acdc"))

            extra_selections = []
            code_text_new.moveCursor(QTextCursor.Start)
            cursor = code_text_new.textCursor()

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
            selections = code_text_new.extraSelections()

            if self.current_index == len(selections) and self.current_line == self.pre_line:
                self.current_index = 0
            elif self.current_line != self.pre_line:
                self.current_index = 0
            print('selections length: ')
            print(len(selections))
            print('current_index: ')
            print(self.current_index)

            if self.current_index < len(selections):
                self.cursor = QTextCursor(selections[self.current_index].cursor)
                code_text_new.setTextCursor(self.cursor)
                if self.current_line == self.pre_line:
                    self.current_index += 1

                if self.pre_cursor is not None:
                    # 设置行的格式
                    format = self.pre_cursor.blockFormat()
                    format.setBackground(QColor("#FFFFFF"))
                    self.pre_cursor.setBlockFormat(format)
                    # 将光标设置为初始位置
                    self.pre_cursor.movePosition(QTextCursor.StartOfBlock)
                    self.pre_cursor.setPosition(self.pre_cursor.position() + len(self.pre_cursor.block().text()),
                                                QTextCursor.KeepAnchor)

                line_number = self.cursor.blockNumber()

                if int(line) == line_number+1:
                    # 设置行的格式
                    format = self.cursor.blockFormat()
                    format.setBackground(QColor("#9294dc"))
                    self.cursor.setBlockFormat(format)

                    # 将光标设置为初始位置
                    self.cursor.movePosition(QTextCursor.StartOfBlock)
                    self.cursor.setPosition(self.cursor.position() + len(self.cursor.block().text()), QTextCursor.KeepAnchor)
                self.pre_cursor = self.cursor
                self.pre_line = self.current_line

    def riskFunction_tableview_double_clicked(self, index):
        tableview = self.ShowRiskFunctionTableView
        pte_content = self.RiskFunctionShowTextEdit
        code_text_new = self.commentCodeEditor
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
            line = data[3].split(',')
            # 使用列表推导式和 strip() 方法去除空格
            cleaned_list = [element.strip() for element in line]
            print(cleaned_list)

            value = data[0].strip()
            print(value)
            # 找到所有匹配字符并存储
            search_text = value
            # cursor = code_text_new.textCursor()
            format = QTextCharFormat()
            format.setBackground(QColor("yellow"))

            extra_selections = []
            code_text_new.moveCursor(QTextCursor.Start)
            cursor = code_text_new.textCursor()

            while cursor.hasComplexSelection() or cursor.atEnd() == False:
                cursor = code_text_new.document().find(search_text, cursor)

                if cursor.isNull() == False:
                    target_number = cursor.block().blockNumber() + 1
                    for line_number in line:
                        if str(target_number) == line_number:
                            selection = QTextEdit.ExtraSelection()
                            selection.format = format
                            selection.cursor = QTextCursor(cursor)
                            extra_selections.append(selection)
                else:
                    break
            code_text_new.setExtraSelections(extra_selections)

            #
            selections = code_text_new.extraSelections()
            self.current_index = 0
            print('selections length: ')
            print(len(selections))
            print('current_index: ')
            print(self.current_index)

            if self.current_index < len(selections):
                self.cursor = QTextCursor(selections[self.current_index].cursor)
                code_text_new.setTextCursor(self.cursor)
                if self.current_line == self.pre_line:
                    self.current_index += 1

                if self.pre_cursor is not None:
                    # 设置行的格式
                    format = self.pre_cursor.blockFormat()
                    format.setBackground(QColor("#FFFFFF"))
                    self.pre_cursor.setBlockFormat(format)
                    # 将光标设置为初始位置
                    self.pre_cursor.movePosition(QTextCursor.StartOfBlock)
                    self.pre_cursor.setPosition(self.pre_cursor.position() + len(self.pre_cursor.block().text()),
                                                QTextCursor.KeepAnchor)

                line_number = self.cursor.blockNumber()
                for line_num in line:
                    if int(line_num) == line_number+1:
                        # 设置行的格式
                        format = self.cursor.blockFormat()
                        format.setBackground(QColor("#9294dc"))
                        self.cursor.setBlockFormat(format)

                        # 将光标设置为初始位置
                        self.cursor.movePosition(QTextCursor.StartOfBlock)
                        self.cursor.setPosition(self.cursor.position() + len(self.cursor.block().text()), QTextCursor.KeepAnchor)
                    self.pre_cursor = self.cursor
                    self.pre_line = self.current_line


    def set_open_text(self, item_path):
        getdata = Getdata(item_path)
        getdata.get_file_info_pre()
        getdata.get_local_info()
        file_content, header_files, macro_definitions, variable_names, function_declarations = getdata.get_all_local_data()
        # 设置tableview中的内容
        self.set_c_file_tableview(header_files, macro_definitions, variable_names, function_declarations)

        risk_function_data = detectRiskFunction(item_path)
        # 添加行数检测
        new_risk_function_data = []
        for data in risk_function_data:
            risk_line = function_exists_in_file(file_content, data['FunctionName'])
            new_data = {
                'FunctionName': data['FunctionName'],
                'RiskLevel': data['RiskLevel'],
                'Solution': data['Solution'],
                'Lines': risk_line
            }
            new_risk_function_data.append(new_data)
        print(new_risk_function_data)
        self.set_RiskFunction_tableview(new_risk_function_data)

        # 设置editor中的内容
        file_content = file_content + '\n' + '//' + item_path
        lexer = get_lexer_by_name('c')
        formatter = HtmlFormatter(style='xcode')
        # 获取样式定义并嵌入到 HTML 代码中
        css_style = formatter.get_style_defs('.highlight')
        highlighted_code = highlight(file_content, lexer, formatter)
        html_code = f'<style>{css_style}</style>{highlighted_code}'
        self.commentCodeEditor.setHtml(html_code)

    def get_code_text(self):
        return self.commentCodeEditor.toPlainText()
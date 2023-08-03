import clang.cindex

from Utils import *
class Getdata:
    def __init__(self, c_file):
        self.c_file = c_file
        self.file_content = ''
        self.header_files = []
        self.macro_definitions = []
        self.variable_names = []
        self.function_declarations = []
        self.variable_names_all = []
        self.function_declarations_all = []

    def get_unique_datas(self, lists):
        unique_lists = list(set(lists))
        return unique_lists

    def get_file_info_pre(self):

        lines = open_with_encodings(self.c_file)
        index = 1
        # print(lines)
        for line in lines:
            if line.startswith('#include'):
                self.header_files.append((line.strip(), index))
            elif line.startswith('#define'):
                self.macro_definitions.append((line.strip(), index))
            self.file_content += line
            index = index + 1
        self.header_files = self.get_unique_datas(self.header_files)
        self.macro_definitions = self.get_unique_datas(self.macro_definitions)

        return self.file_content, self.header_files, self.macro_definitions

    def get_local_info(self):
        index = clang.cindex.Index.create()
        tu = index.parse(self.c_file)

        for node in tu.cursor.walk_preorder():
            if node.location.file is not None and node.location.file.name == self.c_file:
                if node.kind == clang.cindex.CursorKind.VAR_DECL:
                    var_name = node.spelling
                    var_type = node.type.spelling
                    var_location = node.location.line
                    self.variable_names.append((var_name, var_type, var_location))
                elif node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                    func_name = node.spelling
                    func_type = node.type.spelling
                    func_location = node.location.line
                    self.function_declarations.append((func_name, func_type, func_location))

        return self.variable_names, self.function_declarations

    def get_exter_info(self):
        index = clang.cindex.Index.create()
        tu = index.parse(self.c_file)

        for node in tu.cursor.walk_preorder():
            if node.kind == clang.cindex.CursorKind.VAR_DECL:
                var_name = node.spelling
                var_type = node.type.spelling
                var_location = node.location.line
                self.variable_names_all.append((var_name, var_type, var_location))
            elif node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                func_name = node.spelling
                func_type = node.type.spelling
                func_location = node.location.line
                self.function_declarations_all.append((func_name, func_type, func_location))

        return self.variable_names_all, self.function_declarations_all

    def get_all_local_data(self):
        return self.file_content, self.header_files, self.macro_definitions, self.variable_names, self.function_declarations

    def get_all_exter_data(self):
        return self.file_content, self.header_files, self.macro_definitions, self.variable_names_all, self.function_declarations_all

    def get_variable_locations(self, var):
        locals = []
        for variable_tuple in self.variable_names:
            variable = variable_tuple[0]
            type = variable_tuple[1]
            locs = variable_tuple[2]
            if (var == variable):
                locals.append(locs)
        return locals

    def get_func_locations(self, func):
        locals = []
        for func_tuple in self.function_declarations:
            variable = func_tuple[0]
            type = func_tuple[1]
            locs = func_tuple[2]
            if (func == variable):
                locals.append(locs)
        return locals

    def get_unused_entities(self):
        index = clang.cindex.Index.create()
        tu = index.parse(self.c_file)

        unused_entities = []

        # 保存已使用的实体（变量和函数）
        used_entities = set()

        # 遍历语法树
        for node in tu.cursor.walk_preorder():
            if node.location.file is not None and node.location.file.name == self.c_file:
                # 处理变量声明
                if node.kind == clang.cindex.CursorKind.VAR_DECL:
                    var_name = node.spelling
                    # 添加变量名到已使用的实体集合
                    used_entities.add(var_name)

                # 处理函数定义
                elif node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                    func_name = node.spelling
                    # 添加函数名到已使用的实体集合
                    used_entities.add(func_name)

                # 处理变量和函数引用
                elif node.kind == clang.cindex.CursorKind.DECL_REF_EXPR:
                    entity_name = node.spelling
                    # 从已使用的实体集合中移除引用到的变量或函数名
                    used_entities.discard(entity_name)

        # 剩下的实体即为未使用的变量和函数
        for entity_name in used_entities:
            unused_entities.append(entity_name)

        return unused_entities

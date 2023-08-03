# import clang.cindex
#
# def get_variable_function_info(file_path):
#     index = clang.cindex.Index.create()
#     tu = index.parse(file_path)
#
#     variable_info = []
#     function_info = []
#
#     for node in tu.cursor.walk_preorder():
#         if node.kind == clang.cindex.CursorKind.VAR_DECL:
#             var_name = node.spelling
#             var_type = node.type.spelling
#             variable_info.append((var_name, var_type))
#         elif node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
#             func_name = node.spelling
#             func_type = node.type.spelling
#             function_info.append((func_name, func_type))
#
#     return variable_info, function_info
#
# # 调用get_variable_function_info()函数来提取变量名、变量类型、函数名和函数类型
# file_path = '../test.c'  # 替换为你的C语言文件路径
# variables, functions = get_variable_function_info(file_path)
#
# print("Variables:")
# for variable in variables:
#     name, var_type = variable
#     print(f"Variable name: {name}, Variable type: {var_type}")
#
# print("\nFunctions:")
# for function in functions:
#     name, func_type = function
#     print(f"Function name: {name}, Function type: {func_type}")

import clang.cindex

def get_variable_function_info(file_path):
    index = clang.cindex.Index.create()
    tu = index.parse(file_path)

    variable_info = []
    function_info = []

    for node in tu.cursor.walk_preorder():
        if node.location.file is not None and node.location.file.name == file_path:
            if node.kind == clang.cindex.CursorKind.VAR_DECL:
                var_name = node.spelling
                var_type = node.type.spelling
                variable_info.append((var_name, var_type))
            elif node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                func_name = node.spelling
                func_type = node.type.spelling
                function_info.append((func_name, func_type))

    return variable_info, function_info

# 调用get_variable_function_info()函数来提取变量名、变量类型、函数名和函数类型
file_path = '../test.c'  # 替换为你的C语言文件路径
variables, functions = get_variable_function_info(file_path)

print("Variables:")
print(variables)
for variable in variables:
    name, var_type = variable

    # print(f"Variable name: {name}, Variable type: {var_type}")

print("\nFunctions:")
print(functions)
for function in functions:
    name, func_type = function

    # print(f"Function name: {name}, Function type: {func_type}")

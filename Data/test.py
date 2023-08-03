from getdata import *

folder = 'X:\\feem\\work\\c_test_file\\'
file = folder + 'linklist.c'
# file = '../test.cpp'
getdata = Getdata(file)
header_files = []
variable_names = []
macro_definitions = []
function_declarations = []
getdata.get_file_info_pre()
getdata.get_local_info()
file_content, header_files,  macro_definitions, variable_names,function_declarations = getdata.get_all_local_data()
print('header_files: ')
print(header_files)
print('variable_names: ')
print(variable_names)
print('macro_definitions: ')
print(macro_definitions)
print('function_declarations: ')
print(function_declarations)
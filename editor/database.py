# 参考 https://leancloud.cn/docs/sdk_setup-python.html, https://leancloud.github.io/python-sdk/

import leancloud
import os
appId = 'hrwjWdJzRfN5ewluWwtvoono-gzGzoHsz'
appKey = 'J4WDUUz6lekpuSAGiVpLvF3x'
masterkey = "ZDm5SkP4WOnkeK7suMar3gmU"
lean_initialization = leancloud.init(appId, master_key=masterkey)

# import logging
# logging.basicConfig(level=logging.DEBUG)
def add_element(table_name, value_dict):
    """
    @description: 插入函数
    @Time：2023/7/14 || 10:08 ||20324
    """
    Todo = leancloud.Object.extend(table_name)
    todo = Todo()
    for key, value in value_dict.items():
        todo.set(key, value)
    todo.save()
    print('add')

def clear(table_name):
    """
    @description: 清空函数，如果table_name为空不需要删除
    @Time：2023/7/14 || 11:20 ||20324
    """
    YourClass = leancloud.Object.extend(table_name)

    # 查询 class
    query = YourClass.query
    objects = query.find()
    # query = leancloud.Query(table_name)
    # objects = query.find()
    if objects:  #不为空开始删除
        for obj in objects:
            obj.destroy()
        print('delete')

def query_element(table_name,value_key,value):
    query = leancloud.Query(table_name)
    query.equal_to(value_key,value)
    return query.find()

class crawler_database:
    """
    @description: 将爬取的数据存入数据库，addfile函数实现，接受一个file class 对象
    @Time：2023/7/14 || 11:21 ||20324
    """
    def __init__(self):
        self.filename=""
        self.fun_table_name="Function"
        self.gobal_var_table_name = "GobalVar"
        self.Macro_name = "Macro"
        self.Include_name = "Include"
        self.Struct_name = "Struct"
    def clear_element(self):
        #清空元素
        clear(self.fun_table_name)
        clear(self.gobal_var_table_name)
        clear(self.Macro_name)
        clear(self.Include_name)
        clear(self.Struct_name)

    def add_file(self,file_obj):
        # 声明 class
        self.filename=os.path.split(file_obj.file_path)[1]
        for fun_obj in file_obj.fun_list:
            self.add_function(fun_obj)
        for instance in file_obj.var_list:
            self.add_Variable(instance)
        for instance in file_obj.macro_list:
            self.add_Macro(instance)
        for instance in file_obj.struct_list:
            self.add_Struct(instance)
        for instance in file_obj.include_list:
            self.add_Include(instance)

    def add_function(self,fun_obj):
        var_list=[]
        for var_obj in fun_obj.local_variables:
            var_dict = {
                "name":var_obj.name,
                "type":var_obj.type,
                "line":var_obj.line
            }
            var_list.append(var_dict)
        value_dict={
            "file":self.filename,
            "name":fun_obj.name,
            'parameters' : fun_obj.parameters,
            'local_variables':var_list,
            "local_function":fun_obj.local_functions,
            'return_type':fun_obj.return_type,
            'is_define':fun_obj.is_define,
            'begin_line':fun_obj.line,
            'end_line':fun_obj.end_line
        }
        add_element(self.fun_table_name,value_dict)


    def add_Variable(self,object):
        value_dict = {
            "file": self.filename,
            "name":object.name,
            "type":object.type,
            "line":object.line
        }
        add_element(self.gobal_var_table_name, value_dict)

    def add_Macro(self,object):
        value_dict = {
            "file": self.filename,
            "name": object.name,
            "value": object.value,
            "line": object.line
        }
        add_element(self.Macro_name, value_dict)
    def add_Include(self,object):
        value_dict = {
            "file": self.filename,
            "name": object.name,
            "line": object.line
        }
        add_element(self.Include_name, value_dict)
    def add_Struct(self,object):
        value_dict = {
            "file": self.filename,
            "name": object.name,
            "line": object.line,
            "fields":object.fields
        }
        add_element(self.Struct_name, value_dict)
# fun_table_name="Function"
# gobal_var_table_name = "GobalVar"
# Macro_name = "Macro"
# Include_name = "Include"
# Struct_name = "Struct"
# clear(fun_table_name)
# clear(gobal_var_table_name)
# clear(Macro_name)
# clear(Include_name)
# clear(Struct_name)
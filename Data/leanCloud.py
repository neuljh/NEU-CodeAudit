# 参考 https://leancloud.cn/docs/sdk_setup-python.html, https://leancloud.github.io/python-sdk/

import leancloud
from Tool.crawler import *
from Data.crypto import *

appId = 'Your appID'
appKey = 'Your appKey'
masterkey = "Your masterkey"

'''初始化'''
# lean_initialization = leancloud.init(appId, appKey)
lean_initialization = leancloud.init(appId, master_key=masterkey)
# print(lean_initialization)  #None

'''开启调试日志'''
# 调试日志开启后，SDK 会把网络请求、错误消息等信息输出到 IDE 的日志窗口，
# 或是浏览器 Console 或是云引擎日志（如果在云引擎下运行 SDK）。
# import logging
# logging.basicConfig(level=logging.DEBUG)

# '''验证'''
# TestObject = leancloud.Object.extend('TestObject')  #派生一个新的 leancloud.Object 子类 TestObject
# test_object = TestObject()
# test_object.set('words', "Hello world!")    #在当前对象此字段(words)上赋值(Hello world!)
# test_object.save()   #将对象数据保存至服务器


'''风险函数存储'''
# RiskFunctionObject = leancloud.Object.extend('RiskFunctionObject')
# riskFunctionObject = RiskFunctionObject()
# riskFunctionObject.set('FunctionName', "gets")
# riskFunctionObject.set('RiskLevel', "最危险")
# riskFunctionObject.set('Solution', "使用更安全的fgets()函数或定义足够大的数组空间")
# riskFunctionObject.save()

'''风险函数打印'''


def riskFunctionShow(riskFunction):
    print(f'objectId = {riskFunction.get("objectId")}, '
          f'FunctionName = {riskFunction.get("FunctionName")}, '
          f'RiskLevel = {riskFunction.get("RiskLevel")}, '
          f'Solution = {riskFunction.get("Solution")}, ')


'''风险函数查询'''


def riskFunctionQuery(FunctionName):
    RiskFunctionObject = leancloud.Object.extend('RiskFunctionObject')
    query = RiskFunctionObject.query
    query.equal_to('FunctionName', FunctionName)
    RiskFunction_list = query.find()
    for riskFunction in RiskFunction_list:
        # riskFunctionShow(riskFunction)
        result = []
        result.append(riskFunction.get("FunctionName"))
        result.append(riskFunction.get("RiskLevel"))
        result.append(riskFunction.get("Solution"))
        return result


def getRiskFunction():
    """
    获取风险函数库中的所有函数
    返回格式：[{'FunctionName': "xxx",
              'RiskLevel': "xxx",
              'Solution': "xxx"
    }]
    """
    query = leancloud.Query('RiskFunctionObject')
    riskFunctionObject = query.find()
    riskFunctionResult = []
    for riskFunction in riskFunctionObject:
        result = {'FunctionName': riskFunction.get('FunctionName'),
                  'RiskLevel': riskFunction.get('RiskLevel'),
                  'Solution': riskFunction.get('Solution')}
        riskFunctionResult.append(result)
    # print(riskFunctionResult)
    return riskFunctionResult


def addRiskFunction(FunctionName=None, RiskLevel=None, Solution=None):
    RiskFunctionObject = leancloud.Object.extend('RiskFunctionObject')
    riskFunctionObject = RiskFunctionObject()
    riskFunctionObject.set('FunctionName', FunctionName)
    riskFunctionObject.set('RiskLevel', RiskLevel)
    riskFunctionObject.set('Solution', Solution)
    riskFunctionObject.save()
    print('add')
    return True


def deleteRiskFunction(FunctionName):
    query = leancloud.Query('RiskFunctionObject')
    query.equal_to('FunctionName', FunctionName)
    row = query.first()
    if row:
        row.destroy()
        print("delete yes")
        return True
    else:
        print("delete no")
        return False


def detectRiskFunction(filePath):
    fileObj = File(filePath)
    functionName = fileObj.get_function_name()
    print(functionName)

    result = []
    for risk in getRiskFunction():
        if risk['FunctionName'] in functionName:
            result.append(risk)
    print(result)
    return result


# filePath = "D:\Code-reviewer\Code-Reviewer-Porject\c_test_file\graph.c"
# print(detectRiskFunction(filePath))

'''用户信息存储'''


def UserStore(username, password):
    UserObject = leancloud.Object.extend('UserObject')
    userObject = UserObject()
    userObject.set('Username', username)
    str_my_hashpassword = passwd_hash(password)
    userObject.set('Password', str_my_hashpassword)
    userObject.save()


'''用户信息打印'''


def UserShow(riskFunction):
    print(f'objectId = {riskFunction.get("objectId")}, '
          f'Username = {riskFunction.get("username")}, '
          f'Password = {riskFunction.get("password")}, ')


'''用户信息匹配'''


def UserQuery(Login_username):
    '''
    基础查询: 创建Object.query查询对象，用equal_to设置查询条件，用find进行查询
        构建 leancloud.Query；
        向其添加查询条件；
        执行查询并获取包含满足条件的对象的数组。
    '''
    query = leancloud.Query('UserObject')
    query.equal_to('Username', Login_username)
    User_list = query.find()
    for User in User_list:
        return User.get("Password")

# ------------------fuzz------------------

def getStringFuzz():
    query = leancloud.Query('StringFuzzObject')
    FuzzObject = query.find()
    FuzzResult = []
    for Fuzz in FuzzObject:
        result = {'id':Fuzz.get('id'),
                  'FuzzRandomString': Fuzz.get('FuzzRandomString')}
        FuzzResult.append(result)
    # print(FuzzResult)
    return FuzzResult

def getIntFuzz():
    query = leancloud.Query('IntFuzzObject')
    FuzzObject = query.find()
    FuzzResult = []
    for Fuzz in FuzzObject:
        result = {'id':Fuzz.get('id'),
                  'FuzzRandomInteger': Fuzz.get('FuzzRandomInteger')}
        FuzzResult.append(result)
    # print(FuzzResult)
    return FuzzResult

def getByteFuzz():
    query = leancloud.Query('ByteFuzzObject')
    FuzzObject = query.find()
    FuzzResult = []
    for Fuzz in FuzzObject:
        result = {'id':Fuzz.get('id'),
                  'FuzzRandomByte': Fuzz.get('FuzzRandomByte')}
        FuzzResult.append(result)
    # print(FuzzResult)
    return FuzzResult


def addStringFuzz(FuzzRandomString=None):
    FuzzObject = leancloud.Object.extend('StringFuzzObject')

    query = FuzzObject.query
    query.descending('id')
    query.limit(1)
    latest_object = query.first()
    if latest_object is None:
        new_id = 1  # 初始为1
    else:
        latest_id = latest_object.get('id')
        new_id = latest_id + 1  # 比当前最大id+1

    FuzzObject = FuzzObject()
    FuzzObject.set('id', new_id)
    FuzzObject.set('FuzzRandomString', FuzzRandomString)
    FuzzObject.save()
    print('add')
    return True

def addIntFuzz(FuzzRandomInteger=None):
    FuzzObject = leancloud.Object.extend('IntFuzzObject')

    query = FuzzObject.query
    query.descending('id')
    query.limit(1)
    latest_object = query.first()
    if latest_object is None:
        new_id = 1  # 初始为1
    else:
        latest_id = latest_object.get('id')
        new_id = latest_id + 1  # 比当前最大id+1

    FuzzObject = FuzzObject()
    FuzzObject.set('id', new_id)
    FuzzObject.set('FuzzRandomInteger', FuzzRandomInteger)
    FuzzObject.save()
    print('add')
    return True

def addByteFuzz(FuzzRandomByte=None):
    FuzzObject = leancloud.Object.extend('ByteFuzzObject')

    query = FuzzObject.query
    query.descending('id')
    query.limit(1)
    try:
        latest_object = query.first()
        latest_id = latest_object.get('id')
        new_id = latest_id + 1  # Increment the current maximum id
    except leancloud.errors.LeanCloudError as e:
        # Handle the error if no object is found (101 error code)
        if e.code == 101:
            new_id = 1  # Initialize to 1 if no objects found
        else:
            # Handle other errors as needed
            print("Error:", e)

    FuzzObject = FuzzObject()
    FuzzObject.set('id', new_id)
    FuzzObject.set('FuzzRandomByte', FuzzRandomByte)
    FuzzObject.save()
    print('add')
    return True


# def addStringFuzz1(FuzzRandomString=None):
#     FuzzObject = leancloud.Object.extend('StringFuzzObject')
#     FuzzObject = FuzzObject()
#     FuzzObject.set('id', 1)
#     FuzzObject.set('FuzzRandomString', FuzzRandomString)
#     FuzzObject.save()
#     print('add')
#     return True
#
# def addIntFuzz1(FuzzRandomInteger=None):
#     FuzzObject = leancloud.Object.extend('IntFuzzObject')
#     FuzzObject = FuzzObject()
#     FuzzObject.set('id', 1)
#     FuzzObject.set('FuzzRandomInteger', FuzzRandomInteger)
#     FuzzObject.save()
#     print('add')
#     return True
#
# def addByteFuzz1(FuzzRandomByte=None):
#     FuzzObject = leancloud.Object.extend('ByteFuzzObject')
#     FuzzObject = FuzzObject()
#     FuzzObject.set('id', 1)
#     FuzzObject.set('FuzzRandomByte', FuzzRandomByte)
#     FuzzObject.save()
#     print('add')
#     return True

def deleteFuzz(sign, id):
    table = ""
    if sign == 1:
        table = "String"
    elif sign == 2:
        table = "Int"
    elif sign == 3:
        table = "Byte"

    object_name = table + 'FuzzObject'
    query = leancloud.Query(object_name)
    query.equal_to('id', id)
    row = query.first()
    if row:
        row.destroy()
        print("delete yes")
        return True
    else:
        print("delete no")
        return False

def deleteFuzz1(id):
    object_name = 'StringFuzzObject'
    query = leancloud.Query(object_name)
    query.equal_to('id', id)
    row = query.first()
    if row:
        row.destroy()
        print("delete yes")
        return True
    else:
        print("delete no")
        return False

def deleteFuzz2(id):
    object_name = 'IntFuzzObject'
    query = leancloud.Query(object_name)
    query.equal_to('id', id)
    row = query.first()
    if row:
        row.destroy()
        print("delete yes")
        return True
    else:
        print("delete no")
        return False

def deleteFuzz3(id):
    object_name = 'ByteFuzzObject'
    query = leancloud.Query(object_name)
    query.equal_to('id', id)
    row = query.first()
    if row:
        row.destroy()
        print("delete yes")
        return True
    else:
        print("delete no")
        return False

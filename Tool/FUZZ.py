"""
@FileName：FUZZ.py
@Description:
@Time：2023/7/18 10:53
@user: 20324
"""
import random
import string

from Data.leanCloud import *

import sys
from io import StringIO


def get_bytes_to_str(print_bytes):
    # 创建一个字符串缓冲区作为标准输出的替代
    output_buffer = StringIO()
    # 重定向标准输出流到缓冲区
    sys.stdout = output_buffer
    # 执行打印操作
    print(print_bytes)
    # 获取缓冲区中的内容并存储到变量中
    data = output_buffer.getvalue()
    # 还原标准输出流
    sys.stdout = sys.__stdout__
    # 打印存储的内容
    return data


class Fuzz:
    def __init__(self):
        self.len = random.randint(4, 10)
        self.time = 10

    # 生成随机字符串
    def generate_random_string(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(self.len))

    # 生成随机整数
    def generate_random_integer(self, min_value, max_value):
        return get_bytes_to_str(random.randint(min_value, max_value))

    # # 生成随机字节流
    def generate_random_bytes(self):
        return get_bytes_to_str(bytes(random.getrandbits(8) for _ in range(self.len)))

    # def get_result(self):
    #     random_string = self.generate_random_string()
    #     random_integer = self.generate_random_integer(1, pow(10,self.len))
    #     random_bytes = self.generate_random_bytes()
    #     dict={
    #         "String": random_string,
    #         "Integer": random_integer,
    #         "Bytes": random_bytes
    #     }
    #     return dict

    def generate_string(self):
        for i in range(self.time):
            random_string = self.generate_random_string()
            addStringFuzz(random_string)

    def generate_int(self):
        for i in range(self.time):
            random_int = self.generate_random_integer(1, pow(10,self.len))
            addIntFuzz(random_int)

    def generate_byte(self):
        for i in range(self.time):
            random_byte = self.generate_random_bytes()
            addByteFuzz(random_byte)

        
# # 示例用法
# obj=Fuzz(10)
# dict=obj.get_result()
# print("Random String:", dict['String'])
# print("Random Integer:", dict["Integer"])
# print("Random Bytes:", dict["Bytes"])

# obj = Fuzz()
# obj.generate_string()
# obj.generate_byte()
# obj.generate_int()
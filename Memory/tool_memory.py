import subprocess
import os
import re
class ToolMemoryChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.output = ''
        self.error = ''
        self.compile_output = ''
        self.compile_error = ''

    #需要提前调用ToolClang库中的run_compile，如果没有则调用下面的gcc
    #drmemory.exe D:\work1\c_test_file\test.exe
    def run(self):
        cmd = ['drmemory.exe', self.file_path.replace('.c', '.exe')]
        print(cmd)
        # 执行命令并捕获输出
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            output = result.stderr
            self.output = output
            print(self.output)
        except subprocess.CalledProcessError as e:
            error_output = e.stderr
            self.error = error_output
            print(self.error)

    #gcc -o D:\work1\c_test_file\test.exe D:\work1\c_test_file\test.c
    def run_gcc_compile(self):
        cmd = ['gcc', '-o', self.file_path.replace('.c', '.exe'), self.file_path]
        print(cmd)
        # 执行命令并捕获输出
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            output = result.stderr
            self.compile_output = output
            if self.compile_output == '':
                self.compile_output = self.compile_output + 'The program compiles successfully ( '+self.file_path+' )'
            print(self.output)
        except subprocess.CalledProcessError as e:
            error_output = e.stderr
            self.compile_error = error_output
            print(self.error)

    def run_cl_compile(self):
        # clang  -g -o main.exe main.c graph.c
        cmd=f"clang -g -o {self.file_path.replace('.c', '.exe')} {self.file_path}"
        cmd=cmd.split(' ')
        print(cmd)
        # 执行命令并捕获输出
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            output = result.stderr
            self.compile_output = output
            if self.compile_output == '':
                self.compile_output = self.compile_output + 'The program compiles successfully ( '+self.file_path+' )'

        except subprocess.CalledProcessError as e:
            error_output = e.stderr
            self.compile_error = error_output
        print('stdout')
        print(self.compile_output)
        print('stderr')
        print(self.error)

    def extract_memory_leaks(self):
        text=self.output
        errors=[] #error的列表
        errors_summery=[]
        current_error = ""
        recording = False #判断是否开始查找errors_summery 部分

        content = re.sub(r'^~~Dr\.M~~ ','', text, flags=re.IGNORECASE | re.MULTILINE) #删除前缀
        for line in content.splitlines():
            if line.startswith('#'):
                current_error += line + "\n"
            elif line.startswith("Error #"):
                if current_error:  # 不为空
                    errors.append(current_error.strip())  # strip()函数是Python中用于去除字符串首尾的空格或指定字符的方法
                    print(current_error)
                    current_error = ""
                current_error += line + "\n"
            else:
                if current_error:  # 不为空
                    errors.append(current_error.strip())  # strip()函数是Python中用于去除字符串首尾的空格或指定字符的方法
                    print(current_error)
                    current_error = ""

            if line.startswith("ERRORS FOUND:"):
                recording = True
                continue
            if recording and line.strip():
                numbers = re.findall(r'\d+', line) #对于line查找数字,
                errors_summery.append(numbers)
            elif recording and not line.strip():  # 遇到空行，停止记录
                recording = False
        errors_summery=convert_to_list(errors_summery)
        return errors,errors_summery

def convert_to_list(num_list):
    value = [
        'unaddressable access(es)',
        'uninitialized access(es)',
        'invalid heap argument(s)',
        'GDI usage error(s)',
        'handle leak(s)',
        'warning(s)',
        'leak(s)',
        'possible leak(s)'
    ]
    # 在每个子列表的索引 0 处插入 value 中的元素
    main_list_with_value = [[v] + sublist for sublist, v in zip(num_list, value)]
    return main_list_with_value
if __name__ == '__main__':
    # example
    c_file_path = r'D:\work1\c_test_file\test\flawfinder.c'
    tool_memory = ToolMemoryChecker(c_file_path)
    # tool_memory.run_gcc_compile()
    tool_memory.run_cl_compile()
    # tool_memory.run()
    # tool_memory.extract_memory_leaks()


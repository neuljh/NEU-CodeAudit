import subprocess


class ToolCppChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.output = ''
        self.error = ''

    # cppcheck --enable=all --std=c11 --verbose D:\work1\c_test_file\test.c
    def run_scan(self):
        cmd = ['cppcheck', '--enable=all', '--std=c11', '--verbose', self.file_path]
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

if __name__ == '__main__':
    # #example
    c_file_path = 'D:/work1/c_test_file/test.c'
    tool_cppcheck = ToolCppChecker(c_file_path)
    tool_cppcheck.run_scan()

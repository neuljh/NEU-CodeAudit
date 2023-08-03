import re
import subprocess
from Utils import *


class ToolFlawfinder:
    def __init__(self, filepath):
        self.c_file_path = filepath
        self.error = None
        self.result_text = None
        self.copy_right = ''
        self.detect_rules = ''
        self.examing_file = ''
        self.pattern1 = r"FINAL RESULTS:(.*?)ANALYSIS SUMMARY:"
        self.final_results = ''
        self.pattern2 = r"ANALYSIS SUMMARY:(.*?)$"
        self.analysis_summary = ''
        self.hits = ''
        self.detect_lines = ''
        self.detect_real_lines = ''
        self.Hits_level = ''
        self.Hits_level_plus = ''
        self.KSLOC = ''
        self.Minimum_risk_level = ''

        self.pattern3 = r"\[\d+\]\s+(\d+)"  # 匹配方括号和数字
        self.pattern4 = r"\[\d+\+\]\s+(\d+)"  # 匹配方括号+和数字
        self.levels = []
        self.levels_plus = []
        self.levels_plus_KSLOC = []

    def run(self):
        # 构建Flawfinder命令
        cmd = ['flawfinder', self.c_file_path]
        # 执行Flawfinder命令并捕获输出
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
            self.result_text = output
        except subprocess.CalledProcessError as e:
            self.error = e.output

    def get_data(self):
        if self.result_text is not None:
            self.copy_right = self.result_text.splitlines()[0] + neu_copy_right
            self.detect_rules = self.result_text.splitlines()[1]
            self.examing_file = self.result_text.splitlines()[2]
            self.final_results = re.findall(self.pattern1, self.result_text, re.DOTALL)[0].strip()
            self.analysis_summary = re.findall(self.pattern2, self.result_text, re.DOTALL)[0].strip()
            self.hits = self.analysis_summary.splitlines()[0]
            self.detect_lines = self.analysis_summary.splitlines()[1]
            self.detect_real_lines = self.analysis_summary.splitlines()[2]
            self.Hits_level = self.analysis_summary.splitlines()[3]
            self.Hits_level_plus = self.analysis_summary.splitlines()[4]
            self.KSLOC = self.analysis_summary.splitlines()[5]
            self.Minimum_risk_level = self.analysis_summary.splitlines()[6]

    def get_graph_base_data(self):
        self.levels = re.findall(self.pattern3, self.Hits_level)
        self.levels_plus = re.findall(self.pattern4, self.Hits_level_plus)
        self.levels_plus_KSLOC = re.findall(self.pattern4, self.KSLOC)




if __name__ == '__main__':
    # example
    c_file_path = 'D:/work1/c_test_file/graph.c'
    tool_flawfinder = ToolFlawfinder(c_file_path)
    tool_flawfinder.run()
    tool_flawfinder.get_data()
    tool_flawfinder.get_graph_base_data()

    copy_right = tool_flawfinder.copy_right
    print(tool_flawfinder.result_text)
    print(tool_flawfinder.levels)
    print(tool_flawfinder.levels_plus)
    print(tool_flawfinder.levels_plus_KSLOC)
    # ...get other data

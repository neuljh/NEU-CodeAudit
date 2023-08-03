"""
@FileName：compile.py
@Description:
@Time：2023/7/19 9:51
@user: 20324
"""
import os
import subprocess
from Memory import run_cmd
def compile_project(main_path, inc_path="", src_path=""):
    # 对于指定main_path下的main.c文件进行编译
    if not inc_path:
        folder_path=os.path.dirname(main_path)
        inc_path=os.path.join(folder_path,'inc')
        src_path = os.path.join(folder_path, 'src')
    exe_path=main_path.replace('.c','.exe')
    cmd = f'clang -g -o {exe_path} {main_path} {src_path}/*.c -I{inc_path}'
    # cmd_list = cmd.split(' ')
    try:
       result=run_cmd(cmd)
    except subprocess.CalledProcessError as e:
        print(f"GCC compile error: {e.stderr}")

if __name__ == '__main__':
    main_path = r'X:\feem\work\project\main.c'
    # src_path = r'D:\project_code\pythonproject\CodeAuditing\test_c\src'
    # inc_path = r'D:\project_code\pythonproject\CodeAuditing\test_c\inc'
    compile_project(main_path)
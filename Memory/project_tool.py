import os
from Memory import run_cmd,get_FilePath_folder
from Memory.compile import compile_project
"""
    @description: 输入main.py的路径自动检测整个项目的问题
    文件结构目录必须为：
    |-- src/
    |    |-- file1.c
    |    |-- file2.c
    |    |-- ...
    |-- inc/
    |    |-- header1.h
    |    |-- header2.h
    |    |-- ...
    |-- main.c
    @Time：2023/7/19 || 11:28 ||20324
    """
def cppcheck(file_path):
    """
    @description: cppcheck
    @Time：2023/7/19 || 11:47 ||20324
    """
    folder_path=os.path.dirname(file_path)
    src_path=os.path.join(folder_path,'src')
    inc_path=os.path.join(folder_path,'inc')
    cmd=f'cppcheck --enable=all --std=c11 --suppress=missingIncludeSystem --verbose  ' \
        f'{file_path} {src_path}/*.c -I {inc_path}/'
    #cmd='cppcheck --enable=all --std=c11 --suppress=missingIncludeSystem main.c src/*.c -I inc/'
    output=run_cmd(cmd.split(' '))
    return output

def drmemory(file_path):
    """
    @description: 对于输入的c文件，转化为exe文件进行寻找（需要提前进行编译）
    @Time：2023/7/19 || 10:44 ||20324
    """

    cmd = ['drmemory.exe', file_path.replace('.c', '.exe')]
    output=run_cmd(cmd)
    return output

def clangcheck(file_path):
    """
    @description: clang_check
    @Time：2023/7/19 || 11:47 ||20324
    """
    #clang-check.exe -analyze -extra-arg=-std=c11  -extra-arg=-Iinc -p project_folder
    folder_path = os.path.dirname(file_path)
    src_path = os.path.join(folder_path, 'src')
    inc_path = os.path.join(folder_path, 'inc')
    src_list=get_FilePath_folder(src_path)  #src所有c文件的list
    inc_list=get_FilePath_folder(inc_path)
    cmd='clang-check.exe -analyze -extra-arg=-std=c11 -extra-arg=-I{inc_path} {main_path} {cfiles} {headers}'\
        .format(main_path=file_path,cfiles=' '.join(src_list),headers=' '.join(inc_list),inc_path=inc_path)
    output = run_cmd(cmd)
    return output

# def run_code_quality_evaluation(file_path):
#
#     cmd1 = ['clang', '-fprofile-instr-generate='+file_path.replace('.c', '.profraw'), '-fcoverage-mapping', file_path, '-o',file_path.replace('.c', '.exe')]
#     code_evaluation_output=run_cmd(cmd1)
#     print(cmd1)
#     cmd2 = ['llvm-profdata', 'merge', '-o', file_path.replace('.c', '.profdata'), file_path.replace('.c', '.profraw')]
#     code_evaluation_output+=run_cmd(cmd2)
#     cmd3 = ['llvm-cov', 'report', file_path.replace('.c', '.exe'),
#             '-instr-profile='+file_path.replace('.c', '.profdata')]
#     code_evaluation_output += run_cmd(cmd3)

if __name__=='__main__':
    main_path = r'D:\project_code\pythonproject\CodeAuditing\test_c\main.c'
    src_path = r'D:\project_code\pythonproject\CodeAuditing\test_c\src'
    inc_path = r'D:\project_code\pythonproject\CodeAuditing\test_c\inc'
    compile_project(main_path)  #编译整个项目

    output=''
    output=cppcheck(main_path)

    print(output)

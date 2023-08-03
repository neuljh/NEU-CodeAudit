"""
@FileName：fileTree.py
@Description: 文件树实现，
获取指定文件下所有的变量，宏，函数
@Time：2023/7/6 9:15
@user: 20324
"""
import os
import sys


def main():
    folder_path = 'D:\\project_code\\c\\kaoyan'  # 替换为实际文件夹路径
    root=TreeNode(folder_path)
    root.build_tree_recursive()
    # file=root.find_file('my_computer')
    root.filter_files(filter_rule)
    root.print_file_tree()

def filter_rule(filename):
    """
    @description: 过滤规则,选择出指定的文件
    @Time：2023/7/6 || 10:15 ||20324
    """
    text_extensions = ['.c', '.h']  # 可根据需求定义文本文件的扩展名
    ext = os.path.splitext(filename)[1] #获取扩展名
    return ext.lower() in text_extensions

class TreeNode:
    def __init__(self, folder_path):
        if not os.path.isdir(folder_path):
            sys.exit("the path is not a folder")
        self.name = os.path.basename(folder_path)  #当前节点文件夹名字
        self.children = []
        self.folder_path=folder_path
    def find_file(self, target_file):
        """
        @description: 查找指定的文件以及文件夹
        @Time：2023/7/6 || 10:08 ||20324
        """
        if self.name == target_file:  #查询文件夹
            return self.folder_path
        for child in self.children:
            if isinstance(child,TreeNode):
                result = child.find_file(target_file)
                if result: #如果result不为none返回
                    return result
            elif child==target_file:
                    return os.path.join(self.folder_path, child)
        return None
    def build_tree_recursive(self):
        """
        @description:对于指定path，将其文件路径写入到node中
        node节点为树的一部分
        @Time：2023/7/6 || 9:36 ||20324
        """
        folder_path=self.folder_path
        for name in os.listdir(folder_path):
            path = os.path.join(folder_path, name)
            if os.path.isdir(path):
                child_node = TreeNode(path)
                child_node.build_tree_recursive()
                self.children.append(child_node)
            else:
                self.children.append(name)

    def print_file_tree(self, indent=''):
        #打印整个树，遍历操作
        print(indent + self.name)
        for child in self.children:
            if isinstance(child, TreeNode):
                child.print_file_tree(indent + '  ')
            else:
                print(indent + '  --' + child)

    def filter_files(self, filter_func):
        """
        @description: 设置filter_func函数作为过滤规则
        @Time：2023/7/6 || 13:52 ||20324
        """
        filtered_children = []
        for child in self.children:
            if isinstance(child, TreeNode):
                child.filter_files(filter_func)
                if child.children:
                    filtered_children.append(child)
            else:
                if filter_func(child):
                    filtered_children.append(child)
        self.children = filtered_children

if __name__=='__main__':
    main()

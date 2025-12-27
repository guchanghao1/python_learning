# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import os
import shutil

'''
def del_dir(path):
    # 获取当前目录下的子目录或者文件
    lst_file_dir = os.listdir(path)
    for file_dir in lst_file_dir:
        down_path = os.path.join(path, file_dir)
        if os.path.isdir(down_path):
            del_dir(down_path)
        else:
            os.remove(down_path)
    lst_file_dir = os.path.isdir(path)
    if len(lst_file_dir) == 0:
        os.remove(path)


if __name__ == '__main__':
    del_path = ''
    if os.path.isfile(del_path):
        os.remove(del_path)
    else:
        del_dir(del_path)
'''


def delete_path(path):
    if not os.path.exists(path):
        print(f"路径 '{path}' 不存在")
        return

    if os.path.isfile(path):
        os.remove(path)
        print(f"文件 '{path}' 已删除")
    else:
        shutil.rmtree(path)
        print(f"目录 '{path}' 及其所有内容已删除")


if __name__ == '__main__':
    del_path = ''  # 请设置要删除的路径
    if not del_path:
        print("错误：请指定要删除的路径")
    else:
        delete_path(del_path)

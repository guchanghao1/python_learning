# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------

import time, os


# 时间戳转换为时间格式
def timestamp_to_str(timestamp):
    localtime = time.localtime(timestamp)
    ftime = time.strftime('%Y-%M-%D %H:%M:%S', localtime)
    return ftime


# 文件大小转换为MB形式
def bytetoM(size):
    vsize = size / float(1024 * 1024)
    return vsize


if __name__ == '__main__':
    file_info = os.stat("文本分词计数.txt")
    print(f'文本创建时间：{timestamp_to_str(file_info.st_ctime)}')
    print(f"文本大小：{bytetoM(file_info.st_size)} MB")
    print(f'文本访问时间：{timestamp_to_str(file_info.st_atime)}')
    print(f'文本修改时间：{timestamp_to_str(file_info.st_mtime)}')

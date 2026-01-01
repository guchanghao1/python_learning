# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import os

name_tuple = os.walk('D:\Python\练习', topdown=True)
for a, b, c in name_tuple:
    print(f'当前目录{a}')
    if len(b) > 0:
        print(f'当前目录的子目录{b}')
    if len(c) > 0:
        print(f'当前路径下的文件{c}')

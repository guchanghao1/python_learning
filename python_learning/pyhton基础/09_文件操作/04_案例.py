# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 创建一个名为 hello.txt 的文件，并向其中写入一行文字："Hello, World!"
"""
with open("hello.txt", 'w', encoding='utf-8') as f:
    f.write('Hello,Python')
"""

# 读取 hello.txt 文件中的全部内容，并打印到控制台
"""
# with open("hello.txt",'r',encoding="utf-8") as f:
#     a = f.read()
#     print(a)
"""

# 编写一个程序，尝试打开用户输入的文件名。如果文件不存在，捕获异常并给出友好的提示信息，而不是让程序报错。
"""
name = input("请输入你要打开的文件：")

try:
    with open(f"{name}",'r', encoding='utf-8') as f:
        a = f.read()
        print(a)
except:
    print("找不到文件")

"""

# 读取 <案例3.txt>中的数据: 统计字符个数, 构成字典数据
"""
with open("案例\案例3.txt", 'r', encoding='utf-8') as f:
    data = f.read()
dic = {}
for i in data:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

    print(dic)
"""

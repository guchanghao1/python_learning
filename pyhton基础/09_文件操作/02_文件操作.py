# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 什么是文件：
"""

    图片 -- .jpg .png
    视频 -- .MP4
    文本文件 -- .txt
    word -- .doc .doxc
    
    二进制 -- b （没办法用文字和字母来展示的内容）
    0 1  我们将图片内容给 电脑的时候  二进制去识别    
"""

# 文件操作
"""
open(文件名，打开模式，编码格式)
打开模式:
    w = 写入(覆盖原有内容) 
    r = 只读（默认)
    a = 追加（在文件的末尾加上数据）
    b = 二级制 模式
    + = 读写模式
    
操作文件：read() 和 write()
保存退出：close()

解决乱码问题：encoding="utf-8"

"""

# 创建文件
"""
f = open('第一个文件.txt', 'a+', encoding='utf-8')
f.write('append')
f.close()

with open("第二个文件.txt", 'a+', encoding="utf-8") as f:
    f.write('你好')
"""

# 读取文件
"""
# with open("第一个文件.txt", 'r', encoding='utf-8') as f:
#     # 获取全部内容以字符串的形式
#     a = f.read()
#     print(a)
# 
#     # 获取一行内容
#     # b = f.readline()
#     # print(b)
# 
#     # 读取一行一行的内容，用列表包裹
#     # c = f.readlines()
#     # print(c)
"""

# 写入文件
"""
# with open("第二个文件.txt", 'a+', encoding='utf-8') as a:
#     a.write('再见')
"""

# 二级制数据写入
"""
import requests

url = 'https://qcloud.dpfile.com/pc/5IiIEKaeUe9YAbrPUnuVkq34HXnve7gTE5rViBJ3AAGm-T1akhe32FXgB6K0ujZb.jpg'
res = requests.get(url)

con = res.content   # 获取到的数据是二进制

with open('海绵宝宝.jpg', 'wb') as f:
    f.write(con)

print("下载完成")
"""

# 创建文件夹
"""
import os
name = '第三个文件夹'
if not os.path.exists(name):
    os.mkdir(name)
"""

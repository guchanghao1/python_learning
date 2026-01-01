# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 语句结构
'''
try:
    语句
except:
    错误信息
    
    
尝试：
    可能会有错误的代码
那么就：
    报错信息
'''

"""
a = 1
b = '2'

try:
    print(a + b)
except:
    print("有问题")
"""

"""
import random
num = random.randint(1, 100)
max_num = 100
min_num = 1
cs = 1

try:
    while True:
        u = int(input(f"请输入{min_num}~{max_num}的数字："))
        if u < min_num or u > max_num:
            print(f"请输入{min_num}~{max_num}之间的数字!!!")
            continue

        if u == num:
            print("找到了")
            break

        elif u > num:
            max_num = u
            continue

        else:
            min_num = u
            continue

except:
    print("不能为空")
"""

"""
print('11111')
print('22222')

try:
    print('33333')
except:
    print("44444")

print('55555')

"""

"""
import requests

url = 'https://qcloud.dpfile.com/pc/5IiIEKaeUe9YAbrPUnuVkq34HXnve7gTE5rViBJ3AAGm-T1akhe32FXgB6K0ujZb.jpg'
res = requests.get(url)
con = res.content  # 获取到的数据是二进制

img_name_list = ['@#@$*&@^', '#@*#@#', 'haimian', "@##@*#$", '海绵宝宝']
for i in img_name_list:
    try:
        with open(f'{i}.jpg', 'wb') as f:
            f.write(con)
    except:
        print('no')
"""

"""
a = 1
b = '2'
# print(a + b)

try:
    print(a + b)
except TypeError as f:
    print("有问题",f)
"""

"""
num = int(input("请输入一个数字："))
try:
    a = 10 / num
    print(a)
except ZeroDivisionError as f:
    print("不能为0", f)
"""

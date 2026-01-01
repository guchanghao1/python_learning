# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 变量（结果） = 值1 if 条件 else 值2   没有elif
# 变量（结果）= [i for i in range]

# 单列表循环
"""
for i in range(1, 6):
    print(i)

a = [i for i in range(1, 6)]
print(a)
"""

# 多列表循环
"""
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
lis = []
for i, j in zip(a, b):
    x = i + j
    lis.append(x)
print(lis)

a = [i + j for i, j in zip(a, b)]
print(a)
"""

# 将信息用三元运算切割开
"""
data_list = [
    '1995年 164CM 本科',
    '1992年 160CM 本科',
    '1992年 170CM 本科',
    '1991年 168cm 硕士在读',
    '1992年 162cm 本科',
    '1992年 165CM 本科',
    '1992年 165CM 本科',
    '1995年 166cm 本科',
]
y = [i.split(' ')[0] for i in data_list]
x = [i.split(' ')[1] for i in data_list]
z = [i.split(' ')[2] for i in data_list]
for a, b, c in zip(y, x, z):
    print(a, b, c, sep="  |  ")
"""

# 求 最大值，最小值，平均值, 把结果写到字典中。
"""
data_list = [
    ['1', '北京大学', '100', '世界一流大学'],
    ['2', '清华大学', '98.78', '世界一流大学'],
    ['3', '复旦大学', '82.14', '世界一流大学'],
    ['4', '浙江大学', '81.98', '世界一流大学'],
    ['5', '南京大学', '81.43', '世界一流大学'],
    ['6', '上海交通大学', '81.34', '世界一流大学'],
    ['7', '华中科技大学', '80.49', '世界知名高水平大学'],
    ['8', '中国科学技术大学', '80.44', '世界一流大学'],
    ['9', '中国人民大学', '80.41', '世界一流大学'],
    ['10', '天津大学', '80.38', '世界知名高水平大学'],
]

data = [float(i[2]) for i in data_list]
# print(data)

dic = {}
max_n = max(data)
min_n = min(data)
avg_n = sum(data) / len(data)

dic["最大值"] = max_n
dic["最小值"] = min_n
dic['平均值'] = avg_n

print(dic)
"""

# 三元运算 猜数字
"""
import random

num = random.randint(1, 10)
print(num)
a = int(input("猜一个数字:"))



# c = '答对了' if num == a else '答错了'

# d = '答对了' if num == a else '猜小了' if num > a else '猜大了'
# print(d)
"""

# 判断一个数是奇数还是偶数
"""
num = 4
a = '偶数' if num % 2 == 0 else '奇数'
print(a)
"""

# 创建一个新列表，将原列表中的偶数替换为字符串 "even"，奇数替换为 "odd"
"""
a = [1, 2, 3, 4, 5, 6]
data = ['even' if i % 2 == 0 else 'odd' for i in a]
print(data)


lis = []
for i in a:
    if i % 2 == 0:
        i = 'even'
        lis.append(i)

    else:
        i = 'odd'
        lis.append(i)
print(lis)
"""


# 2、将抓到的网址信息进行补全--三元运算
'''
完整链接：https://www.xbiquge.la/34/34844/20504594.html
[
    '/34/34844/16216570.html',
    '/34/34844/16216573.html',
    '/34/34844/16216574.html',
    '/34/34844/20416605.html'
]
'''
"""
href = 'https://www.xbiquge.la/34/34844/20504594.html'
data = [
    '/34/34844/16216570.html',
    '/34/34844/16216573.html',
    '/34/34844/16216574.html',
    '/34/34844/20416605.html'
]
href_s = href.split('34/3')[0]
a = [href_s + i for i in data]
"""

# 3、分开获取数字和后缀---三元运算
'''
[
    'http://img.adoutu.com/picture/1609683038916.jpg',
    'http://img.adoutu.com/picture/1609683038634.jpg',
    'http://img.adoutu.com/picture/1609683038491.gif',
    'http://img.adoutu.com/picture/1609683038191.png',
    'http://img.adoutu.com/picture/1609683037894.jpg',
    'http://img.adoutu.com/picture/1609683037764.gif',
]
'''
"""
data = [
    'http://img.adoutu.com/picture/1609683038916.jpg',
    'http://img.adoutu.com/picture/1609683038634.jpg',
    'http://img.adoutu.com/picture/1609683038491.gif',
    'http://img.adoutu.com/picture/1609683038191.png',
    'http://img.adoutu.com/picture/1609683037894.jpg',
    'http://img.adoutu.com/picture/1609683037764.gif',
]

a = [i.split('re/')[1] for i in data]
b = [i.split('.')[0] for i in a]
c = [i.split('.')[1] for i in a]
print(b)
"""

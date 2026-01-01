# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 数据类型:
"""
字符串 ---- str 
列表  ---- list
元组  ----tuple
字典 ---- dict
整数  ---- int     1 2 
浮点数 --- float   小数
json ---- json
"""

# 字符串【str】
"""
1 - 什么是字符串：引号包裹的信息，是不可变的，用于表示文本数据
2 - 引号：单引号、双引号、三单引号、三双引号
3 - 单引号和三引号的区别：三引号可以换行，由于三引号可以换行，所以可以用来记笔记
"""
# 1 - 单引号 or 双引号 or 三单引号 or 三双引号
a = '字符串,列表'
b = "字符串"
c = '''字符串,列表'''
d = """字符串列表"""
print(a == b == c == d)

# 2 - 字符串的替换【replace】           用法: replace(原数据, 目标数据)   没有的数据就不替换
"""
data = '今天星期一'
data2 = data.replace('一', '二')
print(data2)

data3 = data.replace("二", "三")
print(data3)
"""

# 空格也是字符串的一部分
"""
data1 = "今天 星期六，明天 放假 "
data2 = data1.replace(" ", "*")
print(data2)
"""

# 3 - 统计字符串长度【len】              长度: 元素的个数   用法: len(数据)
"""
data = '今天星期一'
data1 = "今天 星期六，明天 放假 "
# print(len(data))
print(len(data1))
"""

# 4 - 查看数据类型【type】               用法: type(数据)
"""
data1 = "123.12"
print(type(data1))
"""

# 5 - 人机交互【input】                 用法: input(提示性话语)
"""
name = input("请输入名字：")
ages = input("请输入年龄：")
addr = input("请输入地址：")
print(name, ages, addr)
"""

# 6 - 字符串的拼接【字符串格式化输出】
"""
# a - "+" 拼接
print("我的名字是" + name + '，' + "年龄是" + ages, "家住" + addr)
# b - format后置: {}
print("我的名字是{},年龄是{},家住{}".format(name, ages, addr))
# c - format前置: {}
print(f"我的名字是{name},年龄是{ages},家住{addr}")
"""

# 7 - 字符串的空格删除
"""
data1 = "  今天 星期六，明天 放假 "
# a - 区分空字符串和空格
a = ' '
b =''

# b - 全部去除：replace(空格, 空)
data2 = data1.replace(" ",'')
print(data2)

# c - 首尾去除：strip()
data3 = data1.strip()
print(data3)
"""

# 8 - 去除引号【eval】
"""
age = eval(input("请输入年龄："))
# str---int
print(type(age))
"""

# 9 - 字符串的切割【split()】            str -- <切割> -- list
"""
# 索引 （下标）   左边从0开始，右边从-1开始
# a - 规则切法 列表--下标取值
data = ["周杰伦", "林俊杰", "薛之谦", "张杰"]
print(data[0])

data2 = "周杰伦，林俊杰，薛之谦，张杰"
r = data2.split('林')

# b - 不规则切法
data2 = "周杰伦，林俊杰，薛之谦，张杰"
a = data2.split('，林俊')[复习.txt].split('，薛之')[0]
print(a)

data = "https://chat.deepseek.com/a/chat/s/dd19eceb-17dc-41ec3-9205-6b3239a2d9bd"
r = data.split('chat/s/')[复习.txt].split('ec')[0]
print(r)
"""

# 10 - 字符串的拼接【join】              list -- <拼接> -- str
"""
data = ['今天', '星期', '六', ',', '明天', '放假']
# 今天星期六，明天放假
a = ''.join(data)
print(a)
"""

# 11 - 字符串转大写【upper】【lower】
"""
a = "PYTHON,python"
print(a.upper())
print(a.lower())
"""

# 12 - 制表符
"""
print("第一行\t第二行")
print('第一行\n第二行')
"""

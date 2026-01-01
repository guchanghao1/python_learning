# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''
import time

# 语句结构
"""
for i in "循环的内容":
    print(i)
    time.sleep(1)
"""

# range(起始值，结束值)  包头不包尾
"""
for i in range(101):
    print(i)
"""

# 循环字符串
"""
a = "童年的纸飞机，现在终于飞回我手里"
for i in a:
    print(i)
"""

# 循环列表
"""
a = [1, 23, 4, 5]
b = ['python', 'java', 'c++', 'c']
for i in b:
    print(i)
"""

# 循环字典
"""
dic = {
    'name': '张三',
    'ages': 18,
    'addr': '上海',
}

for i in dic.values():
    print(i)

"""

# 使用for循环计算1到100所有整数的和
"""
# 1+2+3+4+5+...+100
num = 0
for i in range(1, 101):
    num += i

print(num)
"""

# 给定单词"programming"，统计其中字母'm'出现的 次数==num
"""
a = "programmingmmmmmmm"
num = 0

for i in a:
    if i == "m":
        num += 1
    print(num)
"""

# 不使用max()函数，找出列表 [34, 12, 89, 5, 67] 中的最大值
"""
data = [34, 12, 89, 5, 67]
# print(max(data))

b = 0
for i in data:
    if b < i:
        b = i
print(b)
"""

# 打印一个5行符号金字塔
"""
a = input("请输入一个符号：")
b = int(input("请输入行数："))

num = 0
for i in range(1, b + 1):
    print(' ' * (b - i), end='')
    print(f'{a}' * (2 * i - 1))

"""

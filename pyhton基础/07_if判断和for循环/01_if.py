# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 语句结构
"""
口诀：if开头 else结尾 中间用elif
判断语句
    判断语句的结构:
        if 条件1:
            执行语句1

        elif 条件2:
            执行语句2:
            ...
        elif 条件n-1:
            执行语句n-1

        else:
            执行语句n

"""

# if判断
"""
import random

num = random.randint(1, 10)
print(num)
a = int(input("请输入数字:"))

if a == num:
    print("猜对了")

elif a > num:
    print("猜大了")

else:
    print("猜小了")
"""

# 年龄
"""
age = int(input("请输入年龄："))

if 0 < age <= 6:
    print("幼儿")

elif 7 <= age <= 17:
    print("少年")

elif 18 <= age <= 35:
    print("青年")

elif 36 <= age <= 59:
    print("中年")

else:
    print("老年")
"""

# 猜三次 猜数字进阶
"""
import random

num = random.randint(1, 10)
print(num)
a = int(input("请输入数字:"))

if a == num:
    print("猜对了")
else:
    if a > num:
        print("猜大了")
    else:
        print("猜小了")


    a = int(input("请输入数字:"))
    if a == num:
        print("猜对了")
    else:
        if a > num:
            print("猜大了")
        else:
            print("猜小了")


        a = int(input("请输入数字:"))
        if a == num:
            print("猜对了")
        else:
            if a > num:
                print("猜大了")
            else:
                print("猜小了")
"""
"""
import random

num = random.randint(1, 10)
print(num)
a = int(input("请输入数字:"))

if a == num:
    print("猜对了")
    exit()
else:
    if a > num:
        print("猜大了")
    else:
        print("猜小了")


a = int(input("请输入数字:"))
if a == num:
    print("猜对了")
    exit()
else:
    if a > num:
        print("猜大了")
    else:
        print("猜小了")


a = int(input("请输入数字:"))
if a == num:
    print("猜对了")
    exit()
else:
    if a > num:
        print("猜大了")
    else:
        print("猜小了")
"""

# 计算器
"""
a1 = int(input("请输入第一个数字："))
a2 = eval(input("请输入第二个数字："))
b = input("请输入运算符【+、-、*、/】：")

if b == '+':
    print(a1 + a2)

elif b == '-':
    print(a1 - a2)

elif b == '*':
    print(a1 * a2)

elif b == '/':
    print(a1 / a2)

else:
    print("请输入正确的字符")

"""

# 输入整数【要求是：100 ~ 1000】，判断其能否被 3 和 7 整除 【余数为0】
"""
num = int(input("请输入数字："))

if 100 <= num <= 1000:
    if num % 3 == 0 and num % 7 == 0:
        print("可以被3和7整除")


    else:
        print("不行")

else:
    print("100到1000以内的数字")
"""

# 判断奇偶数
"""
num = int(input("请输入一个数字"))
if num % 2 == 0:
    print("偶数")

else:
    print("奇数")

"""



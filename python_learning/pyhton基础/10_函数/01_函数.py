# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 函数是什么？  里面的 之前学一个集合  function  功能  函数就是带有特定功能的代码块
"""
print()
len()
sum()
replace()

xxx()
print(type(print))
"""

# 普通代码 -- 封装 --  普通函数 -- 封装 -- 面向对象（终点、重点）
# 平安夜的苹果：七块钱买一斤 -- 平安夜标签 -- 七块钱一个 -- 加一个礼盒 + 平安夜的标签 -- 12一个

# 函数定义 调用
"""
def xxx():  # 见名知意
    pass

xxx() # 调用
"""

# 函数的模板
"""
def 函数名():
    pass


if __name__ == '__main__':  # 运行入口
    函数名()
"""

# 普通代码和函数
"""
# a = 1
# b = 2
# print(a + b)

def jiafa():
    a = 1
    b = 2
    print(a + b)


# jiafa()


def hi():
    print("你好！张三")


# hi()
"""

# 代码执行的顺序
"""
print(1111)


def aaa():
    print(2222)


print(3333)

aaa()
"""

# 案例一：形状
"""
def get_圆形():
    print("圆形")


def get_正方形():
    print("正方形")


def get_长方形():
    print("长方形")


def main():  # 主函数
    op = input("1-- 圆形，2-- 正方形 3-- 长方形：")
    if op == "1":
        get_圆形()

    elif op == "2":
        get_正方形()

    elif op == '3':
        get_长方形()

    else:
        print("请正确输入！！")


main()
"""

# 案例二：计算面积 周长
"""
def get_area():
    w = 50
    h = 40
    print(f"面积是：{w * h}")


get_area()


def get_周长():
    w = 40
    h = 30
    print(f"周长是：{(w + h) * 2}")


get_周长()
"""

# 传参   参数
"""
def hi(a, n):
    print("你好!{}".format(a))
    print("年龄！{}".format(n))


name = input("请输入你的名字：")
ages = input("请输入一下年龄：")
hi(name, ages)
"""

# 计算出边长分别是5,15,25的正方形面积
"""
a = 5
area = a * a
print("正方形边长为{}的面积为{}".format(a, area))

a = 15
area = a * a
print("正方形边长为{}的面积为{}".format(a, area))

a = 25
area = a * a
print("正方形边长为{}的面积为{}".format(a, area))


def xxx(a):
    area = a * a
    print("正方形边长为{}的面积为{}".format(a, area))


xxx(5)
xxx(15)
xxx(25)
"""

# 计算器
"""
def 加法(a, b):
    c = a + b
    print(c)


def 减法(a, b):
    c = a - b
    print(c)


def 乘法(a, b):
    c = a * b
    print(c)


def 除法(a, b):
    c = a / b
    print(c)


def main(a, b):
    op = input("请输入你需要用的运算符（+ - * /）：")

    if op == '+':
        加法(a, b)

    elif op == '-':
        减法(a, b)

    elif op == '*':
        乘法(a, b)

    elif op == '/':
        除法(a, b)

    else:
        print('输入有误')


a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
main(a, b)
"""

# 运行入口
"""
def hi():
    print("你好！张三")


if __name__ == '__main__':  # 运行入口
    hi()
    print('aaaaa,bbbb')  # 在这个文件的函数里面用到的其他内容
"""

# 函数的模板
"""
def main():  # 定义函数
    pass  # 功能代码


if __name__ == '__main__':  # 运行入口
    main()  # 调用函数

"""



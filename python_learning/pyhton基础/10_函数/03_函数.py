# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 定义函数
"""
def 函数()    # 声明
    print()   # 实现
    return


if __name__ == '__main__'
    # 调用
    函数()
    
    print(函数())
    res = 函数()
    print(res)
"""

# 返回值
"""
def main():
    print(111)
    return 


if __name__ == '__main__':
    res = main()
    print(res)
"""

# 参数
'''
定义时传入的参数为形参
调用时传入的参数为实参

'''
"""
def main(x, y):  # 形参
    c = x + y
    return c


if __name__ == '__main__':
    a = 4
    b = 6
    res = main(a, b)
    # res = main(3, 5)    # 实参
    print(res)
"""

# 参数类型：
# 1 - 必须参数：调用的顺序和定义的顺序不能错，还有数量保持一样
"""
def main(name, age, addr):
    return f"我叫{name}，今年{age}"


if __name__ == '__main__':
    res = main('张三', 18)
    print(res)
"""

# 2 - 关键字参数:直接定义
"""
def main(name, age=18):
    return f"我叫{name}，今年{age}"


if __name__ == '__main__':
    res = main("张三",19)
    print(res)
"""

# 3 - 默认参数:
"""
def main(n1, n2=6):
    print(n1)
    print(n2)
    # print(n1 + n2)


main(3, 2)
"""

# 4 - 不定长参数：*args  **kwargs
# *args： 用来接收多个参数,用元组来存放数据,参数中有不定长参数必须放到最后
"""
def main(n, *args):
    print(n)
    print(args)


main("hello", 1, 2, 3, 4, 5)
"""

# **kwargs:用来接收多个参数,用字典存放数据,参数中有不定长参数必须放到最后
"""
def main(**kwargs):
    print(kwargs)


main(x=11, y=12, z=13)
"""

# 动态参数：main(*args, **kwargs)
"""
def main(*args, **kwargs):
    print(args)
    print(kwargs)


main(1, 2, 3, 4, 5, n=3)
"""

# 作用域：
# 局部变量: 在函数中定义的，在函数内使用
# 全局变量(global)：在函数外面定义的，在函数内外使用,使用global在函数内修改
"""
i = 3  # 全局变量

def main():
    global i
    i = 5   # 局部变量
    y = 4  # 局部变量
    c = y + i
    print(i)


main()
print(i)
"""

# 匿名函数 简单的函数操作，
# 结果（变量） = lambda 参数1,参数: 函数体（功能代码）
"""
def main(a, b=1):
    c = a+b
    return c


print(main(10, 20))
print(main(10))

x = lambda a, b=1: a + b
print(x(10, 20))
print(x(10))
"""

# 装饰器： 是一种特殊函数，用于修改其他函数行为，它可以用来扩展或增强原有的功能，而无需修改原始函数的代码
# 原函数 = 装饰器函数(原函数)
# 语法结构
"""
def 装饰器函数(原函数)：
    def 自己定义(*args, **kwargs):
        原函数(*args, **kwargs)
    return 自己定义

@装饰器函数
def 原函数(形参):
    pass

if __name__ == '__main__'
    原函数(实参)
    
    
原函数 = 装饰器函数(原函数)

"""

# 装饰器模板
"""
def 装饰器函数(func):
    def 函数(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return 函数


@装饰器函数
def send_wx(a):
    print("微信", a)
    return 100


@装饰器函数
def send_yx(a, b):
    print("邮件", a, b)


@装饰器函数
def send_xx(a, b, c):
    print("信息", a, b, c)


if __name__ == '__main__':
    a = send_wx('你好')
    print(a)
    send_yx('你好', '张三')
    send_xx('你好', '张三', '上海')
"""

# 案例：每一个函数运行结果之前发一个"准备发送"，之后发一个"发送成功"
"""
def send_wx():
    print("准备发送")
    print("微信")
    print("发送成功")


def send_yx():
    print("准备发送")
    print("邮件")
    print("发送成功")


def send_xx():
    print("准备发送")
    print("信息")
    print("发送成功")


if __name__ == '__main__':
    send_wx()
    send_yx()
    send_xx()
"""

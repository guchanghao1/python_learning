# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# while语句结构
"""
while 条件:
    执行语句

当我们的判断条件为Trun 开启循环
当我们的判断条件为False 退出循环
"""
"""
a = 0
while a < 10:
    print("ok")
    a += 1
    # a = a + 1
"""

# 案例：手机电量
"""
import time

电量 = 100
while 电量 > 20:
    print(f"当前电量{电量}")
    电量 -= 10
    time.sleep(0.5)
print("请充电")
"""

# while True语句结构
"""
while True:
    执行语句

判断条件永远为Trun
需要自己手动添加break 退出

"""

# while 和 while True
"""
n = 6
while n < 5:
    print('ok')

while True:
    print('ok')
"""

# 打印十次今天天气不错（用while）
"""
num = 1
while num < 11:
    # num += 1
    print(f"今天天气不错--{num}")
    num += 1


num = 1
while True:
    if num < 11:
        print(f"今天天气不错--{num}")
        num += 1
    else:
        break


for i in range(1, 11):
    print(f"今天天气不错--{i}")


"""

# 猜数字
"""
import random

cs = 0
num = random.randint(1, 100)
print("猜数字的游戏")
print(num)

while cs < 3:
    cs += 1
    a = int(input("请输入数字："))
    if a == num:
        print("猜对了")
        break
    elif a > num:
        print("猜大了")
    else:
        print("猜小了")
"""

# 数字炸弹
"""
import random

num = random.randint(1, 100)
min_num = 1
max_num = 100

while True:

    user_num = int(input(f"请输入{min_num}~{max_num}的数字："))

    if user_num < min_num or user_num > max_num:
        print(f"请输入{min_num}~{max_num}之间的数字!!!!!")
        continue

    if user_num == num:
        print('猜对了！！炸弹就是{}'.format(num))
        break

    elif user_num > num:
        max_num = user_num
        continue

    else:
        min_num = user_num
        continue

"""

# 让用户输入一系列数字，输入0时结束，输出这些数字的和--while循环
"""
total = 0
while True:
    num = float(input("请输入一个数字（输入0结束）："))
    if num == 0:
        break  # 输入0时退出循环
    total += num  # 将数字加到总和中

print(f"这些数字的总和是：{total}")
"""

# 反复判断奇偶, 输入0为止---While
"""
while True:
    data = eval(input('请输入一个数: '))
    if data != 0:
        if data % 2 == 0:
            print('偶数')
        else:
            print('奇数')
    else:
        break
"""

# 实现用户输入帐号和密码，当帐号为“Admin”且密码为“zhgjx”时，显示“登录成功”，否则显示“登录失败”，失败时允许重复输入三次。--while循环
"""
count = 0
while True:
    user = input("请输入你的账号：")
    pwd = input("请输入你的密码：")
    if user != "Admin" or pwd != "zhgjx":
        count += 1
        print(f"密码或账号错误，请重新输入")
    elif user == "Admin" and pwd == "zhgjx":
        print("密码正确，登录成功！")
        break

    if count == 3:
        print("账号或者密码错误，请等待20秒后重启登录")
        break
"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 数字比较：输入三个数字，输出其中最大的数字--for循环
"""
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
c = int(input("请输入第三个数字："))
"""

# if 判断
"""
if a >= b and a >= c:
    print(a)
elif b >= c and b >= a:
    print(b)
else:
    print(c)
"""

# for 循环
"""
data = []
d = 0
data.append(a)
data.append(b)
data.append(c)

for i in data:
    if d <= i:
        d = i
print(d)
"""

# 金字塔图形---for循环
"""
num = int(input("请输入需要的行数："))
for i in range(1, num + 1):
    print(" " * (num - i) + '*' * (2 * i - 1))
    
# " " * (5 - i)  符号前面的空格（包括符号）
# '*' * (2 * i - 1)
"""

# 输出九九乘法表---for循环
# end  print()
"""
for i in range(1, 10):  # 第一个数字
    for k in range(1, i + 1):  # 1 2 3 4  5 6 7 8 9
        print(f"{k}*{i}={k * i}", end=" ")  # end='' k循环完不换行
    print() # 每次i循环完换行
"""

# 输出水仙花数---for循环
"""
# 153= 1     5    3
for i in range(100, 1001):
    a = i // 100  # 拿到百位数
    b = (i // 10) % 10  # 拿到是十位数
    c = i % 10  # 拿到个位数

    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
"""

# if判断操作
'''
编写一个Python程序，从用户读取一个整数值，
当数字能被4整除时，打印单词“Table”；
当数字能被5整除时打印单词“Palm”。
如果数字既能被4整除又能被5整除，则应打印单词“TablePalm”。
'''
"""
data = int(input("请输入一个整数值："))
if data % 4 == 0 or data % 5 == 0:
    if data % 4 == 0 and data % 5 == 0:
        print("TablePalm")
    elif data % 4 == 0:
        print("Table")
    else:
        print('Palm')
else:
    print("不满足条件")
"""

# 凯撒密码问题--if判断
"""
data = input("请输入你的密码原文：")
data_en = ''

for i in data:
    if "a" <= i <= "z":
        data_en += chr(ord('a') + ((ord(i) - ord('a')) + 4) % 26)
    elif "A" <= i <= "Z":
        data_en += chr(ord('A') + ((ord(i) - ord('Z')) + 4) % 26)
    else:
        data_en += i

print(data_en)
# chr()---  将ASCLl码转回成字符
# ord()---- 转成ASCLL码


# print(ord('f'))
# print(chr(ord('a')))
"""

# 实现用户输入帐号和密码，当帐号为“Admin”且密码为“zhgjx”时，显示“登录成功”，否则显示“登录失败”，失败时允许重复输入三次。--while循环
"""
count = 1
while True:
    user = input("请输入你的账户：")
    pawd = input("请输入你的密码：")

    if user == "Admin" and pawd == "zhgjx":
        print("登录成功！！！")
        break

    else:
        count += 1
        if count <= 3:
            print("密码错误，请重新输入密码！")
        else:
            print("密码或者账号有误，请重新进入")
            break
"""

# 斐波那契数列：使用while循环输出斐波那契数列的前20项（1,1,2,3,5,8...）--while循环
"""
a = 1
b = 1
count = 2
print(a, end=' ')
print(b, end=' ')

while count < 20:
    c = a + b  # 1次 等于2
    if count < 19:
        print(c, end=' ')
    else:
        print(c, end=' ')
    a, b = b, c
    count += 1
"""

# 反复判断奇偶, 输入0为止---While
"""
while True:
    num = int(input("请输入一个数字（输入0退出）"))
    if num == 0:
        break
    else:
        if num % 2 == 0:
            print("这是一个偶数：")
        else:
            print("这是一个奇数：")
"""

# 反向猜数字 --while循环
"""
left = 0
right = 1000
count = 0

data = input("请输入一个答案：")
while True:
    guess = (left + right) // 2
    res = input(f"这个数是{guess}吗：")

    if res == "太大了":
        right = guess
    elif res == "太小了":
        left = guess

    elif res == '答对了':
        break
    count += 1
    if count == 10:
        break
"""
"""
import random
num = random.randint(1, 100)
max_num = 100
min_num = 1
cs = 1

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
"""

# ----------------------------------------------------------------------------------------------------------------------
# 三元运算
# 如果输入可以转换为整数则转换，否则返回None
"""
data = input("请输入字符串：")
res = int(data) if data.isdigit() else 'none'
print(res)
"""

# 如果字典中存在某个键则返回对应的值，否则返回默认值
"""
data = {'name': '张三', "ages": 18}
default = "None"
key = input("请输入你要查找的键：")

res = data[key] if key in data else default
print(res)
"""

# 判断是否为闰年（能被4整除但不能被100整除，或者能被400整除）
"""
year = int(input("请输入年份："))
res = "闰年" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "平年"
print(res)
"""

# ----------------------------------------------------------------------------------------------------------------------
# 文件操作
"""
# 读取 <案例7.txt> 中的数据: 去除重复行
# with open("案例7.txt", 'r', encoding="utf-8") as f:
#     data = f.readlines()
#     data = [i.strip() for i in data]
#     # 集合：特性，不包含重复元素
#     data = list(set(data))
#
# with open("案例7有效数据.txt", 'a+', encoding="utf-8") as f:
#     for i in data:
#         f.write(i + '\n')
"""

# 水费计算
'''
根据 water.txt 文件计算每户一年的水费（单价：1.05元/立方米）。
文件格式：第一列为账号，后12列为每月用水量（相邻数值差为实际用水量）。

计算相邻数值差的总和，得到年用水量。
水费 = 用水量 × 1.05。
'''
"""
# with open("file/water.txt", 'r', encoding='utf-8') as f:
#     for line in f:
#         user = line.strip().split()[0]
#         user_water_data = line.strip().split()[1::]
#
#         water = []
#         for i in range(len(user_water_data) - 1):
#             res = int(user_water_data[i + 1]) - int(user_water_data[i])
#
#             water.append(res)
#
#         water_rate = sum(water) * 1.05
#         print("{}:这一年的水费{}".format(user, round(water_rate, 2)))
"""

# 鸢尾花数据集
''' 
读取鸢尾花数据集 iris.txt 格式；读取后逐行打印出来； 
求每行 4 个数值的最小值，将每行最小值写入 min.txt 文件中。
'''
"""
# with open("file/iris.txt", 'r', encoding="utf-8") as f:
#     for i in f:
#         print(i)
#         data = list(i.strip().split(','))
#         min_num = min(data)
#
#         with open("file/min_iris.txt", 'a+', encoding="utf-8") as f:
#             f.write(min_num + '\n')
"""

# ----------------------------------------------------------------------------------------------------------------------
# 使用函数求1 ~ 100的和
# ==============A、普通代码========================
"""
num = 0
for i in range(1, 101):
    num += i
print(num)
"""

# ==============B、函数代码【一个函数】==============
"""
def main():
    num = 0
    for i in range(1, 101):
        num += i
    print(num)


if __name__ == '__main__':
    main()
"""

# ==============C、函数代码【多个函数 - return】=====
"""
def js(num):
    n = 0
    for i in range(1, num + 1):
        n += i
    print(n)


def main():
    num = 100
    js(num)


if __name__ == '__main__':
    main()
"""

# ==============D、函数代码【多个函数 + return】=====
"""
def p(num, n):
    return f"1到{num}的总和是{n}"


def js(num):
    n = 0
    for i in range(1, num + 1):
        n += i
    return n


def main():
    num = int(input("请输入数字："))
    n = js(num)
    d = p(num, n)
    return d


if __name__ == '__main__':
    a = main()
    print(a)
"""

# ------------------------------------------------------------------------------------------------------------------------
# 判断用户输入的变量名是否合法，G密码必须包含数字、大写字母、小写字母;密码不能以数字开头且不能少于 12 位--if判断  re正则表达式

# 鹦鹉螺，输入横长和纵长，从[0][0]开始，按顺时针方向转动，数字逐一增加--if判断

# 字符串筛选器--if判断
'''
输入一个字符串和一个操作指令（格式：<字符串> <操作类型>），其中操作类型为 1 或 2。
根据操作类型筛选字符：
1：提取所有大写字母，输出结果及其数量。
2：提取所有数字，输出结果及其数量。
若字符串长度超过 60，直接输出“不符合要求”。若操作类型非 1 或 2，原样输出输入内容。
'''

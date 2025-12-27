# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# continue 跳出循环
# break  直接结束

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
"""
import random

cs = 0
num = random.randint(1, 100)
print("猜数字的游戏")
print(num)

while True:
    if cs < 3:
        cs += 1
        a = int(input("请输入数字："))
        if a == num:
            print("猜对了")
            break
        elif a > num:
            print("猜大了")
        else:
            print("猜小了")
    else:
        print("没机会了")
        break
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
data_list = [
    '/34/34844/16216570.html',
    '/34/34844/16216573.html',
    '/34/34844/16216574.html',
    '/34/34844/20416605.html'
]

href = 'https://www.xbiquge.la/34/34844/20504594.html'
href_s = href.split('/34/3')[0]
data = [href_s + i for i in data_list]
print(data)
"""

# 3、分开获取数字和后缀---三元运算
"""
data_list =[
    'http://img.adoutu.com/picture/1609683038916.jpg',
    'http://img.adoutu.com/picture/1609683038634.jpg',
    'http://img.adoutu.com/picture/1609683038491.gif',
    'http://img.adoutu.com/picture/1609683038191.png',
    'http://img.adoutu.com/picture/1609683037894.jpg',
    'http://img.adoutu.com/picture/1609683037764.gif',
]

a = [i.split('ure/')[1] for i in data_list]
b = [i.split('.')[0] for i in a]
c = [i.split('.')[1] for i in a]
print(c)
"""

# 变量（结果） = 值1 if 条件 else 值2   没有elif
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
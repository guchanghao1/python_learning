# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''
# 成绩判断语文 数学 英语三门课成绩, 总分> 240去旅游, 否则去补习班--if判断
"""
a = int(input("输入你的语文成绩："))
b = int(input("输入你的数学成绩："))
c = int(input("输入你的英语成绩："))

d = a + b + c

if d >= 240:
    print("去玩")
else:
    print("补习")
"""

# 某商家推出购物优惠活动, 消费金额满500元, 可享9折优惠, 1000元封顶  1000元 以上88 --if判断
"""
m = int(input("你消费的金额："))
if m >= 500 and m <= 1000:
    a = m * 0.9
    print(a)

elif m > 1000:
    b = m * 0.88
    print(b)

else:
    print("原价购买")

"""

# 尾号限行 星期一：1和6，星期二：2和7，星期三：3和8，星期四：4和9，星期五：5和0--if判断
"""
data = input("你的尾号是多少：")

if data == "1" or data == '6':
    print("星期一限行")
elif data == "2" or data == '7':
    print("星期二限行")
elif data == "3" or data == '8':
    print("星期三限行")
elif data == "4" or data == '9':
    print("星期四限行")
elif data == "5" or data == '0':
    print("星期五限行")

else:
    print("请输入正确的尾号")
"""

# 闰年判断：编写程序判断输入的年份是否是闰年（闰年规则：能被4整除但不能被100整除，或者能被400整除）--if判断
"""
year = int(input("请输入年份："))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("是闰年")
else:
    print("不是闰年")
"""

# 成绩判断语文 数学 英语三门课成绩, 总分> 240去旅游, 否则去补习班--if
"""
a = int(input("输入你的语文成绩："))
b = int(input("输入你的数学成绩："))
c = int(input("输入你的英语成绩："))

d = a + b + c

if 60 <= a <= 100 and 60 <= b <= 100 and 60 <= c <= 100:
    if d > 240:
        print("去旅游")
    else:
        print('去补习')
else:
    if a > 100 or b > 100 or c > 100:
        print("请输入正确的分数!!!")
    else:
        print("不及格")

"""

# 输入, a b c, 范围在 【0~100】中, 判断三角形类型--if
"""
a = int(input("输入第一条边："))
b = int(input("输入第二条边："))
c = int(input("输入第三条边："))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("等边三角形")
    elif a == b or a == c or b == c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("非三角形")
"""

# 要求将九九乘法表以左对齐的方法输出--for
"""
for i in range(1, 10):  # 第一个数字
    for j in range(1, i + 1):  # 第二个数字
        print(f"{i}*{j}={i * j}", end="  ")
    print()
"""


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 基本运算符
"""
print(1 + 1)
print(2 - 1)
print(1 * 2)
print(4 / 2)

print(10 // 3)  # 除并且取整数
print(10 % 3)  # 取余
print(2 ** 3)  # 求幂
"""

# 复合赋值运算 += -= *= /= //= **= %=
"""
a = 10
# a += 2
# print(a)
# a -= 2
# print(a)

# a *= 2
# print(a)

# a /= 2
# print(a)

# a //= 3
# print(a)

# a **= 2
# print(a)

a %= 2
print(a)
"""

# 比较运算符 > < == >= <=  !=  in    not in
"""
print(10 > 9)
print(10 < 9)
print(10 == 10)
print(10 == 9)

print(10 >= 9)
print(10 <= 9)

print(10 != 9)

a = [1, 3, 5, 9, 4]
print(2 in a)
b = ['周杰伦', '林俊杰', '张杰', '杨宗纬']
print("周杰伦" in b[1:3])

print('张杰' not in b)

"""

# 逻辑运算符 and与 or或 not非
"""
print(True and True)
print(False and False)
print(True and False)

print(True or True)
print(False or False)
print(True or False)
print(4 > 3 or 3 > 4)

print(not 4 < 3)
"""
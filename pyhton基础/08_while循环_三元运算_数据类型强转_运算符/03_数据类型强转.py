# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# int -- str
a = 123  # int
b = str(a)
print(b)
print(type(b))

# str -- 数字型
c = '1.23'
# d = int(c)
# e = eval(c)
f = float(c)
print(f)
print(type(f))

data1 = [1, 2, 3, 4, 5, 6, 7]
data1 = set(data1)
print(data1)
print(type(data1))

data2 = '123'
data2 = list(data2)
print(data2)

data3 = [('a', 1), ('b', 3)]
data3 = dict(data3)
print(data3)

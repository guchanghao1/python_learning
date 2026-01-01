# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 字符串---- 用引号包裹的
# 1 - 什么是列表？  用[]包裹的内容  可以包裹全部数据类型   可变的
"""
a = [1, '123', ('123'), [1, 2, 3]]  # 子列表
print(type(a))
"""

# 2 - 统计列表长度（元素个数）  len()
"""
a = [1, '123', ('123', '456'), [1, 2, 3]]  # 子列表
print(len(a))
"""

# 3 - 列表的索引(下标)    0开始    包头不包尾
"""
b = [1, 2, 3, 4, 5, 6, 7]
print(b[-1])
"""

# 4 - 列表的切片
"""
b = [1, 2, 3, 4, 5, 6, 7]
a = b[:-2]  # [1, 2, 3, 4, 5, 6]   删除他经过的元素
a1 = b[:4]  # [1]      拿到经过的元素

# b[开始下标：结束下标]   包头不包尾  【左闭右开】
c = b[3:-1]

# 下标和元素个数   b[开始下标：结束下标:步长]
b = [1, 2, 3, 4, 5, 6, 7]
d = b[0:20:3]
print(d)
"""

# 5 - 求列表中的最大值【max(列表)】、最小值【min(列表)】、总和【sum(列表)】、平均值【sum(列表) / len(列表)】
"""
b = [1, 2, 3, 4, 5, 6, 7]
print(max(b))
print(min(b))
print(sum(b))
print(sum(b) / len(b))
"""

# 6 - 列表的增删改查(CURD)
"""
# 查询  index()
data = [1, 2, 3, 4, 5, 6, 7]
data2 = ['周杰伦', '薛之谦', '汪苏泷', '林俊杰', '张杰']
# 用下标查
print(data[1])
print(data[-1])

# index() 用值取下标
a = data2.index('薛之谦')
print(a)

# 用切片
c = data2[1:4]
print(c)

# 增
data2 = ['周杰伦', '薛之谦', '汪苏泷', '林俊杰', '张杰']
# 1 - append 末尾增加
# a = "杨宗纬"
data2.append('杨宗纬')
print(data2)

# 2 - insert  指定位置
data2.insert(0, "杨宗纬")
print(data2)

# 增加多条数据
data2 = ['周杰伦', '薛之谦', '汪苏泷', '林俊杰', '张杰', "杨宗纬", "汪峰"]
# 1 - +
a = [1, 2, 3]
b = data2 + a
print(b)

# 2 - extend
a = [1, 2, 3]
data2.extend(a)
print(data2)

# 改
data2 = ['周杰伦', '薛之谦', '汪苏泷', '林俊杰', '张杰', "杨宗纬", "汪峰"]
# 用下标改   覆盖 修改
data2[2] = "杨宗纬"
print(data2)

data2[2] = ("汪峰")
print(data2)

# 删除
data2 = ['周杰伦', '薛之谦', '汪苏泷', '林俊杰', '张杰', "杨宗纬", "汪峰"]
# 从末尾删除
data2.pop()
print(data2)

# 删除指定元素   下标
data2.pop(3)
print(data2)

# 指定数据删除
data2.remove("杨宗纬")
print(data2)

# 清空列表
data2.clear()
print(data2)
"""

# 7 - 列表的排序【sorted()，sort()】
"""
data = [9, 3, 5, 6, 1, 7, 2, 1.1, 1.2, -1, -2]
print(sorted(data))

data.sort()
print(data)

data.sort(reverse=True)
print(data)
print(data[::-1])
"""

# 8 - 列表的循环
"""
# 单列表循环
import time

a = [9, 1, 2, 3, 4, 5, 6, 7]
for i in a:  # i 来循环 a里面的数据，从最开始的数据开始循环
    print(i)
    time.sleep(1)

# 多列表循环
sg_list = ['苹果', '香蕉', '西瓜', '榴莲']
dz_list = ['长沙', '西安', '广州', '三亚']

for dz, sg in zip(sg_list, dz_list):
    print(dz, sg)
"""
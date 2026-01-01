# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 定义字典   键值对  '键':'值'  换行
"""
a = {}
print(type(a))

b = {'歌名': '一路向北', '歌手': '周杰伦', '作词': '方文山'}
print(type(b))
print(b)

c = {
    '歌名': '一路向北',
    '歌手': '周杰伦',
    '作词': '方文山'
}
print(type(c))
print(c)
"""

# 集合：花括号包裹的信息，无序的，不可重复的
# 和字典的区别，{}里面放的键值对那么就是字典，放的其他数据是集合 只有空字典，没有空集合
"""
a = {1, 2, 3, 4, 5}
b = {1, 1, 1, 2, 3}
print(type(a))
print(b)
"""

# 序列化
"""
# 序列化 有序有下标，无序没下标
# 有序：字符串、列表、元组
# 无序的，去重的：集合、字典
# 键(不能是列表，不能是元组) 和 值(是任何数据)
a = '1234','12'
a1 = '4123'

b = ['12', 34]
b1 = [34, '12']

c = ('12', 34)
c1 = (34, '12')

d1 = {'12', 34}
d2 = {34: '12'}

d = {
    'name': '张三',
    'ages': 18,
    'addr': '上海'
}

e = {
    'addr': '上海',
    'name': '张三',
    'ages': 18,
}
print(d[1])
"""

# 不可重复的
"""
e = {
    'addr': '上海',
    'name': '张三',
    'ages': 18,
    'addr': '上海',
    'name': '张三',
    'ages': 18,
    'addr': '上海',
    'name': '张三',
    'ages': 18,
    'addr': '上海',
    'name': '张三',
    'ages': 18,
    'addr': '上海',
    'name': '张三',
    'ages': 18,

}
print(e)
"""

# 字典操作
# 增删改查(CURD) C--crement U--update R--read D--delete
"""
# 增加   定义键 输入值  键一定是不在字典中的
# data = {
#     '姓名': '周杰伦',
#     '职业': '歌手',
#     '地址': '中国',
#     '歌曲': [{
#         '歌名1': '龙卷风',
#         '歌名2': '稻香',
#     }]
# }
# data['歌名'] = "青花瓷"
# print(data)
#
# []
# data1 = {
#     '姓名': '周杰伦',
#     '职业': '歌手',
#     '地址': '中国',
# }

# a = ['龙卷风', '稻香']
# b = {'歌名1': "晴天", "歌名2": "一路向北"}
# data1['歌曲'] = a
# print(data1)
# data1['歌曲'] = b
# print(data1)
"""

# 查询
"""
# data1 = {
#     '姓名': '周杰伦',
#     '职业': '歌手',
#     '地址': '中国',
# }
# print(data1['职业'])

data2 = {
    '姓名': '周杰伦',
    '职业': '歌手',
    '地址': '中国',
    '歌曲': {
        '歌名1': '龙卷风',
        '歌名2': '稻香',
    }
}
# print(data2['歌曲']['歌名1'])

data3 = {
    '姓名': '周杰伦',
    '职业': '歌手',
    '地址': '中国',
    '歌曲': [{
        '歌名1': '龙卷风',
        '歌名2': '稻香',
    }],
    '歌曲1': {
        '歌名1': '龙卷风',
        '歌名2': '稻香',
    },
    '朋友': [
        {'张三': {'age': 40, 'sexs': '男'}},
        {'李四': {'age': 41, 'sexs': '女'}},
        {'王五': {'age': 42, 'sexs': '男'}},
    ]
}
print(data3['朋友'][1]['李四']['sexs'])

"""

# 高级查询  keys()  values()  items()
"""
data1 = {
    '姓名': '周杰伦',
    '职业': '歌手',
    '地址': '中国',
}

# k = data1.keys()
# v = data1.values()
# item = data1.items()

# print(k)
# print(v)
# print(item)

k_list = list(data1.keys())
v_list = list(data1.values())
i_list = list(data1.items())

for k, v in i_list:
    print(k, v, sep="   |   ")

"""

# 修改   有则改 无则增  键一定是在字典中的
"""
data1 = {
    '姓名': '周杰伦',
    '职业': '歌手',
    '地址': '中国',
}

# 覆盖
# data1['姓名'] = "林俊杰"
# data1['地址'] = '台湾'
# data1['电话'] = 10011
data1['姓名'] = "张杰"
print(data1)
"""

# 删除 del clear
"""
data = {
    '姓名': '周杰伦',
    '职业': '歌手',
    '地址': '中国',
    '歌曲': [{
        '歌名1': '龙卷风',
        '歌名2': '稻香',
    }],
    '歌曲1': {
        '歌名1': '龙卷风',
        '歌名2': '稻香',
    },
    '朋友': [
        {'张三': {'age': 40, 'sexs': '男'}},
        {'李四': {'age': 41, 'sexs': '女'}},
        {'王五': {'age': 42, 'sexs': '男'}},
    ]
}
# del data['地址']
# print(data)

# data.clear()
# print(data)

"""

# 案例一
"""
a = 'name: 张三；age: 18；addr: 上海；sex: 男；phone: 1001'
data = a.split('；')
# print(data)

dic = {}
for i in data:
    k = i.split(':')[0]
    v = i.split(':')[1]
    dic[k] = v
print(dic['age'])
"""

# 案例二
"""
dic = {
    'name': '张三',
    'age': '18',
    'addr': '北京',
    'sex': '男',
    'phone': '1001'
}

response = '我叫: name, 今年: age, 我来自: addr, 性别是: sex, 电话是: phone'

# ---------------------------以上是题目-------------------------------------------

# 1 - replace  简单
# data = response.replace('name', dic['name']).replace('age', dic['age']).replace('addr', dic['addr']).replace('sex', dic['sex']).replace('phone', dic['phone'])
# print(data)

k = list(dic.keys())
v = list(dic.values())

for key, val in zip(k, v):
    response = response.replace(key, val)

print(response)
"""

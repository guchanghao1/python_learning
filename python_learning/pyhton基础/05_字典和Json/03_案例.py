# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 创建和访问字典
'''
创建一个包含你个人信息的字典（姓名、年龄、城市等）
打印出字典中的特定值（如只打印你的年龄）
'''
"""
data = {
    "name": "张三",
    "ages": "19",
    "addr": "长沙"
}

# print(data)
# print(data['ages'])
"""

# 字典操作
'''
创建一个空字典，然后依次添加键值对
编写代码检查字典中是否存在某个键
删除字典中的某个键值对
'''
"""
data2 = {}
data2['歌手1'] = "周杰伦"
data2['歌手2'] = '林俊杰'
data2['歌手3'] = '李荣浩'
data2['歌手4'] = '薛之谦'

# if "歌手6" in data2.keys():
#     print("存在")
# else:
#     print('不存在')


# del data2['歌手4']
# print(data2)
#
# data2.clear()
# print(data2)
"""

# 遍历字典
'''
编写代码打印字典中的所有键
编写代码打印字典中的所有值
编写代码同时打印字典中的键和值
'''
"""
# for i in data3.keys():
#     print(i)
#
# for i in data3.values():
#     print(i)
#
# for i in data3.items():
#     print(i)

data3['歌曲'] = {}
data3['歌曲']['名字1'] = '晴天'
print(data3)
"""

# 输出单个值
"""
data = '{"歌手": "周杰伦", "歌手2": "林俊杰", "歌手3": "张杰"}'

a = eval(data)['歌手']
print(a)

import json

b = json.loads(data)['歌手2']
print(b)
"""

# 字典格式 转 列表嵌套格式   --->   （A字典格式转换成B列表嵌套格式）
'''
A、转换前格式（字典）：   天气预报：forecast
    {
        '19.06.2021': {'date': '19.06.2021', 'temp_max': 27, 'temp_min': 22, 'precipitations': 0.0}, 
        '20.06.2021': {'date': '20.06.2021', 'temp_max': 23, 'temp_min': 16, 'precipitations': 6.2}, 
        '21.06.2021': {'date': '21.06.2021', 'temp_max': 23, 'temp_min': 15, 'precipitations': 2.0}, 
    }
B、转换后的格式（大列表嵌套小列表格式）：
    [
        ['19.06.2021', 27, 22, 0.0],    
        ['20.06.2021', 23, 16, 6.2],    
        ['21.06.2021', 23, 15, 2.0], 
    ]
'''
"""
data_dic = {
    '19.06.2021': {'date': '19.06.2021', 'temp_max': 27, 'temp_min': 22, 'precipitations': 0.0},
    '20.06.2021': {'date': '20.06.2021', 'temp_max': 23, 'temp_min': 16, 'precipitations': 6.2},
    '21.06.2021': {'date': '21.06.2021', 'temp_max': 23, 'temp_min': 15, 'precipitations': 2.0},
}

方法一：
data_list = list(data_dic.values())
# print(data_list)
li = []
for data in data_list:
    result = list(data.values())
    li.append(result)
for i in li:
    print(i)
    
方法二：
v = list(data_dic.values())
for data in v:
    r = list(data.values())
    print(r)

"""

# 案例实战：字典查询
''' 
data = {'msg': '查询成功!', 'v_code': '220,38', 'errCode': 0, 'v_type': 'sld'}
需要把220取出来
'''
"""
data = {'msg': '查询成功!', 'v_code': '220,38', 'errCode': 0, 'v_type': 'sld'}
data2 = data['v_code'].split(',')[0]
print(data2)
"""

# 字典操作
''' 
假设字典变量dic_country存储了部分国家的国家名与首都名的对应关系，其中国家名为键，首都名为值，即键值对为“国家名:首都名”。
样本数据如下：
    dic_country={"China":"Beijing","America":"Washington","Norway":"Oslo","Japan":\
    "Tokyo","Germany":"Berlin","Canada":"Ottawa","France":"Paris","Thailand":"Bangkok"}
    试编写程序，根据用户输入的国家名查询首都名，如果存在则输出查询结果，否则提示“未查询该国家名！”。
    假设对国家名进行查询不区分大小写。（功能简称：字典）
'''
"""
dic_country = {
    "China": "Beijing",
    "America": "Washington",
    "Norway": "Oslo",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "France": "Paris",
    "Thailand": "Bangkok"
}
user_input = input('请输入要查询的国家名: ')
key_list = list(dic_country.keys())
value_list = list(dic_country.values())
for key, value in zip(key_list, value_list):
    if user_input == key:
        print('{}的首都是: {}'.format(key, value))
        break
else:
    print('未查询该国家名')
"""

# 接收一个字符串，分别统计大写字母、小写字母、数字、其他字符的个数，并以字典的形式返回结果。
"""
dic = {}
upper = 0
lower = 0
digit = 0
other = 0
s = 'Hlello World!778@#sWelcome!%'
for i in s:
    if i.isupper() == True:
        upper += 1
    elif i.islower() == True:
        lower += 1
    elif i.isdigit() == True:
        digit += 1
    else:
        other += 1
dic['upper'] = upper
dic['lower'] = lower
dic['digit'] = digit
dic['other'] = other
print(dic)

"""

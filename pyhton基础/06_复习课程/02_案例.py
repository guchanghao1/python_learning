# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''
# 数据类型
"""
字符串       str         ''
列表        list        []
元组        tuple       ()
字典        dict        {}
json       json       '{""}'
整型        int         1 2 3 4
浮点型      float       123.456
集合        set         {}
"""
# ----------------------------------------------------------------------------------------------------------------------

# 字符串
# 1、输入一段字符，统计其中单词的个数，单词之间用空格分隔。如：Python is an object oriented programming language
"""
a = input("请输入一段字符：")
print(len(a.split()))
"""

# 2、字符串切片训练
''' 
设计一个程序，输入是一个字符串'  长春工程学院-土木工程学院-智能建造专业 '（样本字符串），
注意：字符串前面是两个空格，最后有一个空格。

然后按下列要求操作：
（1）删除所输入字符串的首尾空格（要求两种方法完成：strip()和replace()），并分别输出。然后对删除空格后的字符串进行下面的操作。
（2）输出这个字符串的长度。
（3）用切片的方式用一句Python语句输出“长春工程学院”。
（4）用切片的方式用一句Python语句输出“土木学院”。（提示：两次切片再拼接）
（5）用切片的方式用一句Python语句输出“智造”。（要求起始和结束使用反向索引）
（6）使用split方法切出三个子串，并逆序输出第二个子串。
（7）输出字符串中“学院”出现的次数。
（8）使用replace()方法将串中的“智能建造”用“智造”替换，并输出替换后的串。
'''
"""
# 所输入字符串的首尾空格（要求两种方法完成：strip()和replace()），并分别输出。然后对删除空格后的字符串进行下面的操作。
b = '  长春工程学院-土木工程学院-智能建造专业 '
print(b.replace(' ', ''))
print(b.strip())

# （2）输出这个字符串的长度。
print(len(b))

# （3）用切片的方式用一句Python语句输出“长春工程学院”。
print(b[2:8])
print(b[9:15])

# （4）用切片的方式用一句Python语句输出“土木学院”。（提示：两次切片再拼接）
# （5）用切片的方式用一句Python语句输出“智造”。（要求起始和结束使用反向索引）
print(b[9:15])
a = b[9:11]
c = b[13:15]
print(a + c)

# （6）使用split方法切出三个子串，并逆序输出第二个子串。
a = b.split('-')[1]
print(a)
print(a[::-1])

# （7）输出字符串中“学院”出现的次数。
a = b.count('学院')
print(a)

# （8）使用replace()方法将串中的“智能建造”用“智造”替换，并输出替换后的字符串。
a = b[-7:-6]
c = b[-4:-3]
d = a + c
data = b.replace('智能建造', d)
print(data)
"""

# 3、人机交互：简单的登录界面
"""
print('----------------------')
a = input("请输入你的注册用户名：")
b = input("请输入你的注册密码：")
print("恭喜你！ 注册成功")
print('----------------------')
"""

# 4、判断字符串中、数字几个、大写字母几个、小写字母几个、其他字符几个
"""
data = input("请输入字符串：")
sz = 0
dx = 0
xx = 0
qt = 0
for i in data:
    if i.isdigit():  # 判断是否是数字
        sz += 1
    elif i.isupper():  # 判断是否是大写
        dx += 1
    elif i.islower():  # 判断是否是小写
        xx += 1
    else:
        qt += 1

print(f"数字有{sz}个，大写有{dx}个，小写有{xx}个，其他字符{qt}个")
"""

# 5、输入一组以顿号“,”为间隔的英文字母，按字母顺序逆序输出
"""
data = 'f, e, b, a, c, d'
data1 = sorted(data.split(','), reverse=True)
print(data1)
"""

# 6、字符连接：从键盘输入一组单词和一个连接符，并将这组单词存入列表中。然后使用连接符将列表中的单词串联起来
"""
data = ['python', 'pycharm', 'java', 'c++']
s = '=='
a = f'{s}'.join(data)
print(a)
"""
# ----------------------------------------------------------------------------------------------------------------------

# 列表
# 1、使用多列表遍历进行数据匹配
"""
a = ['姓名：', '年龄：', '性别：', '职业：']
b = ['张三', 18, '男', '学生']

for x, y in zip(a, b):
    print(x, y)
"""

# 2、列表切片倒序输出：[::-1]  [开始下标:结束下标:步长]
"""
a = [1, 2, 3, 4, 5, 6]
print(a[::-1])
"""

# 3、输入购买的水果和重量，算出总价
'''
name_list = ['苹果', '香蕉', '西瓜', '橘子', '榴莲']
pric_list = ['8', '6', '3', '12', '28']
'''
"""
name_list = ['苹果', '香蕉', '西瓜', '橘子', '榴莲']
pric_list = ['8', '6', '3', '12', '28']
name = input("请输入购买的水果：")
w = eval(input("请输入购买的重量："))  # input 输出的是字符串，所以需要强制转换 使用eval()/ int()
a = eval(pric_list[name_list.index(name)])
b = a * w
print(b)
"""

# 4、功能如下：
'''
（1）从键盘输5个城市的名字，存入一个列表中。要求：
    ① 第一个城市是你所在家乡的城市名。
    ② 每个汉字城市名的前面加上拼音首字母缩写，如：cc长春 。
    ③ 用一个input函数完成5个城市名字的输入，如：input("请输入5个城市的名字，用空格分隔：") 。
（2）将该列表中元素，即5个城市的名字用for循环遍历输出。
（3）用索引值输出列表中你家乡的名字。再切片输出所有其它城市名字。
（4）对该列表进行逆序输出。要求用两种方法完成（切片法和使用reverse()方法）。
（5）对该列表进行降序排序，并输出。要求用两种方法完成（sorted()和sort()）。
（6）对降序排序后的列表，用切片方法，输出你家乡的名字及其前面和后面的名字（如果有的话）。注：不能直接使用0、1、2、……这样的索引值，即你家乡城市名的索引值使用inexe()函数获得。提示：需要用if 语句。
（7）将你家乡城市的名字前面和后面的城市（如果有的话），改名为任意其他城市的名字，并输出。注：还是不能直接用数字作为索引值。提示：需要用if 语句。
（8）将刚才改名的1个（如果你家乡所在城市排在第一位或最后一位）或2个城市的名字删除，并输出剩下的城市名字。注：还是不能直接用数字作为索引值。提示：需要用if 语句。
'''
"""
# （1）从键盘输5个城市的名字，存入一个列表中。要求：
data = ['nj南京', 'bj北京', 'sh上海', 'wh武汉', 'gz广州']

# （2）将该列表中元素，即5个城市的名字用for循环遍历输出。
for i in data:
    print(i)

# （3）用索引值输出列表中你家乡的名字。再切片输出所有其它城市名字。
print(data[3])
a = data[0:3]
b = data[4:]
print(a + b)

# （4）对该列表进行逆序输出。要求用两种方法完成（切片法和使用reverse()方法）。
print(data[::-1])
data.sort(reverse=True)
print(data)

# （5）对该列表进行降序排序，并输出。要求用两种方法完成（sorted()和sort()）。
a = sorted(data, reverse=True)
print(a)

data.sort(reverse=True)
print(data)

# （6）对降序排序后的列表，用切片方法，输出你家乡的名字及其前面和后面的名字（如果有的话）。注：不能直接使用0、1、2、……这样的索引值，即你家乡城市名的索引值使用inexe()函数获得。提示：需要用if 语句。
data.sort(reverse=True)
h = input("我的家乡：")
a = data.index(h)
if a > 0:
    print(data[a - 1])

if a < len(data) - 1:
    print(data[a + 1])

# （7）将你家乡城市的名字前面和后面的城市（如果有的话），改名为任意其他城市的名字，并输出。注：还是不能直接用数字作为索引值。提示：需要用if 语句。
data.sort(reverse=True)
h = input("我的家乡：")
a = data.index(h)
if a > 0:
    data[a - 1] = "cs长沙"

if a < len(data) - 1:
    data[a + 1] = "hz杭州"

print(data)

# （8）将刚才改名的1个（如果你家乡所在城市排在第一位或最后一位）或2个城市的名字删除，并输出剩下的城市名字。注：还是不能直接用数字作为索引值。提示：需要用if 语句。
data.sort(reverse=True)
h = input("我的家乡：")
a = data.index(h)
if a > 0:
    data[a - 1] = "cs长沙"
    b = data.index('cs长沙')
    del data[b]

if a < len(data) - 1:
    data[a + 1] = "hz杭州"
    c = data.index('hz杭州')
    del data[c]

print(data)
"""

# 5、列表操作
'''
1、计算列表长度
2、列表末尾追加 seven
3、在第一个位置插入 Tony
4、修改第2个元素, Kelly
5、删除列表中 eric
6、删除列表中第三个元素
7、删除列表中第2~4个元素
8、所有列表元素反转
9、获取Tong索引值
'''
"""
li = ['alex', 'eric', 'rain', 'mike', 'alice', 'lucy']
print(len(li))

li.append('seven')
print(li)

li.insert(1, 'Tony')
print(li)

li[1] = 'Kelly'
print(li)

li.remove('eric')
print(li)

li.pop(2)
print(li)

del li[1:5]
print(li)

print(li[::-1])

a = li.index('mike')
print(a)
"""

# 6、列表操作
'''
1、将列表备份
2、整个列表清空
3、为每位同学随机生成成绩（0-100分）。将名单与成绩组合成字典并打印。
'''
"""
data_list = ['方志强', '史荣滨', '曾加美', '陈子婷', '邓家欣', '方文敏',
             '方泽榕', '李诗慧', '刘海琳', '刘奕梓', '刘裔毅', '刘颖榆',
             '吴家琪', '许文迪', '钟修杨', '朱嘉婵', '朱茜茜', '庄园园',
             '陈惠香', '陈铭霞', '陈铭轩', '成浩杰', '成文静', '符骏轩',
             '黄聪颐', '黄思思', '黄梓佳', '江仕豪', '柯璎芷', '李凯铃',
             '李小卉', '李晓月', '李雄杰', '李志豪', '林才云', '林日烽',
             '林淑屏', '林思雯', '刘佳禾', '骆文翰', '邵佳楠', '黄溶溶',
             '温雅淋', '吴俊堂', '严景森', '严巧玲', '田泽莲', '钟坤盛',
             '周婷', '周泽霖', '朱峰荣', '卓珊伊', '陈嘉辉', '张茵意',
             '钟夏楠']

a = data_list
print(a)

data_list.clear()
print(data_list)

import random
dic = {}
for i in data_list:
    dic[i] = random.randint(70, 100)
print(dic)
"""

# 7、元祖操作
'''
1、元祖切片
2、查找
3、元素次数统计
4、元祖长度
5、在创建一个元祖, 将两个元祖合并
'''
"""
tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10)
print(tuple_1[4:8])
print(tuple_1[-2])
print(tuple_1.count(10))
print(len(tuple_1))

a = (11, 13, 13)
b = tuple_1 + a
print(b)
"""
# ----------------------------------------------------------------------------------------------------------------------

# 字典
# 1、创建和访问字典
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

print(data['name'])

data = {
    'name': '张三',
    'age': '18',
    'addr': '上海',
}

print(data['name'])
"""

# 2、字典操作
'''
创建一个空字典，然后依次添加键值对
编写代码检查字典中是否存在某个键
删除字典中的某个键值对
'''
"""
data = {
    'name': '张三',
    'age': '18',
    'addr': '上海',
}

a = input("输入你需要检查键：")

if a in data.keys():
    print("在")
else:
    print("不存在")

del data['addr']
print(data)
"""

# 3、遍历字典
'''
编写代码打印字典中的所有键
编写代码打印字典中的所有值
编写代码同时打印字典中的键和值
'''
"""
data = {
    'name': '张三',
    'age': '18',
    'addr': '上海',
}

for i in data.keys():
    print(i)

for i in data.values():
    print(i)

for i in data.items():
    print(i)

# """

# 4、输出单个值
"""
data = {
    "name": "张三",
    "ages": "19",
    "addr": "长沙"
}
print(data['ages'])
"""

# 5、字典格式 转 列表嵌套格式   --->   （A字典格式转换成B列表嵌套格式）
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
data = {
    '19.06.2021': {'date': '19.06.2021', 'temp_max': 27, 'temp_min': 22, 'precipitations': 0.0},
    '20.06.2021': {'date': '20.06.2021', 'temp_max': 23, 'temp_min': 16, 'precipitations': 6.2},
    '21.06.2021': {'date': '21.06.2021', 'temp_max': 23, 'temp_min': 15, 'precipitations': 2.0},
}

a = list(data.values())
li = []
for i in a:
    b = list(i.values())
    li.append(b)
    # print([b])

print(li)
"""

# 6、需要把220取出来
"""
data = {'msg': '查询成功!', 'v_code': '220,38', 'errCode': 0, 'v_type': 'sld'}
print(data['v_code'].split(',')[0])
"""

# 7、根据用户输入的国家名查询首都名
''' 
假设字典变量dic_country存储了部分国家的国家名与首都名的对应关系，其中国家名为键，首都名为值，即键值对为“国家名:首都名”。
样本数据如下：
    dic_country={"China":"Beijing","America":"Washington","Norway":"Oslo","Japan":"Tokyo","Germany":"Berlin","Canada":"Ottawa","France":"Paris","Thailand":"Bangkok"}
    根据用户输入的国家名查询首都名，如果存在则输出查询结果，否则提示“未查询该国家名！”。
'''
"""
dic_country = {"China": "Beijing",
               "America": "Washington",
               "Norway": "Oslo",
               "Japan": "Tokyo",
               "Germany": "Berlin",
               "Canada": "Ottawa",
               "France": "Paris",
               "Thailand": "Bangkok"}

a = input("请输入国家名字：")
# 方法一
if a in dic_country.keys():
    print(dic_country[f'{a}'])
else:
    print("不存在")

# 方法二
key = list(dic_country.keys())
vel = list(dic_country.values())

for k, v in zip(key, vel):
    if a == k:
        print(v)
        break
else:
    print('不存在')
"""

# 8、接收一个字符串，分别统计大写字母、小写字母、数字、其他字符的个数，并以字典的形式返回结果。
"""
data = input("请输入字符串：")
sz = 0
dx = 0
xx = 0
qt = 0
dic = {}
for i in data:
    if i.isdigit():  # 判断是否是数字
        sz += 1
    elif i.isupper():  # 判断是否是大写
        dx += 1
    elif i.islower():  # 判断是否是小写
        xx += 1
    else:
        qt += 1

dic['upper'] = dx
dic['lower'] = xx
dic['digit'] = sz
dic['other'] = qt

print(dic)
"""


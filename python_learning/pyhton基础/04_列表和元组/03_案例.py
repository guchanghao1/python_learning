# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------

# 使用多列表遍历进行数据匹配
"""
a = ['姓名：', '年龄：', '性别：', '职业：']
b = ['张三', 18, '男', '学生']
for x, y in zip(a, b):
    print(x, y)
"""

# 列表切片倒序输出：[::-1]
"""
# 字符串的倒序输出：s = 'aAsmr3idd4bugs7Dlsf9eAF'
s = 'aAsmr3idd4bugs7Dlsf9eAF'
a = s[::-1]
print(a)

b = ['1', '2', '3', '4', '5']
print(b[::-1])
"""

# 列表查询
'''
name_list = ['苹果', '香蕉', '西瓜', '橘子', '榴莲']
pric_list = ['8', '6', '3', '12', '28']

name = input("请输入购买的水果：")
weig = eval(input("请输入购买的重量："))
pric = eval(pric_list[name_list.index(name)])
total = weig * pric

print(f'购买的是{name}，重量是{weig}，总价是{total}')
'''

# 列表操作
''' 
功能如下：
（1）从键盘输5个城市的名字，存入一个列表中。要求：
    ① 第一个城市是你所在家乡的城市名。
    ② 每个汉字城市名的前面加上拼音首字母缩写，如：cc长春 。
    ③ 用一个input函数完成5个城市名字的输入，如：input("请输入5个城市的名字，用空格分隔：") 。
（2）将该列表中元素，即5个城市的名字用for循环遍历输出。
（3）用索引值输出列表中你家乡的名字。再切片输出所有其它城市名字。
（4）对该列表进行逆序输出。要求用两种方法完成（切片法和使用reverse()方法）。
（5）对该列表进行降序排序，并输出。要求用两种方法完成（sorted()和sort()）。
（6）对降序排序后的列表，用切片方法，输出你家乡的名字及其前面和后面的名字（如果有的话）。注：不能直接使用0、1、2、……这样的索引值，
    即你家乡城市名的索引值使用inexe()函数获得。提示：需要用if 语句。
（7）将你家乡城市的名字前面和后面的城市（如果有的话），改名为任意其他城市的名字，并输出。注：还是不能直接用数字作为索引值。
    提示：需要用if 语句。
（8）将刚才改名的1个（如果你家乡所在城市排在第一位或最后一位）或2个城市的名字删除，并输出剩下的城市名字。
    注：还是不能直接用数字作为索引值。提示：需要用if 语句。
'''
"""
# （1）从键盘输5个城市的名字
city_list = input('请输入5个城市的名字，用空格分隔：').split(' ')
print(city_list)

# （2）将该列表中元素，即5个城市的名字用for循环遍历输出
city_list = input('请输入5个城市的名字，用空格分隔：').split(' ')
for city in city_list:
    print(city)

# （3）用索引值输出列表中你家乡的名字。再切片输出所有其它城市名字。
city_list = input('请输入5个城市的名字，用空格分隔：').split(' ')
jx_city = city_list[0]
qt_city = city_list[1:]
print(jx_city)
print(qt_city)

# （4）对该列表进行逆序输出。要求用两种方法完成（切片法和使用reverse()方法）
city_list = input('请输入5个城市的名字，用空格分隔：').split(' ')
result_1 = city_list[::-1]
print(result_1)
city_list.reverse()
print(city_list)

# （5）对该列表进行降序排序，并输出。要求用两种方法完成（sorted()和sort()）。
city_list = input('请输入5个城市的名字，用空格分隔：').split(' ')
result_2 = sorted(city_list, reverse=True)
print(result_2)
city_list.sort(reverse=True)
print(city_list)

# （6）对降序排序后的列表，用切片方法，输出你家乡的名字及其前面和后面的名字（如果有的话）
city_list = input('请输入5个城市的名字，用空格分隔：').split(' ')
home = input("请输入你的家乡：")
cs_sort = sorted(city_list, reverse=True)
a = city_list.index(home)
if a > 0:
    print(city_list[a - 1])

if a < len(city_list) - 1:
    print(city_list[a + 1])

# （7）将你家乡城市的名字前面和后面的城市，改名为任意其他城市的名字，并输出  # nj南京 bj北京 sh上海 wh武汉 gz广州
city_list = input('请输入5个城市的名字，用空格分隔：').split(' ')
home = input("请输入你的家乡：")
cs_sort = sorted(city_list, reverse=True)
a = city_list.index(home)
if a > 0:
    city_list[a - 1] = "sz苏州"

if a < len(city_list) - 1:
    city_list[a + 1] = 'hz杭州'

print(city_list)

# （8）将刚才改名的1个（如果你家乡所在城市排在第一位或最后一位）或2个城市的名字删除，并输出剩下的城市名字
city_list = input('请输入5个城市的名字，用空格分隔：').split(' ')
home = input("请输入你的家乡：")
cs_sort = sorted(city_list, reverse=True)
a = city_list.index(home)
if a > 0:
    city_list[a - 1] = "sz苏州"
    b = city_list.index('sz苏州')
    del city_list[b]

if a < len(city_list) - 1:
    city_list[a + 1] = 'hz杭州'
    c = city_list.index('hz杭州')
    del city_list[c]

print(city_list)
"""

# 列表操作
''' 
1、计算列表长度
2、列表末尾追加 seven
3、在第一个位置插入 Tony
4、修改第2个元素, Kelly
5、删除列表中 eric
6、删除列表中第二个元素
7、删除列表中第三个元素
8、删除列表中第2~4个元素
9、所有列表元素反转
10、获取Tong索引值
'''
"""
li = ['alex', 'eric', 'rain', 'mike', 'alice', 'lucy']
result = len(li)
print(result)

li.append('seven')
print(li)

li.insert(0, 'Tong')
print(li)

li[1] = 'Kelly'
print(li)

li.remove('eric')
print(li)

remove_data = li.pop(1)
print(remove_data)
print(li)

li.pop(2)
print(li)

del li[1: 5]
print(li)

li.sort()
print(li)

data = li.index('Tong')
print(data)
"""

# 列表操作
'''
1、将刘艳添加到最后
2、将刘艳添加到列表第五个
3、将钟夏楠删除
4、将列表名单反转
5、将列表备份
6、整个列表清空
7、为每位同学随机生成成绩（0-100分）。将名单与成绩组合成字典并打印。
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

data_list.append('刘艳')
print(data_list)

data_list.insert(4, '刘艳')
print(data_list)

data_list.remove('钟夏楠')
print(data_list)

new_list = data_list[::-1]
print(new_list)

aaa = data_list
print(aaa)

data_list.clear()
print(data_list)

import random

dic = {}
for i in data_list:
    dic[i] = random.randint(60, 100)
print(dic)

"""

# 元祖操作
"""
tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10)

# 1、元祖切片
result = tuple_1[1: 4]
print(result)

# 2、检索
result = tuple_1[3]
print(result)

# 3、元素次数统计
tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10)
print(tuple_1.count(10))

# 4、元祖长度
result = len(tuple_1)

# 5、在创建一个元祖, 将两个元祖合并
tuple_2 = (11, 12, 13)
result2 = tuple_1 + tuple_2
print(result2)
"""

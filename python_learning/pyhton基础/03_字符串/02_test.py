# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

"""
第二题：人机交互  你的名字(网名，英文名) 性别 爱好
第一题：前置和后置拼接你的 名字(网名，英文名) 性别 爱好
第三题：切割 找一句话 将里面词语切割出来
"""

# 倒序输出[::-1]
"""
data9 = "123456789"
print(data9[::-2])
"""

# 字符串的后两个替换前两个
"""
a = "abcdef"
b = a[:2]
c = a[-2:]
# print(c)
d = a.replace(b, c)[:-2]
print(d)
"""

# 字符拼接：从键盘输入一组单词和一个连接符，并将这组单词存入列表中。然后使用连接符将列表中的单词串联起来
"""
a = ['abc', 'def', 'fed', 'cba']
b = '-'.join(a)
print(b)
"""

# 输入一段字符，统计其中单词的个数，单词之间用空格分隔。#Python is an object-oriented programming language
"""
a = input('请输入字符串：')
print(len(a.split()))
"""

# 字符串切片训练
''' 
设计一个程序，输入是一个字符串“  长春工程学院-土木工程学院-智能建造专业 ”（样本字符串），注意：字符串前面是两个空格，最后有一个空格。
然后按下列要求操作。
（0）删除所输入字符串的首尾空格（要求两种方法完成：strip()和replace()），并分别输出。然后对删除空格后的字符串进行下面的操作。
（1）输出这个字符串的长度。
（2）用切片的方式用一句Python语句输出“长春工程学院”。
（3）用切片的方式用一句Python语句输出“土木学院”。（提示：两次切片再拼接）
（4）用切片的方式用一句Python语句输出“智造”。（要求起始和结束使用反向索引）
（5）使用split方法切出三个子串，并逆序输出第二个子串。
（6）输出字符串中“学院”出现的次数。
（7）使用replace()方法将串中的“智能建造”用“智造”替换，并输出替换后的串。
'''
"""
data_str = '  长春工程学院-土木工程学院-智能建造专业 '
# 1: 删除所输入字符串的首尾空格     strip()和replace()
result_1 = data_str.replace(' ', '')
print(result_1)
result_2 = data_str.strip()
print(result_2)

# 2: 输出这个字符串的长度
data_str = '  长春工程学院-土木工程学院-智能建造专业 '
result_3 = len(data_str)
print(result_3)

# 3: 用切片的方式输出 “长春工程学院”                          [起始下标: 末尾下标+1]
data_str = '  长春工程学院-土木工程学院-智能建造专业 '
result_4 = data_str[2: 8]
print(result_4)

# 4: 用切片的方式输出“土木学院”。（提示：两次切片再拼接）
data_str = '  长春工程学院-土木工程学院-智能建造专业 '
result_5 = data_str[9: 11] + data_str[13: 15]
print(result_5)

# 5: 用切片的方式输出“智造”。（要求起始和结束使用反向索引）
data_str = '  长春工程学院-土木工程学院-智能建造专业 '
result_6 = data_str[-7] + data_str[-4]
print(result_6)

# 6: 使用split方法切出三个子串，并逆序输出第二个子串。
data_str = '  长春工程学院-土木工程学院-智能建造专业 '
result_7 = data_str.split('-')[-2]
print(result_7)

# 7: 出字符串中“学院”出现的次数
data_str = '  长春工程学院-土木工程学学院-智能建造专业 '
result_8 = data_str.count('学院')
print(result_8)

# 8: 使用replace()方法将串中的“智能建造”用“智造”替换，并输出替换后的串。
data_str = '  长春工程学院-土木工程学学院-智能建造专业 '
result_9 = data_str.replace('智能建造', '智造')
print(result_9)
"""

# 人机交互：登录界面
"""
print('-------------------------')
print('       注册界面           ')
acc = input('请输入您注册用户名: ')
pwd = input('请输入您注册的密码: ')
print('恭喜您！注册成功！')
print('-------------------------')
print('-------------------------')
print('       登录界面           ')
x = input('请输入您登录用户名: ')
y = input('请输入您注册的密码: ')
if x == acc and y == pwd:
    print('登录成功')
else:
    print('登录失败')
print('-------------------------')
"""

# 判断字符串中  数字几个 大写字母几个 小写字母几个
"""
data = input('请输入内容：')
s = 0
x = 0
d = 0
o = 0
for i in data:
    if i.isdigit() == True:
        s += 1
    elif i.islower() == True:
        x += 1
    elif i.isupper() == True:
        d += 1
    else:
        o += 1
print('数字{}个 大写字母{}个 小写字母{}个 其他字符{}个'.format(s, d, x, o))
"""

# 输入一组以顿号“、”为间隔的英文字母，按字母顺序逆序输出
"""
data = 'e、b、a、d、c、f'
result = sorted(data.split('、'), reverse=True)
print(result)
"""

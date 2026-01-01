# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import string


def passwd_pre(pwd):
    char_list = []
    for char in pwd:
        if char in 'abcde':
            char = '!'
        elif char in 'fghij':
            char = '@'
        elif char in 'klmno':
            char = '$'
        elif char in 'pqrst':
            char = '%'
        elif char in 'uvwxyz':
            char = '*'
        elif char in 'Z':
            char = 'a'
        else:
            char = chr(ord(char.lower()) + 1)
        char_list.append(char)
        return ''.join(char_list)


def change_pwd(pwd, str1, str2):
    char_list = ''
    pwd = pwd.lower()
    for char in pwd:
        j = str1.find(char)
        if j == -1:
            char_list = char_list + char
        else:
            char_list = char_list + str2[j]
    return char_list


def change_password(pwd):
    if pwd == None:
        return '无数据'
    char = ''
    char_pre = passwd_pre(pwd)
    char_len = len(pwd)
    # 替换字符
    char_str = change_pwd(pwd, '0123456789' + string.ascii_lowercase, string.ascii_lowercase + '0123456789')
    if len(pwd) <= 4:
        char = char_pre + char_str[0:char_len]
    else:
        char = char_pre + char_str[0:4]
    return char


if __name__ == '__main__':
    while True:
        pwd = input('请输入密码：')
        if pwd == 'q':
            break
        else:
            new_pwd = change_password(pwd)
            print('你输入原码是：', pwd, '加密后的是', new_pwd)

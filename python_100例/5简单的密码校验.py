# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------

def check_len(pwd):
    if len(pwd) < 5:
        return False
    else:
        return True


def check_data(pwd):
    check = [0, 0, 0, 0]
    for i in pwd:
        if i.islower():
            check[0] = 1
        if i.isupper():
            check[1] = 1
        if i.isdigit():
            check[2] = 1
        if not i.isalpha() or i.isdigit() or i.isspace():
            check[3] = 1

    if sum(check) == 4:
        return True
    else:
        return False


def check_rep(pwd):
    num = len(pwd)
    for i in range(num - 4):
        a = pwd[i:i + 4]
        b = pwd[i + 4::]
        if a in b:
            return False

    return True


if __name__ == '__main__':
    msg = ""
    while True:
        pwd = input("password:")
        if pwd == 'q':
            print('out')
            break
        c1 = check_len(pwd)
        if not c1:
            print('short,try again')
            continue
        c2 = check_data(pwd)
        if not c2:
            print('try again')
            continue
        c3 = check_rep(pwd)
        if not c3:
            print('wrong,try again')
            continue
        print('success!!')
        break

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''


def 增加():
    print('---------------------增加学生数据 - --------------------')
    sid = input("请输入学号：")
    name = input("请输入姓名：")
    ages = input("请输入年龄：")
    sexs = input("请输入性别：")
    addr = input("请输入地址：")
    info = "{} - {} - {} - {} - {}".format(sid, name, ages, sexs, addr)
    with open("学生管理系统.txt", 'a+', encoding="utf-8") as f:
        f.write(info + '\n')
    print("保存完成")


def 查询():
    print('---------------------查询学生数据 - --------------------')
    name = input("请输入你需要查询的名字：")
    with open("学生管理系统.txt", 'r', encoding="utf-8") as f:
        for i in f:
            stu = i.strip()
            stu_name = stu.split(' - ')[1]

            if stu_name == name:
                print("查询完成:{}".format(stu))


def 修改():
    print('---------------------修改学生数据 - --------------------')
    new_list = []
    id = input("请输入需要修改的学号：")
    with open("学生管理系统.txt", 'r', encoding="utf-8") as f:
        for i in f:
            data = i.strip().split(' - ')

            if id == data[0]:
                name = input("请输入姓名：")
                ages = input("请输入年龄：")
                sexs = input("请输入性别：")
                addr = input("请输入地址：")
                info = '{} - {} - {} - {} - {}'.format(id, name, ages, sexs, addr)

                new_list.append(info)

            else:
                new_list.append(' - '.join(data))

    with open("学生管理系统.txt", 'w', encoding="utf-8") as f:
        for i in new_list:
            f.write(i + '\n')
    print('修改成功')


def 删除():
    print('---------------------删除学生数据 - --------------------')
    id = '202501'
    new_list = []

    with open("学生管理系统.txt", 'r', encoding="utf-8") as f:
        data_list = f.readlines()

    data = [i.strip() for i in data_list]
    for i in data:
        if id not in i:
            new_list.append(i)

    with open("学生管理系统.txt", 'w', encoding="utf-8") as f:
        for i in new_list:
            f.write(i + '\n')
    print("删除成功")


def 学生管理系统():
    print('-------------------欢迎使用学生管理系统 - ------------------')
    print('---------------------0.退出学生数据 - --------------------')
    print('---------------------1.增加学生数据 - --------------------')
    print('---------------------2.查询学生数据 - --------------------')
    print('---------------------3.修改学生数据 - --------------------')
    print('---------------------4.删除学生数据 - --------------------')

    while True:
        op = input("请输入你的操作选项：")

        if op == "0":
            print("退出学生管理系统")
            break

        elif op == "1":
            增加()

        elif op == "2":
            查询()

        elif op == "3":
            修改()

        elif op == "4":
            删除()

        else:
            print('输入有误，请重新进入')
            break


if __name__ == '__main__':
    学生管理系统()

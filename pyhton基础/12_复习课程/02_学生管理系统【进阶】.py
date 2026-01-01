# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------
''''''


def add_stu():
    print("欢迎进入新增学生数据".center(47, '*'))
    # 先去找文件中有没有这个学生，没有的话就添加，有的话就判断已存在
    try:
        with open("学生管理系统.txt", 'r', encoding='utf-8') as f:
            stu_data = f.readlines()
    except FileNotFoundError:
        stu_data = []

    while True:
        sid = input("请输入学号：")
        id = [i.split(' - ')[0] for i in stu_data if i.strip()]
        if sid in id:
            print("学号已存在")
            continue
        else:
            name = input("请输入姓名：")
            ages = input("请输入年龄：")
            sexs = input("请输入性别：")
            addr = input("请输入地址：")
            stu_info = "{} - {} - {} - {} - {}".format(sid, name, ages, sexs, addr)

        with open("学生管理系统.txt", "a+", encoding="utf-8") as f:
            f.write(stu_info + "\n")
        print("保存完成")
        break


def show_stu():
    print("欢迎进入查询学生数据".center(47, '*'))
    name_id = input("请输入需要查询的学生ID或者姓名：")
    if name_id == "0":
        return "用户已取消查询操作，返回主菜单"

    with open("学生管理系统.txt", 'r', encoding="utf-8") as f:
        found = False  # 先设定一个寻找值

        for i in f:
            data_list = i.strip().split(' - ')
            if (name_id in data_list[0]) or (name_id in data_list[1]):
                print(f"学号：{data_list[0]}")
                print(f"姓名：{data_list[1]}")
                print(f"年龄：{data_list[2]}")
                print(f"性别：{data_list[3]}")
                print(f"地址：{data_list[4]}")
                found = True  # 找到后为True
        if not found:
            print('该学生不存在，请先添加')


def upd_stu():
    print("欢迎进入修改学生数据".center(47, '*'))
    s_id = input("请输入需要修改的学生ID：")
    if s_id == "0":
        print("用户已取消修改操作，返回主菜单")
        return
    found = False
    new_list = []
    with open("学生信息管理系统.txt", 'r', encoding='utf8') as f:
        data = f.readlines()
    for i in data:
        s_data = i.strip().split(' - ')
        if s_id == s_data[0]:
            found = True
            name = input("请输入姓名：")
            ages = input("请输入年龄：")
            # sexs = input("请输入性别：")
            addr = input("请输入地址：")
            new_line = f"{s_id} - {name} - {ages} - {addr}\n"
            new_list.append(new_line)
            print("修改完成！！！")
        else:
            new_list.append(i)
    if not found:
        print("没有改学生ID")

    with open("学生信息管理系统.txt", 'w', encoding='utf-8') as f:
        f.writelines(new_list)


def del_stu():
    print("欢迎进入删除学生数据".center(47, '*'))

    s_id = input("请输入需要删除的学生ID：")
    if s_id == "0":
        print("用户已取消删除操作，返回主菜单")
        return
    found = False
    with open("学生管理系统.txt", 'r', encoding="utf-8") as f:
        data_list = f.readlines()
    new_list = []
    for data in data_list:
        s_data = data.strip().split(' - ')
        if s_id == s_data[0]:
            found = True
            print("删除成功")
        else:
            new_list.append(data)
    if not found:
        print("该学生不存在")
    with open("学生管理系统.txt", 'w', encoding="utf-8") as f:
        f.writelines(new_list)


def main():
    print("欢迎使用学生管理系统".center(48, "-"))
    print("0.退出学生数据".center(50, '-'))
    print("1.增加学生数据".center(50, '-'))
    print("2.查询学生数据".center(50, '-'))
    print("3.修改学生数据".center(50, '-'))
    print("4.删除学生数据".center(50, '-'))

    while True:
        op = input("请输入操作选项：")
        if op == "1":
            add_stu()
        elif op == "2":
            show_stu()
        elif op == "3":
            upd_stu()
        elif op == "4":
            del_stu()
        elif op == "0":
            print("用户退出系统")
            break
        else:
            print('输入有误，请重新输入')


if __name__ == '__main__':
    main()

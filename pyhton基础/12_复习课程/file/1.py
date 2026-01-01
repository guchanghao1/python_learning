# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''


def 增加():
    print("欢迎进入新增学生信息管理系统".center(48, '*'))
    # 不能出现相同的学号出现
    try:
        with open("../../work/学生信息管理系统.txt", 'r', encoding="utf-8") as f:
            stu_data = f.readlines()
    except:
        stu_data = []

    while True:
        sid = input("请输入学号：")
        if sid == "0":
            break
        id_list = [i.split(' - ')[0] for i in stu_data]
        if sid in id_list:
            print("学号已存在，请重新输入！！！")
            break

        else:
            name = input("请输入名字：")
            ages = input("请输入年龄：")
            addr = input("请输入地址：")
            stu_info = f'{sid} - {name} - {ages} - {addr}'

            with open("../../work/学生信息管理系统.txt", 'a+', encoding="utf-8") as f:
                f.write(stu_info + "\n")
            print(f"此'{sid}'ID学生信息保存完成")


def 查询():
    print("欢迎进入查询学生信息管理系统".center(48, '*'))
    sid = input("请输入需要查找的ID：")
    if sid == "0":
        return
    with open("../../work/学生信息管理系统.txt", 'r', encoding="utf-8") as f:
        for i in f:
            data_list = i.strip().split(' - ')
            if sid in data_list:
                print(f"学号：{data_list[0]}")
                print(f"姓名：{data_list[1]}")
                print(f"年龄：{data_list[2]}")
                print(f"地址：{data_list[3]}")
                print(f"此'{sid}'ID学生信息修改完成")
                break
            else:
                print("学生信息文件不存在！！！")
                break


def 修改():
    print("欢迎进入修改学生信息管理系统".center(48, '*'))
    sid = input("请输入需要查找的ID：")
    new_list = []
    found = False
    if sid == "0":
        return

    with open("../../work/学生信息管理系统.txt", 'r', encoding='utf8') as f:
        for i in f:
            s_data = i.strip().split(' - ')
            if sid == s_data[0]:
                name = input("请输入姓名：")
                ages = input("请输入年龄：")
                addr = input("请输入地址：")
                found = True
                new_line = f"{sid} - {name} - {ages} - {addr}\n"
                new_list.append(new_line)
                print(f"此'{sid}'ID学生信息修改完成！！！")
                continue
            else:
                new_list.append(i)

        if not found:
            print("学生信息文件不存在！！！")

        with open("../../work/学生信息管理系统.txt", 'w', encoding='utf-8') as f:
            for i in new_list:
                f.write(i)


def 删除():
    print("欢迎进入删除学生信息管理系统".center(48, '*'))
    sid = input("请输入需要查找的ID：")
    found = False
    new_list = []
    if sid == "0":
        return
    with open("../../work/学生信息管理系统.txt", 'r', encoding="utf-8") as f:
        for data in f:
            id_data = data.strip().split(" - ")[0]
            if sid == id_data:
                found = True
                print(f"此'{sid}'ID学生信息删除成功")
            else:
                new_list.append(data)

        if not found:
            print("学生信息不存在！！！")
        with open("../../work/学生信息管理系统.txt", 'w', encoding="utf-8") as f:
            for i in new_list:
                f.write(i)


def main():
    print("欢迎使用学生信息管理系统".center(48, '*'))
    print("0.退出学生系统".center(50, '-'))
    print("1.增加学生数据".center(50, '-'))
    print("2.查询学生数据".center(50, '-'))
    print("3.修改学生数据".center(50, '-'))
    print("4.删除学生数据".center(50, '-'))

    while True:
        print()
        op = int(input("请输入操作选项："))

        if op == 0:
            break
        elif op == 1:
            增加()
        elif op == 2:
            查询()
        elif op == 3:
            修改()
        elif op == 4:
            删除()


if __name__ == '__main__':
    main()

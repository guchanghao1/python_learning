# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# pip install pymysql

import pymysql

# ipconfig
# ip 属于每台电脑的身份证   192.168.1.8
# 端口 ： 代表电脑上的每个软件
# 主机：localhost -- 127.0.0.1  开发测试 测试ip
# mysql 端口号：3306

# 建立连接
db = pymysql.connect(
    # host= 'localhost',
    host='127.0.0.1',  # 主机
    port=3306,
    user='root',
    password="root123",
    db="学习",
    charset='utf8'
)

# 创建一个工具
kit = db.cursor()  # 游标

# 创建表
class_sql = \
    '''
    create table if not exists 班级表(
    id int primary key not null auto_increment,
    name varchar (50)
    );
'''

kit.execute(class_sql)

student_sql = '''
    create table if not exists 学生表(
    id  int primary key not null auto_increment,
    name varchar (50),
    ages varchar (50),
    sexe varchar (50)
    );
'''
kit.execute(student_sql)

# 数据插入
"""
# 单行插入
add_data = '''insert into 学生表 values (1,"张三","18","男");'''
kit.execute(add_data)
db.commit()  # 提交

name = input("请写入你的名字：")
ages = input("请写入你的年龄：")
sexe = input("请写入你的性别：")

add_data = f'''insert into 学生表 values (0,"{name}","{ages}","{sexe}");'''
kit.execute(add_data)
db.commit()  # 提交
print("ok ----- {}".format(name))

# 多行
info_list = [
    (0, '小月月', 18, 2),
    (0, '王语嫣', 29, 1),
    (0, '李丽', 22, 2),
    (0, '赵四', 30, 1),
    (0, '周晓雯', 28, 2),
    (0, '陈明', 35, 1),
    (0, '林小玉', 19, 2),
]
for info in info_list:
    # print(info)
    data_list = '''insert into 学生表 values ("{}", "{}","{}","{}");'''.format(info[0], info[1], info[2], info[3])
    kit.execute(data_list)
    db.commit()  # 提交
"""

# 数据查询
"""
find_data = '''select * from 学生表  where  ages = '19' and sexe = "2" '''
kit.execute(find_data)  # 执行查询语句
data = kit.fetchall()  # 用工具去查询并且返回
for i in data:
    print(i)

kit.close()  # 关闭工具
db.commit()  # 数据提交
db.close()  # 关闭数据表
"""

# 数据修改
"""
up_data = '''
    update 学生表 set sexe = '女' where id=1; 
'''
kit.execute(up_data)
db.commit()
kit.close()
db.close()
"""

# 数据删除
"""
drop_data = '''
 delete from 学生表 where name = "张三";
'''
kit.execute(drop_data)
kit.close()
db.commit()
db.cursor()
"""
# 删除表格
"""
drop_data = '''
    drop table 班级表;
'''
kit.execute(drop_data)
kit.close()
db.commit()
db.cursor()
"""


# pip install sqlalchemy
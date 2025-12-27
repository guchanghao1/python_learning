# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

from create_table import student
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# 1、链接：  '数据库类型+数据库驱动://用户名:密码@mysql地址:mysql端口/数据库名字?charset=utf8'
link = 'mysql+pymysql://root:root123@127.0.0.1:3306/学习?charset=utf8'
# 引擎  ： mysql 链接
engine = create_engine(link)

# 2、工具： 游标 / 会话
dbsess = sessionmaker(bind=engine)
session = dbsess()

# 3、数据操作
'''
session.add(变量)
data =session.query(类).filter(类.字段(条件)).all()
session.query(类).filter(类.字段(条件)).update({字段:修改后的内容})
session.query(类).filter(类.字段(条件)).delete()
'''

# 增加  add() add_all()
'''
# 单条添加
user = student(0,"张三",18,'男','武汉')
session.add(user)
# 多条添加
a = student(0, "李四", 22, '男', '北京')
b = student(0, "王五", 25, '女', '上海')
c = student(0, "赵六", 19, '男', '广州')
d = student(0, "钱七", 21, '女', '深圳')
e = student(0, "孙八", 24, '男', '杭州')
f = student(0, "周九", 20, '女', '南京')
g = student(0, "吴十", 23, '男', '成都')
session.add_all([a, b, c, d, e, f, g])
print("添加成功")
'''

# 查询  query().filter()
'''
# 查询全部学生信息
data_all = session.query(student).all()
for i in data_all:
    print(i.id, i.名字, i.年龄, i.性别, i.地址)  # 实例的属性 == i.属性

# 查询年龄18到20的学生信息
data = session.query(student).filter(student.年龄.between(18,20)).all()
for i in data:
    print(i.id, i.名字, i.年龄, i.性别, i.地址)  # 实例的属性 == i.属性

# 查询性别为男的全部信息
data =session.query(student).filter(student.性别=="男").all()
data =session.query(student).filter(student.性别==2)
for i in data:
    print(i.id, i.名字, i.年龄, i.性别, i.地址)

# 排序 order_by  [asc()--升序,desc()--降序]
# 查询性别为男的信息, 并按年龄大小排序
data =session.query(student).filter(student.性别==2).order_by(student.年龄.desc())
for i in data:
    print(i.id, i.名字, i.年龄, i.性别, i.地址)

# 查询性别为男的信息, 并按年龄大小排序,然后id大小排序
data =session.query(student).filter(student.性别==2).order_by(student.年龄).order_by(student.id.desc())
for i in data:
    print(i.id, i.名字, i.年龄, i.性别, i.地址)
'''

# 修改 updata()   1.查询到信息 2.修改
'''
# 把所有的年龄改成18
session.query(student).update({'年龄': 18})

# 单个字段：把id为2的 学生名字改成 小红
session.query(student).filter(student.id == 2).update({'名字':'小红'})

# 多个字段：把id为2的学生 名字-张三 性别-女
session.query(student).filter(student.id == 2).update({'名字': '张三', '性别': '女'})
'''

# 删除 delete()
"""
# 删除id为5
session.query(student).filter(student.id == 5).delete()

# 删除周九
session.query(student).filter(student.名字 == "周九").delete()

# 清空数据表
session.query(student).delete()
"""

# 4、数据库提交+关闭
session.commit()
session.close()


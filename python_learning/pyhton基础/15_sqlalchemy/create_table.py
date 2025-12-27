# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, Enum

# 1、链接：  '数据库类型+数据库驱动://用户名:密码@mysql地址:mysql端口/数据库名字?charset=utf8'
link = 'mysql+pymysql://root:root123@127.0.0.1:3306/学习?charset=utf8'
# 引擎  ： mysql 链接
engine = create_engine(link)

# 2、写类
# 初始化
base = declarative_base()
# 创建表
class student(base):
    __tablename__ = "学生信息表"

    # 类变量  不需要传参 但是要用self
    # 字段  Column  变量  字段名  数据类型 约束条件   int -- integer  varchar -- string flaot enum
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    名字 = Column(String(50))
    年龄 = Column(Integer)
    性别 = Column(Enum('女', '男'))
    地址 = Column(String(50))

    # 初始化
    def __init__(self, id, name, ages, sexs, addr):
        self.id = id
        self.名字 = name
        self.年龄 = ages
        self.性别 = sexs
        self.地址 = addr


# 3、生成
base.metadata.create_all(engine)

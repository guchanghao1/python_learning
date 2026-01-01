# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 面向对象
'''
关于面向对象：两大核心概念 -- 类 对象   核心思想 -- 万物皆对象
关于类：  它是一个抽象的概念，定义了某一类事物应该具有的特征和行为（属性和方法） 本身只是一个定义，他是不占任何内存空间的

关于方法（行为）：方法是对象所具有的行为或功能，方法通常用于操作对象内部的属性，或者让对象执行某个动作。是定义在类中的函数，但是在面向对象中称为方法
        调用：实力对象.方法()
关于属性(特征)：属性是对象所具有的特征或状态，是存储在对象里的数据，每个对象的属性值都是独立的，修改一个对象的属性不会影响另一个对象，
        调用：实力对象.属性

关于对象/实例对象：对象是类的一个具体实体，创建一个对象的过程叫做 实例化，每个对象都有自己独立的空间，都属于类本身的类型，自定义类型对象属于可变数据类型

类：设计图
对象：房子
实例化： 建造过程
实例对象： 建好了的属于个人的房子
属性： 房子的硬装
方法： 房子的软装
'''

# 定义类
"""
class Dog:  # 定义类
    # 关于描述狗的内容

    # 公告的属性
    tui_num = 4
    has_mao = True
    has_weiba = True

    def brak(self):
        print("狗叫")

    def bite(self):
        print("咬人")

    def play(self):
        print(f"{self.name}捡球")


class Person:  # 定义类
    # 关于描述人的内容
    tui_num = 2
    has_mao = False
    has_weiba = False

    def speak(self):
        print("说话")

    def eat(self):
        print("吃饭")

    def play(self):
        print("打游戏")
"""

# 实例属性: 属于各个对象自己的
"""
# 顺序 ：自己的空间去找 --- 类空间 --- 父类
小黄 = Dog()  # 实例化 实例对象  有了一个单独的空间
小黄.bite()

# 修改实例属性，直接修改
小黄.ages = 4  # 创建实例属性，并且复制
小黄.ages = 5
print(小黄.ages)

大黄 = Dog()  # 单独的空间
大黄.ages = 6
# print(大黄.has_mao)  # 调用属性
print(大黄.ages)

# 小黄.brak = "狗不叫"
# 小黄.狗不叫()  # 会先去找小狗的bark，在这里我们实例空间的bark值把类空间的值给覆盖了，这里是狗不叫(),那么就调用不到，会报错

# 测试
大黄.brak()
"""

# self: 他代表的是实例对象本身
# 实例方法：定义在类中的函数，用于操作类的实例对象。由实例对象调用的方法称之为实例方法
"""
小黄 = Dog()
小黄.name = "小白"
小黄.play()

大黄 = Dog()
大黄.name = "大白"
大黄.play()
"""

# 实例属性
"""
class Dog:  # 定义类
    tui_num = 4
    has_mao = True
    has_weiba = True

    def info(self, name, ages, color):
        self.name = name
        self.ages = ages
        self.color = color

    def brak(self):
        print("狗叫")

    def bite(self):
        print("咬人")

    def play(self):
        print("捡球")

    def dog_info(self):
        print(f"姓名：{self.name},年龄：{self.ages},颜色：{self.color}")


小狗 = Dog()
# 第二种
小狗.info('小白', 4, '白色')

# 第一种
# 小狗.name = "小白"
# 小狗.ages = "4"
# 小狗.color = "白色"
小狗.dog_info()


大狗 = Dog()
大狗.info("大黑", 6, "黑色")

# 大狗.name = "大黑"
# 大狗.ages = "6"
# 大狗.color = "黑色"
大狗.dog_info()
"""

# 构造函数：一个特殊的方法 初始化 在创建类的 实例对象调用   就会自动调用
# __init__(self):  # 初始化
"""
class Dog:  # 定义类
    tui_num = 4
    has_mao = True
    has_weiba = True

    def __init__(self, name, ages, color):  # 显性
        print("__init__正在使用")
        self.name = name
        self.ages = ages
        self.color = color

    def brak(self):
        print("狗叫")

    def bite(self):
        print("咬人")

    def play(self):
        print("捡球")

    def dog_info(self):
        print(f"姓名：{self.name},年龄：{self.ages},颜色：{self.color}")


小狗 = Dog("小白", 4, '白色')
小狗.dog_info()
"""

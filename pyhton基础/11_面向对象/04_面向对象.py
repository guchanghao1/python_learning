# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 面向对象的四大特性
"""
封装：将属性和方法绑起来，形成一个独立的对象 ，对外部隐藏细节，只暴露接口
多态：同一个操作，不同的对象去操作，可以产生不同的结果
抽象: 隐藏复杂的细节部分，只给接口---运行
继承：允许一个类（子类/派生类）继承另一个类（父类/基类）的属性和方法。子类可以复用父类的功能，并可以扩展或重写父类的功能。提高代码的复用性
object: 是所有类的一个父类

语法结构：
class 父类:
    def 方法(self):
        pass


class 子类(父类):
    pass


s = 子类()
s.方法()

作用：
1.代码复用： 不用去写多余的代码
2.方法重写：子类要用自己的方法，那么他会直接覆盖父类的
3.功能扩展：子类新增父类没有的方法和属性

继承的类型
单继承：一个子类继承一个父类
多继承：一个子类继承多个父类  ,少用，对于整体项目来说，会被类的 整体层次 搞得异常复杂

"""

# 继承
'''
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print("年龄：", self.age)

    def say_name(self):
        print("姓名", self.name)


class Student(Person):
    def __init__(self, name, age, addr):
        Person.__init__(self, name, age)  # 必须显式调用父类的初始化方法，
        self.addr = addr

    def say_age(self):
        print("我的年龄", self.age)

    # 扩展父类没有的功能
    def info(self):
        print(f"我叫{self.name}，今年{self.age}岁，来自{self.addr}")


s = Student("李四", 20, "上海")
s.say_age()  # 子类的方法
s.say_name()  # 父类的方法
s.info()  # 子类的方法
'''

# 案例 作业
'''
class 大黄:
    def __init__(self):
        self.name = '大黄'
        self.age = 8
        self.color = "黄色"

    def bark(self):
        print("汪汪汪")

    def play(self):
        print("捡球")


class 小黄(大黄):
    def __init__(self):
        self.name = "小黄"


小黄 = 小黄()
print(小黄.name)
小黄.play()
'''
'''
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_age(self):
        print("年龄：", self.__age)


class Student(Person):
    pass


s = Student("李四", 20)
# print(s.__age)
# 获取私有属性
# s.say_age() 
# print(s._Person__age)
'''

# 多继承
'''
class A:
    def aa(self):
        print("aaa")

    def abc(self):
        print("123")


class B:
    def bb(self):
        print('bbb')

    def abc(self):
        print("456")


class C(A, B):
    def cc(self):
        print("ccc")


a = A()
b = B()
c = C()
# c.aa()
# c.bb()
# c.cc()
# c.abc()

# print(dir(object))
# print(dir(a))
# print(dir(b))
# print(dir(c))

print(B.mro())
print(C.mro())
'''
'''
class A:
    def aa(self):
        print("aaa")


class B(A, C):
    def bb(self):
        print("bbb")


class C(A):
    def cc(self):
        print("ccc")


a = A()
b = B()
c = C()

a.aa()

b.aa()
b.bb()

c.aa()
c.cc()
'''

# super()
# 有自己的功能的情况下，不进行覆盖，获取到父类的功能
"""
class A:
    def say(self):
        print("A", self)


class B(A):
    def say(self):
        # A.say(self)  # 第一种方法
        super().say()  # 第二种方法
        print("B", self)


b = B()
b.say()
"""

# 多态
"""
class Anm:
    # 抽象方法：是一个声明，我告诉你这样一个功能。但是不写，你必须给我实现，我不会告诉你怎么实现
    def Cry(self):
        pass


class Dog(Anm):
    def Cry(self):
        print("汪汪汪")


class Cat(Anm):
    def Cry(self):
        print("喵喵喵")


def Anm_cry(Anm):
    return Anm.Cry()

d = Dog()
c = Cat()

# Anm_cry(d)
# Anm_cry(c)

# 同一个操作，不同的对象去操作，可以产生不同的结果: 去函数里面调用方法
"""

# 面积和周长  三角形 矩形 圆形  求面积公式用海伦公式
"""
import math


class Shape:
    def area(self):
        pass

    def per(self):
        pass


# 圆形
class 圆形(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        c = math.pi * self.r * self.r
        return c

    def per(self):
        c = math.pi * self.r * 2
        return c


class 矩形(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        r = self.w * self.h
        return r

    def per(self):
        r = (self.w + self.h) * 2
        return r


# 多态使用  统一的接口  处理的数据不同
def info(Shape):   # 接口
    print(f"面积:{Shape.area()}")
    print(f"周长:{Shape.per()}")


info(圆形(5))
info(矩形(20, 30))

"""

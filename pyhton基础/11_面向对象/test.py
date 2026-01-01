# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 简单的计算器
"""
a = int(input())
b = int(input())
op = input()

if op == '+':
    c = a + b
    print(c)
elif op == '-':
    c = a - b
    print(c)
elif op == '*':
    c = a * b
    print(c)
elif op == '/':
    c = a / b
    print(c)
else:
    print("输入错误！！！")
"""

# 面向对象案例：计算器
"""
class Jsq:
    def __init__(self):
        self.结果 = 0
        self.计算历史 = []

    def add(self, a, b):
        self.结果 = a + b
        self.计算历史.append(f"{a}+{b}={self.结果}")
        return self.结果

    def sub(self, a, b):
        self.结果 = a - b
        self.计算历史.append(f"{a}-{b}={self.结果}")
        return self.结果

    def mul(self, a, b):
        self.结果 = a * b
        self.计算历史.append(f"{a}*{b}={self.结果}")
        return self.结果

    def div(self, a, b):
        if b != 0:

            self.结果 = a / b

            self.计算历史.append(f"{a}/{b}={self.结果}")
            return self.结果
        else:
            print("被除数不能为0")

    def show_计算历史(self):
        if not self.计算历史:
            return "还没有记录"

        return "\n".join(self.计算历史)


计算器 = Jsq()
print(计算器.add(4, 5))
print(计算器.sub(6, 3))
print(计算器.mul(6, 3))
print(计算器.div(6, 3))

print("计算历史")
print(计算器.show_计算历史())
"""

# 购物车
"""
class Shopping:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item_name, price):
        self.items.append(item_name)

        self.total += price
        # self.total = self.total + price

        return "购物车已添加{}，单价是{}".format(item_name, price)

    def check(self):
        if not self.items:
            return "购物车是空的"
        res = "购买了{}，总额是{}".format(self.items, self.total)
        return res


shop = Shopping()
shop.add_item("苹果", 5)
shop.add_item("梨子", 6)

print(shop.check())
"""

# 作业：做判断，如果id = user并且pad = password，那么才可以去访问我的余额，不然访问不到
"""
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

        # 正确的账户名和密码
        self.__id = "admin"
        self.__password = '123456'

    def __money(self):
        self.__money = '8000'
        print("您的余额是：{}".format(self.__money))

    def get_money(self):
        if self.name == self.__id and self.pwd == self.__password:
            self.__money()
        else:
            print("账号或者密码错误！！！！")


name = input("请输入你的账户名：")
pwd = input("请输入你的密码：")

a = User(name, pwd)
a.get_money()
"""

# 求面积和周长  三角形 根号math.sqrt() 求面积公式用海伦公式
# 写一个继承的类
'''
A、利用 Python 创建一个类 Bag，其成员包括实例属性 category (种类) 和 color (颜色)，
    实例方法 showInfo用来输出实例属性 category 和 color 的值;

B、创建派生类 Backpack，继承Bag 类，新增实例属性 size(尺寸)，
    重写基类的实例方法 showInfo 输出所有实例属性的值
'''

# 购买背包的款式
"""
class Bag:
    def __init__(self, category, color):
        self.category = category
        self.color = color

    def showInfo(self):
        print("这是一个{}，它是{}的".format(self.category, self.color))


class Backpack(Bag):
    def __init__(self, category, color, size):
        Bag.__init__(self, category, color)
        self.size = size

    def showInfo(self):
        print("这是一个{}，它是{}的,它是一个{}的".format(self.category, self.color, self.size))


mybug = Backpack('书包', '白色', '中号')
mybug.showInfo()
"""

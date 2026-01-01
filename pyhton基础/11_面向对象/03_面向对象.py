# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 熊猫福宝
"""
class 熊猫福宝:
    def __init__(self):
        self.color = "黑白色"
        self.sex = "雌性"
        self.addr = "四川"
        self.sleeps = "坐着睡觉"

    def eat(self, food):
        return "福宝正在吃{}".format(food)

    def play(self, fun):
        return "福宝正在玩{}".format(fun)

    def sleep(self):
        return f"福宝正在{self.sleeps}"


pandas = 熊猫福宝()
print(pandas.eat("竹子"))
print(pandas.play("爬树"))
print(pandas.sleep())
"""

# 类对象
"""
class Car:   # 类对象
    num_cars = 0  # 类变量

    def __init__(self, make):
        self.汽车品牌 = make
        Car.num_cars += 1

    def come(self):
        print(f"一辆{self.汽车品牌}正在出现")


car1 = Car("奔驰")
car1.come()

car2 = Car('宝马')
car2.come()

car3 = Car('丰田')
car3.come()

print(Car.num_cars)    # 修改类变量
"""

# 变量
'''
1 - 实例变量：属于特定对象实例的变量，每个对象都拥有自己独立的一份实例变量，修改一个对象的实例变量不会影响其他对象。
            需要带self，不需要传参

2 - 普通变量(局部变量)：在函数或方法内部定义的变量，在函数内部直接定义和使用
                    不需要带self，需要传参

3 - 类变量：类的里面 方法的外面定义的, 属于类本身的变量，被所有实例共享。一个对象对类变量的修改，其他对象也会看到这个变化。  
            不需要传参，但使用需要用到self 去获取值



4 - 全局变量：在模块级别定义的变量。它的作用域是整个模块，在模块内的任何函数、类中都可以访问。
   在函数和类之外定义。在函数或类方法内部如果要修改全局变量，需要使用 global 关键字声明。
   类外面的变量，可以被所有使用，不需要传参但是不能改变
'''
"""
global_var = "全局变量"


class 变量:
    class_var = "类变量"  # 类的里面 方法的外面定义的
    a = 1
    b = 2

    def __init__(self):  # 构造方法，特殊方法 初始化
        self.class_var_init = "我是初始化中的---- {}".format(self.class_var)
        self.init_var = "实例变量"  # 用self在方法里面定义的变量

        self.global_var_init = "我是初始化中的---- {}".format(global_var)

    def 自定义方法(self):
        class_var_method = "我是自定义方法中的---- {}".format(self.class_var)
        # print(class_var_method)
        
        init_var_method = "我是自定义方法中的---- {}".format(self.init_var)
        # print(init_var_method)
        
        common_var = "普通变量"  # 直接在方法里面定义的
        self.传参(common_var)  # 传进来
        
        global_var_method = "我是自定义方法中的---- {}".format(global_var)
        # print(global_var_method)

    def 传参(self, common_var):  # 接收
        # print('传参---{}'.format(common_var))  # 使用
        print("我是{}，我是{}，我是{}".format(self.class_var, self.init_var, common_var))


实例对象 = 变量()  # 实例对象

# 类变量
# print(实例对象.class_var)  # 在外面的类变量
# print(实例对象.class_var_init)  # 在初始化的类变量
# print(实例对象.自定义方法())  # 在自定义中的类变量
#
# print(实例对象.init_var)
# print(实例对象.自定义方法())  # 在自定义中的实例变量

实例对象.自定义方法()
print(实例对象.global_var_init)
"""

# 案例
"""
company = "爱心宠物之家"
class Dog:
    # 这里是类变量
    A = "犬科动物"
    total = 0

    def __init__(self, name, breed):  # 自动执行
        # 这是实例变量
        self.name = name
        self.breed = breed
        Dog.total += 1

        # 使用到了   实例变量和      全局变量和       类变量
        print(f"你好{name},欢迎来到{company},你是第{Dog.total}只来的小狗")

    def bark(self):
        # 使用实例变量
        print(f"{self.name} 汪汪叫")
        print(f"{self.name}它是一直{self.breed}")

    def birthday(self, age):
        # 普通变量
        ages = age
        print(f"{self.name}今天{ages}岁了")


dog = Dog("小黄", "中华田园犬")
dog.bark()
dog.birthday(4)
"""

# 公有属性：普通形式的变量名
# 受保护的属性：在前面加上'_'
# 私有属性：在前面加上 '__'
"""
class User:
    def __init__(self):
        self.name = "张三"  # 共有属性
        self._ages = 20  # 一个下划线，其实在提示我们 不要再类的外面去访问
        self.__pwd = '123456'  # 实例变量的私有属性
        __aaa = '12345678'  # 普通变量的私有属性

    def password(self):   # 访问私有属性，给了一个接口去访问
        print(self.__pwd)  # 访问的是属性


张三 = User()
print(张三.name)
print(张三._ages)  # 不建议
# print(张三.__pwd)  # AttributeError: 'User' object has no attribute '__pwd'
# print(张三.__aaa)  # AttributeError: 'User' object has no attribute '__aaa'
张三.password()
"""


# 公有方法:普通形式的变量名
# 私有方法:在前面加上 '__'
"""
class User:
    def __init__(self, name, pwd):
        self.user = name
        self.pwd = pwd

    # 公有方法
    def users(self):
        self.id = "zhangsan"
        self.password = '123456'
        print(self.id, self.password)

    # 私有方法
    def __money(self):
        self.money = "8000"
        print(self.money)

    def get_money(self):
        self.__money()  # 这里访问的是方法


张三 = User("zhangsan", '123456')
张三.users()

# 张三.__money()  # AttributeError: 'User' object has no attribute '__money'
张三.get_money()
"""



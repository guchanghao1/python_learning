# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

# 函数性质：
"""
定义： def 
调用： 函数名()
返回值： 终止函数代码的执行，以及函数的结果 默认是None
"""

# 函数模板
"""
def main():
    return 'ok'   # 结果


if __name__ == '__main__':
    print(main())
    
    a = main()
    print(a)
"""

# 函数练习1
"""
def 高考():
    print("一模：400分")
    print("二模：500分")
    print("三模：600分")
    return "高考分是700"


print(高考())

"""

# 函数练习2
"""
def main():
    def A():
        # print("666")  # A函数的过程
        return 666

    return A()


if __name__ == '__main__':
    print( main() )
"""

# 函数练习3
"""
def main():
    def A():
        def B():
            def C():
                print("999")

            return C

        return B

    return A

if __name__ == '__main__':
    A = main()
    B = A()
    V= B()
    V()

    # main( A( B( C() ) ) )
"""

# 函数案例：完善列表执行
"""
# a_list = [1, 2, 3, 4]
# b_list = [5, 6, 7, 8, 9]
#
# if len(a_list) == len(b_list):
#     res = [a + b for a, b in zip(a_list, b_list)]
#     print(res)
# else:
#     print("长度不一致")


def 判断长度(a_list, b_list):
    if len(a_list) == len(b_list):
        return True

    else:
        return False


def 计算(a_list, b_list):
    res = [a + b for a, b in zip(a_list, b_list)]
    return res


def main():
    a_list = [1, 2, 3, 4]
    b_list = [5, 6, 7, 8]

    if 判断长度(a_list, b_list) == True:
        res = 计算(a_list, b_list)
        return res
    else:
        return "长度不一致"


if __name__ == '__main__':
    A = main()
    print(A)
"""

# 函数案例：判断数字是否是质数   >=2  只有 1 和 本身
"""
def is_质数(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False

        else:
            return True


if __name__ == '__main__':
    num = 2
    if is_质数(num) == True:
        print("是质数")
    else:
        print("不是质数")
"""

# 函数案例：求1 -100质数
"""
def is_质数(num):
    if num < 2:
        return False

    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True


if __name__ == '__main__':
    for num in range(1, 101):
        if is_质数(num) == True:
            print(num)
"""

# 编写一个函数，判断一个数字是偶数还是奇数，返回 "Even" 或 "Odd"
"""
def number(num):
    if num % 2 == 0:
        return "Even！"
    else:
        return "Odd!"


if __name__ == '__main__':
    num = int(input("请输入一个整数："))
    print(number(num))
"""

# 编写一个函数，计算并返回一个列表中所有数字的平均值
"""
def avg(number):
    data = [eval(i) for i in number]
    s = sum(data) / len(data)
    return s


n = 5
number = [input("请输入第{}个数：".format(i)) for i in range(1, n + 1)]
print(avg(number))

"""

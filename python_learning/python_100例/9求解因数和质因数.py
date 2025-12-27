# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
''''''

'''
# 判断是否为质数
def is_prime(num):
    if type(num) != int:
        return False
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 获取因数
def get_factor(num):
    factor = 2
    yield 1
    yield num  # 相当于特殊的return
    org_num = num  # 存储原值
    while factor * factor <= num:
        while not num % factor:
            yield factor
            num //= factor
            if num > 1:
                yield num
        num = org_num  # 把原值还回去
        factor += 1


# 获取质因数
def get_pf(num):
    list_prime = []
    factor = 2
    if is_prime(num):
        list_prime.append(num)
        return list_prime
    org_num = num
    while factor * factor <= num:
        while num % factor == 0:
            num //= factor
            if is_prime(factor):
                list_prime.append(factor)
            if is_prime(num):
                list_prime.append(num)
        num = org_num
        factor += 1
    return list_prime


if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    list_factor = get_factor(num)
    list_factor = list(set(list_factor))
    list_factor.sort()
    print(f'整数{num}的因数{list_factor}')
    for i in list_factor:
        p_f = get_pf(i)
    new_list = list(set(p_f))
    new_list.sort()
    print(f'整数{num}的质因数{new_list}')
'''


# 判断是否为质数
def is_prime(num):
    if type(num) != int or num < 1:
        return False
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 获取所有因数
def get_factor(num):
    factors = set()
    factors.add(1)
    factors.add(num)

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)

    return sorted(factors)


# 获取质因数分解
def get_pf(num):
    list_prime = []
    temp = num
    factor = 2

    while factor * factor <= temp:
        while temp % factor == 0:
            list_prime.append(factor)
            temp //= factor
        factor += 1

    if temp > 1:
        list_prime.append(temp)

    return list_prime


if __name__ == '__main__':
    num = int(input('请输入正整数：'))

    # 获取所有因数
    list_factor = get_factor(num)
    print(f'整数{num}的因数: {list_factor}')

    # 获取质因数分解
    prime_factors = get_pf(num)
    print(f'整数{num}的质因数分解: {prime_factors}')

    # 获取所有质因数（去重）
    unique_prime_factors = list(set(prime_factors))
    unique_prime_factors.sort()
    print(f'整数{num}的唯一质因数: {unique_prime_factors}')

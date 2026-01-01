# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------

'''yield 生成器与迭代器的用法'''
"""
def test():
    print('测试程序开始！')
    first_rec = yield 1
    print(f'第一次收到内容:{first_rec}')
    first_rec = yield 2
    print(f'第二次收到内容:{first_rec}')
    first_rec = yield 3
    print(f'第三次收到内容:{first_rec}')
    yield 666
    


if __name__ == '__main__':
    rec = test()
    value0 = next(rec)
    value1 = rec.send('第一次发送')
    value2 = rec.send('第二次发送')
    value3 = rec.send('第三次发送')

    print(value0, value1, value2, value3)
"""


# 读取大文本文件
"""
def read_file(file_addr):
    read_number = 1024
    with open(file_addr, 'rb')as file:
        while True:
            content = file.read(read_number)
            if content:
                yield content
            else:
                return


if __name__ == '__main__':
    file1 = read_file('D:\Python\python_test\基础班课程笔记\爬虫\练习\搜狗图片\如果你想成为一个有钱人,你必须做出正确的选择.jpg')
    n = 0
    for i in file1:
        n += 1
        print(f'这是第{n}次迭代')
        print(i)
"""


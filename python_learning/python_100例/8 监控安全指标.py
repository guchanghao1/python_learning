# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import time


def read_lastdata(file_addr):
    with open(file_addr, 'r', encoding='utf-8')as file:
        last = file.seek(0, 2)
        while True:
            last_data = file.readline()
            if not last_data:
                time.sleep(1)
                continue
            yield last_data


def show(last_data):
    list_data = last_data.split(',')
    if (list_data[3] == '瓦斯' or list_data[3] == 'CO') and (list_data[5] == '越上限报警'):
        print(f'警告！！！{list_data[0]}{list_data[3]}')
    if (list_data[3] == '瓦斯' or list_data[3] == 'CO') and (list_data[5] == '警报解除'):
        print(f'警报解除-{list_data[0]}{list_data[3]}')


if __name__ == '__main__':
    message = read_lastdata('文本分词计数.txt')
    for information in message:
        show(information)

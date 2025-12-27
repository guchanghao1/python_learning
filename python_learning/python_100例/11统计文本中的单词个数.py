# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import re


class Counterword(object):
    def __init__(self, file_nmae):
        self.file_name = file_nmae
        self.cou_dict = {}

    def count_num(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                words = [s.lower() for s in re.findall('\w+', line)]
                # 使用正则表达式 \w+ 匹配 line 中的所有单词，\w 匹配字母、数字和下划线（相当于 [a-zA-Z0-9_]）+ 表示匹配一个或多个连续的 \w 字符返回一个包含所有匹配单词的列表
                for word in words:
                    self.cou_dict[word] = self.cou_dict.get(word, 0) + 1
                    """等价如下"""
                    # if word in self.cou_dict:
                    #     self.cou_dict[word] += 1
                    # else:
                    #     self.cou_dict[word] = 1

    def top(self, num):
        return sorted(self.cou_dict.items(), key=lambda item: item[1], reverse=True)[1:num + 1]


if __name__ == '__main__':
    cou_word = Counterword('文本分词计数.txt')
    cou_word.count_num()
    top_num = cou_word.top(5)
    for i in top_num:
        print(i)

# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import re


# text = "The rapid advancement of technology, especially in Artificial Intelligence (AI), " \
#        "is reshaping our world. From self-driving cars to virtual assistants like Siri and " \
#        "Alexa, AI is everywhere! However, we must ask: are we prepared for these changes? It's" \
#        " a double-edged sword; it offers incredible convenience but also poses significant challenges. " \
#        "We need to ensure that this technology benefits all of humanity, not just a privileged few. Let's " \
#        "work towards a future where humans and machines collaborate harmoniously."
# with open('文本分词计数.txt', 'w', encoding='utf-8') as t:
#     t.write(text)
def get_char(txt):
    vltx = re.split('[:;,."\s]\s*', txt)  # 正则表达式，需要学习
    dic = dict()  # 空字典
    for i in vltx:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic_sorted = sorted(dic.items(), key=lambda item: item[1], reverse=True)  # sorted函数的运用
    return dic_sorted


if __name__ == '__main__':
    with open('文本分词计数.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
        result = get_char(txt)
        print(result[:-1])  # 切片

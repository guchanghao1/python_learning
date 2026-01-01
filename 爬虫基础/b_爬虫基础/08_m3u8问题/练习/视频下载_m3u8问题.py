# !/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
# ----------------------------------------------------------------------------------------------------------------------
import os
import requests
import time

url_all = 'https://vip.lzcdn2.com/20220318/7_a4fcd924/1200k/hls/mixed.m3u8'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
}

res_all = requests.get(url_all, headers=headers)

id_all_list = res_all.text.split('\n')

if not os.path.exists('豆瓣电影top'):
    os.mkdir('豆瓣电影top')

turn = 1
for id_num in id_all_list:

    if (".ts"in id_num) and ("00" in id_num):  # ''不行，”“可以
        print(id_num)
        url_ts = f'https://vip.lzcdn2.com/20220318/7_a4fcd924/1200k/hls/{id_num}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        }
        try:
            res_ts = requests.get(url_ts, headers=headers)
            data = res_ts.content
        except Exception as e:
            print(e)
            time.sleep(60)

        with open('豆瓣电影top/电影：肖申克的救赎.mp4', 'ab') as f:
            f.write(data)
            time.sleep(0.5)
            print(turn)
            turn += 1

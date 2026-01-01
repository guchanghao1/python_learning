# https://quotes.toscrape.com/           第1页
# https://quotes.toscrape.com/page/1/    第1页
# https://quotes.toscrape.com/page/2/    第2页
# ......
# https://quotes.toscrape.com/page/10/    第10页
# https://quotes.toscrape.com/page/11/    没有我要的数据

# 一页有10条 名人名言
# 总共有10页


import requests
from lxml import etree

Dictum = []  # 名言
celebrity = []  # 名人


def get_data(page):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "priority": "u=0, i",
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url, headers=headers)

    html = etree.HTML(response.text)

    # 用xpath解析
    # <span class="text"
    text_list = html.xpath('//span[@class="text"]/text()')  # 名言
    # <small
    auth_list = html.xpath('//small[@itemprop="author"]/text()')  # 作者

    # 找Next 下一页
    next = html.xpath('//ul[@class="pager"]/li[@class="next"]/a/text()')
    print(next)

    for text, auth in zip(text_list, auth_list):
        Dictum.append(text)
        celebrity.append(auth)
        print(f'名言是：{text},作者是：{auth}')

    return next


# 思路
# 死循环
# 先抓数据，
# 再判断页面上有没有Next，
# 没有就不抓
# break 跳出循环
page = 1
while True:
    print(f'----------开始下载第{page}页----------')
    # 如果是1-9页 flag = ['Next ']  否则 flag=[]
    flag = get_data(page)  # 先抓
    page += 1

    # 再判断
    if flag == []:
        break

# 第1次循环 page=1    抓数据   page=2    flag = ['Next ']    条件不成立  接着循环
# 第10次循环 page=10  抓数据   page=11   flag=[]             条件成立  break


result = {"名言": Dictum, "名人": celebrity}

import pandas

pd = pandas.DataFrame(result)
pd.to_excel("名人名言.xlsx", index=False)

# 作业 爬名人名言 保存到Excel中！


# https://image.baidu.com/search/acjson?tn=resultjson_com&word=%E8%B5%B5%E4%B8%BD%E9%A2%96&ie=utf-8&fp=result&fr=&ala=0&applid=10605110429382764690&pn=30&rn=30&nojc=0&gsm=1e&newReq=1

import requests
import uuid
import os

word = input("你要爬什么？")
page = int(input("你要爬几页？"))
if not os.path.exists(word):
    os.mkdir(word)

#  第一次循环 i=0  第二次循环i=1  第三次循环i=2
#  第一次循环 pn=0  第二次循环pn=30  第三次循环pn=60

for i in range(0,page):
    print(f'----------开始爬取第{i+1}页----------')
    params = {
        'word': word,
        'pn': str(i*30),  # 第一页0 第二页30 第三页60
        'rn': '60',  # 每一页有30张图片  一页必须<=60张
        'newReq': '1'
    }

    url = 'https://image.baidu.com/search/acjson'

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'accept-language':'zh-CN,zh;q=0.9'
    }

    res = requests.get(url,headers=headers,params=params)

    img_list = res.json()['data']['images']
    print(len(img_list))
    for i in img_list:
        url = i['thumburl']  # 图片的链接
        unique_id = uuid.uuid4()  # 图片的名称
        id_str = str(unique_id)

        # 保持图片
        res = requests.get(url).content
        with open(f'{word}/{id_str}.JPEG','wb') as f:
            f.write(res)
        print(f'{word}-下载完成')
        # break
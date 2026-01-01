import math


# https://www.kuwo.cn/singer_detail/1062
def test():
    total = 1041
    #  一页有20首单曲
    page = math.ceil(total / 20)  # 向上取整数
    print(page)


import requests


# 1、首先获取到这个歌手的页数
def get_page(id):
    params = {
        "artistid": id,  # 歌手id
        "pn": "1",  # 第1页
        "rn": "20",  # 每一页的数量
        "httpsStatus": "1",
        "reqId": "0f32aec0-e31a-11f0-b9d3-27e23c5b7d23",
        "plat": "web_www",
        "from": ""
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    total = response.json()['data']['total']
    page_total = math.ceil(total / 20)  # 总页数
    print(f'总共有{total}首歌曲，总共有{page_total}页')
    get_all_page_data(page_total,id)


# 2、获取每一页的数据
def get_all_page_data(page_total,id):
    for page in range(1, page_total + 1):
        print(f'----------开始获取第{page}页----------')
        params = {
            "artistid": id,  # 歌手id
            "pn": str(page),  # 第page页
            "rn": "20",  # 每一页的数量
            "httpsStatus": "1",
            "reqId": "0f32aec0-e31a-11f0-b9d3-27e23c5b7d23",
            "plat": "web_www",
            "from": ""
        }
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        data_list = response.json()['data']['list']

        for data in data_list:
            name = data['name']
            release_time = data['releasedate']
            time = data['songTimeMinutes']
            print(f'歌曲是：{name}，发布时间是：{release_time}，时长：{time}')


if __name__ == "__main__":
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://www.kuwo.cn/singer_detail/5371",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Secret": "5328f3d248702a6de65fc3e67ff0f71f7cac9cb26dabc47479cd1dabf5cb2dc800f7ff93",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "_ga": "GA1.2.2047039925.1766833751",
        "_gid": "GA1.2.2059329972.1766833751",
        "Hm_lvt_cdb524f42f0ce19b169a8071123a4797": "1766833750,1766835082",
        "HMACCOUNT": "34F1CD1E408C916F",
        "Hm_lpvt_cdb524f42f0ce19b169a8071123a4797": "1766836063",
        "_ga_ETPBRPM9ML": "GS2.2.s1766833750$o1$g1$t1766836063$j60$l0$h0",
        "Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324": "pxxpYWBF8zcw4JF2tcmeZQXspMf2sMHD"
    }
    url = "https://www.kuwo.cn/api/www/artist/artistMusic"
    # 请输入歌手的id
    id = input("请输入歌手的id:")
    get_page(id)
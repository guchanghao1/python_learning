# https://dmfengche.cc/ 风车动漫

import requests, os

if not os.path.exists("阿凡达"):
    os.mkdir("阿凡达")

# 1、获取每一个片段的id
# url = "https://vip.lz-cdn14.com/20230415/21857_c0c5bc6b/2000k/hls/mixed.m3u8"  # 新宝可梦
url = "https://vip.lzcdn2.com/20220318/25_6073fde1/1200k/hls/mixed.m3u8"  # 阿凡达
res = requests.get(url)
# 如何过滤出片段的id？
# 1、以换行分割这个字符串
id_list = res.text.split("\n")

# 2、遍历这个列表,把符合条件的打印出来
index = 1
for id in id_list:
    # 3、如果".ts"包含在元素中，就打印
    if ".ts" in id:
        print(f"----------开始下载第{index}个片段----------")
        # 4、拼接完整的片段地址
        # ts = f"https://vip.lz-cdn14.com/20230415/21857_c0c5bc6b/2000k/hls/{id}"  # 新宝可梦的片段地址
        ts = f"https://vip.lzcdn2.com/20220318/25_6073fde1/1200k/hls/{id}"  # 阿凡达的片段地址

        # 5、追加写入到文件中   a 表示追加
        with open(f'阿凡达/阿凡达.mp4', 'ab') as f:
            f.write(requests.get(ts).content)

        index += 1

# 作业  去下载一个你喜欢的电影或者动漫

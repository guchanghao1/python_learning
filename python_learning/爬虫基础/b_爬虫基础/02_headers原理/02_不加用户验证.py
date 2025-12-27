import requests
import os

# 如果img文件夹不存在，就创建
if not os.path.exists('img'):
    os.mkdir('img')

# 在图片上右键  点复制图片地址
url = 'https://pic.qqans.com/up/2024-6/17183287193742704.jpg'
url = 'https://pic.qqans.com/up/2024-6/17183287197107817.jpg'

res = requests.get(url)
print(res.status_code)
# print(res.content)  # 200 成功

with open('img/1.jpg', 'wb') as f:
    f.write(res.content)

'''
例子 ：
有人 向你 借钱
如果 这个人 不亮明身份 肯定不接

总结：
服务器 原则上 只会给浏览器返回数据
爬虫  是一个代码  不是真正的浏览器
原则上 服务器 是不会给爬虫 返回数据的


有两种情况：
1、有的服务器比较简单，不去验证用户的信息
2、有的服务器比较严格，需要验证用户的信息
'''

# 图片格式是计算机存储图片的格式，
# 常见的存储的格式有 bmp，jpg，png，tif，gif，pcx，tga，exif，fpx，svg，psd，cdr，pcd，dxf，ufo，eps，ai，raw，WMF，webp，avif，apng 等。

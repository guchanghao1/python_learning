import requests
import os

res = requests.get('https://pvp.qq.com/zlkdatasys/heroskinlist.json')
data_json = res.json()
pflb = data_json['pflb20_3469']  # 皮肤列表
yxlb = data_json['yxlb20_2489']  # 英雄列表

for i in pflb:
    yx_name = i['yxmclb_9965']  # 英雄名称
    pf_name = i['pfmclb_7523']  # 皮肤名称
    pf_url = i['fmlb_4536']  # 皮肤链接

    if not os.path.exists(f'王者荣耀/{yx_name}'):
        os.makedirs(f'王者荣耀/{yx_name}')

    with open(f'王者荣耀/{yx_name}/{pf_name}.jpg', 'wb') as f:
        f.write(requests.get(pf_url).content)

    print(f'{yx_name} {pf_name}.jpg 下载成功')

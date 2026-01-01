import requests
import os

if not os.path.exists('英雄联盟'):
    os.mkdir('英雄联盟')

class LOL:
    def __init__(self):
        self.url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2943148'
        self.url_detail = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2943148'

    def get_data(self):
        hero = requests.get(self.url).json()['hero']
        for i in hero:
            heroId = i['heroId']
            yx_name = i['name']

            print(f'----------开始下载{yx_name}的皮肤----------')
            self.get_detail(heroId,yx_name)
            # break

    def get_detail(self,heroId,yx_name):

        if not os.path.exists(f'英雄联盟/{yx_name}'):
            os.makedirs(f'英雄联盟/{yx_name}')  # makedirs 创建多层路径

        skins = requests.get(self.url_detail.format(heroId)).json()['skins']
        for i in skins:
            pf_name = i['name']
            mainImg = i['mainImg']
            if mainImg != '':
                # 保存皮肤
                res = requests.get(mainImg).content
                with open(f'英雄联盟/{yx_name}/{pf_name}.jpg','wb') as f:
                    f.write(res)

                print(f'{pf_name}.jpg下载成功')
            # break










if __name__ == '__main__':
    lol = LOL()
    lol.get_data()
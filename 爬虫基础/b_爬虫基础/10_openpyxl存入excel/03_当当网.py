import requests,os
from lxml import etree
from openpyxl.workbook import Workbook
from urllib.parse import quote

if not os.path.exists("当当网"):
    os.mkdir("当当网")

wb = Workbook()
sheet = wb.active
sheet.append(["书名", "价格", "时间", "简介", "出版社"])

keyword = input("请输入关键字：")
key = quote(keyword, encoding='gbk')
print(key)  # %B0%AE%C7%E9

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "$ddscreen": "2",
    "__permanent_id": "20251230203059826269807400051901740",
    "__visit_id": "20251230203059827200193386702141325",
    "__out_refer": "1767097860%7C\\u0021%7Cwww.baidu.com%7C\\u0021%7C",
    "__rpm": "s_112100.155956512835%2C155956512836..1767098054522%7Cs_112100.94003212839%2C94003212840.1.1767098092858",
    "pos_0_start": "1767098327962",
    "pos_9_end": "1767098328021",
    "ad_ids": "88414785%2C3312392%2C49391241%2C49391208%2C65565325%2C2041689%2C2035199%7C%234%2C5%2C4%2C5%2C5%2C4%2C6",
    "pos_0_end": "1767098328212",
    "search_passback": "3b59114a6894d2e3edc75369fc010000fd40670020c75369",
    "__trace_id": "20251230203911042196855290827468142"
}

for page in range(1, 101):
    print(f"----------开始爬取第{page}页----------")
    url = f"https://search.dangdang.com/?key={key}&act=input&page_index={page}"

    response = requests.get(url, headers=headers, cookies=cookies)

    html = etree.HTML(response.text)

    # ul class="bigimg"
    li_s = html.xpath('//ul[@class="bigimg"]/li')
    for li in li_s:
        书名 = li.xpath('.//a/@title')[0]
        价格 = float(li.xpath('.//p[@class="price"]/span[1]/text()')[0].replace("¥", ""))

        时间 = li.xpath('.//p[@class="search_book_author"]/span[2]/text()')  # [' /2025-06-01']
        出版时间 = "".join(时间).replace("/", "").strip()  # 2025-06-01
        出版时间 = 出版时间 if 时间 != [] else "无时间"

        出版社 = li.xpath('.//p[@class="search_book_author"]/span[3]/a/text()')  # ['太白文艺出版社']
        最终出版社 = "".join(出版社)
        最终出版社 = 最终出版社 if 出版社 != [] else "无出版社"

        简介 = li.xpath('.//p[@class="detail"]/text()')
        最终简介 = "".join(简介)
        最终简介 = 最终简介 if 简介 != [] else "无简介"

        sheet.append([书名, 价格, 出版时间, 最终简介, 最终出版社])

wb.save(f"当当网/{keyword}.xlsx")


# 爬取当当网 你感兴趣的书籍信息 然后保存到excel

# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import openpyxl
from openpyxl.drawing.image import Image
import warnings  # 警告

warnings.filterwarnings('ignore')  # 出现警告就忽略+
img = Image('D:\Python\python_test\基础班课程笔记\爬虫\练习\搜狗图片\如果你想成为一个有钱人,你必须做出正确的选择.jpg')  # 创建对象
wb = openpyxl.load_workbook('./emp.xlsx')
ws = wb.get_sheet_by_name('Sheet1')
ws.add_image(img, 'P2')
wb.save('./emp.xlsx')

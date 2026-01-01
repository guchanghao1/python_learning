# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
from PyPDF2 import PdfFileWriter, PdfFileReader


def create_watermark(pdf_watermark, pdf_org, pdf_result):
    watermark = PdfFileReader(pdf_watermark)  # 读取水印文件
    water_page = watermark.getPage(0)  # 水印文件的第一页
    v_reader = PdfFileReader(pdf_org)
    n_page = len(v_reader.pages)  # 获取待加水印的pdf的总页数
    # 生成新的pdf文件
    v_writer = PdfFileWriter()
    for i in range(n_page):
        one_page = v_reader.getPage(i)
        one_page.merge_page(water_page)
        # 合并完成后写入新的pdf文件中
        v_writer.add_page(one_page)
    with open(pdf_result, "wb") as file:
        v_writer.write(file)  # 将v_writer中的数据写入file


if __name__ == '__main__':
    create_watermark('', '', '')
    # 把水印当成原文件，这样不会把文字挡住

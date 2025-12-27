# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import PyPDF2
import os


def create_path(path_name):
    if not os.path.exists(path_name):
        os.makedirs(path_name)  # 多级目录


def get_filename(path):
    lit_filename = []
    for filename in os.listdir(path):
        if filename.endswith('.pdf'):
            filename_full = os.path.join(path, filename)
            lit_filename.append(filename_full)
    return lit_filename


def set_psd(lst_file, out_path, passwd):
    create_path(out_path)
    for file in lst_file:
        file_obj = open(file, 'rb')
        pdf_read_obj = PyPDF2.PdfFileReader(file_obj)
        pdf_write_obj = PyPDF2.PdfFileWriter()
        for page_num in range(len(pdf_read_obj.pages)):
            page_obj = pdf_read_obj.pages[page_num]
            pdf_write_obj.addPage(page_obj)  # 获取一页，就向对象中添加一页
        pdf_write_obj.encrypt(passwd)
        filename = file.split('\\')[-1]
        file_out = open(os.path.join(out_path, filename), 'wb')
        pdf_write_obj.write(file_out)
        file_obj.close()
        file_out.close()


if __name__ == '__main__':
    files = get_filename('')
    out_path = ''
    set_psd(files, out_path, "")

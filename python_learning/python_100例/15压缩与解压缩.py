# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import os, zipfile


def get_zipinfo(zipfile_name):
    zfile_obj = zipfile.ZipFile(zipfile_name, 'r')
    zipfile_info = zfile_obj.infolist()
    zfile_obj.close()
    return zipfile_info


def zip_file(path):
    zipname = os.path.basename(path) + '.zip'
    zipfile_obj = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    print('正在压缩文件')
    # 将文件、文件夹压缩
    for cur_dir, lst_dir, lst_file in os.walk(path, topdown=False):
        for dir_file_nmae in lst_dir:
            dirname = os.path.join(path, dir_file_nmae)
            zipfile_obj.write(dirname)
        for dir_file_nmae in lst_file:
            filename = os.path.join(path, dir_file_nmae)
            zipfile_obj.write(filename)
        zipfile_obj.close()


def extract_zipfie(path):
    zfile_obj = zipfile.ZipFile(path, 'r')
    zfile_obj.extractall()
    zfile_obj.close()


if __name__ == '__main__':
    path_path = input('请输入地址：')
    zip_name = input('请输入压缩文件名称')
    zip_file(path_path)
    zip_info = get_zipinfo(zip_name)
    for info in zip_info:
        print(f'文件（目录）名{info.filename}，压缩前大小{round(info.file_size, 0)}byte，'
              f'压缩后大小{round(info.compress_size, 0)}')
    extract_zipfie(zip_name)

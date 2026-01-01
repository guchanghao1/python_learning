# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import os

'''
def search_file(search_path, key_word):
    if not os.path.isdir(search_path):
        print('查找的不是文件夹，退出')
        return
    for file_or_dir in os.listdir(search_path):
        path_join = os.path.join(search_path, file_or_dir)
        if os.path.isdir(path_join):
            # 递归
            search_file(path_join, key_word)
            # 查找的关键字在文件名中存在
        elif key_word in os.path.basename(path_join):
            print(os.path.abspath(path_join))


if __name__ == '__main__':
    search_path = input('请输入要查找的目录：')
    key_word = input('请输入关键字：')
    print(f'f文件夹{search_path}中包含：{key_word}关键字')
    search_file(search_path, key_word)
'''


def search_file(search_path, key_word):
    """
    在指定目录及其子目录中搜索文件名包含关键字的文件

    Args:
        search_path (str): 要搜索的目录路径
        key_word (str): 要搜索的关键字

    Returns:
        list: 包含匹配文件绝对路径的列表
    """
    results = []

    # 检查路径是否存在
    if not os.path.exists(search_path):
        print(f'错误：路径 "{search_path}" 不存在')
        return results

    # 检查是否为目录
    if not os.path.isdir(search_path):
        print('错误：查找的不是文件夹')
        return results

    try:
        for file_or_dir in os.listdir(search_path):
            path_join = os.path.join(search_path, file_or_dir)

            if os.path.isdir(path_join):
                # 递归搜索子目录
                results.extend(search_file(path_join, key_word))
            elif key_word in file_or_dir:  # 直接使用文件名而不是重新获取
                abs_path = os.path.abspath(path_join)
                results.append(abs_path)
                print(abs_path)

    except PermissionError:
        print(f'警告：没有权限访问目录 {search_path}')
    except Exception as e:
        print(f'访问目录 {search_path} 时发生错误: {e}')

    return results


def main():
    """主函数"""
    search_path = input('请输入要查找的目录：').strip()
    key_word = input('请输入关键字：').strip()

    if not search_path or not key_word:
        print('错误：目录和关键字不能为空')
        return

    print(f'在文件夹 "{search_path}" 中搜索包含 "{key_word}" 关键字的文件：')

    results = search_file(search_path, key_word)

    if results:
        print(f'\n搜索完成！共找到 {len(results)} 个文件')
    else:
        print('\n未找到匹配的文件')


if __name__ == '__main__':
    main()

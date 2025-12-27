# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''


# ----------------------------------------------------------------------------------------------------------------------


def color_set(str_data, select_color):
    color_dict = {
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'NORMAL': '\033[0m',
    }
    select_color = select_color.upper()
    if select_color in color_dict.keys():
        return f'{color_dict.get(select_color)}{str_data}{color_dict.get("NORMAL")}'
    else:
        return f'{color_dict.get("NORMAL")}{str_data}{color_dict.get("NORMAL")}'


if __name__ == '__main__':
    data = color_set('123', 'red')
    print(data)

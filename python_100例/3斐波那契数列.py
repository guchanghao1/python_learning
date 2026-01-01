# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
fir_num = 0
sec_num = 1
option = int(input('请输入需要多少项：'))
if option == 1:
    print([fir_num])
elif option == 2:
    print([fir_num, sec_num])
else:
    list_num = [0, 1]
    for i in range(3, option + 1):
        fir_num, sec_num = sec_num, fir_num + sec_num  # 难点，多理解·
        list_num.append(sec_num)
    print(list_num)

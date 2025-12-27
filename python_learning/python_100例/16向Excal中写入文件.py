# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np

emp_info = pd.DataFrame(data={
    '姓名': ['a', 'b', 'c', 'd', 'e', 'f', ],
    '物理': np.random.randint(0, 100, size=6),  # 数据类型为 数组，与列表相似，但非！！
    '化学': np.random.randint(0, 100, size=6),
    '生物': np.random.randint(0, 100, size=6)
}, index=np.arange(1, 7))  # index是行索引
emp_info.to_excel('./emp.xlsx', index=False)
vfile = pd.read_excel('./emp.xlsx', index_col=0)
sum_score = vfile.sum(axis=1)
avg_score = vfile.mean(axis=1)
vfile['总分'] = sum_score
vfile['平均分'] = avg_score
vfile.to_excel('./emp.xlsx', index=False)

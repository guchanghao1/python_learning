# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
import openpyxl

# 有三个做图表的方法
wb = openpyxl.load_workbook('./emp.xlsx')
# 获取操作的工作表
sheet = wb.active
# 数据范围
sel_data = openpyxl.chart.Reference(sheet, min_col=2, min_row=1, max_col=4, max_row=7)
# 设置X轴
titlex = openpyxl.chart.Reference(sheet, min_col=1, min_row=2, max_row=7)
# 柱状图
chart_obj = openpyxl.chart.BarChart()
chart_obj.type = 'col'
chart_obj.style = 10
chart_obj.title = '学生成绩'
chart_obj.x_axis.title = '姓名'
chart_obj.x_axis.title = '成绩'
chart_obj.add_data(sel_data, titles_from_data=True)  # 数据中包含标题行
chart_obj.set_categories(titlex)
sheet.add_chart(chart_obj, 'A9')
wb.save('./emp.xlsx')

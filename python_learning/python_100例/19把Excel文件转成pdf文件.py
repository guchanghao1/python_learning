from win32com import client
import os

# 调用Excel服务,会打开Excel应用程序
xlapp = client.Dispatch("Excel.Application")
# 绝对路径
basepath = os.getcwd()  # 获取当前路径
excel_name = os.path.join(basepath, 'emp.xlsx')
pdf_name = os.path.join(basepath, 'emp.pdf')
books = xlapp.Workbooks.Open(excel_name)
books.ExportAsFixedFormat(0, pdf_name)
xlapp.Quit()
# 加个循环，可以批量操作

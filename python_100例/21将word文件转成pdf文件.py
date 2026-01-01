
'''
from win32com import client
import os


def dox2pdf(doc_name, pdf_name):
    try:
        w_process = client.Dispatch("Word.Application")  # 调用word服务
        if os.path.exists(pdf_name):
            os.remove(pdf_name)
        vdoc = w_process.Documents.Open(doc_name, ReadOnly=1)  # 保存原word不被修改
        vdoc.SaveAs(pdf_name, FileFormat=17)
        vdoc.Close()
        w_process.Quit()
        return pdf_name
    except  Exception as e:
        print(e)
        return -1


if __name__ == '__main__':
    basepath = os.getcwd()  # 获取当前的工作路径
    doc_name = 'D:\南通海太隧道预制箱涵项目\文件\2024.12.20钢筋超耗分析.docx'
    pdf_name = os.path.join(basepath, '\2024.12.20钢筋超耗分析.pdf')
    vret = dox2pdf(doc_name, pdf_name)
    if vret != -1:
        print('成功')
    else:
        print('失败')
# (-2147352567, '发生意外。', (0, 'Microsoft Word', '很抱歉，找不到您的文件
# 。该项目是否已移动、重命名或删除?\r (D:\\南通海太隧道预制箱涵项目\\文件\x824.12.20
# 钢筋超耗分析.docx)', 'wdmain11.chm', 24654, -2146823114), None)

'''
from win32com import client
import os


def doc2pdf(doc_name, pdf_name):
    try:
        # 确保输出目录存在
        os.makedirs(os.path.dirname(pdf_name), exist_ok=True)

        w_process = client.Dispatch("Word.Application")
        w_process.Visible = False  # 设置为不可见模式

        # 检查源文件是否存在
        if not os.path.exists(doc_name):
            print(f"源文件不存在: {doc_name}")
            return -1

        # 如果目标PDF文件已存在，先删除
        if os.path.exists(pdf_name):
            os.remove(pdf_name)

        # 打开Word文档
        vdoc = w_process.Documents.Open(doc_name, ReadOnly=1)
        vdoc.SaveAs(pdf_name, FileFormat=17)  # FileFormat=17 表示PDF格式
        vdoc.Close()
        w_process.Quit()

        # 检查是否成功生成PDF
        if os.path.exists(pdf_name):
            print(f"PDF文件已生成: {pdf_name}")
            return pdf_name
        else:
            print("PDF文件生成失败")
            return -1

    except Exception as e:
        print(f"转换过程中发生错误: {e}")
        try:
            w_process.Quit()
        except:
            pass
        return -1


if __name__ == '__main__':
    # 使用原始字符串(r前缀)避免转义字符问题
    basepath = os.getcwd()

    # 方法1：使用原始字符串
    doc_name = r'D:\南通海太隧道预制箱涵项目\文件\2024.12.20钢筋超耗分析.docx'

    # 方法2：使用正斜杠
    # doc_name = 'D:/南通海太隧道预制箱涵项目/文件/2024.12.20钢筋超耗分析.docx'

    # 方法3：转义反斜杠
    # doc_name = 'D:\\南通海太隧道预制箱涵项目\\文件\\2024.12.20钢筋超耗分析.docx'

    # 修复PDF路径 - 不要以反斜杠开头
    pdf_name = os.path.join(basepath, '2024.12.20钢筋超耗分析.pdf')

    print(f"源文件路径: {doc_name}")
    print(f"目标PDF路径: {pdf_name}")
    print(f"源文件是否存在: {os.path.exists(doc_name)}")

    vret = doc2pdf(doc_name, pdf_name)
    if vret != -1:
        print('Word转PDF成功!')
    else:
        print('Word转PDF失败!')

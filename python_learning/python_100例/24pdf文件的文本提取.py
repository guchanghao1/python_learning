# !/usr/bin/env python
# -*- coding: utf-8 -*-
''''''
# ----------------------------------------------------------------------------------------------------------------------
from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    pdf_path = './emp.pdf'
    text = extract_text_from_pdf(pdf_path)
    if text:
        print(text)

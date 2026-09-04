from docx import Document
import os

def convert_txt_to_docx(txt_file, docx_file):
    doc = Document()
    with open(txt_file, 'r', encoding='utf-8') as f:
        for line in f:
            doc.add_paragraph(line.strip('\n'))
    doc.save(docx_file)

convert_txt_to_docx('schorlarship.txt', 'schorlarship.docx')
convert_txt_to_docx('top_20_global_phd_programs.md', 'top_20_global_phd_programs.docx')

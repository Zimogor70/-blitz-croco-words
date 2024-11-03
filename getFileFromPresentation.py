'''
Откройте файл презентации в программе с помощью объекта Presentation библиотеки pptx
'''
import zipfile
from pptx import Presentation


prs = Presentation('src\Zimnyaya_igra_1.pptx')
for slide in prs.slides:
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        print(shape.text)
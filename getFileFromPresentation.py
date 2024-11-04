'''Задача 2024.10.23.04
Сохраните из этой презентации только слова,
 всякие "Правила", "Тур 1" и другие объяснение не нужны.
Сохраните все слова в файл words.txt'''
from pptx import Presentation

with open('words.txt','w',encoding="utf8") as file:
    file.write('')
    prs = Presentation('src\Zimnyaya_igra_1.pptx')
    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            file.write(shape.text_frame.text)


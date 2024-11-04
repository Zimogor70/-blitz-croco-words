'''Задача 2024.10.30.01
После выполнения задачи выше, сохраните полученный список слов в файл words.txt.'''
from pptx import Presentation

words_list = list('')
with open('words.txt','w',encoding="utf8") as file:
    file.write('')
    prs = Presentation('src\Zimnyaya_igra_1.pptx')
    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            words_list.append(shape.text_frame.text)
    file.writelines(words_list)


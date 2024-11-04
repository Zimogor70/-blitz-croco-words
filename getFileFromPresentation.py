'''Задача 2024.10.30.02
Напишите тест, который проверяет, что в строке находится всего одно слово.'''
from pptx import Presentation


def only_one_word(line: str) -> bool:
    line.strip()
    if ' ' in line:
        return False
    return True


words_list = list('')
with open('words.txt', 'w', encoding="utf8") as file:
    file.write('')
    prs = Presentation('src\Osennyaya_igra_3.pptx')
    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            if only_one_word(shape.text_frame.text):
                words_list.append(shape.text_frame.text+'\n')
    file.writelines(words_list)

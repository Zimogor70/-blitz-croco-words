from pptx import Presentation
from check_spell import check_spell


def only_one_word(line: str) -> bool:
    return ' ' not in line and line.isalpha()


def send_to_check(lst: set) -> list:
    ret_lst = list()
    for elem in lst:
        ret_lst.append(check_spell(elem))
    return ret_lst


def pars_and_save(ls_files):
    words_set = set()
    with open('words.txt', 'w', encoding="utf8") as file:
        file.write('')
        for name in ls_files:
            prs = Presentation('src\\'.__add__(name))
            for slide in prs.slides:
                for shape in slide.shapes:
                    if not shape.has_text_frame:
                        continue
                    if only_one_word(shape.text.strip()):
                        words_set.add(shape.text.strip() + '\n')
            file.writelines(send_to_check(words_set))

from pptx import Presentation


def only_one_word(line: str) -> bool:
    return ' ' not in line and line.isalpha()


def pars_and_save(ls_files):
    words_list = list('')
    with open('words.txt', 'w', encoding="utf8") as file:
        file.write('')
        for name in ls_files:
            prs = Presentation('src\\'.__add__(name))
            for slide in prs.slides:
                for shape in slide.shapes:
                    if not shape.has_text_frame:
                        continue
                    if only_one_word(shape.text.strip()):
                        words_list.append(shape.text.strip() + '\n')
            file.writelines(words_list)

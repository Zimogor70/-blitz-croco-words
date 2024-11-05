'''Задача 2024.11.04.06
Дополните код проекта blitz-croco-words функцией, которая на вход получает список слов,
отправляет их в Yandex Speller, и возвращает список проверенных и отредактированных слов.
Вставьте использование этой функции между парсингом презентаций и сохранением в words.txt'''
from extract import extr_zip
from parsave import pars_and_save
from check_spell import check_spell


def main():
    pars_and_save(extr_zip('src\croco-blitz-source.zip'))
    # lst = ['Колакал', 'малако']
    # st: str = ''
    # for elem in lst:
    #     st += elem + ' '
    # print(check_spell(st.strip()))


if __name__ == "__main__":
    main()

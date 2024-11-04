'''Задача 2024.11.01.01
Теперь рефакторим код.
Ракладываем его по уровням и задачам.
1 уровень - читаем архив и собираем слова из каждого файла
2 уровень (ниже) - читаем файл с презентацией и достаём из него слова.
Уровни лучше разнести по разным файлам.'''
from extract import extr_zip
from parsave import pars_and_save


def main():
    pars_and_save(extr_zip('src\croco-blitz-source.zip'))


if __name__ == "__main__":
    main()

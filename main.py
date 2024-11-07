'''Задача 2024.11.06.02
Учитывая даты сохраните в файл words.txt слова в формате:
слово:дата'''
from extract import extr_zip
from parsave import pars, save, send_to_check


def main():
    save(send_to_check(pars(extr_zip('src\croco-blitz-source.zip'))))


if __name__ == "__main__":
    main()

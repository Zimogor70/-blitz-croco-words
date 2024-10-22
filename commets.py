import os # подключаем библиотеку os
from pathlib import Path # подключаем класс Path из библиотеки pathlib
from zipfile import ZipFile # подключаем класс ZipFile из библиотеки zipfile

ZIP_FILENAME = "croco-blitz-source.zip" # переменная с именем zip файла


def read_zipped_file(): # функция для чтения zip файла
    # переменная, которая хранит путь к текущей папке
    current_folder = os.path.dirname(os.path.realpath(__file__))
    # начинаем работу с zip файлом через archive
    with ZipFile(Path(current_folder) / 'src' / ZIP_FILENAME) as archive:
        for f in archive.namelist(): # в цикле перебираем всё содержимое архива
            print(f) # печатаем имя каждого элемента содержащегося в архиве


if __name__ == "__main__":
    read_zipped_file()
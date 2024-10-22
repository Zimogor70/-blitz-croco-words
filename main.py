import pathlib
from zipfile import ZipFile
pathlib.Path(__file__).parent.resolve()

with ZipFile('src/croco-blitz-source.zip','r') as filezip:
    print(filezip.namelist())
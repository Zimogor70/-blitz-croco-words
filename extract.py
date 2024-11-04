import zipfile


def extr_zip(name: str) -> list:
    list_of_pres: list = []
    with zipfile.ZipFile(name, 'r') as archive:
        for f in archive.namelist():
            list_of_pres.append(f)
        archive.extractall('src\\')
    return list_of_pres

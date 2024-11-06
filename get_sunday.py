'''Задача 2024.11.06.01
Попробуйте написать даты, когда проходила каждая игра,
учитывая что игры проходили по воскресеньям.'''

from datetime import date, timedelta


def allsundays(year):
    d = date(year, 1, 1)
    d += timedelta(days=6 - d.weekday())
    while d.year == year:
        yield d
        d += timedelta(days=7)


for d in allsundays(2024):
    print(d)

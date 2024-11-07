'''Задача 2024.11.06.01
Попробуйте написать даты, когда проходила каждая игра,
учитывая что игры проходили по воскресеньям.'''
import datetime
import os

path = "src\Zimnyaya_igra_1.pptx"

# file modification
timestamp = os.path.getmtime(path)

# convert timestamp into DateTime object
datestamp = datetime.datetime.fromtimestamp(timestamp)
print('Modified Date/Time:', datestamp)

# file creation
c_timestamp = os.path.getctime(path)

# convert creation timestamp into DateTime object
c_datestamp = datetime.datetime.fromtimestamp(c_timestamp)

print('Created Date/Time on:', c_datestamp)

import sqlite3


def main():
    con = sqlite3.connect('words.db')  # соединение с базой или создание, если таковой нет
    add_data(con,'movie',{'1','Uly Guly'})
    # cur = con.cursor()  # получаем курсор базы
    # # cur.execute('CREATE TABLE IF NOT EXISTS movie(title, year, score)')
    # # res = cur.execute('SELECT name FROM sqlite_master') # get link on object classes of cursor
    # # print(res.fetchone()) # получаем кортеж данных отработавшего запроса
    # # исполяем запрос на создание таблицы, если нет таковой
    # cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
    # # в списке храним записи для последующего добавления в таблицу
    # data = [
    #     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    #     ("Monty Python's The Meaning of Life", 1983, 7.5),
    #     ("Monty Python's Life of Brian", 1979, 8.0),
    # ]
    # # исполняем запрос на добавление записей из data
    # cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    con.commit()  # зафиксировать результаты транзакции в БД



def add_data(con: sqlite3.Connection, t_name: str, d: {str, str}):
    cur = con.cursor()
    for values in d:
        cur.executemany(f'INSERT INTO {t_name} (title) VALUES(?)',values)
    cur.close()


if __name__ == '__main__':
    main()

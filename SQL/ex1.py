import sqlite3 as sq


with sq.connect("saber.dp") as con:  #Подключаемся к бд
    cur = con.cursor()  #Команда для начала работы с базой данных
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT NOT NULL,
    old INTEGER NOT NULL DEFAULT 1,
    score INTEGER
    )""")
    for i in range(1, 14):
        cur.execute(f"""INSERT INTO users (name, old, score)
        VALUES ('Чел{str(i)}',{str(i)}, 1000*{str(i)})""")

    cur.execute("SELECT * FROM users")
    for result in cur:
        print(result)

#IF NOT EXIST - если таблица с таким названием не существует
#NOT NULL - значение в столбце никогда не будем пустым
#DEFAULT - задать значение по умолчанию


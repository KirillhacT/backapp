import sqlite3 as sq

with sq.connect("saber.dp") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS games")
    cur.execute("""CREATE TABLE IF NOT EXISTS games (
    user_id INTEGER,
    score INTEGER NOT NULL,
    time INTEGER NOT NULL
    )""")
    for i in range(10):
        cur.execute(f"INSERT INTO games (score, time) VALUES (1000*{i}, 10*{i})")
    cur.execute("SELECT * FROM games")
    for result in cur:
        print(result)
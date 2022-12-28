import sqlite3 as sq

with sq.connect("saber.dp") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS tab1")
    cur.execute("""CREATE TABLE IF NOT EXISTS tab1 (
    score INTEGER,
    name TEXT
    )""")
    cur.execute("DROP TABLE IF EXISTS tab2")
    cur.execute("""CREATE TABLE IF NOT EXISTS tab2 (
    val INTEGER,
    type TEXT
    )""")


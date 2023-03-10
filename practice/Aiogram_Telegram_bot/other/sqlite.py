import sqlite3

async def db_start():
    global db, cur

    db = sqlite3.connect('new.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id PRIMARY KEY, photo TEXT, description TEXT)")
    db.commit()

async def create_profile(user_id):
    user = cur.execute(f"SELECT 1 FROM profile WHERE user_id == {user_id}").fetchone()
    if not user:
        # command = f"INSERT INTO profile VALUES({user_id}, {''}, {''})"
        cur.execute("INSERT INTO profile VALUES(?, ?, ?)", (user_id, '', ''))
        db.commit()

async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute(f"UPDATE profile SET photo = '{data['photo']}', description = '{data['desc']}' WHERE user_id == {user_id}")
        db.commit()

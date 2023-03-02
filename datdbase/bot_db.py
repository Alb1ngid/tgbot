import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")  # .db
    cursor = db.cursor()

    if db:
        print("бд подключена")

    db.execute("CREATE TABLE IF NOT EXISTS anceta"
               "(id INTEGER PRIMARY KEY,username TEXT,"
               "name TEXT,age INTEGER,gender TEXT,"
               "region TEXT, photo TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as date:
        cursor.execute("INSERT INTO anceta VALUES "
                       "(?,?,?,?,?,?,?)", tuple(date.values()))
        db.commit()

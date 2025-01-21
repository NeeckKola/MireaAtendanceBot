import sqlite3 as sq

db = sq.connect('databases/studandstar.db')
cur = db.cursor()

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS studentsdata("
                "id INTEGER, "
                "groupa TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS starostdata("
                "username TEXT,"
                "id INTEGER, "
                "groupa TEXT)")
    cur.execute("INSERT INTO starostdata (username, groupa) VALUES (?, ?)", ('neeck_kola', 'ККСО-03-21'))
    db.commit()

async def cmd_start_db(message):
    cur.execute('SELECT * FROM starostdata WHERE username = ?', (message.from_user.username,))
    username_exists_in_starostdata = cur.fetchone() is not None
    cur.execute('SELECT * FROM studentsdata WHERE id = ?',(message.from_user.id,))
    user = cur.fetchone() is not None
    cur.execute('SELECT id FROM starostdata WHERE username = ?', (message.from_user.id,))
    id_exist_in_starostdata = cur.fetchone() is not None
    if username_exists_in_starostdata and not id_exist_in_starostdata:
        cur.execute('UPDATE starostdata SET id = ? WHERE username = ?', (message.from_user.id, message.from_user.username))
        db.commit()

async def check_student_by_id(user_id):
    cur.execute('SELECT * FROM studentsdata WHERE id = ?', (user_id,))
    result = cur.fetchone()

    # Если результат не None, то пользователь с указанным id существует в таблице
    if result is not None:
        print(f"check_student_by_id: Пользователь с id {user_id} существует в таблице studentsdata.")
        return True
    else:
        print(f"check_student_by_id: Пользователь с id {user_id} не найден в таблице studentsdata.")
        return False

async def check_starost_by_id(user_id):
    cur.execute('SELECT * FROM starostdata WHERE id = ?', (user_id,))

    result = cur.fetchone()

    # Если результат не None, то пользователь с указанным id существует в таблице
    if result is not None:
        print(f"check_starost_by_id: Пользователь с id {user_id} существует в таблице starostsdata.")
        return True
    else:
        print(f"check_starost_by_id: Пользователь с id {user_id} не найден в таблице starostsdata.")
        return False

async def get_student_group_by_id(user_id):
    cur.execute('SELECT groupa FROM studentsdata WHERE id = ?', (user_id,))

    result = cur.fetchone()

    # Если результат не None, то возвращаем значение groupa
    if result is not None:
        groupa_value = result[0]
        print(f"get_student_group_by_id: Значение groupa для пользователя с id {user_id}: {groupa_value}")
        return groupa_value
    else:
        print(f"get_student_group_by_id: Пользователь с id {user_id} не найден в таблице studentsdata.")
        return None

async def get_starost_group_by_id(user_id):
    cur.execute('SELECT groupa FROM starostdata WHERE id = ?', (user_id,))

    result = cur.fetchone()

    # Если результат не None, то возвращаем значение groupa
    if result is not None:
        groupa_value = result[0]
        print(f"get_starost_group_by_id: Значение groupa для пользователя с id {user_id}: {groupa_value}")
        return groupa_value
    else:
        print(f"get_starost_group_by_id: Пользователь с id {user_id} не найден в таблице studentsdata.")
        return None



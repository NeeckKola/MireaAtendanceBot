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
    # Выполнение SQL-запроса
    cur.execute('SELECT * FROM studentsdata WHERE id = ?', (user_id,))
    # Получение результата запроса
    result = cur.fetchone()

    # Если результат не None, то пользователь с указанным id существует в таблице
    if result is not None:
        print(f"check_student_by_id: Пользователь с id {user_id} существует в таблице studentsdata.")
        return True
    else:
        print(f"check_student_by_id: Пользователь с id {user_id} не найден в таблице studentsdata.")
        return False

async def check_starost_by_id(user_id):
    # Выполнение SQL-запроса
    cur.execute('SELECT * FROM starostdata WHERE id = ?', (user_id,))

    # Получение результата запроса
    result = cur.fetchone()

    # Если результат не None, то пользователь с указанным id существует в таблице
    if result is not None:
        print(f"check_starost_by_id: Пользователь с id {user_id} существует в таблице starostsdata.")
        return True
    else:
        print(f"check_starost_by_id: Пользователь с id {user_id} не найден в таблице starostsdata.")
        return False

async def get_student_group_by_id(user_id):
    # Выполнение SQL-запроса SELECT
    cur.execute('SELECT groupa FROM studentsdata WHERE id = ?', (user_id,))

    # Получение результата запроса
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
    # Выполнение SQL-запроса SELECT
    cur.execute('SELECT groupa FROM starostdata WHERE id = ?', (user_id,))

    # Получение результата запроса
    result = cur.fetchone()

    # Если результат не None, то возвращаем значение groupa
    if result is not None:
        groupa_value = result[0]
        print(f"get_starost_group_by_id: Значение groupa для пользователя с id {user_id}: {groupa_value}")
        return groupa_value
    else:
        print(f"get_starost_group_by_id: Пользователь с id {user_id} не найден в таблице studentsdata.")
        return None



# async def update_active_status(user_id, active):
#     Выполнение SQL-запроса UPDATE
#     cur.execute('UPDATE studentsdata SET active = ? WHERE id = ?', (active, user_id))
#     Фиксация изменений
#     db.commit()
#
# async def check_active_status(user_id):
#     Выполнение SQL-запроса SELECT
#     cur.execute('SELECT active FROM studentsdata WHERE id = ?', (user_id,))
#
#     Получение результата запроса
#     result = cur.fetchone()
#
#     Если результат не None и равен 1, то параметр active равен 1
#     if result is not None and result[0] == 1:
#         print(f"check_active_status: Параметр active для пользователя с id {user_id} равен 1.")
#         return True
#     else:
#         print(f"check_active_status: Параметр active для пользователя с id {user_id} не равен 1 или пользователя не существует.")
#         return False
#

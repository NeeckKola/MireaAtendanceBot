from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)
import databases as db

# Меню
async def menu_kbrd(message):
    await db.cmd_start_db(message)
    if await db.check_starost_by_id(message.from_user.id):
        kb_btn = [
            [
                KeyboardButton(text="Общий скип")
            ],
        ]
        keyboard = ReplyKeyboardMarkup(
            keyboard=kb_btn,
            resize_keyboard=True,
            input_field_placeholder="Меню"
        )
        await message.answer("Обеспечь отдых товарищу:", reply_markup=keyboard)
    elif await db.check_student_by_id(message.from_user.id):
        kb_btn = [
            [KeyboardButton(text="Переподписаться на другую группу")]
        ]
        keyboard = ReplyKeyboardMarkup(
            keyboard=kb_btn,
            resize_keyboard=True,
            input_field_placeholder="Меню"
        )
        await message.answer("Вы подписаны на: " + f"{await db.get_student_group_by_id(message.from_user.id)}", reply_markup=keyboard)
    else:
        kb_btn = [
            [KeyboardButton(text="Подписаться на группу")]
        ]
        keyboard = ReplyKeyboardMarkup(
            keyboard=kb_btn,
            resize_keyboard=True,
            input_field_placeholder="Меню"
        )
        await message.answer("Узнай когда можно скипнуть",
                             reply_markup=keyboard)


# Подписка на рассылку
issubscribing = False
async def subscribe(message):
    db.cur.execute('INSERT INTO studentsdata (id, groupa) VALUES (?, ?)', (message.from_user.id,message.text))
    await message.answer("Вы теперь подписаны на: " + f"{message.text}")
    issubscribing = False
    db.db.commit()
    await menu_kbrd(message)

isresubscribing =False
async def resubscribe(message):
    db.cur.execute('UPDATE studentsdata SET groupa = ? WHERE id = ?', (message.text, message.from_user.id))
    await message.answer("Вы теперь переподписаны на: " + f"{message.text}")
    isresubscribing = False
    db.db.commit()
    await menu_kbrd(message)


# админское меню
# iseditingstarost = False
# показать список старост
# async def showstarostlist (message):
#     db.cur.execute('SELECT username FROM starostdata')
#     results = db.cur.fetchall()
#     builder = InlineKeyboardBuilder()
#     for result in results:
#         username = result[0]
#         builder.row()
#         name = str({username})
#         builder.add(types.InlineKeyboardButton(
#             text=name,
#             callback_data=name)
#         )
#         builder.add(types.InlineKeyboardButton(
#             text=emoji.emojize(':pencil:'),
#             callback_data=name)
#         )
#         builder.add(types.InlineKeyboardButton(
#             text=emoji.emojize(':cross_mark:'),
#             callback_data=name)
#         )
#         builder.adjust(3)
#     builder.add(types.InlineKeyboardButton(
#         text=emoji.emojize('+'),
#         callback_data="add_starost")
#     )
#     await message.answer(
#             "Редактирование списка старост",
#             reply_markup=builder.as_markup()
#     )
#
# async def editstarost (message, starosttoedit):
#     await message.answer("Имя изменено с " + f"{starosttoedit}" +" на " + f"{message.text}")
#     await showstarostlist(message)
#     iseditingstarost = False
#
# isaddingstarost = False
# isaddinggroupa = False
# starosttoadd = None
# groupatoadd = None
# async def addstarost(message):
#     db.cur.execute('INSERT INTO studentsdata (id, groupa) VALUES (?, ?)', (message.from_user.id, message.text))
#     await message.answer("Вы теперь подписаны на: " + f"{message.text}")
#     issubscribing = False
#     db.db.commit()
#     await menu_kbrd(message)
#
#
# Меню админа
# botadmin = 'neeck_kola'
# async def admin_menu(message):
#     if str(message.from_user.username) == botadmin:
#         kb_btn = [
#             [
#                 KeyboardButton(text="Редактировать список старост"),
#             ],
#             [
#                 KeyboardButton(text="Меню"),
#             ]
#         ]
#         keyboard = ReplyKeyboardMarkup(
#             keyboard=kb_btn,
#             resize_keyboard=True,
#             input_field_placeholder="Админское меню"
#         )
#         await message.answer("Эуээеэеэ", reply_markup=keyboard)
#
#
#


from aiogram import types, F, Router, Bot
from aiogram.filters import Command
import keyboards
import databases as db
import mireabot

router = Router()


# Старт
@router.message(Command("start"))
async def start(message: types.Message):
    await keyboards.menu_kbrd(message)

#Регистрация пользователя
@router.message(F.text == "Подписаться на группу")
async def subscribe(message: types.Message):
    await message.answer("введи свою группу")
    keyboards.issubscribing = True

@router.message(F.text == "Переподписаться на другую группу")
async def resubscribe(message: types.Message):
    if await db.check_student_by_id(message.from_user.id):
        await message.answer("введи свою группу")
        keyboards.isresubscribing = True
    else:
        await message.answer("введи свою группу")
        keyboards.issubscribing = True

@router.message(F.text == "Общий скип")
async def sendskip(message: types.Message):
    if await db.check_starost_by_id(message.from_user.id):
        targetgroup = await db.get_starost_group_by_id(message.from_user.id)
        print(targetgroup)
        db.cur.execute('SELECT id FROM studentsdata WHERE groupa = ?', (targetgroup,))
        results = db.cur.fetchall()
        print(results)
        for result in results:
                user_id = result[0]
                await mireabot.mybot.send_message(user_id, 'скип')
        await mireabot.mybot.send_message(message.from_user.id, 'Успешная рассылка')

@router.message()
async def echo(message: types.Message):
    if keyboards.issubscribing == True:
        await keyboards.subscribe(message)
    elif keyboards.isresubscribing == True:
        await keyboards.resubscribe(message)
    # if keyboards.iseditingstarost == True:
    #     await keyboards.editstarost(message, starosttoedit)
    # elif keyboards.isaddingstarost == True:
    #     await keyboards.addstarost(message)







# проверка
# @router.message(Command("check"))
# async def id(message: types.Message):
#     await message.answer(f"Ваш ID: {message.from_user.username} ,{'neeck_kola' in starostdata.df.values} ,{str(message.from_user.username) in starostdata.df.values}")
#
# @router.message(Command("id"))
# async def id(message: types.Message):
#     await message.answer(f"Ваш ID: {message.from_user.id}")
#
# админское меню
# @router.message(Command("admin"))
# async def adminmenu(message: types.Message):
#     await keyboards.admin_menu(message)
#
# Редактирование списка старост
# @router.message(F.text == "Редактировать список старост")
# async def with_puree(message: types.Message):
#     if str(message.from_user.username) == keyboards.botadmin:
#         await keyboards.showstarostlist(message)
#
# starosttoedit = None
# @router.callback_query(lambda callback_query: callback_query.data in starostdata.df["Id"].values)
# async def editstarost(callback: types.CallbackQuery):
#     await callback.message.delete()
#     keyboards.iseditingstarost = True
#     starosttoedit = callback.data
#     await callback.message.answer("введите новый id для " + f"{callback.data}")
#
# @router.callback_query(F.data=="add_starost")
# async def addstarost(callback: types.CallbackQuery):
#     await callback.message.answer("введи ссылку на старосту")
#     keyboards.iseditingstarost = True



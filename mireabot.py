import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import config
import databases as db
import handlers

mybot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(handlers.router)
    await db.db_start()
    await mybot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(mybot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
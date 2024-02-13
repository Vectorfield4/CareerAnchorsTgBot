import asyncio
from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
import os

TOKEN = os.environ.get("BOT_TOKEN")
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    from handlers import *
    asyncio.run(main())


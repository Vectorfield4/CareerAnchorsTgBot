import asyncio
from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
import os

from sqlalchemy import URL

import database.config
from database import BaseModel, create_async_engine, get_session_maker, proceed_schemas

TOKEN = os.environ.get("BOT_TOKEN")

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
postgres_url = URL.create(
        drivername="postgresql+asyncpg",
        username=database.config.user,
        host=database.config.host,
        password=database.config.password,
        database=database.config.database,
        port=database.config.port
    )
async_engine = create_async_engine(postgres_url)
session_maker = get_session_maker(async_engine)
async def main() -> None:

    await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot)

if __name__ == '__main__':
    from handlers import *

    asyncio.run(main())


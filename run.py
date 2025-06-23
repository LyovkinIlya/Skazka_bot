import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from aiogram import Bot, Dispatcher

# надо будет импортировать Роутер

async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router()
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('Бот включен')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
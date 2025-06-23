import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from aiogram import Bot, Dispatcher

from code_qr.qr_handlers import qr





async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(qr)
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('Бот включен')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
import asyncio
from aiogram import Dispatcher, types, Bot

dp = Dispatcher()


@dp.message()
async def hello(message: types.Message):
    await message.answer('Подождите, пожалуйста, я думаю...')
    await asyncio.sleep(3)
    await message.send_copy(message.from_user.id)

async def main():
    bot = Bot(token='7811218172:AAGjuFp2Lb8WwEHDsA1Q2jIGiPNhqaB4FbE')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
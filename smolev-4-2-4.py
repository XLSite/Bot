import asyncio
from aiogram import Dispatcher, types, Bot, F
from aiogram.filters import Command

dp = Dispatcher()

@dp.message(Command('start'))
async def hello(message: types.Message):
    await message.answer('answer')
    await message.reply('reply')

@dp.message(F.text == 'Menu')
async def menu(message: types.Message):
    await message.answer('menu')

async def main():
    bot = Bot(token='7811218172:AAGjuFp2Lb8WwEHDsA1Q2jIGiPNhqaB4FbE')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
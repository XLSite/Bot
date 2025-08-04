import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message

dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: Message) -> None:
    await message.answer(f'Добрый день, {message.from_user.full_name}\nРады приветствовать Вас в нашем магазине!')

@dp.message(F.text == 'О нас')
async def menu_handler(message: Message) -> None:
    await message.answer('Мы работаем с 2001 года')

@dp.message(F.text == 'Веб-сайт')
async def hello_handler(message: Message) -> None:
    await message.answer('https://megabotshopper.ru')

@dp.message(F.text == 'Контакты')
async def morse_handler(message: Message) -> None:
    await message.answer(f'Наш адрес:\nг. Москва, ул.Веселая, 15\n\nТелефон:\n+7(999) 999-99-99')

@dp.message()
async def all_handler(message: Message) -> None:
    await message.answer('Я ловлю всех и вся')

async def main() -> None:
    token = "7811218172:AAGjuFp2Lb8WwEHDsA1Q2jIGiPNhqaB4FbE"
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
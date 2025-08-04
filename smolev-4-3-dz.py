import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

dp = Dispatcher()
BOT_TOKEN = "7811218172:AAH5iuVHwETX1-GwVSTY-nqcGRJ-VAG_i08"
course_price = {'python': 15000, 'aiogram': 7000, 'telebot': 7500, 'django': 20000}
course_names = {'python': "Курс по Python", 'aiogram': "Курс по Aiogram", 'telebot': "Курс по Telebot", 'django': "Курс по Django"}
text_about = "Пускай, тебе и кажется, что только отправлять сообщения да создавать клавиатуру, но на самом деле из этого состоят все боты на 90%, где оставшиеся 10 занимает работа с базой данных."
support_url = "https://rkn.gov.ru/"


@dp.message(Command('start'))
@dp.callback_query(F.data == 'menu')
async def start_command(message: types.Message) -> None:
    kb = [
        [types.KeyboardButton(text="Каталог")],
        [
            types.KeyboardButton(text="Профиль"),
            types.KeyboardButton(text="Техподдержка"),
        ],
        [types.KeyboardButton(text="О нас")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Приветствуем в нашем магазине!', reply_markup=keyboard)

@dp.message(F.text == 'Каталог')
async def catalog_handler(message: types.Message) -> None:
    kb = [
        [
            types.InlineKeyboardButton(text="Курс по Python", callback_data="python"),
            types.InlineKeyboardButton(text="Курс по Aiogram", callback_data="aiogram")
        ],
        [
            types.InlineKeyboardButton(text="Курс по Telebot", callback_data="telebot"),
            types.InlineKeyboardButton(text="Курс по Django", callback_data="django")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer('Наши курсы:', reply_markup=keyboard)

@dp.callback_query(F.data == 'python')
async def course_python_handler(callback: types.CallbackQuery) -> None:
    kb = [
        [types.InlineKeyboardButton(text="Купить курс", callback_data="order_python")],
        [types.InlineKeyboardButton(text="Вернуться в каталог",callback_data="catalog")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.answer(f'{course_names[callback.data]}\nЦена - {course_price[callback.data]} руб', reply_markup=keyboard)

@dp.callback_query(F.data == 'aiogram')
async def course_python_handler(callback: types.CallbackQuery) -> None:
    kb = [
        [types.InlineKeyboardButton(text="Купить курс", callback_data="order_aiogram")],
        [types.InlineKeyboardButton(text="Вернуться в каталог",callback_data="catalog")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.answer(f'{course_names[callback.data]}\nЦена - {course_price[callback.data]} руб', reply_markup=keyboard)

@dp.callback_query(F.data == 'telebot')
async def course_python_handler(callback: types.CallbackQuery) -> None:
    kb = [
        [types.InlineKeyboardButton(text="Купить курс", callback_data="order_telebot")],
        [types.InlineKeyboardButton(text="Вернуться в каталог",callback_data="catalog")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.answer(f'{course_names[callback.data]}\nЦена - {course_price[callback.data]} руб', reply_markup=keyboard)

@dp.callback_query(F.data == 'django')
async def course_python_handler(callback: types.CallbackQuery) -> None:
    kb = [
        [types.InlineKeyboardButton(text="Купить курс", callback_data="order_django")],
        [types.InlineKeyboardButton(text="Вернуться в каталог",callback_data="catalog")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.answer(f'{course_names[callback.data]}\nЦена - {course_price[callback.data]} руб', reply_markup=keyboard)


@dp.callback_query(F.data == 'catalog')
async def get_menu(query: types.CallbackQuery) -> None:
    await catalog_handler(query.message)

@dp.callback_query(F.data.startswith('order_'))
async def order_course(query: types.CallbackQuery) -> None:
    course_name = query.data.split('_')[1]
    await query.message.answer(
        f'"{course_names[course_name]}" успешно куплен.'
    )

@dp.message(F.text == 'Профиль')
async def get_profile_handler(message: types.Message) -> None:
    kb = [
        [
            types.InlineKeyboardButton(
                text='Вернуться в Меню', callback_data='menu'
            )
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(
        f'Ваше имя: {message.from_user.full_name}\nID: {message.from_user.id}\nБаланс: 20 000 руб.',
        reply_markup=keyboard
    )

@dp.message(F.text == 'Техподдержка')
async def support_handler(message: types.Message) -> None:
    kb = [
        [
            types.InlineKeyboardButton(
                text='Связаться с нами', url=support_url
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Вернуться в Меню', callback_data='menu'
            )
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer('Помощь:', reply_markup=keyboard)

@dp.message(F.text == "О нас")
async def about_handler(message: types.Message) -> None:
    await message.answer(text_about)

async def main() -> None:
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
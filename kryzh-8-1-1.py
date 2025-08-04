from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

BOT_TOKEN = "7811218172:AAH5iuVHwETX1-GwVSTY-nqcGRJ-VAG_i08"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

async def process_start_command(message = Message):
    await message.answer(f"Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь")

async def process_help_command(message=Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

async def send_echo(message=Message):
    await  message.reply(text=message.text)

dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_echo)

if __name__ == "__main__":
    dp.run_polling(bot)
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from keyboards import menu_kb, start_kb, ikb, ExitReplay
from time import sleep
import random

TOKEN_API = "5330446051:AAEWOOzIukJqBgyI0N5CjRAZv9ooTJaIe5Q"

#Бот - сервер, который будет взаимодействовать с API telegram
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)
stickerExample = "CAACAgIAAxkBAAEH-7xkAkIVDFgDcNq14QbDzcNY1mB91AACAw4AAkD-yUuLHupAbb8sOC4E"
KB = ExitReplay("Меню")()

photos_list = []
with open("photos.txt", encoding='utf-8') as file:
    for i in file:
        photos_list.append(i)
# kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#one_time_keyboard - клавиатура закрывается после первого использования

def  send_random_photo():
    random_number = random.randint(0, len(photos_list) - 1)
    return photos_list.pop(random_number)


async def on_startup(_):
    print("Бот был запущен")

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    text = "Привет, добро пожаловать в бота"
    await bot.send_sticker(message.from_user.id, sticker=stickerExample)
    await message.answer(text=text, reply_markup=start_kb)
    await message.delete()

@dp.message_handler(Text(equals="Меню"))
async def echo(message: types.Message):
    text = "Меню бота: "
    await message.answer(text=text, reply_markup=menu_kb)

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == "like":
        await callback.answer("Благодарю")
        # await bot.send_message(callback.message.chat.id, text="Благодарю)")
    elif callback.data == "dislike":
        await callback.answer("Ну ладно")
        # await bot.send_message(callback.message.chat.id, text="Ну ладно")
    elif callback.data == "dont_like":
        random_photo = send_random_photo()
        await bot.send_photo(callback.message.chat.id, photo=random_photo, reply_markup=ikb)
        await callback.answer()

@dp.message_handler(Text(equals="Помощь"))
async def help(message: types.Message):
    text = "<em>Помощь <b>находится</b> в разработке!</em>😅"
    await message.answer(text=text, parse_mode="HTML")
    await bot.send_location(chat_id=message.chat.id, latitude=55, longitude=10, reply_markup=KB)

@dp.message_handler(Text(equals="Выход"))
async def exit(message: types.Message):
    await bot.send_message(message.chat.id, text="Оривидерчи", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals="Отправить фото")) #Будет отправлять в чат, из которого написали
async def send_photo(message: types.Message):
    # await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Нравится ли тебе эта фотография?", reply_markup=ikb)
    random_photo = send_random_photo()
    await bot.send_photo(message.chat.id, photo=random_photo, reply_markup=ikb)

@dp.message_handler(Text(equals="Секрет"))
async def gen(message: types.Message):
    for i in range(1, 11):
        sleep(0.1)
        await bot.send_message(message.chat.id, text=f"{str(i)}%", reply_markup=ReplyKeyboardRemove())
    sleep(0.5)
    await bot.send_message(message.chat.id, text="Поздравляю, ты ебобо)", reply_markup=menu_kb)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
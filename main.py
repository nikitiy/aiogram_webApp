from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from aiogram.types.web_app_info import WebAppInfo

from config import *

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Клавиатура рядом с сообщением
ibtn_markup = InlineKeyboardMarkup(row_width=1)
# Кнопка с сообщением
ibtn = InlineKeyboardButton("Жмакнуть", web_app=WebAppInfo(url=WEB_APP_URL))
# Добавление кнопки к клавиатуре
ibtn_markup.add(ibtn)

# Обычная клавиатура
btn_markup = ReplyKeyboardMarkup(resize_keyboard=True)
# Кнопка в области обычной клавиатуры
btn = KeyboardButton("Ну или тут жмакни 🤷‍", web_app=WebAppInfo(url=WEB_APP_URL))
# Добавление кнопки к клавиатуре
btn_markup.add(btn)


# Обработчик команды "/start"
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    # Отправка сообщений с клавиатурами и удаление сообщения пользователя "/start"
    await message.answer("Привет! Я бот, которого попросили отправить тебе эту кнопку", reply_markup=btn_markup)
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://sun9-48.userapi.com/impg/99sr3duW9QmScm2E92YO62IX-lk0SCFXS7iWlg/ZzMx4vOkI88.jpg?size=666x500&quality=95&sign=ae40df49bdf9464980d98e00f9f1fc9a&type=album",
        caption="↓ Посмотри что тут есть ↓",
        reply_markup=ibtn_markup
    )
    await message.delete()


# Обработчик всех сообщений от пользователя
@dp.message_handler()
async def any_messages(message: types.Message):
    # Отправка сообщений
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://sun9-58.userapi.com/impg/51JITtE7C7jPF-1augXmXk06SLpieJB2aZ-KUA/cRBYFZT16U4.jpg?size=666x500&quality=95&sign=f8810eddcf08ece777202b9abab24100&type=album",
        caption="↓ ЖМАКАЙ!!!! ↓",
        reply_markup=ibtn_markup
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

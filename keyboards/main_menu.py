# кнопки
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Залишити заявку на тур")],
        [KeyboardButton(text="Замовити консультацію")],
    ],
    resize_keyboard=True
)
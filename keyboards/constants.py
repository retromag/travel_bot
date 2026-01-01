from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

BACK = "⬅️ Назад"
EXIT = "❌ Вийти"

nav_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=BACK), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)

consult_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅ Назад"), KeyboardButton(text="Я прочитав")]
    ],
    resize_keyboard=True
)


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Залишити заявку на тур")],
        [KeyboardButton(text="Замовити консультацію")],
    ],
    resize_keyboard=True
)

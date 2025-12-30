from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.constants import back, countries, EXIT

countries_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇮🇹 Италия"), KeyboardButton(text="🇪🇸 Испания")],
        [KeyboardButton(text="🇫🇷 Франция"), KeyboardButton(text="🇹🇷 Турция")],
        [KeyboardButton(text=back), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)

dates_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Июнь"), KeyboardButton(text="Июль")],
        [KeyboardButton(text="Август"), KeyboardButton(text="Сентябрь")],
        [KeyboardButton(text=back), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)

budget_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="до 1000€")],
        [KeyboardButton(text="1000–2000€")],
        [KeyboardButton(text="2000€+")],
        [KeyboardButton(text=back), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)

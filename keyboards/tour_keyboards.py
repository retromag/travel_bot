from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.constants import BACK, EXIT

countries_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Турція"), KeyboardButton(text="Єгипет")],
        [KeyboardButton(text="Греція"), KeyboardButton(text="Свій варіант")],
        [KeyboardButton(text=BACK)]
    ],
    resize_keyboard=True
)

regions = {
        "Турція": ["Аланія", "Кемер", BACK],
        "Єгипет": ["Шарм", "Хургада", BACK],
    }

def regions_kb(country: str):
    if country not in regions:
        return None
    else:
        return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=r)] for r in regions[country]],
            resize_keyboard=True
    )

stars_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⭐⭐⭐⭐ 4")],
        [KeyboardButton(text="⭐⭐⭐⭐⭐ 5")],
        [KeyboardButton(text=BACK), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)

food_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Все Вкл"), KeyboardButton(text="Сніданки")],
        [KeyboardButton(text=BACK), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)

nights_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="7"), KeyboardButton(text="10")],
        [KeyboardButton(text=BACK), KeyboardButton(text=EXIT)],
    ],
    resize_keyboard=True
)

adults_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="2"), KeyboardButton(text="3")],
        [KeyboardButton(text=BACK), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)

children_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="0"), KeyboardButton(text="1")],
        [KeyboardButton(text=BACK), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)

place_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кишинів"), KeyboardButton(text="Варшава")],
        [KeyboardButton(text=BACK), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)

budget_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="до 1500€")],
        [KeyboardButton(text="до 3000€")],
        [KeyboardButton(text=BACK), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)

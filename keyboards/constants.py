from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


BACK = "⬅️ Назад"
EXIT = "❌ Вийти"
nav_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=BACK), KeyboardButton(text=EXIT)]
    ],
    resize_keyboard=True
)
# choose_country = "Країна відпочинку"
# region = "Регіон відпочинку"
# stars = "Категорія готелю"
month = "📅 Выберите месяц поездки:"
budget = "💰 Выберите бюджет:"
EXIT = "❌ Завершить"


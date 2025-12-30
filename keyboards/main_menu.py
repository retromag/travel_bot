# кнопки
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏖 Подобрать тур самостоятельно")],
        [KeyboardButton(text="🏨 Отели")],
        [KeyboardButton(text="💬 Проконсультироваться со специалистом")],
        [KeyboardButton(text="📞 Контакты")]
    ],
    resize_keyboard=True
)
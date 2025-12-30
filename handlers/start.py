# /start

from aiogram import types
from aiogram.filters import Command
from keyboards.main_menu import main_menu

async def start_command(message: types.Message):
    await message.answer(
        "🌍 Добро пожаловать в туристическое агентство!\n"
        "Выберите нужное действие 👇",
        reply_markup=main_menu
    )
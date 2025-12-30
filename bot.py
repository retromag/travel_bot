import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command

from config import BOT_TOKEN
from database import connect_db

from handlers.start import start_command
from handlers.consultation import (
    consultation_start,
    consultation_save,
    ConsultationState
)

from handlers.hotels import hotels_info
from handlers.contacts import contacts_info

from handlers.tour import (
    choose_tour,
    process_country,
    process_dates,
    process_budget,
    back_from_budget,
    back_from_dates,
    exit_tour,
    TourForm
)

from keyboards.constants import back, EXIT

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.message.register(start_command, Command("start"))

dp.message.register(
    consultation_start,
    lambda message: message.text == "💬 Проконсультироваться со специалистом"
)

dp.message.register(
    consultation_save,
    ConsultationState.waiting_for_question
)

dp.message.register(
    hotels_info,
    lambda message: message.text == "🏨 Отели"
)

dp.message.register(
    contacts_info,
    lambda message: message.text == "📞 Контакты"
)

dp.message.register(
    choose_tour,
    lambda message: message.text == "🏖 Подобрать тур самостоятельно"
)

dp.message.register(
    back_from_budget,
    lambda m: m.text == back,
    TourForm.budget
)

dp.message.register(
    back_from_dates,
    lambda m: m.text == back,
    TourForm.dates
)

dp.message.register(back_from_budget, lambda m: m.text == back, TourForm.budget)
dp.message.register(back_from_dates, lambda m: m.text == back, TourForm.dates)
dp.message.register(exit_tour, lambda m: m.text == EXIT, TourForm.budget)
dp.message.register(exit_tour, lambda m: m.text == EXIT, TourForm.dates)
dp.message.register(exit_tour, lambda m: m.text == EXIT, TourForm.country)

dp.message.register(process_country, TourForm.country)
dp.message.register(process_dates, TourForm.dates)
dp.message.register(process_budget, TourForm.budget)

async def main():
    await connect_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

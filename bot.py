import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command, StateFilter

from config import BOT_TOKEN
from database import connect_db

from handlers.start import start_command
from handlers.consultation import (
    consultation_start,
    ConsultationState, consultation_ack_handler,
    consultation_question_handler
)

from handlers.tour import (
    choose_tour,
    process_food,
    process_stars,
    process_adults,
    process_nights,
    process_region,
    process_children,
    process_country,
    process_dates,
    process_place,
    process_children_age,
    process_budget,
    TourForm,
    back_handler,
    exit_tour
)

from keyboards.constants import BACK, EXIT

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.message.register(start_command, Command("start"))

dp.message.register(
    consultation_start,
    lambda message: message.text == "Замовити консультацію"
)

dp.message.register(consultation_ack_handler, StateFilter(ConsultationState.waiting_for_ack))
dp.message.register(consultation_question_handler, StateFilter(ConsultationState.waiting_for_question))


dp.message.register(
    choose_tour,
    lambda m: m.text == "Залишити заявку на тур"
)

dp.message.register(exit_tour, lambda m: m.text == EXIT)
dp.message.register(back_handler, lambda m: m.text == BACK)

dp.message.register(process_country, TourForm.country)
dp.message.register(process_region, TourForm.region)
dp.message.register(process_stars, TourForm.stars)
dp.message.register(process_food, TourForm.food)
dp.message.register(process_nights, TourForm.nights)
dp.message.register(process_adults, TourForm.adults)
dp.message.register(process_children, TourForm.children)
dp.message.register(process_children_age, TourForm.children_age)
dp.message.register(process_dates, TourForm.dates)
dp.message.register(process_place, TourForm.place)
dp.message.register(process_budget, TourForm.budget)

async def main():
    await connect_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

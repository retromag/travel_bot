from aiogram import types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards.tour_keyboards import countries_kb, dates_kb, budget_kb
from keyboards.constants import choose_country, month, budget, back, EXIT
from  keyboards.main_menu import main_menu

class TourForm(StatesGroup):
    country = State()
    dates = State()
    budget = State()

async def choose_tour(message: types.Message, state: FSMContext):
    await message.answer(
        choose_country,
        reply_markup=countries_kb
    )
    await state.set_state(TourForm.country)

async def process_country(message: types.Message, state: FSMContext):
    if message.text in [back, EXIT]:
        return
    await state.update_data(country=message.text)

    await message.answer(
        month,
        reply_markup=dates_kb
    )
    await state.set_state(TourForm.dates)

async def process_dates(message: types.Message, state: FSMContext):
    if message.text in [back, EXIT]:
        return
    await state.update_data(dates=message.text)

    await message.answer(
        budget,
        reply_markup=budget_kb
    )
    await state.set_state(TourForm.budget)

async def process_budget(message: types.Message, state: FSMContext):
    if message.text in [back, EXIT]:
        return
    data = await state.get_data()

    await message.answer(
        "✅ Ваша заявка сформирована!\n\n"
        f"🌍 Страна: {data['country']}\n"
        f"📅 Месяц: {data['dates']}\n"
        f"💰 Бюджет: {message.text}\n\n"
        "Наш специалист подберёт варианты ✨",
        reply_markup=main_menu
    )

    await state.clear()

async def back_from_budget(message: types.Message, state: FSMContext):
    await message.answer(
        month,
        reply_markup=dates_kb
    )
    await state.set_state(TourForm.dates)

async def back_from_dates(message: types.Message, state: FSMContext):
    await message.answer(
        choose_country,
        reply_markup=countries_kb
    )
    await state.set_state(TourForm.country)

async def exit_tour(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "❌ Вы вышли из подбора тура.",
        reply_markup=main_menu
    )

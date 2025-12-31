from collections import defaultdict

from aiogram import types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards.tour_keyboards import (
    countries_kb,
    stars_kb, regions_kb,
    food_kb, nights_kb, adults_kb, children_kb, place_kb, budget_kb, regions)
from keyboards.constants import  month, budget, BACK, EXIT, nav_kb
from keyboards.main_menu import main_menu

class TourForm(StatesGroup):
    country = State()
    region = State()
    stars = State()
    food = State()
    nights = State()
    adults = State()
    children = State()
    children_age = State()
    dates = State()
    place = State()
    budget = State()

async def choose_tour(message: types.Message, state: FSMContext):
    await message.answer(
        "🌍 Оберіть країну:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=countries_kb
    )
    await state.set_state(TourForm.country)

async def process_country(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return
    country = message.text
    await state.update_data(country=country)
    kb = regions_kb(country)
    if kb:
        await message.answer(
            "📍 Оберіть регіон:\n(Свій варіант можно ввести з клавіиатури)",
            reply_markup=kb
        )
        await state.set_state(TourForm.region)
    else:
        await state.update_data(region="Не вказано")
        # страна введена вручную → регион пропускаем
        await message.answer(
            "⭐ Кількість зірок:\n(Свій варіант можно ввести з клавіиатури)",
            reply_markup=stars_kb
        )
        await state.set_state(TourForm.stars)

async def process_region(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return
    await state.update_data(region=message.text)

    await message.answer(
        "⭐ Кількість зірок:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=stars_kb
    )
    await state.set_state(TourForm.stars)

async def process_stars(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return
    await state.update_data(stars=message.text)

    await message.answer(
        "🍽 Тип харчування:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=food_kb
    )

    await state.set_state(TourForm.food)

async def process_food(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return
    await state.update_data(food=message.text)
    await message.answer(
        "🌙 Кількість ночей:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=nights_kb
    )
    await state.set_state(TourForm.nights)

async def process_nights(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return
    await state.update_data(nights=message.text)

    await message.answer(
        "👨‍👩‍👧 Дорослі:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=adults_kb
    )
    await state.set_state(TourForm.adults)

async def process_adults(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return

    await state.update_data(adults=message.text)

    await message.answer(
        "🧒 Кількість дітей:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=children_kb
    )
    await state.set_state(TourForm.children)

async def process_children(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return
    count = int(message.text)

    await state.update_data(children=count)
    if count == 0:
        return await process_children_age(message, state)
    await message.answer(
        "Введіть вік дітей через кому:",
    reply_markup = nav_kb
    )
    await state.set_state(TourForm.children_age)

async def process_children_age(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return

    await state.update_data(children_age=message.text)

    await message.answer(
        "📅 Дата виїзду:\n(Впишіть дату з клавіиатури, наприклад - 26.01.2026)",
        reply_markup=nav_kb
    )
    await state.set_state(TourForm.dates)

async def process_dates(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return

    await state.update_data(dates=message.text)

    await message.answer(
        "Відправлення з\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=place_kb
    )
    await state.set_state(TourForm.place)

async def process_place(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return

    await state.update_data(place=message.text)

    await message.answer(
        "💰 Бюджет:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=budget_kb
    )
    await state.set_state(TourForm.budget)

async def process_budget(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        return

    await state.update_data(budget=message.text)

    await finish_booking(message, state)

async def finish_booking(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(
        "✅ Заявка прийнята!\n\n"
        f"🌍 Країна: {data.get('country', '—')}\n"
        f"📍 Регіон: {data.get('region', '—')}\n"
        f"⭐ Зірки: {data.get('stars', '—')}\n"
        f"🍽 Харчування: {data.get('food', '—')}\n"
        f"🌙 Ночі: {data.get('nights', '—')}\n"
        f"👨‍👩‍👧 Дорослі: {data.get('adults', '—')}\n"
        f"🧒 Діти: {data.get('children', '—')}\n"
        f"📅 Дата виїзду: {data.get('dates', '—')}\n"
        f"💰 Бюджет: {data.get('budget', '—')}\n\n"
        f"Як тільки все буде готово ми відправимо вам варіанти відпочинку за найкращими цінами.",
        reply_markup=main_menu
    )

    await state.clear()

async def exit_tour(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Ви повернулись у головне меню",
        reply_markup=main_menu
    )

async def back_handler(message: types.Message, state: FSMContext):
    current = await state.get_state()
    if current == TourForm.country:
        await message.answer(
        "Ви повернулися назад",
        reply_markup=main_menu)

    elif current == TourForm.region:
        await state.set_state(TourForm.country)
        await message.answer("🌍 Оберіть країну:", reply_markup=countries_kb)

    elif current == TourForm.stars:
        data = await state.get_data()
        country = data.get("country")
        if country in regions:
            await state.set_state(TourForm.region)
            await message.answer(
                "📍 Оберіть регіон:",
                reply_markup=regions_kb(country)
            )
        else:
            # если страны нет (ввод вручную) — возвращаемся к стране
            await state.set_state(TourForm.country)
            await message.answer(
                "🌍 Оберіть країну:",
                reply_markup=countries_kb
            )

    elif current == TourForm.food:
        await state.set_state(TourForm.stars)
        await message.answer("⭐ Кількість зірок:", reply_markup=stars_kb)

    elif current == TourForm.nights:
        await state.set_state(TourForm.food)
        await message.answer("🍽 Тип харчування:", reply_markup=food_kb)

    elif current == TourForm.adults:
        await state.set_state(TourForm.nights)
        await message.answer("🌙 Кількість ночей:", reply_markup=nights_kb)

    elif current == TourForm.children:
        await state.set_state(TourForm.adults)
        await message.answer("👨‍👩‍👧 Дорослі:", reply_markup=adults_kb)

    elif current == TourForm.children_age:
        await state.set_state(TourForm.children)
        await message.answer("🧒 Кількість дітей:", reply_markup=children_kb)

    elif current == TourForm.dates:
        data = await state.get_data()
        children = data.get("children", 0)

        if children == 0:
            # возрастов не было → возвращаемся к children
            await state.set_state(TourForm.children)
            await message.answer(
                "🧒 Кількість дітей:",
                reply_markup=children_kb
            )
        else:
            # были дети → возвращаемся к возрасту
            await state.set_state(TourForm.children_age)
            await message.answer(
                "Введіть вік дітей через кому:",
                reply_markup=nav_kb
            )

    elif current == TourForm.place:
        await state.set_state(TourForm.dates)
        await message.answer("📅 Дата виїзду:", reply_markup=nav_kb)

    elif current == TourForm.budget:
        await state.set_state(TourForm.place)
        await message.answer("Відправлення з", reply_markup=place_kb)

    else:
        await message.answer("Назад неможливо", reply_markup=nav_kb)
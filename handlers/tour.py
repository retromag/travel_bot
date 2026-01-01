from collections import defaultdict

from aiogram import types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from database import tour_request_save
from keyboards.tour_keyboards import (
    countries_kb,
    stars_kb,
    regions_kb,
    food_kb,
    nights_kb,
    adults_kb,
    children_kb,
    place_kb,
    budget_kb, regions
)
from keyboards.constants import nav_kb, main_menu

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

        await message.answer(
            "⭐ Кількість зірок:\n(Свій варіант можно ввести з клавіиатури)",
            reply_markup=stars_kb
        )
        await state.set_state(TourForm.stars)

async def process_region(message: types.Message, state: FSMContext):
    await state.update_data(region=message.text)

    await message.answer(
        "⭐ Кількість зірок:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=stars_kb
    )
    await state.set_state(TourForm.stars)

async def process_stars(message: types.Message, state: FSMContext):
    await state.update_data(stars=message.text)

    await message.answer(
        "🍽 Тип харчування:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=food_kb
    )

    await state.set_state(TourForm.food)

async def process_food(message: types.Message, state: FSMContext):
    await state.update_data(food=message.text)

    await message.answer(
        "🌙 Кількість ночей:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=nights_kb
    )
    await state.set_state(TourForm.nights)

async def process_nights(message: types.Message, state: FSMContext):
    await state.update_data(nights=message.text)

    await message.answer(
        "👨‍👩‍👧 Дорослі:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=adults_kb
    )
    await state.set_state(TourForm.adults)

async def process_adults(message: types.Message, state: FSMContext):
    await state.update_data(adults=message.text)

    await message.answer(
        "🧒 Кількість дітей:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=children_kb
    )
    await state.set_state(TourForm.children)

async def process_children(message: types.Message, state: FSMContext):
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
    await state.update_data(children_age=message.text)

    await message.answer(
        "📅 Дата виїзду:\n(Впишіть дату з клавіиатури, наприклад - 26.01.2026)",
        reply_markup=nav_kb
    )
    await state.set_state(TourForm.dates)

async def process_dates(message: types.Message, state: FSMContext):
    await state.update_data(dates=message.text)

    await message.answer(
        "Відправлення з\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=place_kb
    )
    await state.set_state(TourForm.place)

async def process_place(message: types.Message, state: FSMContext):
    await state.update_data(place=message.text)

    await message.answer(
        "💰 Бюджет:\n(Свій варіант можно ввести з клавіиатури)",
        reply_markup=budget_kb
    )
    await state.set_state(TourForm.budget)

async def process_budget(message: types.Message, state: FSMContext):
    await state.update_data(budget=message.text)

    await finish_booking(message, state)

async def finish_booking(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = message.from_user

    await tour_request_save(
        user_id=user.id,
        username=user.username,
        country=data.get("country"),
        region=data.get("region"),
        stars=data.get("stars"),
        food=data.get("food"),
        nights=data.get("nights"),
        adults=int(data.get("adults")),
        children=int(data.get("children")),
        children_age=data.get("children_age"),
        dates=data.get("dates"),
        place=data.get("place"),
        budget=data.get("budget")
    )

    admin_id = 570166124
    await message.bot.send_message(
        admin_id,
        f"Нова заявка:\n"
        f"👤 {user.full_name} (@{user.username})\n"
        f"🌍 Країна: {data.get("country")}"
        f"📍 Регіон: {data.get("region")}"
        f"⭐ Зірки: {data.get("stars")}"
        f"🍽 Харчування: {data.get("food")}"
        f"🌙 Ночі: {data.get("nights")}"
        f"👨‍👩‍👧 Дорослі: {data.get("adults")}"
        f"🧒 Діти: {data.get("children")}"
        f"📅 Дата виїзду: {data.get("dates")}"
        f"💰 Бюджет: {data.get("budget")}"
    )

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

BACK_STEPS = {
    TourForm.country: (
        None,
        "Ви повернулися у головне меню",
        lambda _: main_menu
    ),
    TourForm.region: (
        TourForm.country,
        "🌍 Оберіть країну:",
        lambda _: countries_kb
    ),
    TourForm.food: (
        TourForm.stars,
        "⭐ Кількість зірок:",
        lambda _: stars_kb
    ),
    TourForm.nights: (
        TourForm.food,
        "🍽 Тип харчування:",
        lambda _: food_kb
    ),
    TourForm.adults: (
        TourForm.nights,
        "🌙 Кількість ночей:",
        lambda _: nights_kb
    ),
    TourForm.children: (
        TourForm.adults,
        "👨‍👩‍👧 Дорослі:",
        lambda _: adults_kb
    ),
    TourForm.children_age: (
        TourForm.children,
        "🧒 Кількість дітей:",
        lambda _: children_kb
    ),
    TourForm.place: (
        TourForm.dates,
        "📅 Дата виїзду:",
        lambda _: nav_kb
    ),
    TourForm.budget: (
        TourForm.place,
        "Відправлення з",
        lambda _: place_kb
    ),
}

async def back_from_dates(message: types.Message, state: FSMContext):
    data = await state.get_data()
    children = data.get("children", 0)

    if children == 0:
        await state.set_state(TourForm.children)
        await message.answer(
            "🧒 Кількість дітей:",
            reply_markup=children_kb
        )
    else:
        await state.set_state(TourForm.children_age)
        await message.answer(
            "Введіть вік дітей через кому:",
            reply_markup=nav_kb
        )

async def back_from_stars(message: types.Message, state: FSMContext):
    data = await state.get_data()
    country = data.get("country")

    if country in regions:
        await state.set_state(TourForm.region)
        await message.answer(
            "📍 Оберіть регіон:",
            reply_markup=regions_kb(country)
        )
    else:
        await state.set_state(TourForm.country)
        await message.answer(
            "🌍 Оберіть країну:",
            reply_markup=countries_kb
        )

async def back_handler(message: types.Message, state: FSMContext):
    current = await state.get_state()

    if current == TourForm.stars:
        await back_from_stars(message, state)
        return

    if current == TourForm.dates:
        await back_from_dates(message, state)
        return

    step = BACK_STEPS.get(current)
    if not step:
        await message.answer("Назад неможливо", reply_markup=nav_kb)
        return

    prev_state, text, kb_factory = step
    await state.set_state(prev_state)
    await message.answer(text, reply_markup=kb_factory(None))

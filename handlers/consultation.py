# консультация

from aiogram import types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database import save_consultation

class ConsultationState(StatesGroup):
    waiting_for_question = State()

async def consultation_handler(message: types.Message):
    await save_consultation(
        user_id=message.from_user.id,
        username=message.from_user.username,
        question=message.from_user.question
    )

    await message.answer(
        "✅ Ваша заявка отправлена!\n"
        "Наш специалист свяжется с вами в ближайшее время 📞"
    )

async def consultation_start(message: types.Message, state: FSMContext):
    await message.answer(
        "ПЛАТНА\n"
        "Платна консультація — це індивідуальний розбір вашого запиту з конкретними рекомендаціями.\n"
        "ви отримуєте:\n"
        "— аналіз напрямку під ваші дати та бюджет\n"
        "— варіанти розміщення і перельотів\n"
        "— пояснення ризиків, сезонності та підводних каменів\n"
        "— відповіді на конкретні запитання щодо бронювання\n\n"
        "При бронюванні відпочинку в нашій компанії вартість консультації входить у рахунок оплати вашої "
        "поїздки.\n"
        "Якщо ви передумали або бронюєтесь самостійно/в іншому місці — вартість консультації не повертається."
    )
    await state.set_state(ConsultationState.waiting_for_question)

async def consultation_save(message: types.Message, state: FSMContext):
    await save_consultation(
        user_id=message.from_user.id,
        username=message.from_user.username,
        question=message.text
    )

    await state.clear()

    await message.answer(
        "✅ Ваш вопрос отправлен!\n"
        "Наш специалист свяжется с вами в ближайшее время 📞"
    )

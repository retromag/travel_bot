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
        "💬 Напишите ваш вопрос специалисту.\n"
        "Опишите проблему как можно подробнее 👇"
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

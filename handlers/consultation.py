# консультация

from aiogram import types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from database import save_consultation
from keyboards.constants import nav_kb, consult_kb, BACK, EXIT, main_menu


class ConsultationState(StatesGroup):
    waiting_for_ack = State()
    waiting_for_question = State()


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
        "Якщо ви передумали або бронюєтесь самостійно/в іншому місці — вартість консультації не повертається.",
        reply_markup=consult_kb
    )
    await state.set_state(ConsultationState.waiting_for_ack)


async def consultation_ack_handler(message: types.Message, state: FSMContext):
    if message.text == "Я прочитав":

        await message.answer(
            "📩 Тепер напишіть своє питання:",
            reply_markup=nav_kb
        )

        await state.set_state(ConsultationState.waiting_for_question)

    elif message.text == "⬅ Назад":

        await state.clear()
        await message.answer(
            "Ви повернулися в головне меню",
            reply_markup=main_menu
        )

    else:
        await message.answer("❌ Оберіть кнопку нижче")

async def consultation_question_handler(message: types.Message, state: FSMContext):
    if message.text in [BACK, EXIT]:
        await state.clear()
        await message.answer("Консультація скасована.", reply_markup=main_menu)
        return

        # Сохраняем в БД
    await save_consultation(
        user_id=message.from_user.id,
        username=message.from_user.username,
        question=message.text
        )

    # Можно отправить уведомление админу
    admin_id = 570166124
    await message.bot.send_message(
        admin_id,
        f"Нова консультація:\n"
        f"👤 {message.from_user.full_name} (@{message.from_user.username})\n"
        f"❓ {message.text}"
        )

    # Ответ пользователю
    await message.answer(
        "✅ Ваша заявка відправлена!\n"
        "Наш спеціаліст з вами зв'яжеться 📞",
        reply_markup=main_menu
        )

    await state.clear()

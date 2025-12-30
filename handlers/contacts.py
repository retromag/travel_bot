from aiogram import types

async def contacts_info(message: types.Message):
    await message.answer(
        "📞 Контакты туристического агентства\n\n"
        "📍 Рим, Италия\n"
        "☎ +39 123 456 789\n"
        "📧 travel@mail.com\n"
        "🕘 Пн–Пт 09:00–18:00"
    )

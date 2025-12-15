from aiogram import Bot, Dispatcher, types

from app.config import settings
from app.llm import generate_sql
from app.services import BaseService

API_TOKEN = settings.TELEGRAM_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message()
async def handle_message(message: types.Message):
    """Обработка сообщений от пользователей"""

    user_query = message.text
    query = await generate_sql(user_query)
    result = await BaseService.execute_sql_query(query)
    await message.answer(f"Ответ: {result}")


async def bot_telegram():
    """Запускает Telegram бота"""

    await dp.start_polling(bot)

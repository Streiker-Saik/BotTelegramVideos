import aiohttp

from app.config import settings

API_URL = "https://router.huggingface.co/v1"
API_KEY = settings.HUGGING_TOKEN
MODEL = "moonshotai/Kimi-K2-Instruct-0905"

async def generate_sql(user_query: str) -> str:
    """Отправка запроса к модели Hugging Face для генерации SQL-запроса."""

    prompt = (
        "У вас есть следующие таблицы:\n"
        "- videos (id, creator_id, video_created_at, views_count, likes_count, comments_count, reports_count, "
        "created_at, updated_at)\n"
        "- video_snapshots (id, video_id, views_count, likes_count, comments_count, reports_count, delta_views_count, "
        "delta_likes_count, delta_comments_count, delta_reports_count, created_at, updated_at)\n\n"
        f"Напишите SQL-запрос для следующего вопроса: {user_query}."
    )

    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{API_URL}/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": MODEL,
                "messages": [{"role": "user", "content": prompt}],
            },
        ) as response:
            response.raise_for_status()
            result = await response.json()

            return result["choices"][0]["message"]["content"]

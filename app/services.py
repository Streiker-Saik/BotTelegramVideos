from typing import Optional, TypeVar

from sqlalchemy import select, text

from app.database import async_session_maker
from app.models import Video, VideoSnapshot

T = TypeVar("T")


class BaseService:
    """Базовый сервис запросов к БД"""

    model = None

    @classmethod
    async def add(cls, obj_data):
        """Добавление нового объекта"""
        async with async_session_maker() as session:
            obj = cls.model(**obj_data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    @classmethod
    async def find_by_id(cls, model_id: int) -> Optional[T]:
        """Получение объекта по ID"""
        async with async_session_maker() as session:
            obj = await session.get(cls.model, model_id)
            return obj

    @classmethod
    async def find_all(cls, **filter_by) -> list[T]:
        """Получение всех объектов"""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def execute_sql_query(cls, sql_query: str) -> str:
        """Выполняет SQL-запрос и возвращает результат"""
        sql_query = cls._clean_sql_query(sql_query)
        async with async_session_maker() as session:
            try:
                result = await session.execute(text(sql_query))
                return str(result.scalar())
            except Exception as e:
                return f"Ошибка выполнения SQL-запроса: {e}"

    @classmethod
    def _clean_sql_query(cls, sql_query: str) -> str:
        """Очистка SQL-запроса от лишних символов"""
        query = sql_query.replace("sql\n", "").replace("```", "").strip()
        return query


class VideoService(BaseService):
    model = Video


class VideoSnapshotsService(BaseService):
    model = VideoSnapshot

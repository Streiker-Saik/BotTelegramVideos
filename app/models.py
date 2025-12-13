from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func

from app.database import Base


class Video(Base):
    """Модель для видео"""

    __tablename__ = "videos"

    id = Column(String, primary_key=True)
    creator_id = Column(String, nullable=False)
    video_created_at = Column(DateTime)
    views_count = Column(Integer, nullable=False)
    likes_count = Column(Integer, nullable=False)
    comments_count = Column(Integer, nullable=False)
    reports_count = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class VideoSnapshot(Base):
    """Модель для почасовых замеров видео"""

    __tablename__ = "video_snapshots"

    id = Column(String, primary_key=True)
    video_id = Column(String, ForeignKey("videos.id"))
    views_count = Column(Integer, nullable=False)
    likes_count = Column(Integer, nullable=False)
    comments_count = Column(Integer, nullable=False)
    reports_count = Column(Integer, nullable=False)
    delta_views_count = Column(Integer, nullable=False)
    delta_likes_count = Column(Integer, nullable=False)
    delta_comments_count = Column(Integer, nullable=False)
    delta_reports_count = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

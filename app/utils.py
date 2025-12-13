import asyncio
import json
import os
from datetime import datetime
from typing import Any

from app.config import BASE_DIR
from app.services import VideoService, VideoSnapshotsService


def load_json(file_path: str) -> dict[str, Any]:
    """Загрузка JSON"""
    if not os.path.exists(file_path):
        return {}

    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            if not isinstance(data, dict) or "videos" not in data:
                return {}
            return data

    except json.JSONDecodeError:
        return {}


async def load_json_video_to_db(file_path: str) -> None:
    """Запись из JSON в БД статистику по роликам"""

    data = load_json(file_path)

    for video_data in data.get("videos"):
        video_id = video_data.get("id")

        if await VideoService.find_by_id(video_id):
            continue

        video_created_at = datetime.fromisoformat(video_data.get("video_created_at")).replace(tzinfo=None)
        created_at = datetime.fromisoformat(video_data.get("created_at")).replace(tzinfo=None)
        updated_at = datetime.fromisoformat(video_data.get("updated_at")).replace(tzinfo=None)

        video_data_dict = {
            "id": video_id,
            "creator_id": video_data.get("creator_id"),
            "video_created_at": video_created_at,
            "views_count": video_data.get("views_count"),
            "likes_count": video_data.get("likes_count"),
            "comments_count": video_data.get("comments_count"),
            "reports_count": video_data.get("reports_count"),
            "created_at": created_at,
            "updated_at": updated_at,
        }
        await VideoService.add(video_data_dict)


async def load_json_snapshot_to_db(file_path: str) -> None:
    """Запись из JSON в БД почасовые замеры по роликам"""

    data = load_json(file_path)

    for video_data in data.get("videos"):
        for snapshot_data in video_data.get("snapshots"):
            snapshot_id = snapshot_data.get("id")

            if await VideoSnapshotsService.find_by_id(snapshot_id):
                continue

            created_at = datetime.fromisoformat(snapshot_data.get("created_at")).replace(tzinfo=None)
            updated_at = datetime.fromisoformat(snapshot_data.get("updated_at")).replace(tzinfo=None)

            snapshot_data_dict = {
                "id": snapshot_data.get("id"),
                "video_id": snapshot_data.get("video_id"),
                "views_count": snapshot_data.get("views_count"),
                "likes_count": snapshot_data.get("likes_count"),
                "comments_count": snapshot_data.get("comments_count"),
                "reports_count": snapshot_data.get("reports_count"),
                "delta_views_count": snapshot_data.get("delta_views_count"),
                "delta_likes_count": snapshot_data.get("delta_likes_count"),
                "delta_comments_count": snapshot_data.get("delta_reports_count"),
                "delta_reports_count": snapshot_data.get("delta_comments_count"),
                "created_at": created_at,
                "updated_at": updated_at,
            }

            await VideoSnapshotsService.add(snapshot_data_dict)


if __name__ == "__main__":
    file = BASE_DIR / "data" / "videos.json"

    async def main():
        await load_json_video_to_db(file)
        await load_json_snapshot_to_db(file)

    asyncio.run(main())

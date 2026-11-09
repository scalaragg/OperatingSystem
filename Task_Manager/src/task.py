"""Модель задачи для Task Manager."""
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any


@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    status: bool = False
    author: str = ""
    created_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat(timespec="seconds")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        return cls(
            id=int(data.get("id", 0)),
            title=str(data.get("title", "")).strip(),
            description=str(data.get("description", "")).strip(),
            status=bool(data.get("status", data.get("completed", False))),
            author=str(data.get("author", "")).strip(),
            created_at=str(data.get("created_at", "")),
        )

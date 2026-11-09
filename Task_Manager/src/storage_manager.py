"""Работа с JSON-файлом. UI и бизнес-логика от файла не зависят."""
import json
from pathlib import Path
from typing import Iterable

from task import Task


class StorageManager:
    def __init__(self, filename: str | Path):
        self.filename = Path(filename)
        self.filename.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> list[Task]:
        if not self.filename.exists():
            return []

        raw = self.filename.read_text(encoding="utf-8").strip()
        if not raw:
            return []

        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return self._migrate_legacy(raw)

        if not isinstance(data, list):
            raise ValueError("JSON-файл задач должен содержать список.")

        return [Task.from_dict(item) for item in data if isinstance(item, dict)]

    def save(self, tasks: Iterable[Task]) -> None:
        data = [task.to_dict() if isinstance(task, Task) else task for task in tasks]
        temp = self.filename.with_suffix(self.filename.suffix + ".tmp")
        temp.write_text(
            json.dumps(data, ensure_ascii=False, indent=4) + "\n",
            encoding="utf-8",
        )
        temp.replace(self.filename)

    def add(self, task: Task) -> Task:
        tasks = self.load()
        tasks.append(task)
        self.save(tasks)
        return task

    def update(self, task: Task) -> Task:
        tasks = self.load()
        for index, current in enumerate(tasks):
            if current.id == task.id:
                tasks[index] = task
                self.save(tasks)
                return task
        raise ValueError(f"Задача с id={task.id} не найдена.")

    def delete(self, task_id: int) -> None:
        tasks = self.load()
        filtered = [task for task in tasks if task.id != task_id]
        if len(filtered) == len(tasks):
            raise ValueError(f"Задача с id={task_id} не найдена.")
        self.save(filtered)

    def next_id(self) -> int:
        tasks = self.load()
        return max((task.id for task in tasks), default=0) + 1

    def _migrate_legacy(self, raw: str) -> list[Task]:
        tasks = []
        for index, line in enumerate(raw.splitlines(), start=1):
            line = line.strip()
            if not line:
                continue
            if "|" in line:
                title, description = line.split("|", 1)
            else:
                title, description = line, ""
            tasks.append(Task(
                id=index,
                title=title.strip(),
                description=description.strip(),
            ))
        if tasks:
            self.save(tasks)
        return tasks

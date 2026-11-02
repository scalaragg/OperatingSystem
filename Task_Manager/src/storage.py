"""Загрузка и сохранение задач в формате JSON.

Поддерживается автоматическая миграция старого формата:
Название задачи | Описание задачи
"""
import json
from pathlib import Path


def _convert_legacy_line(line):
    """Преобразовать одну строку старого TXT-формата в словарь задачи."""
    line = line.strip()
    if not line:
        return None

    if "|" in line:
        title, description = line.split("|", 1)
        title = title.strip()
        description = description.strip()
    else:
        title = line
        description = ""

    if not title:
        return None

    return {"title": title, "description": description, "completed": False}


def load_tasks(name_file):
    """Загрузить задачи. Старый текстовый формат автоматически мигрирует в JSON."""
    path = Path(name_file)

    if not path.exists():
        return []

    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        return []

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Сохраняем исходный файл как резервную копию до преобразования.
        backup = path.with_suffix(path.suffix + ".bak")
        if not backup.exists():
            backup.write_text(raw + "\n", encoding="utf-8")

        tasks = [
            task for task in (_convert_legacy_line(line) for line in raw.splitlines())
            if task is not None
        ]
        save_tasks(tasks, path)
        return tasks

    if not isinstance(data, list):
        raise ValueError("Файл задач должен содержать JSON-массив.")

    tasks = []
    for item in data:
        if isinstance(item, str):
            converted = _convert_legacy_line(item)
            if converted:
                tasks.append(converted)
        elif isinstance(item, dict) and str(item.get("title", "")).strip():
            tasks.append({
                "title": str(item.get("title", "")).strip(),
                "description": str(item.get("description", "")).strip(),
                "completed": bool(item.get("completed", False)),
            })
    return tasks


def save_tasks(task_list, name_file):
    """Атомарно сохранить список задач в JSON UTF-8."""
    path = Path(name_file)
    path.parent.mkdir(parents=True, exist_ok=True)

    normalized = []
    for item in task_list:
        if isinstance(item, str):
            task = _convert_legacy_line(item)
            if task:
                normalized.append(task)
        elif isinstance(item, dict) and str(item.get("title", "")).strip():
            normalized.append({
                "title": str(item.get("title", "")).strip(),
                "description": str(item.get("description", "")).strip(),
                "completed": bool(item.get("completed", False)),
            })

    temporary_path = path.with_suffix(path.suffix + ".tmp")
    temporary_path.write_text(
        json.dumps(normalized, ensure_ascii=False, indent=4) + "\n",
    )
    temporary_path.replace(path)

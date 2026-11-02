"""Загрузка и сохранение списка задач."""


def load_tasks(name_file):
    """Загрузить задачи из файла. Одна задача хранится в одной строке."""
    try:
        with open(name_file, "r", encoding="utf-8") as file:
            return [line.rstrip("\n") for line in file if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(task_list, name_file):
    """Сохранить список задач в прежнем текстовом формате."""
    with open(name_file, "w", encoding="utf-8") as file:
        for task in task_list:
            file.write(f"{str(task).rstrip()}\n")

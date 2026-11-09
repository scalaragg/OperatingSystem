"""Фасад приложения: CRUD и запуск интерфейса."""
from task import Task
from storage_manager import StorageManager


class TaskManager:
    def __init__(self, storage: StorageManager, interface=None):
        self.storage = storage
        self.interface = interface

    def create_task(self, title: str, description: str = "", author: str = "") -> Task:
        title = title.strip()
        if not title:
            raise ValueError("Название задачи не может быть пустым.")

        task = Task(
            id=self.storage.next_id(),
            title=title,
            description=description.strip(),
            author=author.strip(),
        )
        return self.storage.add(task)

    def edit_task(self, task_id: int, title: str, description: str = "", author: str = "") -> Task:
        tasks = self.storage.load()
        current = next((task for task in tasks if task.id == task_id), None)
        if current is None:
            raise ValueError(f"Задача с id={task_id} не найдена.")

        title = title.strip()
        if not title:
            raise ValueError("Название задачи не может быть пустым.")

        current.title = title
        current.description = description.strip()
        current.author = author.strip()
        return self.storage.update(current)

    def delete_task(self, task_id: int) -> None:
        self.storage.delete(task_id)

    def toggle_status(self, task_id: int) -> Task:
        tasks = self.storage.load()
        current = next((task for task in tasks if task.id == task_id), None)
        if current is None:
            raise ValueError(f"Задача с id={task_id} не найдена.")

        current.status = not current.status
        return self.storage.update(current)

    def run(self):
        if self.interface is None:
            raise RuntimeError("Для запуска TaskManager нужен Interface.")
        self.interface.build()
        self.interface.show_tasks()
        self.interface.root.mainloop()

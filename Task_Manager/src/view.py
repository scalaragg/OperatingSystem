"""Функции представления данных Task Manager."""


def show_tasks(task_collection, list_widget):
    """Показать задачи в переданном пользовательском списке."""
    list_widget.show_tasks(task_collection)


def show_menu():
    """Старое консольное меню, оставлено для совместимости."""
    print("\\n1. Посмотреть задачи\\n2. Добавить задачу")
    print("3. Изменить задачу\\n4. Удалить задачу\\n5. Выход")


def show_collection(collection):
    """Старый вывод коллекции для консольной версии."""
    if not collection:
        print("Список задач пуст.")
        return
    for number, content in enumerate(collection, start=1):
        print(f"{number}. {content}")

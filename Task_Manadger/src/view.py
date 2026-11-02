"""Функции консольного представления, оставленные для старой версии."""


def show_menu():
    print("\\n1. Посмотреть задачи\\n2. Добавить задачу")
    print("3. Изменить задачу\\n4. Удалить задачу\\n5. Выход")


def show_collection(collection):
    if not collection:
        print("Список задач пуст.")
        return
    for number, content in enumerate(collection, start=1):
        print(f"{number}. {content}")

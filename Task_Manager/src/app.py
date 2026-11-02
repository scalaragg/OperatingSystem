"""Старая консольная версия приложения (не используется в основном запуске)."""
from .storage import load_tasks, save_tasks
from .view import show_menu, show_collection
from .core import add_task, edit_task, delete_tasks
from .config import NAME_FILE_SAVES
from .utils import insure_saves_file

collection = []


def app():
    insure_saves_file(NAME_FILE_SAVES)
    collection.clear()
    collection.extend(load_tasks(NAME_FILE_SAVES))

    is_running = True
    while is_running:
        show_menu()
        choice_user = input("Введите ваш выбор: ")
        match choice_user:
            case "1":
                show_collection(collection)
            case "2":
                add_task(collection)
                save_tasks(collection, NAME_FILE_SAVES)
            case "3":
                show_collection(collection)
                edit_task(collection)
                save_tasks(collection, NAME_FILE_SAVES)
            case "4":
                show_collection(collection)
                delete_tasks(collection)
                save_tasks(collection, NAME_FILE_SAVES)
            case "5":
                save_tasks(collection, NAME_FILE_SAVES)
                is_running = False
                print("До свидания!")
            case _:
                print("Такого пункта нет...")

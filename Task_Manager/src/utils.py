"""Вспомогательные функции приложения."""
import os
import sys


def check_confirm(select_task, task_list):
    """Проверить, что введён номер существующей задачи."""
    if select_task.isdigit() and 0 < int(select_task) <= len(task_list):
        return True
    if select_task.isdigit():
        print(f"Задачи с номером {select_task} нет в списке!")
    else:
        print("Введите именно номер задачи!")
    return False


def get_base_din():
    """Вернуть каталог приложения (поддерживается запуск из PyInstaller)."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.realpath(__file__))


def insure_saves_file(name_file):
    """Создать файл сохранения, если его ещё нет."""
    os.makedirs(os.path.dirname(os.path.abspath(name_file)), exist_ok=True)
    if not os.path.exists(name_file):
        with open(name_file, "w", encoding="utf-8"):
            pass

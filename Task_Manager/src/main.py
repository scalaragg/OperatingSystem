"""Точка входа в Task Manager"""
from config import NAME_FILE_SAVES
from storage_manager import StorageManager
from task_manager import TaskManager
from ui.interface import Interface


def main():
    storage = StorageManager(NAME_FILE_SAVES)
    manager = TaskManager(storage)
    Interface(manager)
    manager.run()


if __name__ == "__main__":
    main()

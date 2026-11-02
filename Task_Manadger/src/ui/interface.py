import tkinter as tk
from tkinter import messagebox

from .Button import AppButton
from .Frame import AppFrame
from .Listbox import Listbox
from config import NAME_FILE_SAVES
from storage import load_tasks


class Interface:
    def __init__(self, window_w=400, window_h=400):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root_w = window_w
        self.root_h = window_h
        self.root.geometry(f"{self.root_w}x{self.root_h}")
        self.root.minsize(320, 300)

        # Иконка необязательна: приложение должно запускаться и без неё.
        icon_path = NAME_FILE_SAVES.parent / "assets" / "icon.ico"
        if icon_path.exists():
            try:
                self.root.iconbitmap(str(icon_path))
            except tk.TclError:
                pass

        self.frames = {}
        self.buttons = []
        self.list_task = None
        self.create_interface()

    def create_interface(self):
        self.create_frames(["menu", "tasks"])
        self.create_buttons()
        self.add_listbox("tasks")
        self.frames["menu"].hide(False)
        self.frames["tasks"].hide(True)

    def create_frames(self, name_frame):
        colors = ["black", "grey"]
        for name, color in zip(name_frame, colors):
            self.frames[name] = AppFrame(
                self.root, color, self.root_w, self.root_h
            )

    def create_buttons(self):
        self.buttons.append(AppButton(
            self.frames["menu"],
            text="Посмотреть все задачи",
            command=self.show_tasks,
            width=24,
            height=3,
        ))
        self.buttons.append(AppButton(
            self.frames["tasks"],
            text="Вернуться в меню",
            command=lambda: self.command_quit("tasks", True),
        ))
        self.buttons.append(AppButton(
            self.frames["tasks"],
            text="Обновить список",
            command=self.show_all_tasks,
        ))

    def add_listbox(self, name_frame):
        self.list_task = Listbox(self.frames[name_frame])

    def show_tasks(self):
        self.command_quit("menu", True)
        self.show_all_tasks()

    def show_all_tasks(self):
        self.list_task.delete_list()
        for content in load_tasks(NAME_FILE_SAVES):
            self.list_task.add_to_list(content)

    def command_quit(self, name_frame, flag):
        if not flag:
            return
        if name_frame == "menu":
            self.frames["menu"].hide(True)
            self.frames["tasks"].hide(False)
        elif name_frame == "tasks":
            self.frames["tasks"].hide(True)
            self.frames["menu"].hide(False)

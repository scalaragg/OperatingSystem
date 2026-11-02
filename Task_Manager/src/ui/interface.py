"""Главное окно графического приложения Task Manager."""
import tkinter as tk
from pathlib import Path

from .AppButton import AppButton
from .AppLabel import AppLabel
from .AppListbox import AppListbox
from .Frame import AppFrame
from config import NAME_FILE_SAVES
from storage import load_tasks
from view import show_tasks


class Interface:
    def __init__(self, window_w=500, window_h=420):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry(f"{window_w}x{window_h}")
        self.root.minsize(360, 300)
        self.root_w = window_w
        self.root_h = window_h

        icon_path = Path(NAME_FILE_SAVES).parent / "assets" / "icon.ico"
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

    def create_frames(self, names):
        for name, color in zip(names, ("#20232b", "#20232b")):
            self.frames[name] = AppFrame(
                self.root, color, self.root_w, self.root_h
            )

    def create_buttons(self):
        AppLabel(
            self.frames["menu"],
            "Task Manager",
            font=("Arial", 22, "bold"),
            bg="#20232b",
            fg="white",
        )
        AppLabel(
            self.frames["menu"],
            "Ваш список задач в одном месте",
            font=("Arial", 11),
            bg="#20232b",
            fg="#d6d9e0",
        )
        self.buttons.append(AppButton(
            self.frames["menu"],
            text="Посмотреть все задачи",
            command=self.show_tasks,
            width=25,
            height=2,
        ))

        AppLabel(
            self.frames["tasks"],
            "Мои задачи",
            font=("Arial", 18, "bold"),
            bg="#20232b",
            fg="white",
        )
        self.buttons.append(AppButton(
            self.frames["tasks"],
            text="Обновить список",
            command=self.show_all_tasks,
        ))
        self.buttons.append(AppButton(
            self.frames["tasks"],
            text="Вернуться в меню",
            command=lambda: self.command_quit("tasks", True),
        ))

    def add_listbox(self, name_frame):
        self.list_task = AppListbox(self.frames[name_frame])

    def show_tasks(self):
        self.command_quit("menu", True)
        self.show_all_tasks()

    def show_all_tasks(self):
        tasks = load_tasks(NAME_FILE_SAVES)
        show_tasks(tasks, self.list_task)

    def command_quit(self, name_frame, flag):
        if not flag:
            return
        if name_frame == "menu":
            self.frames["menu"].hide(True)
            self.frames["tasks"].hide(False)
        elif name_frame == "tasks":
            self.frames["tasks"].hide(True)
            self.frames["menu"].hide(False)

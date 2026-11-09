"""Tkinter-прослойка приложения."""
import tkinter as tk
from tkinter import messagebox

from task_manager import TaskManager

from .AppButton import AppButton
from .AppEntry import AppEntry
from .AppLabel import AppLabel
from .AppListbox import AppListbox


class Interface:
    def __init__(self, manager: TaskManager):
        self.manager = manager
        self.manager.interface = self
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("650x520")
        self.root.minsize(500, 420)

        self.title_entry = None
        self.description_entry = None
        self.author_entry = None
        self.task_list = None
        self.status_label = None

    def build(self):
        main = tk.Frame(self.root, padx=12, pady=12)
        main.pack(fill="both", expand=True)

        AppLabel(main, "Менеджер задач",
                 font=("Arial", 20, "bold"))

        form = tk.Frame(main)
        form.pack(fill="x")

        tk.Label(form, text="Название:").pack(anchor="w")
        self.title_entry = AppEntry(form)

        tk.Label(form, text="Описание:").pack(anchor="w")
        self.description_entry = AppEntry(form)

        tk.Label(form, text="Автор:").pack(anchor="w")
        self.author_entry = AppEntry(form)

        buttons = tk.Frame(main)
        buttons.pack(fill="x", pady=5)

        AppButton(buttons, "Добавить", self.create_task)
        AppButton(buttons, "Изменить", self.edit_task)
        AppButton(buttons, "Удалить", self.delete_task)
        AppButton(buttons, "Статус", self.toggle_status)
        AppButton(buttons, "Обновить", self.show_tasks)

        self.task_list = AppListbox(main)
        self.status_label = tk.Label(main, text="", anchor="w")
        self.status_label.pack(fill="x", padx=10, pady=3)

    def get_input(self):
        return {
            "title": self.title_entry.get_input(),
            "description": self.description_entry.get_input(),
            "author": self.author_entry.get_input(),
        }

    def ask_confirm(self, message: str) -> bool:
        return messagebox.askyesno("Подтверждение", message)

    def show_tasks(self):
        tasks = self.manager.storage.load()
        self.task_list.show_tasks(tasks)
        self.status_label.config(text=f"Задач: {len(tasks)}")

    def _selected_id(self):
        task_id = self.task_list.get_selected_id()
        if task_id is None:
            messagebox.showwarning("Задача", "Сначала выберите задачу.")
        return task_id

    def create_task(self):
        try:
            data = self.get_input()
            self.manager.create_task(**data)
            self._clear_inputs()
            self.show_tasks()
        except ValueError as error:
            messagebox.showerror("Ошибка", str(error))

    def edit_task(self):
        task_id = self._selected_id()
        if task_id is None:
            return
        try:
            self.manager.edit_task(task_id, **self.get_input())
            self.show_tasks()
        except ValueError as error:
            messagebox.showerror("Ошибка", str(error))

    def delete_task(self):
        task_id = self._selected_id()
        if task_id is None:
            return
        if self.ask_confirm("Удалить выбранную задачу?"):
            try:
                self.manager.delete_task(task_id)
                self.show_tasks()
            except ValueError as error:
                messagebox.showerror("Ошибка", str(error))

    def toggle_status(self):
        task_id = self._selected_id()
        if task_id is None:
            return
        try:
            self.manager.toggle_status(task_id)
            self.show_tasks()
        except ValueError as error:
            messagebox.showerror("Ошибка", str(error))

    def _clear_inputs(self):
        for entry in (self.title_entry, self.description_entry, self.author_entry):
            entry.delete(0, tk.END)

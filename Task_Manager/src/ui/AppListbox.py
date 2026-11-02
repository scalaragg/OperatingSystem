"""Список задач с методами добавления, очистки и обновления."""
import tkinter as tk


class AppListbox(tk.Listbox):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            activestyle="dotbox",
            font=("Arial", 11),
            selectmode=tk.SINGLE,
            **kwargs,
        )
        self.pack(fill="both", expand=True, padx=12, pady=10)

    def add_to_list(self, content):
        self.insert(tk.END, content)

    def delete_list(self):
        self.delete(0, tk.END)

    def show_tasks(self, tasks):
        self.delete_list()
        if not tasks:
            self.add_to_list("Список задач пока пуст.")
            return

        for number, task in enumerate(tasks, start=1):
            title = task.get("title", "Без названия")
            description = task.get("description", "")
            status = "✓" if task.get("completed", False) else "○"
            line = f"{number}. {status} {title}"
            if description:
                line += f" — {description}"
            self.add_to_list(line)

"""Собственный Listbox для отображения задач."""
import tkinter as tk


class AppListbox(tk.Listbox):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            font=("Arial", 11),
            selectmode=tk.SINGLE,
            activestyle="dotbox",
            **kwargs,
        )
        self.pack(fill="both", expand=True, padx=10, pady=10)

    def show_tasks(self, tasks):
        self.delete(0, tk.END)
        for task in tasks:
            status = "✓" if task.status else "○"
            text = f"{task.id}. {status} {task.title}"
            if task.description:
                text += f" — {task.description}"
            if task.author:
                text += f" [{task.author}]"
            self.insert(tk.END, text)

    def get_selected_id(self):
        selection = self.curselection()
        if not selection:
            return None
        value = self.get(selection[0])
        try:
            return int(value.split(".", 1)[0])
        except (ValueError, IndexError):
            return None

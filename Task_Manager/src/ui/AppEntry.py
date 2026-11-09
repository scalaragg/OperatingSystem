"""Переиспользуемое поле ввода."""
import tkinter as tk


class AppEntry(tk.Entry):
    def __init__(self, master, **kwargs):
        super().__init__(master, font=("Arial", 11), **kwargs)
        self.pack(fill="x", padx=10, pady=5)

    def get_input(self) -> str:
        return self.get().strip()

"""Переиспользуемая кнопка приложения."""
import tkinter as tk


class AppButton(tk.Button):
    def __init__(self, master, text, command=None, width=18, height=2, **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            width=width,
            height=height,
            cursor="hand2",
            **kwargs,
        )
        self.pack(pady=4)

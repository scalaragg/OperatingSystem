"""Переиспользуемая подпись приложения."""
import tkinter as tk


class AppLabel(tk.Label):
    def __init__(self, master, text, font=("Arial", 12), bg=None, fg=None,
                 anchor="center", **kwargs):
        options = {"text": text, "font": font, "anchor": anchor}
        if bg is not None:
            options["bg"] = bg
        if fg is not None:
            options["fg"] = fg
        options.update(kwargs)
        super().__init__(master, **options)
        self.pack(pady=5)

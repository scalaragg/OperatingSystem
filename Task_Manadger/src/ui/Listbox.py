import tkinter as tk


class Listbox(tk.Listbox):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True, padx=10, pady=10)

    def add_to_list(self, content):
        self.insert(tk.END, content)

    def delete_list(self):
        self.delete(0, tk.END)

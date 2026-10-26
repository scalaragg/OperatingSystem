"""
                              === Функции для просмотра и показа задач ===

                                    === Версия приложения: 0.0.9 ===
"""

### Показ списка задач
import tkinter as tk
from storage import  load_tasks, save_tasks
from config import NAME_FILE_SAVES
collections = load_tasks([],NAME_FILE_SAVES)

def main():
    show_all_tasks()

def show_all_tasks():
    frame_menu.pack_forget()
    frame_tasks.pack()
    tasks = tk.Listbox(frame_tasks)

    for number, content in enumerate(collection):
        word = ''
        for symbol in content:
            if symbol != '|':
                word =f'{word}{symbol}'
            else:
                break
    tasks.insert(tk.END, word)
    tasks.pack()

def create_menu():
    frame_menu.pack_forget()
    frame_menu.pack()


main()
create_menu()
root.mainloop()

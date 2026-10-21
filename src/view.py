"""
                              === Функции для просмотра и показа задач ===

                                    === Версия приложения: 0.0.9 ===
"""

### Показ списка задач
import tkinter as tk
from enum import nonmember
from itertools import count

root = tk.Tk()
root.geometry('400x400')

collection = ["task_1 | create menu", "task_2 | add main", "task_3 | edit", "task_4 | delete"]


frame_menu = None
frame_tasks = None

def main():

    global frame_menu, frame_tasks

    frame_menu = tk.Frame(root, background='black', width=400, height=400)
    frame_tasks = tk.Frame(root, background='black', width=400, height=400)
    frame_menu.pack_propagate(False)
    frame_menu.pack_propagate(False)

    button_show_tasks = tk.Button(frame_menu, text="Посмотреть все задачи", command=show_all_tasks)
    button_show_tasks.pack()

    button_exit = tk.Button(frame_menu, text="Exit", command=create_menu())
    button_exit.pack()

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
root.mainloop()

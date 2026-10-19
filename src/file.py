import tkinter as tk

current = ""
stored = None
operator = None


def calculate():
    global current, stored, operator

    if stored is None or operator is None or current == "":
        return

    num1 = float(stored)
    num2 = float(current)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "%":
        if num2 == 0:
            label.config(text="Ошибка")
            current = ""
            stored = None
            operator = None
            return
        result = num1 % num2
    else:
        return

    if result == int(result):
        result = int(result)

    current = str(result)
    label.config(text=current)
    stored = None
    operator = None


def handle_input(char):
    global current, stored, operator

    if char in "0123456789":
        current += char
        label.config(text=current)

    elif char in "+-*%":
        if current != "":
            if stored is not None and operator is not None:
                calculate()
            stored = current
            current = ""
            operator = char
            label.config(text=str(stored) + " " + operator)

    elif char == "=":
        calculate()


# ====================== ИНТЕРФЕЙС ======================

root = tk.Tk()
root.geometry("320x480")
root.title("Калькулятор")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Поле вывода
header = tk.Frame(root, bg="#1e1e1e", padx=12, pady=20)
header.pack(fill="x")

label = tk.Label(
    header,
    text="0",
    font=("Segoe UI", 28, "bold"),
    bg="#1e1e1e",
    fg="white",
    anchor="e"
)
label.pack(fill="x")

# Рамка для кнопок
buttons_frame = tk.Frame(root, bg="#1e1e1e")
buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

layout = [
    # ряд 0
    ("7", 0, 0, 1), ("8", 0, 1, 1), ("9", 0, 2, 1), ("*", 0, 3, 1),
    # ряд 1
    ("4", 1, 0, 1), ("5", 1, 1, 1), ("6", 1, 2, 1), ("%", 1, 3, 1),
    # ряд 2
    ("1", 2, 0, 1), ("2", 2, 1, 1), ("3", 2, 2, 1), ("-", 2, 3, 1),
    # ряд 3
    ("0", 3, 0, 2), (".", 3, 2, 1), ("+", 3, 3, 1),   # 0 занимает 2 колонки
    # ряд 4
    ("=", 4, 0, 4),                                   # = на всю ширину
]

for text, row, col, colspan in layout:
    # Цвет кнопок
    if text in "+-*%=":
        bg = "#ff9500"
        fg = "white"
        active = "#ffb340"
    else:
        bg = "#333333"
        fg = "white"
        active = "#555555"

    btn = tk.Button(
        buttons_frame,
        text=text,
        font=("Segoe UI", 18),
        bg=bg,
        fg=fg,
        activebackground=active,
        activeforeground=fg,
        bd=0,
        relief="flat",
        command=lambda c=text: handle_input(c)
    )
    btn.grid(row=row, column=col, columnspan=colspan,
             sticky="nsew", padx=4, pady=4, ipady=12)

# Делаем ячейки одинакового размера
for i in range(5):
    buttons_frame.rowconfigure(i, weight=1)
for i in range(4):
    buttons_frame.columnconfigure(i, weight=1)

root.mainloop()
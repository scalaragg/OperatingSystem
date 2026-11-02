"""Точка входа в графическую версию Task Manager.

Файл рассчитан на запуск напрямую из PyCharm кнопкой Run.
"""
from ui.interface import Interface


def main():
    app = Interface()
    app.root.mainloop()


if __name__ == "__main__":
    main()

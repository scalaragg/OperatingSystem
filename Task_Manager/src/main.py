"""Точка входа в графическую версию Task Manager."""
from ui.Interface import Interface


def main():
    app = Interface()
    app.root.mainloop()


if __name__ == "__main__":
    main()

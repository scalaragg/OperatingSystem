"""Обратная совместимость со старым именем класса Listbox."""
from .AppListbox import AppListbox


class Listbox(AppListbox):
    pass


__all__ = ["Listbox", "AppListbox"]

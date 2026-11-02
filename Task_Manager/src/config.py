"""Настройки приложения."""
from pathlib import Path

# Файл данных находится в корне проекта (рядом с папкой src).
PROJECT_DIR = Path(__file__).resolve().parent.parent
NAME_FILE_SAVES = PROJECT_DIR / "saves.json"

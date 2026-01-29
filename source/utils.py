from datetime import datetime
from pathlib import Path

from config import LOG_FILE


def read_urls(file_path: Path) -> list[str]:
    """Lit un fichier txt et retourne la liste des URLs"""
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} n'existe pas.")
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def ensure_dir(directory: Path):
    """Crée le répertoire s'il n'existe pas"""
    directory.mkdir(parents=True, exist_ok=True)


def log(string: str):
    log_str = f"{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} : {string}"
    print(log_str)
    with open(LOG_FILE, 'a', encoding="utf-8",) as f:
        f.write(log_str + "\n")

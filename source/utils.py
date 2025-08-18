from pathlib import Path

def read_urls(file_path: Path) -> list[str]:
    """Lit un fichier txt et retourne la liste des URLs"""
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} n'existe pas.")
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def ensure_dir(directory: Path):
    """Crée le répertoire s'il n'existe pas"""
    directory.mkdir(parents=True, exist_ok=True)
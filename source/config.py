from pathlib import Path

# Racine du projet (remonte d’un niveau depuis source/)
BASE_DIR = Path(__file__).parent.parent

# Fichier contenant les URLs
URL_FILE = BASE_DIR / "data" / "urls.txt"

# Dossier de téléchargement
DOWNLOAD_DIR = BASE_DIR / "downloads"

# Fichier log (optionnel)
LOG_FILE = BASE_DIR / "log.txt"

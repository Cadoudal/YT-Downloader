#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
import os
import platform

# --- Choix du répertoire d'installation ---
install_path = input("Où voulez-vous installer YT-Downloader ? [par défaut : répertoire courant] ")
if not install_path:
    install_path = Path.cwd()
else:
    install_path = Path(install_path).expanduser()

PROJECT_DIR = install_path / "YT-Downloader"

# --- Cloner le dépôt GitHub si nécessaire ---
if not PROJECT_DIR.exists():
    print(f"Clonage du projet dans {PROJECT_DIR}...")
    subprocess.run(["git", "clone", "https://github.com/Cadoudal/YT-Downloader.git", str(PROJECT_DIR)], check=True)
else:
    print(f"Le dossier {PROJECT_DIR} existe déjà. Mise à jour du dépôt...")
    subprocess.run(["git", "-C", str(PROJECT_DIR), "pull"], check=True)

# --- Création du virtualenv ---
VENV_DIR = PROJECT_DIR / "venv"
if not VENV_DIR.exists():
    print("Création du virtualenv...")
    subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)], check=True)
else:
    print("Virtualenv déjà existant.")

# --- Détection du binaire Python dans le venv ---
if platform.system() == "Windows":
    PYTHON_BIN = VENV_DIR / "Scripts" / "python.exe"
else:
    PYTHON_BIN = VENV_DIR / "bin" / "python3"

# --- Installation des dépendances ---
REQ_FILE = PROJECT_DIR / "source" / "requirements.txt"
if not REQ_FILE.exists():
    print(f"Erreur : fichier requirements.txt introuvable : {REQ_FILE}")
    sys.exit(1)

print("Installation des dépendances...")
subprocess.run([str(PYTHON_BIN), "-m", "pip", "install", "--upgrade", "pip"], check=True)
subprocess.run([str(PYTHON_BIN), "-m", "pip", "install", "-r", str(REQ_FILE)], check=True)

print("\nInstallation terminée !")
print(f"Pour lancer le projet :\n 1. Activez le virtualenv :\n    source {VENV_DIR}/bin/activate  (Linux/macOS)\n    {VENV_DIR}\\Scripts\\activate   (Windows)\n 2. Lancez main.py :\n    python {PROJECT_DIR}/source/main.py")

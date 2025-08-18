#!/usr/bin/env python3
"""
Installateur multiplateforme pour YT-Downloader
Linux / macOS / Windows
"""

import os
import sys
import subprocess
from pathlib import Path
import platform


install_path = input("Où voulez-vous installer YT-Downloader ? [par défaut : répertoire courant] ")
if not install_path:
    install_path = Path.cwd()
else:
    install_path = Path(install_path).expanduser()

PROJECT_DIR = install_path / "YT-Downloader"
REPO_URL = "https://github.com/Cadoudal/YT-Downloader.git"
VENV_DIR = PROJECT_DIR / "venv"
REQ_FILE = PROJECT_DIR / "source" / "requirements.txt"

def run(cmd, shell=False):
    """Exécute une commande et stoppe en cas d'erreur"""
    print(f"💻 Exécution : {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    result = subprocess.run(cmd, shell=shell)
    if result.returncode != 0:
        print("❌ Une erreur est survenue. Arrêt de l'installation.")
        sys.exit(1)

def clone_or_update_repo():
    if PROJECT_DIR.exists():
        print(f"🔄 Le projet existe déjà dans {PROJECT_DIR}, mise à jour ...")
        run(["git", "-C", str(PROJECT_DIR), "pull"])
    else:
        print(f"📥 Clonage du projet dans {PROJECT_DIR} ...")
        run(["git", "clone", REPO_URL, str(PROJECT_DIR)])

def create_virtualenv():
    if not VENV_DIR.exists():
        print(f"🐍 Création de l'environnement virtuel dans {VENV_DIR} ...")
        run([sys.executable, "-m", "venv", str(VENV_DIR)])
    else:
        print(f"✅ Environnement virtuel déjà existant : {VENV_DIR}")

def install_requirements():
    if platform.system() == "Windows":
        pip_exe = VENV_DIR / "Scripts" / "pip.exe"
    else:
        pip_exe = VENV_DIR / "bin" / "pip"

    if not REQ_FILE.exists():
        print(f"❌ Fichier requirements.txt introuvable : {REQ_FILE}")
        sys.exit(1)

    print("📦 Installation des dépendances Python ...")
    run([str(pip_exe), "install", "--upgrade", "pip"])
    run([str(pip_exe), "install", "-r", str(REQ_FILE)])

def main():
    clone_or_update_repo()
    create_virtualenv()
    install_requirements()
    print("\n🎉 Installation terminée !")
    if platform.system() == "Windows":
        python_path = VENV_DIR / "Scripts" / "python.exe"
    else:
        python_path = VENV_DIR / "bin" / "python"
    print(f"Pour lancer le projet :\n  cd {PROJECT_DIR}\n  {python_path} main.py")

if __name__ == "__main__":
    main()

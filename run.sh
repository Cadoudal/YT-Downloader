#!/bin/bash

# Quitter en cas d'erreur
set -e

# Nettoyer l'écran
clear

echo "=== Lancement de YT-Downloader ==="

# Vérifier que l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo "Erreur : environnement virtuel 'venv' introuvable."
    echo "Veuillez d'abord lancer setup.sh"
    exit 1
fi

# Activer l'environnement virtuel
# shellcheck disable=SC1091
source venv/bin/activate

# Lancer le script principal
python3 source/main.py

echo "=== Fin du téléchargement ==="

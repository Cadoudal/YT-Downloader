#!/bin/bash

# Quitter en cas d'erreur
set -e

# Nettoyer l'écran
clear

echo "=== YT-Downloader Setup ==="

# 1️⃣ Créer l'environnement virtuel si inexistant
if [ ! -d "venv" ]; then
    echo "Création de l'environnement virtuel..."
    python3 -m venv venv
else
    echo "Environnement virtuel déjà existant."
fi

# 2️⃣ Activer l'environnement virtuel
echo "Activation de l'environnement virtuel..."
# shellcheck disable=SC1091
source venv/bin/activate

# 3️⃣ Installer les dépendances
echo "Installation des dépendances..."
pip install --upgrade pip
pip install -r requirements.txt

# 4️⃣ Créer les dossiers nécessaires
echo "Création des dossiers data/ et downloads/..."
mkdir -p data downloads

# 5️⃣ Vérifier urls.txt
if [ ! -f "data/urls.txt" ]; then
    echo "Veuillez ajouter vos URLs dans data/urls.txt"
else
    echo "urls.txt trouvé dans data/"
fi

echo "=== Setup terminé ==="
echo "Pour lancer le script :"
echo "source venv/bin/activate && python3 source/main.py"

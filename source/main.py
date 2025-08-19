from config import URL_FILE, DOWNLOAD_DIR, LOG_FILE
from utils import read_urls, ensure_dir
from downloader import download_audio
from converter import convert_m4a_to_mp3

def main():
    print("YT-Downloader démarré...")

    # Création du dossier de téléchargement
    ensure_dir(DOWNLOAD_DIR)

    # Lecture des URLs et téléchargement si possible
    try:
        urls = read_urls(URL_FILE)
        if urls:
            download_audio(urls, DOWNLOAD_DIR, LOG_FILE)
        else:
            print("Aucune URL trouvée dans urls.txt")
    except Exception as e:
        print(f"Erreur lecture URLs : {e}")

    # Conversion de m4a vers mp3 (toujours exécutée)
    convert_m4a_to_mp3(DOWNLOAD_DIR, LOG_FILE)

    print("Téléchargement terminé !")

if __name__ == "__main__":
    main()
from config import URL_FILE, DOWNLOAD_DIR
from utils import read_urls, ensure_dir
from downloader import download_audio

def main():
    print("YT-Downloader démarré...")

    # Lecture des URLs
    try:
        urls = read_urls(URL_FILE)
        if not urls:
            print("Aucune URL trouvée dans urls.txt")
            return
    except Exception as e:
        print(f"Erreur lecture URLs : {e}")
        return

    # Création du dossier de téléchargement
    ensure_dir(DOWNLOAD_DIR)

    # Téléchargement
    download_audio(urls, DOWNLOAD_DIR)

    print("Téléchargement terminé !")

if __name__ == "__main__":
    main()

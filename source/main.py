from config import DOWNLOAD_DIR, LOG_FILE, URL_FILE
from downloader import download
from utils import ensure_dir, read_urls


def main():

    print("YT-Downloader démarré")

    # Création du dossier de téléchargement
    ensure_dir(DOWNLOAD_DIR)

    # Lecture des URLs et téléchargement si possible
    try:
        urls = read_urls(URL_FILE)
        if urls:
            download(urls=urls, target_dir=DOWNLOAD_DIR, log_file=LOG_FILE)
        else:
            print("Aucune URL trouvée dans urls.txt")
    except Exception as e:
        print(f"Erreur lecture URLs : {e}")

    print("Travail terminé !")


if __name__ == "__main__":
    main()

from config import DOWNLOAD_DIR, URL_FILE
from downloader import download_yt, get_list_of_YouToube_instance
from utils import ensure_dir, read_urls, log


def main():

    print("YT-Downloader démarré")

    # Création du dossier de téléchargement
    ensure_dir(DOWNLOAD_DIR)

    # Lecture des URLs et téléchargement si possible
    try:
        urls = read_urls(URL_FILE)
        if urls:
            yt_list = get_list_of_YouToube_instance(urls)
        else:
            log("Aucune URL trouvée dans urls.txt")
    except Exception as e:
        log(f"Erreur lecture URLs : {e}")

    download_yt(yt_list=yt_list, target_dir=DOWNLOAD_DIR)


if __name__ == "__main__":
    main()

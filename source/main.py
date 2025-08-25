from config import DOWNLOAD_DIR, LOG_FILE, URL_FILE
from converter import convert_m4a_to_mp3
from downloader import download_audio, download_video
from utils import ensure_dir, read_urls


def main():

    print("YT-Downloader démarré")

    # Création du dossier de téléchargement
    ensure_dir(DOWNLOAD_DIR)

    # Lecture des URLs et téléchargement si possible
    try:
        urls = read_urls(URL_FILE)
        if urls:
            while True:
                print("Telecharger :")
                print("   1. La vidéo")
                print("   2. L'audio")
                print("   3. Convertir uniquement")
                choix = input("Choix : ")
                if choix == "1":
                    download_video(urls, DOWNLOAD_DIR, LOG_FILE)
                    break
                elif choix == "2":
                    download_audio(urls, DOWNLOAD_DIR, LOG_FILE)
                    break
                elif choix == "3":
                    break
                else:
                    print("Option invalide")

        else:
            print("Aucune URL trouvée dans urls.txt")
    except Exception as e:
        print(f"Erreur lecture URLs : {e}")

    # Conversion de m4a vers mp3 (toujours exécutée)
    choix = input('Voulez-vous convertir les audios en mp3 ? (o/n) : ')
    if choix == "o":
        convert_m4a_to_mp3(DOWNLOAD_DIR, LOG_FILE)

    print("Travail terminé !")


if __name__ == "__main__":
    main()

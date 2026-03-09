from utils import download_audio, display_menu

def main():

    while True:
        choix = display_menu()
        if choix == "1":
            url = input("Entrez l'URL de la vidéo YouTube: ")
            output_path = input("Entrez le chemin de sortie: ")
            download_audio(url, output_path)
        elif choix == "2":
            print("Fonction de téléchargement de vidéo à venir!")
        elif choix == "3":
            print("Au revoir!")
            break
if __name__ == "__main__":
    main()

def download_audio(url, output_path):
    import requests
    response = requests.get(url)
    with open(output_path, 'wb') as f:
        f.write(response.content)

def display_menu():
    print("Bienvenue dans YT-Downloader!".center(50, '='))
    print("1. Télécharger de l'audio")
    print("2. Télécharger de la vidéo")
    print("3. QUitter")
    choix = input("Choisir une option: ")
    return choix
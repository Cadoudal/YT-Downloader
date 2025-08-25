from pathlib import Path

from pytubefix import YouTube
from tqdm import tqdm


def download_audio(urls: list[str], target_dir: Path, log_file: Path):
    """Télécharge l'audio de chaque URL dans target_dir avec barre de progression"""

    for url in tqdm(urls, desc="Téléchargement", unit="vidéo"):
        try:
            yt = YouTube(url)
            stream = yt.streams.get_audio_only()

            if stream is None:
                print(f"⚠️ Aucun flux audio trouvé pour {yt.title}")
                continue  # passe à l'URL suivante

            stream.download(output_path=str(target_dir))

        except Exception as e:
            with open(log_file, "a") as log:
                log.write(f"DOWNLOAD FAIL: {url} : {e}\n")


def download_video(urls: list[str], target_dir: Path, log_file: Path):
    """Télécharge la vidéo de chaque URL dans target_dir avec barre de progression"""

    for url in tqdm(urls, desc="Téléchargement", unit="vidéo"):
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()

            if stream is None:
                print(f"⚠️ Aucun flux vidéo trouvé pour {yt.title}")
                continue  # passe à l'URL suivante

            stream.download(output_path=str(target_dir))

        except Exception as e:
            with open(log_file, "a") as log:
                log.write(f"DOWNLOAD FAIL: {url} : {e}\n")

from datetime import datetime
from pathlib import Path

from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress
from tqdm import tqdm


def download(urls: list[str], target_dir: Path, log_file: Path):
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
                log.write(
                    f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} | DOWNLOAD FAIL: {url} : {e}\n")


def download_video_playlist(urls: list[str], target_dir: Path, log_file: Path):
    """Télécharge les vidéos de la playlist en URL dans target_dir avec barre de progression"""

    for url in urls:
        try:
            pl = Playlist(url)
            for video in tqdm(pl.videos, desc=pl.title, unit='vidéo'):
                stream = video.streams.get_highest_resolution()
                if stream is None:
                    print(f"⚠️ Aucun flux vidéo trouvé pour {video.title}")
                    continue  # passe à l'URL suivante
                stream.download(output_path=str(target_dir))

        except Exception as e:
            with open(log_file, "a") as log:
                log.write(f"DOWNLOAD FAIL: {url} : {e}\n")

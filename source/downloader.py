from pytubefix import YouTube
from pathlib import Path
from tqdm import tqdm

def download_audio(urls: list[str], target_dir: Path):
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
            print(f"Erreur pour {url}: {e}")

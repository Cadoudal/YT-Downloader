from pathlib import Path
import ffmpeg # pyright: ignore[reportMissingImports]
from tqdm import tqdm  # Ajout de tqdm

def convert_m4a_to_mp3(directory: Path, log_file: Path):
    """Convertit tous les fichiers .m4a du dossier en .mp3 avec une barre de progression"""
    m4a_files = list(directory.glob("*.m4a"))
    for m4a_file in tqdm(m4a_files, desc="Conversion M4A → MP3"):
        mp3_file = m4a_file.with_suffix(".mp3")
        try:
            (
                ffmpeg
                .input(str(m4a_file))
                .output(str(mp3_file), audio_bitrate='192k', acodec='libmp3lame')
                .overwrite_output()
                .run(quiet=True)
            )
            tqdm.write(f"Converti : {m4a_file.name} → {mp3_file.name}")
            m4a_file.unlink()
        except ffmpeg.Error as e:
            tqdm.write(f"Erreur conversion {m4a_file.name} : {e}")
            with open(log_file, "a") as log:
                log.write(f"CONVERSION FAIL: {m4a_file.name} : {e}\n")
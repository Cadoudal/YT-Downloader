from pathlib import Path
import ffmpeg

def convert_m4a_to_mp3(directory: Path):
    """Convertit tous les fichiers .m4a du dossier en .mp3"""
    for m4a_file in directory.glob("*.m4a"):
        mp3_file = m4a_file.with_suffix(".mp3")
        try:
            (
                ffmpeg
                .input(str(m4a_file))
                .output(str(mp3_file), audio_bitrate='192k', acodec='libmp3lame')
                .overwrite_output()
                .run(quiet=True)
            )
            print(f"Converti : {m4a_file.name} → {mp3_file.name}")
            
            # Suppression du fichier .m4a original
            m4a_file.unlink()

        except ffmpeg.Error as e:
            print(f"Erreur conversion {m4a_file.name} : {e}")
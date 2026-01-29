import subprocess
from pathlib import Path

from pytubefix import Playlist, YouTube
from slugify import slugify
from utils import log


def get_list_of_YouToube_instance(urls: list[str]):
    """Reads the list of urls, and returns a list of YouTube() instances

    Args:
        urls (list[str]): list of urls from text file

    Returns:
        vid_instance (list[YouTube]): list of videos
    """
    # List of Youtube()instance made from the url that match a YT video in the file
    vid_instances = [
        YouTube(url) for url in urls if 'https://www.youtube.com/watch?v=' in url]

    # List of PLaylist()instance made from the url that match a YT video in the file
    pl_instances = [
        Playlist(url) for url in urls if 'https://www.youtube.com/playlist?list=' in url]

    # add all videos in playlists to the list of video urls

    for pl in pl_instances:
        vid_instances.extend(pl.videos)

    return vid_instances


def download_yt(yt_list: list[YouTube], target_dir: Path):

    for yt in yt_list:
        # Get the best mp4 stream for video
        video = yt.streams.filter(adaptive=True, only_video=True, file_extension="mp4").order_by(
            "resolution").desc().first()
        # Video fallback if no mp4 available
        if video is None:
            video = (yt.streams
                     .filter(adaptive=True, only_video=True)
                     .order_by("resolution").desc()
                     .first())
        # Get the best mp4 stream for audio
        audio = yt.streams.filter(
            adaptive=True, only_audio=True, file_extension="mp4").order_by("abr").desc().first()
        # fallback audio if no mp4 available
        if audio is None:
            audio = yt.streams.filter(
                adaptive=True, only_audio=True).order_by("abr").desc().first()

        if not video or not audio:
            raise RuntimeError("Aucun couple audio/vidéo adapté trouvé")

        log(f"Traitement de la vidéo {yt.title}")
        clean_video_title = slugify(yt.title, lowercase=False, separator=" ")

        # Download video stream
        log(f"\tTéléchargement de la vidéo")
        video_path = video.download(
            filename=f'{yt.title}_video_temp', output_path=target_dir)
        # Download audio stream
        log(f"\tTéléchargement de l'audio")
        audio_path = audio.download(
            filename=f'{yt.title}_audio_temp', output_path=target_dir)

        # merge audio and video
        log("\tFusion de l'audio et de la vidéo")
        output_path = target_dir.joinpath(f'{clean_video_title}.mp4')
        ffmpeg_cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel", "error",
            "-nostats",
            "-y", "-i", video_path, "-i",
            audio_path, '-c', 'copy', output_path]
        try:
            subprocess.run(ffmpeg_cmd, check=True)
            log("\tSupression des fichiers temp")
            Path(video_path).unlink()
            Path(audio_path).unlink()
        except Exception as e:
            log(e)

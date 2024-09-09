from pytube import YouTube
import os

def download_audio(video_url, output_path='downloads'):
    """
    Downloads audio from a YouTube video and saves it as a WAV file.
    
    Args:
        video_url (str): The URL of the YouTube video.
        output_path (str): Directory to save the downloaded audio.
    
    Returns:
        str: Path to the downloaded audio file.
    """
    os.makedirs(output_path, exist_ok=True)
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file_path = audio_stream.download(output_path=output_path)
    base, ext = os.path.splitext(audio_file_path)
    new_file_path = f"{base}.wav"
    os.rename(audio_file_path, new_file_path)
    return new_file_path

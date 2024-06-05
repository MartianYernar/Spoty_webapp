from pytube import YouTube
from moviepy.editor import *
import os

def download_youtube_audio(url, output_path):
    
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=output_path)
    
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    audio_clip = AudioFileClip(out_file)
    audio_clip.write_audiofile(new_file)
    audio_clip.close()
    
    
    os.remove(out_file)
    return new_file

# Video from youtube  / clip of shape of you ed sheeran for ex
url = 'https://youtu.be/JGwWNGJdvx8?si=VhQ34A6WYLDxWohG'
output_path = './downloads'
mp3_file = download_youtube_audio(url, output_path)
print(f"MP3 file saved to {mp3_file}")

# # this does not work, Error opening output files: Invalid argument
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
from dotenv import load_dotenv
load_dotenv()
from moviepy import VideoFileClip
from utils import log

log_file = os.getenv('extract_audio_log')
#writing both to daily log and global log


def extract_audio(video_path, title):
    try:
        video = VideoFileClip(video_path)
        
        audio_path = os.path.join(os.getenv('audio_folder'), f"{title}.mp3")
        print(audio_path)
        
        video.audio.write_audiofile(audio_path, codec='libmp3lame')
        video.close()
        message = "Audio extracted: {title}"
        
        log(message, log_file)
        print(f"Audio extracted: {title}.mp3")
    except Exception as e:
        print(f"An error occurred: {e}", log_file)
        

# test
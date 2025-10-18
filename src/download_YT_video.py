from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
from dotenv import load_dotenv
load_dotenv()
from moviepy import VideoFileClip
from datetime import datetime
from extract_audio import extract_audio
from utils import log


log_file = os.getenv('download_YT_log')
#writing both to daily log and global log


def download_video(video_url):
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        video = yt.streams.get_highest_resolution()
        
        out = os.getenv('video_folder')
        
        video_path = video.download(out)
        message = "Downloaded: {video.title}"
        log(message, log_file)
        return video_path
    except Exception as e:
        log(f"An error occurred: {e}", log_file)
 
# # test
if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=1yMozrDEqbg'
    video_path = download_video(url)

    if video_path:
        title = os.path.splitext(os.path.basename(video_path))[0]
        extract_audio(video_path, title)

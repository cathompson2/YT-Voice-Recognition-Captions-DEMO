from download_YT_video import download_video
from extract_audio import extract_audio, log
from pytubefix import YouTube
import os
from dotenv import load_dotenv
load_dotenv()
import time
from utils import valid_video, clearfolders, log
   

def main():
    video_folder = os.getenv('video_folder')
    audio_folder = os.getenv('audio_folder')
    
    folder = input("Would you like to clear out any audio or video files?\nA = Audio, V = Video, N = No - ").strip().lower()
    if folder == "a":
        clearfolders(audio_folder)
    if folder == "v":
        clearfolders(video_folder)
    if folder not in ["a", "v", "n"]:
        print("Not an option, continuing to next step")
        time.sleep(2)
    
    
    while True: #Confirmation check to make sure the video is both valid and the correct one
        link = input("Please provide a link to a youtube video that you want extracted, or enter E to Exit:\n" ).strip()
        if link.lower() == "e":
            print("Thank you, goodbye")
            time.sleep(1)
            break
        video = valid_video(link)
        
        if video:
            response = input(f"Video found, is this the video you would like to extract? \"{video.title}\"\nY = Yes, N = No - ").strip().lower()
            if response == "y":
                print("Beginning download")
                break
            elif response == "n":
                print("Try again") 
        else:
            print("That link is invalid, try again")
            time.sleep(1)
   
   
    video_path = download_video(link)
    
    if (video_path):
        title = os.path.splitext(os.path.basename(video_path))[0]
        extract_audio(video_path, title)
    
    
if __name__ == "__main__":
   main()
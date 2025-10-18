import os
import time
from pytubefix import YouTube
from datetime import datetime

def valid_video(url): #Validation Method
    try:
        youtube = YouTube(url)
        title = youtube.title
        return youtube
    except Exception:
        return None
    
    
def log(message, log_file):
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a' )as log:
        log.write(f'{message}, {timestamp}\n')
    print(f'Log entry added: {message}, {timestamp}')
    
    
def clearfolders(path): #Clearing folders of videos
    files = os.listdir(path)
    if not files:
        print("No files available to clear")
        return
    choice = input("Would you like to clear all files, or choose a specific one?\nA = All, S = Specific - ").strip().lower()
    
    if choice == "a":
        for filename in files:
            file_path = os.path.join(path, filename)
            os.remove(file_path)
            print(f"Removed \"{filename}\"")
            log(f"File \"{filename}\" was deleted", path)
            time.sleep(0.1)
    if choice == "s":
        for filename in files:
            file_choice = input(f"Would you like to delete \"{filename}\" \nY = Yes, N = No - ").strip().lower()
            if file_choice == "y":
                os.remove(os.path.join(path, filename))
                print(f"Removed \"{filename}\"")
                log(f"File \"{filename}\" was deleted", path)
                time.sleep(1)
        time.sleep(1)
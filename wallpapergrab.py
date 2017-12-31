import ctypes
import praw
import os
import subprocess
import requests
import shutil
import io

from pathlib import Path

print("Setting directory...")
directory_jpg = os.getcwd()
directory_jpg = directory_jpg + "/" + "image.jpg"



image_jpg=Path(directory_jpg)
if image_jpg.is_file():
        os.remove(directory_jpg)
        print("Deleting .jpg file")





r = praw.Reddit('script', user_agent='WallpaperGrab')
 
                     
print("Fetching wallpaper..")
wallpaper=r.subreddit('wallpapers').hot(limit=1)
for item in wallpaper:
        stock_URL = item.url


end = ".jpg"
if stock_URL.endswith(end):
    direct_URL = stock_URL
    
    
else:
    direct_URL = stock_URL + '.jpg'

print("Downloading wallpaper..")
print(direct_URL)
download = requests.get(direct_URL)
with io.open(directory_jpg, 'wb') as file:
        file.write(download.content)


commandCall = "pcmanfm --set-wallpaper=" + directory_jpg

subprocess.call(commandCall, shell=True)




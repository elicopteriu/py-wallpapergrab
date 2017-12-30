import ctypes
import praw
import os
import requests
import shutil
import io

from pathlib import Path

print("Setting directory...")
directory = os.getcwd()
directory += "\\" + "image.bmp"
directory_jpg = os.getcwd()
directory_jpg = directory_jpg + "\\" + "image.jpg"

print("Checking if older image exists...")
image=Path(directory)
if image.is_file():
        os.remove(directory)
        print("Deleting .bmp file")



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


os.rename('image.jpg','image.bmp')





SPI_SETDESKWALLPAPER = 0x14     #which command (20)

SPIF_UPDATEINIFILE   = 0x2 #forces instant update
src = directory #full file location
#in python 3.4 you have to add 'r' before "path\img.jpg"

print(ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, src, SPIF_UPDATEINIFILE))
#SystemParametersInfoW instead of SystemParametersInfoA (W instead of A)

print("Wallpaper set")
print("Done")



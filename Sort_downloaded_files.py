import os 
import shutil
import time
import socket
print(socket.gethostname())
os.chdir(r"C:\Users\Kaddu Livingstone\Downloads")
while True:
    for item in os.listdir():
        if item.endswith(".jpg") or item.endswith(".PNG") or item.endswith(".GIF") or item.endswith(".RAW")or item.endswith(".png") or item.endswith(".gif") or item.endswith(".raw"):
            try:
                shutil.move(item, r"C:\Users\Kaddu Livingstone\Pictures",item)
            except OSError:
                time.sleep(5)
                os.remove(item) 
        elif item.endswith(".docx") or item.endswith(".doc") or item.endswith(".pdf") or item.endswith(".wps")or item.endswith(".txt"):
            try:
                shutil.move(item, r"C:\Users\Kaddu Livingstone\Documents",item)
            except OSError:
                time.sleep(5)
                os.remove(item)
        elif item.endswith(".MP4 ") or item.endswith(".MOV") or item.endswith(".webm")or item.endswith(".mp4"):
            try:
                shutil.move(item, r"C:\Users\Kaddu Livingstone\Videos",item)
            except OSError:
                time.sleep(5)
                os.remove(item)
        elif item.endswith(".MP3 ") or item.endswith(".WAV") or item.endswith(".mp3")or item.endswith(".wav"):
            try:
                shutil.move(item, r"C:\Users\Kaddu Livingstone\Music",item)
            except OSError:
                time.sleep(5)
                os.remove(item)
    time.sleep(5)
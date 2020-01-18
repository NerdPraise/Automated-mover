from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        for filename in os.listdir(folder_to_track):
            files = filename.split(".")
            src = folder_to_track + "/" + filename
            if files[-1] == "pdf":                
                new_destination = pdf_folder + "/" + filename
            elif files[-1] == "mp4":
                new_destination = video_folder + "/" + filename
            else:
                pass
            os.rename(src, new_destination)


folder_to_track = "C:/Users/user/Desktop/cloney"
pdf_folder = "C:/Users/user/Downloads/Documents"
video_folder = "C:/Users/user/Downloads/Video"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=False)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()

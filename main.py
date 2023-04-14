import os
import logging
import time
from utils import *
from watchdog.observers import Observer
from watchdog.utils.dirsnapshot import DirectorySnapshot, DirectorySnapshotDiff
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from watchdog.events import (
    EVENT_TYPE_CREATED,
    EVENT_TYPE_DELETED,
    EVENT_TYPE_MODIFIED,
    EVENT_TYPE_MOVED
)

origin = "C:/Users/laura/OneDrive/Documents/prueba/repository"
destination = "C:/Users/laura/OneDrive/Documents/prueba"

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        or_path = event.src_path.replace("\\", "/")
        #print(or_path)
        server_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(or_path))))
        print(server_name)
        file_name = os.path.basename(or_path)
        print(file_name)
        dest_file_path = os.path.join(destination,server_name).replace("\\", "/")
        print(dest_file_path)
        extension = ('.var', '.fil', '.tdr', '.txt')
        if file_name.endswith(extension):
            shutil.copy(or_path, dest_file_path)
            print("copy")

    
    # def on_modified(self, event):
    #     if os.path.exists(path_a) and os.path.exists(path_b):
    #         mtime_a = os.stat(path_a).st_mtime
    #         mtime_b = os.stat(path_b).st_mtime
    #     if mtime_a > mtime_b:
    #         shutil.copy2(path_a, path_b)
    #         print(f"The file {path_a} has been updated in {path_b}.")
    #     elif mtime_b > mtime_a:
    #         shutil.copy2(path_b, path_a)
    #         print(f"The file {path_b} has been updated in {path_a}.")

    def on_deleted(self, event):
        or_path = event.src_path.replace("\\", "/")
        filename = os.path.basename(event.src_path)
        print(filename)
        server_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(or_path))))
        print(server_name)
        dest_file_path = os.path.join(destination,server_name, filename).replace("\\", "/")
        if(os.path.exists(dest_file_path)):
                logging.info(f"Deleting {dest_file_path}")
                removed_file = os.remove(dest_file_path)
        print("on_deleted", event.src_path)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,format="%(levelname)s | %(asctime)s | %(message)s")

    path = os.path.abspath(origin)
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
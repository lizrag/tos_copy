import os
import logging
import time
import shutil
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from watchdog.events import (
    EVENT_TYPE_CREATED,
    EVENT_TYPE_DELETED,
    EVENT_TYPE_MODIFIED,
    EVENT_TYPE_MOVED
)

origin = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
destination = "C:/Users/laura.rangelroman/Documents/folder_sync_project"

lock = threading.Lock()

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Replace backslashes with forward slashes in the source path.
        or_path = event.src_path.replace("\\", "/")
        print(or_path)
        server = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(or_path)))))
        print(server)
        # Extract the first folder name from the path
        first_dir = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(or_path))))
        print(f"{first_dir} este es el primer directorio")
        # Extract the file name from the path
        file_name = os.path.basename(or_path)
        print(file_name)
        # Extract the secind folder
        second_dir = os.path.basename(os.path.dirname(os.path.dirname(or_path)))
        print(f"{second_dir} este es el segundo directorio")
        # Extract the subdir 
        third_dir = os.path.basename(os.path.dirname(or_path))
        print(f"{third_dir} este es el tercer directorio")
        # Create a path to the target destination directory
        # dest_file_path = os.path.join(destination,server,first_dir,second_dir,third_dir).replace("\\", "/")
        
        #Ignore certain names of directories
        ignore_dirs = ['logs', 'bin', 'archive']

        #extracts the number of componentes in the path 
        num_components = len([component for component in or_path.split("/") if component])
        print(num_components)

        # Check how many components there are to create the paths
        if num_components >= 11:
            # There are 11 components, create destination path accordingly
            dest_file_path = os.path.join(destination, server, first_dir, second_dir, third_dir).replace("\\", "/")
        elif num_components <= 10:
            # There are 10 components, create destination path accordingly
            dest_file_path = os.path.join(destination,first_dir, second_dir, third_dir).replace("\\", "/")
            print(dest_file_path)
        else:
            # Handle the case where there are a different number of components
            logging.warning(f"Unexpected number of components in path: {num_components}")
            return
        
        #Ignore the directories checking each folder
        if third_dir in ignore_dirs or second_dir in ignore_dirs or first_dir in ignore_dirs:
            logging.info(f"Ignoring directory because it's in the ignore list")
            return
        
        # Creates the TOS folder if does not exist
        # subdir_parent_dir = os.path.join(destination, first_dir, second_dir).replace("\\", "/")
        # print(subdir_parent_dir)
        # if not os.path.exists(subdir_parent_dir):
        #     os.makedirs(subdir_parent_dir, exist_ok=True)

        # Creates the subdir folder if it doesn't exist
        if not os.path.exists(dest_file_path):
            os.makedirs(dest_file_path, exist_ok=True)

        # If the file that triggered the event has a valid extension and not an extension that should be include, copy it to the target directory
        extension = ('.var', '.fil', '.tdr', '.txt')
        ignore_extension = ('.log')
        if file_name.endswith(extension) and not file_name.endswith(ignore_extension):
            shutil.copy2(or_path, os.path.join(dest_file_path, file_name))
            logging.info(f"Copied {or_path} to {dest_file_path}")
            print("copy")



    def on_modified(self, event):
    # Only process files, not directories.
        if not event.is_directory:
            or_path = event.src_path.replace("\\", "/")
            # Extract the server name and the file name from the path.
            server_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(or_path))))
            file_name = os.path.basename(or_path)
            print(file_name)
            # Create a path to the target directory and replace backslashes with forward slashes
            dest_file_path = os.path.join(destination, server_name).replace("\\", "/")
            if os.path.exists(dest_file_path) and os.path.isdir(dest_file_path): # verify destination path
                extension = ('.var', '.fil', '.tdr', '.txt')
                ignore_extension = ('.log')
                if file_name.endswith(extension) and not file_name.endswith(ignore_extension):
                    # Use a lock to ensure that the file is only updated once
                    with lock:
                        # If the source file is newer, update the destination file and print a message.
                        src_mtime = os.stat(or_path).st_mtime
                        dst_file_path = os.path.join(dest_file_path, file_name).replace("\\", "/")
                        if os.path.exists(or_path) and os.path.exists(dst_file_path):
                            mtime_a = os.stat(or_path).st_mtime
                            mtime_b = os.stat(dst_file_path).st_mtime
                            if mtime_a > mtime_b:
                                shutil.copy2(or_path, dst_file_path)
                                print(f"The file {or_path} has been updated in {dst_file_path}.")
                                logging.info(f"File updated from {or_path} in {dst_file_path}")
                            else:
                                print(f"The file {or_path} has not been updated in {dst_file_path}.")
                                logging.info(f"File not updated from {or_path} in {dst_file_path}")
                else:
                    print(f"The destination path {dest_file_path} is invalid.")
                        

    def on_deleted(self, event):
        or_path = event.src_path.replace("\\", "/")
        filename = os.path.basename(event.src_path)
        print(filename)
        server_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(or_path))))
        print(server_name)
        dest_file_path = os.path.join(destination,server_name, filename).replace("\\", "/")
        # If the target file exists, delete it and print a message.
        if(os.path.exists(dest_file_path)):
                logging.info(f"Deleted {dest_file_path}")
                removed_file = os.remove(dest_file_path)




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
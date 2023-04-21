import os
import logging
import time
import shutil
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

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Replace backslashes with forward slashes in the source path.
        or_path = event.src_path.replace("\\", "/")
        print(or_path)
        # Extract the server name from the path
        server_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(or_path))))
        #print(server_name)
        # Extract the file name from the path
        file_name = os.path.basename(or_path)
        #print(file_name)
        # Extract the TOS dir
        dir_tos = os.path.basename(os.path.dirname(os.path.dirname(or_path)))
        #print(dir_tos)
        # Extract the subdir of TOS
        subdir = os.path.basename(os.path.dirname(or_path))
        #print(subdir)
        # Create a path to the target destination directory
        dest_file_path = os.path.join(destination,server_name, dir_tos, subdir).replace("\\", "/")
        #print(dest_file_path)

        # Exclude certain directories from being created
        exclude_dirs = ['logs', 'bin', 'archive']
        if dir_tos in exclude_dirs or subdir in exclude_dirs:
            logging.warning(f'Skipping {or_path} because it is in an excluded directory')
        
        # Creates the TOS folder if does not exist
        subdir_parent_dir = os.path.join(destination, server_name, dir_tos).replace("\\", "/")
        if not os.path.exists(subdir_parent_dir):
            os.makedirs(subdir_parent_dir, exist_ok=True)
        else:
            logging.error('The TOS folder could not be created')

        # Creates the subdir folder if it doesn't exist
        if not os.path.exists(dest_file_path):
            os.makedirs(dest_file_path, exist_ok=True)
        else:
            logging.error('The subdir could not be created')

        # If the file that triggered the event has a valid extension and not an extension that should be include, copy it to the target directory
        extension = ('.var', '.fil', '.tdr', '.txt')
        ignore_extension = ('.log')
        if file_name.endswith(extension) and not file_name.endswith(ignore_extension):
            shutil.copy2(or_path, os.path.join(dest_file_path, file_name))
            logging.info(f"Copied {or_path} to {dest_file_path}")
            print("copy")
        else:
            logging.error('The file could not be copied in {dest_file_path}')

    def on_modified(self, event):
        # Only process files, not directories.
        if not event.is_directory:
            or_path = event.src_path.replace("\\", "/")
            # Extract the server name and the file name from the path.
            server_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(or_path))))
            file_name = os.path.basename(or_path)
            print(file_name)
            # Create a path to the target directory and replace backslashes with forward slashes
            dest_file_path = os.path.join(destination,server_name).replace("\\", "/")
            extension = ('.var', '.fil', '.tdr', '.txt')
            ignore_extension = ('.log')
            if file_name.endswith(extension) and not file_name.endswith(ignore_extension):
                src_mtime = os.stat(or_path).st_mtime
                dst_file_path = os.path.join(dest_file_path, file_name).replace("\\", "/")
                # If the source file is newer, copy it to the destination directory and print a message.
                if os.path.exists(or_path) and os.path.exists(dest_file_path):
                        mtime_a = os.stat(or_path).st_mtime
                        mtime_b = os.stat(dest_file_path).st_mtime
                        # print(mtime_a)
                        # print(mtime_b)
                        shutil.copy2(or_path, dest_file_path)
                        print(f"The file {or_path} has been updated in {dest_file_path}.")
                        logging.info(f"File updated from {or_path} in {dest_file_path}")
            else:
                logging.error('The file could not be updated in {dest_file_path}')

    def on_deleted(self, event):
        or_path = event.src_path.replace("\\", "/")
        filename = os.path.basename(event.src_path)
        print(filename)
        server_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(or_path))))
        print(server_name)
        dest_file_path = os.path.join(destination,server_name, filename).replace("\\", "/")
        # If the target file exists, delete it and print a message.
        extension = ('.var', '.fil', '.tdr', '.txt')
        ignore_extension = ('.log')
        exclude_dirs = ['logs', 'bin', 'archive']
        # If the file that triggered the event has a valid extension and not an extension that should be ignored, delete it from the target directory, but exclude certain directories.
        if filename.endswith(extension) and not filename.endswith(ignore_extension):
            if os.path.exists(dest_file_path):
                # Check if the file is within an excluded directory
                excluded = False
                for dir in exclude_dirs:
                    if dir in dest_file_path.split('/'):
                        logging.warning(f"Skipping deletion of {dest_file_path} because it is in an excluded directory.")
                        excluded = True
                        break
                if not excluded:
                    logging.info(f"Deleted {dest_file_path}")
                    removed_file = os.remove(dest_file_path)
            else:
                logging.error(f"The file {dest_file_path} could not be deleted.")
        else:
            logging.error(f"The file {filename} could not be deleted because it has an ignored extension.")





if __name__ == '__main__':
    logging.basicConfig(filename="sync.log",level=logging.INFO,format="%(levelname)s | %(asctime)s | %(message)s")

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
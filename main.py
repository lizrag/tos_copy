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


def find_references(or_path, references):
    found_ref = False
    for ref in references:
        if ref in or_path and not found_ref:
            index = or_path.index(ref)
            # add all the components that comes after the reference
            new_route = or_path[index:]
            found_ref = True
    if not found_ref:
        new_route = or_path
    print(f"this is the {new_route}")
    return new_route


class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.events = ""
    def on_created(self, event):
        # Replace backslashes with forward slashes in the source path.
        event_t = event.event_type
        or_path = event.src_path.replace("\\", "/")
        file_name = os.path.basename(or_path)   
        #Ignore certain names of directories
        ignore_dirs = ['logs', 'bin', 'archive']
        #check for the references folders
        references = ['server_a', 'server_b', 'server_c']

        # Look for the first reference in the list of references
        new_route = find_references(or_path, references)
        print(new_route)
        # #Creates the new destination path
        dest_file_path = os.path.join(destination,new_route).replace("\\", "/")
        print(dest_file_path)     
        # # Split the new route into a list of path components
        path_components = new_route.split("/")

        # #Ignore the directories checking each folder
        skip_processing = False
        for component in path_components:
            if not skip_processing:
                if component in ignore_dirs:
                    logging.info(f"Ignoring directory {component} because it's in the ignore list")
                    skip_processing = True

        # # # # Remove the last componentonent (the file name) if it contains a dot (".")
        if "." in path_components[-1]:
            path_components = path_components[:-1]
        # Create each folder in the destination path, if it does not exist
        current_path = ""
        for comp in path_components:
            current_path = os.path.join(current_path, comp).replace("\\", "/")
            if not os.path.exists(os.path.join(destination, current_path)):
                os.makedirs(os.path.join(destination, current_path))
        

        # # # # If the file that triggered the event has a valid extension and not an extension that should be include, copy it to the target directory
        extension = ('.var', '.fil', '.tdr', '.txt')
        ignore_extension = ('.log')
        if file_name.endswith(extension) and not file_name.endswith(ignore_extension):
            print(dest_file_path)
            shutil.copy2(or_path, dest_file_path)
            logging.info(f"Copied {or_path} to {dest_file_path}")
            print("copy")
            self.events = dest_file_path



    def on_modified(self, event):
        # Replace backslashes with forward slashes in the source path.
        or_path = event.src_path.replace("\\", "/")
        file_name = os.path.basename(or_path)   
        #check for the references folders
        references = ['server_a', 'server_b', 'server_c']

        # Look for the first reference in the list of references
        new_route = find_references(or_path, references)
        print(new_route)

        #Creates the new destination path
        dest_file_path = os.path.join(destination,new_route).replace("\\", "/")
        print(dest_file_path)     
        # Split the new route into a list of path components
        path_components = new_route.split("/")

        # Remove the last componentonent (the file name) if it contains a dot (".")
        if "." in path_components[-1]:
            path_components = path_components[:-1]
        # Create each folder in the destination path, if it does not exist
        current_path = ""
        for comp in path_components:
            current_path = os.path.join(current_path, comp).replace("\\", "/")
            dest_file_path = (os.path.join(destination, current_path)).replace("\\", "/")

        if os.path.exists(dest_file_path) and os.path.isdir(dest_file_path):
                extension = ('.var', '.fil', '.tdr', '.txt')
                ignore_extension = ('.log')
                if file_name.endswith(extension) and not file_name.endswith(ignore_extension):
                    try:
                        shutil.copy2(or_path, dest_file_path)
                        print(f"The file {file_name} has been updated in {dest_file_path}.")
                        logging.info(f"File updated from {or_path} in {current_path}")
                        self.events = dest_file_path
                    except Exception as e:
                        print(f"Error copying file {file_name}: {e}")
                        logging.error(f"Error copying file {file_name}: {e}")

                        

    def on_deleted(self, event):
        # Replace backslashes with forward slashes in the source path.
        or_path = event.src_path.replace("\\", "/")
        file_name = os.path.basename(or_path)   
        #Ignore certain names of directories
        ignore_dirs = ['logs', 'bin', 'archive']
        #check for the references folders
        references = ['server_a', 'server_b', 'server_c']

        # Look for the first reference in the list of references
        new_route = find_references(or_path, references)
        print(new_route)
    
        # Split the new route into a list of path components
        path_components = new_route.split("/")    

        #Ignore the directories checking each folder
        skip_processing = False
        for component in path_components:
            if not skip_processing:
                if component in ignore_dirs:
                    logging.info(f"Ignoring directory {component} because it's in the ignore list")

        #Creates the new destination path
        dest_file_path_remove = os.path.join(destination,new_route).replace("\\", "/")
        print(f"Esta es la dest {dest_file_path_remove}") 

        # If the target file exists, delete it and print a message.
        if(os.path.exists(dest_file_path_remove)):
            try:
                os.remove(dest_file_path_remove)
                print(f"The file {file_name} has been deleted from {dest_file_path_remove}.")
                logging.info(f"File deleted from {dest_file_path_remove}")
            except Exception as e:
                print(f"Error deleting file {file_name}: {e}")
                logging.error(f"Error deleting file {file_name}: {e}")




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
import os
# import shutil
# import logging
# import tempfile
import time
from main import MyHandler
from unittest.mock import MagicMock
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pytest


# Test Case 0: Sync the starting repo structure to the server
# Expected Results: All directories and files in the initial structure should be copied to the server.


# Test Case 1: Create a file
# Expected Result: File is created on server
def test_on_created():
    # Set the directories where the Watchdog observer will listen for events and where the test file will be created
    origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
    file_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b/TOS/console"
    
    # Create an instance of the MyHandler class to handle the Watchdog events
    handler = MyHandler()
    
    # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
    origin_observer = Observer()
    origin_observer.schedule(handler, origin_route, recursive=True)
    
    # Start the observer to listen for events
    origin_observer.start()

    # Create the test file at the file_route path using the open function, write some content to it, and wait for one second to allow the observer to detect the created event
    file = os.path.join(file_route, 'test_file_8.txt')
    with open(file, 'w') as f:
        f.write('Hello, Watchdog!')
    origin_observer.join(timeout=1)

    # Stop the observer and check if the file has been created correctly by checking if the handler.events directory exists
    origin_observer.stop()
    assert os.path.exists(handler.events)




# Test Case 2: Modify a file
# Expected Result: File is modified on server
def test_on_modified():
    # Set up the observer and handler
    origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
    file_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b/TOS/console"
    handler = MyHandler()
    observer = Observer()
    observer.schedule(handler, origin_route, recursive=True)
    observer.start()

    # Wait for the observer to start
    time.sleep(1)

    # Create the file to be modified
    file_path = os.path.join(file_route, 'test_file0_11.txt')
    with open(file_path, 'w') as f:
        f.write('Hello, Watchdog!')

    # Wait for the observer to detect the creation event
    time.sleep(1)

    # Modify the file created in the previous test case
    with open(file_path, "r+") as f:
        f.write('This is a modification.')

    # Wait for the observer to detect the modification
    time.sleep(1)

    observer.stop()

    # Check if the modification event was detected
    assert os.path.exists(handler.events)




    



# # Test Case 3: Delete a file
# # Expected Result: File is deleted from server



# # Test Case 4: Create a directory
# # Expected Result: Directory is created on server



# # Test Case 5: Delete a directory
# # Expected Result: Directory is deleted from server


# # Test Case 6: Create a file with an extension that should be ignored
# # Expected Result: No changes to server



# # Test Case 7: Modify a file with an extension that should be ignored
# # Expected Result: No changes to server




# # Test Case 8: Delete a file with an extension that should be ignored
# # Expected Result: No changes to server




# Test Case 9: Create a directory that should be ignored
# Expected Result: No changes to server



# Test Case 10: Delete a directory that should be ignored
# Expected Result: No changes to server



# Test Case 11: Create/Modify/Delete a file in a sub-directory
# Expected Result: File is created/modified/deleted on server in the correct sub-directory



# Test Case 12: Create/Modify/Delete a file in a directory that should be ignored
# Expected Result: No changes to server



# Test Case 13: Verify program output and error handling for any error cases



# Test Case 14 (Bonus): Create/modify/delete files and directories.
# Expected Result: Verify alerts are sent out via email.  Confirm contents and frequency of these alerts are in line with expectations.
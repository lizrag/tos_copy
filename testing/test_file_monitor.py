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
# def test_on_created():
#     # Set the directories where the Watchdog observer will listen for events and where the test file will be created
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     file_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b/TOS/console"
    
#     # Create an instance of the MyHandler class to handle the Watchdog events
#     handler = MyHandler()
    
#     # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
#     origin_observer = Observer()
#     origin_observer.schedule(handler, origin_route, recursive=True)
    
#     # Start the observer to listen for events
#     origin_observer.start()

#     # Create the test file at the file_route path using the open function, write some content to it, and wait for one second to allow the observer to detect the created event
#     file = os.path.join(file_route, 'test_file_8.txt')
#     with open(file, 'w') as f:
#         f.write('Hello, Watchdog!')
#     origin_observer.join(timeout=1)

#     # Stop the observer and check if the file has been created correctly by checking if the handler.events directory exists
#     origin_observer.stop()
#     assert os.path.exists(handler.events)




# Test Case 2: Modify a file
# Expected Result: File is modified on server
# def test_on_modified():
#     # Set up the observer and handler
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     file_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b/TOS/console"
#     handler = MyHandler()
#     observer = Observer()
#     observer.schedule(handler, origin_route, recursive=True)
#     observer.start()

#     # Create the file to be modified
#     file_path = os.path.join(file_route, 'test_file0_11.txt')
#     with open(file_path, 'w') as f:
#         f.write('Hello, Watchdog!\n')
#         f.write('This is a modified file')

#     # Wait for the observer to detect the modification
#     time.sleep(1)

#     observer.stop()

#     # Check if the modification event was detected
#     #assert os.path.exists(handler.events)
#     assert handler.event_type == 'modified'



# # Test Case 3: Delete a file
# # Expected Result: File is deleted from server
# def test_on_deleted():
#     # Set the directories where the Watchdog observer will listen for events and where the test file will be created
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     file_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b/TOS/console"

#     # Create an instance of the MyHandler class to handle the Watchdog events
#     handler = MyHandler()

#     # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
#     origin_observer = Observer()
#     origin_observer.schedule(handler, origin_route, recursive=True)

#     # Start the observer to listen for events
#     origin_observer.start()

#     # Create the test file at the file_route path using the open function, write some content to it, and wait for one second to allow the observer to detect the created event
#     file = os.path.join(file_route, 'test_file_delete.txt')
#     with open(file, 'w') as f:
#         f.write('This is a test!')
#     origin_observer.join(timeout=1)

#     # Delete the test file and wait for one second to allow the observer to detect the deleted event
#     os.remove(file)
#     origin_observer.join(timeout=1)

#     # Stop the observer and check if the file has been deleted correctly by checking if the handler.events directory doesn't exist
#     origin_observer.stop()
#     assert not os.path.exists(handler.events)



# # Test Case 4: Create a directory
# # Expected Result: Directory is created on server
# def test_on_created_dir():
#     # Set the directories where the Watchdog observer will listen for events and where the test file will be created
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     dir_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_a/TOS"
    
#     # Create an instance of the MyHandler class to handle the Watchdog events
#     handler = MyHandler()
    
#     # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
#     origin_observer = Observer()
#     origin_observer.schedule(handler, origin_route, recursive=True)
    
#     # Start the observer to listen for events
#     origin_observer.start()

#     # Create the test directory at the dir_route path using os.makedirs() function and wait for one second to allow the observer to detect the created event
#     test_dir = os.path.join(dir_route, 'test_dir')
#     os.makedirs(test_dir)
#     origin_observer.join(timeout=1)

#     # Stop the observer and check if the directory has been created correctly by checking if the handler.events directory exists
#     origin_observer.stop()
#     assert os.path.exists(handler.events)



# # Test Case 5: Delete a directory
# # Expected Result: Directory is deleted from server


# Test Case 6: Create a file with an extension that should be ignored
# Expected Result: No changes to server
# def test_on_created_ignored():
#     # Set the directories where the Watchdog observer will listen for events and where the test file will be created
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     file_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b/TOS/console"
#     dest_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/server_b/TOS/console"

#     # Create an instance of the MyHandler class to handle the Watchdog events
#     handler = MyHandler()

#     # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
#     origin_observer = Observer()
#     origin_observer.schedule(handler, origin_route, recursive=True)

#     # Start the observer to listen for events
#     origin_observer.start()

#     # Create the test file at the file_route path using the open function, write some content to it, and wait for one second to allow the observer to detect the created event
#     file = os.path.join(file_route, 'test_file_8.log')
#     with open(file, 'w') as f:
#         f.write('Test content')

#     # Stop the observer
#     origin_observer.stop()

#     # Check that the file was not copied to dest_route
#     file_dest = os.path.join(dest_route, 'test_file_8.log')
#     assert not os.path.exists(file_dest)



# # Test Case 7: Modify a file with an extension that should be ignored
# # Expected Result: No changes to server
# def test_on_modified_ignored():
#     # Set the directories where the Watchdog observer will listen for events and where the test file will be created
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     file_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b/TOS/console"
#     dest_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/server_b/TOS/console"

#     # Create an instance of the MyHandler class to handle the Watchdog events
#     handler = MyHandler()

#     # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
#     origin_observer = Observer()
#     origin_observer.schedule(handler, origin_route, recursive=True)

#     # Start the observer to listen for events
#     origin_observer.start()

#     # Create the test file at the file_route path using the open function, write some content to it
#     file = os.path.join(file_route, 'test_file.log')
#     with open(file, 'w') as f:
#         f.write('Test content')

#     # Wait for one second to allow the observer to detect the created event
#     time.sleep(1)

#     # Modify the test file by appending some more content to it, and wait for one second to allow the observer to detect the modified event
#     with open(file, 'a') as f:
#         f.write('This is a modified file')
#     time.sleep(1)

#     # Stop the observer
#     origin_observer.stop()

#     # Check that the file was not copied to dest_route
#     file_dest = os.path.join(dest_route, 'test_file.log')
#     assert not os.path.exists(file_dest)

#     # Check that the handler received a "modified" event
#     assert handler.event_type == 'modified'



# # Test Case 8: Delete a file with an extension that should be ignored
# # Expected Result: No changes to server
# def test_on_deleted_ignored():
#     # Set the directories where the Watchdog observer will listen for events and where the test file will be created
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     file_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b/TOS/console"
#     dest_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/server_b/TOS/console"

#     # Create an instance of the MyHandler class to handle the Watchdog events
#     handler = MyHandler()

#     # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
#     origin_observer = Observer()
#     origin_observer.schedule(handler, origin_route, recursive=True)

#     # Start the observer to listen for events
#     origin_observer.start()

#     # Create the test file at the file_route path using the open function, write some content to it
#     file = os.path.join(file_route, 'test_file_8.log')
#     with open(file, 'w') as f:
#         f.write('Test content')

#     # Remove the test file and wait for one second to allow the observer to detect the deletion event
#     os.remove(file)
#     time.sleep(1)

#     # Stop the observer and check if the file was not copied to dest_route
#     origin_observer.stop()
#     file_dest = os.path.join(dest_route, 'test_file_8.log')
#     assert not os.path.exists(file_dest)



# Test Case 9: Create a directory that should be ignored
# Expected Result: No changes to server
# def test_on_created_ignoredir():
#     # Set the directories where the Watchdog observer will listen for events and where the test file will be created
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     dir_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_a/TOS/bin"
    
#     # Create an instance of the MyHandler class to handle the Watchdog events
#     handler = MyHandler()
    
#     # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
#     origin_observer = Observer()
#     origin_observer.schedule(handler, origin_route, recursive=True)
    
#     # Start the observer to listen for events
#     origin_observer.start()

#     file = os.path.join(dir_route, 'test9.txt')
#     with open(file, 'w') as f:
#         f.write('Hello, Watchdog!')

#     origin_observer.join(timeout=1)

#     # Stop the observer and check if the directory has ignored correctly by checking if the handler.events directory exists
#     origin_observer.stop()
#     assert not os.path.exists(handler.events)



# Test Case 10: Delete a directory that should be ignored
# Expected Result: No changes to server
# def test_create_and_delete_ignored_file():
#     # Set the directories where the Watchdog observer will listen for events and where the test file will be created
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     dir_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_c/TOS/logs"

#     # Create an instance of the MyHandler class to handle the Watchdog events
#     handler = MyHandler()

#     # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
#     origin_observer = Observer()
#     origin_observer.schedule(handler, origin_route, recursive=True)

#     # Start the observer to listen for events
#     origin_observer.start()

#     # Create the test file at the dir_route path using the open function, write some content to it
#     file = os.path.join(dir_route, 'test_file.txt')
#     with open(file, 'w') as f:
#         f.write('Test content')

#     # Remove the test file and wait for one second to allow the observer to detect the deletion event
#     os.remove(file)
#     time.sleep(1)

#     # Stop the observer and check if the destination route is still empty
#     origin_observer.stop()
#     assert not os.path.exists(handler.events)


# Test Case 11: Create/Modify/Delete a file in a sub-directory
# Expected Result: File is created/modified/deleted on server in the correct sub-directory
# def test_on_subdirectory():
#     # Set the directories where the Watchdog observer will listen for events and where the test file will be created
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     file_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b/TOS/Raven/var"

#     # Create an instance of the MyHandler class to handle the Watchdog events
#     handler = MyHandler()

#     # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
#     origin_observer = Observer()
#     origin_observer.schedule(handler, origin_route, recursive=True)

#     # Start the observer to listen for events
#     origin_observer.start()

#     # Create the test file at the file_route path using the open function, write some content to it, and wait for one second to allow the observer to detect the created event
#     file = os.path.join(file_route, 'test_file.var')
#     with open(file, 'w') as f:
#         f.write('Test content')
#     time.sleep(1)

#     # Modify the test file by appending some text to it, and wait for one second to allow the observer to detect the modified event
#     with open(file, 'a') as f:
#         f.write(' This is a modification')
#     time.sleep(1)

#     # Remove the test file and wait for one second to allow the observer to detect the deleted event
#     os.remove(file)
#     time.sleep(1)

#     # Stop the observer and check if the file has been created, modified, and deleted correctly by checking if the handler.events 
#     origin_observer.stop()
#     assert not os.path.exists(handler.events)



# Test Case 12: Create/Modify/Delete a file in a directory that should be ignored
# Expected Result: No changes to server
# def test_on_ignoresubdirectory():
#     # Set the directories where the Watchdog observer will listen for events and where the test file will be created
#     origin_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository"
#     file_route = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b/TOS/logs"

#     # Create an instance of the MyHandler class to handle the Watchdog events
#     handler = MyHandler()

#     # Create an instance of the Watchdog Observer class and schedule the MyHandler instance to handle events in the origin_route directory
#     origin_observer = Observer()
#     origin_observer.schedule(handler, origin_route, recursive=True)

#     # Start the observer to listen for events
#     origin_observer.start()

#     # Create the test file at the file_route path using the open function, write some content to it, and wait for one second to allow the observer to detect the created event
#     file = os.path.join(file_route, 'test_file01.log')
#     with open(file, 'w') as f:
#         f.write('Test content')
#     time.sleep(1)

#     # Modify the test file by appending some text to it, and wait for one second to allow the observer to detect the modified event
#     with open(file, 'a') as f:
#         f.write(' This is a modification')
#     time.sleep(1)

#     # Remove the test file and wait for one second to allow the observer to detect the deleted event
#     os.remove(file)
#     time.sleep(1)

#     # Stop the observer and check if the file has been created, modified, and deleted correctly by checking if the handler.events 
#     origin_observer.stop()
#     assert not os.path.exists(handler.events)


# Test Case 13: Verify program output and error handling for any error cases



# Test Case 14 (Bonus): Create/modify/delete files and directories.
# Expected Result: Verify alerts are sent out via email.  Confirm contents and frequency of these alerts are in line with expectations.
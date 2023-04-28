import os
import shutil
import logging
import tempfile
import time
from main import MyHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def test_on_created(tmpdir):
    # Create a temporary source file
    src_file = os.path.join(tmpdir, 'test.txt')
    with open(src_file, 'w') as f:
        f.write('Test file')

    # Set up the destination directory
    dest_dir = os.path.join(tmpdir, 'destination')
    os.makedirs(dest_dir)

    # Set up the event handler
    handler = MyHandler()
    handler.destination = dest_dir

    # Call the on_created method with the created file event
    event = FileSystemEventHandler()
    handler.on_created(event)

    # Assert that the file was copied to the destination directory
    dest_file = os.path.join(dest_dir, 'test.txt')
    assert os.path.exists(dest_file)
    with open(dest_file, 'r') as f:
        assert f.read() == 'Test file'


# Test Case 0: Sync the starting repo structure to the server
# Expected Results: All directories and files in the initial structure should be copied to the server.


# Test Case 1: Create a file
# Expected Result: File is created on server
# def test_create_file(tmpdir):
#     with tempfile.TemporaryDirectory() as dir:
#         handler = MyHandler()
#         def on_created(event):
#             assert event.is_directory is False
#             assert event.event_type == "created"
#             assert event.src_path == os.path.join(dir, "text.txt")
#         handler.on_created = on_created
#         observer = Observer()
#         observer.schedule(handler, path=dir, recursive=False)
#         observer.start()
#         with open(os.path.join(dir, "text.txt"), "w") as f:
#             f.write("text")
#         observer.stop()
#         observer.join()
    #assert False


# Test Case 2: Modify a file
# Expected Result: File is modified on server
# def test_modify_file(tmpdir):
#     with tempfile.TemporaryDirectory() as dir:
#         handler = MyHandler()
#         def on_modified(event):
#             assert not event.is_directory
#             assert event.event_type == "modified"
#             assert event.src_path == os.path.join(dir, "text.txt")
#         handler.on_modified = on_modified
#         observer = Observer()
#         observer.schedule(handler, path=dir, recursive=False)
#         observer.start()
#         with open(os.path.join(dir, "text.txt"), "w+") as f:
#             f.write("text")
#             time.sleep(1)
#             f.write("new text")

#         time.sleep(1)
#         observer.stop()
#         observer.join()


# # Test Case 3: Delete a file
# # Expected Result: File is deleted from server

def test_delete_file(tmpdir):
    with tempfile.TemporaryDirectory() as dir:
        handler = MyHandler()
        def on_deleted(event):
            assert not event.is_directory
            assert event.event_type == "deleted"
            assert event.src_path == os.path.join(dir, "text.txt")
        handler.on_deleted = on_deleted
        observer = Observer()
        observer.schedule(handler, path=dir, recursive=False)
        observer.start()
        with open(os.path.join(dir, "text.txt"), "w") as f:
            f.write("text")
        time.sleep(1)
        os.remove(os.path.join(dir, "text.txt"))
        time.sleep(1)
        observer.stop()
#         observer.join()


# # Test Case 4: Create a directory
# # Expected Result: Directory is created on server
# def test_create_directory(tmpdir):
#     with tempfile.TemporaryDirectory() as dir:
#         handler = FileSystemEventHandler()
#         def on_created(event):
#             assert event.is_directory
#             assert event.event_type == "created"
#             assert event.src_path == os.path.join(dir, "testdir")
#         handler.on_created = on_created
#         observer = Observer()
#         observer.schedule(handler, path=dir, recursive=False)
#         observer.start()
#         os.mkdir(os.path.join(dir, "testdir"))
#         time.sleep(1)
#         observer.stop()
#         observer.join()


# # Test Case 5: Delete a directory
# # Expected Result: Directory is deleted from server
# def test_delete_directory(tmpdir):
#     with tempfile.TemporaryDirectory() as dir:
#         handler = FileSystemEventHandler()
#         def on_deleted(event):
#             assert not event.is_directory
#             assert event.event_type == "deleted"
#             assert event.src_path == os.path.join(dir, "testdir")
#             handler.on_deleted = on_deleted
#             observer = Observer()
#             observer.schedule(handler, path=dir, recursive=False)
#             observer.start()
#             os.mkdir(os.path.join(dir, "testdir"))

#             time.sleep(1)
#             os.rmdir(os.path.join(dir, "testdir"))
#             time.sleep(1)
#             observer.stop()
#             observer.join()

# # Test Case 6: Create a file with an extension that should be ignored
# # Expected Result: No changes to server
# def test_ignore_files_with_specific_extension(tmpdir):
#     with tempfile.TemporaryDirectory() as dir:
#         # Crea un archivo con la extensión .log
#         with open(os.path.join(dir, "text.log"), "w") as f:
#             f.write("text")
#         handler = FileSystemEventHandler()
#         events = []
#         def on_created(event):
#             ignore_extension = ('.log')
#             if event.is_directory is False and event.src_path.endswith(ignore_extension):
#                 print(f"The file {event.src_path} was not copied because it has the extension {ignore_extension}")
#             else:
#                 events.append(event)
#         handler.on_created = on_created
#         observer = Observer()
#         observer.schedule(handler, path=dir, recursive=False)
#         observer.start()
#         time.sleep(1)
#         observer.stop()
#         observer.join()


# # Test Case 7: Modify a file with an extension that should be ignored
# # Expected Result: No changes to server
# def test_ignore_modified_files_with_specific_extension(tmpdir):
#     with tempfile.TemporaryDirectory() as dir:
#         with open(os.path.join(dir, "text.var"), "w") as f:
#             f.write("text")
#         with open(os.path.join(dir, "text.log"), "w") as f:
#             f.write("text")
#         handler = FileSystemEventHandler()
#         events = []
#         def on_modified(event):
#             ignore_extension = ('.log')
#             if event.is_directory is False and event.src_path.endswith(ignore_extension):
#                 print(f"The file {event.src_path} was not copied because it has the extension {ignore_extension}")
#             else:
#                 events.append(event)
#         handler.on_modified = on_modified
#         observer = Observer()
#         observer.schedule(handler, path=dir, recursive=False)
#         observer.start()
#         time.sleep(1)
#         with open(os.path.join(dir, "text.log"), "a") as f:
#             f.write("more text")
#         time.sleep(1)
#         observer.stop()
#         observer.join()

#         assert not events, f"Unexpected events: {events}"



# # Test Case 8: Delete a file with an extension that should be ignored
# # Expected Result: No changes to server
# def test_ignore_deleted_files_with_specific_extension(tmpdir):
#     with tempfile.TemporaryDirectory() as dir:
#         with open(os.path.join(dir, "text.var"), "w") as f:
#             f.write("text")
#         with open(os.path.join(dir, "text.log"), "w") as f:
#             f.write("text")
#         handler = FileSystemEventHandler()
#         events = []
#         def on_deleted(event):
#             ignore_extension = ('.log')
#             if event.is_directory is False and event.src_path.endswith(ignore_extension):
#                 print(f"The file {event.src_path} was not copied because it has the extension {ignore_extension}")
#             else:
#                 events.append(event)
#         handler.on_deleted = on_deleted
#         observer = Observer()
#         observer.schedule(handler, path=dir, recursive=False)
#         observer.start()
#         time.sleep(1)
#         os.remove(os.path.join(dir, "text.log"))
#         time.sleep(1)

#         observer.stop()
#         observer.join()

#         assert not events, f"Unexpected events: {events}"



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
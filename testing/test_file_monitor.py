import shutil
import os
import pytest
import tempfile
from main import *
from watchdog.events import FileSystemEvent

# @pytest.fixture
# def handler():
#     return MyHandler()

# def test_on_created(handler, capsys):
#     # Create test file in source directory
#     test_file = os.path.join(origin, "test.txt")
#     with open(test_file, "w") as f:
#         f.write("test")

#     # Trigger on_created event
#     event = FileSystemEvent(test_file)
#     handler.on_created(event)

#     # Check if file was copied to destination
#     dest_file = os.path.join(destination, "repository", "Documents", "folder_sync_project", "test.txt")
#     assert os.path.exists(dest_file)

#     # Check if program outputs correct message
#     captured = capsys.readouterr()
#     expected_output = "Copied {} to {}\n".format(test_file, dest_file)
#     assert captured.out == expected_output


# Define the paths for testing


# Test Case 0: Sync the starting repo structure to the server
# Expected Results: All directories and files in the initial structure should be copied to the server.


# Test Case 1: Create a file
# Expected Result: File is created on server, program outputs list of files that were created
def test_create_file(tmpdir):
    with tempfile.TemporaryDirectory() as dir:
        handler = FileSystemEventHandler()
        def on_created(event):
            assert event.is_directory is False
            assert event.event_type == "created"
            assert event.src_path == os.path.join(dir, "text.txt")
        handler.on_created = on_created
        observer = Observer()
        observer.schedule(handler, path=dir, recursive=False)
        observer.start()
        with open(os.path.join(dir, "text.txt"), "w") as f:
            f.write("text")
        observer.stop()
        observer.join()
    #assert False

    

# Test Case 2: Modify a file
# Expected Result: File is modified on server, program outputs list of files that were changed



# Test Case 3: Delete a file
# Expected Result: File is deleted from server, program outputs list of files that were deleted



# Test Case 4: Create a directory
# Expected Result: Directory is created on server, program outputs list of directories that were created



# Test Case 5: Delete a directory
# Expected Result: Directory is deleted from server, program outputs list of directories that were deleted



# Test Case 6: Create a file with an extension that should be ignored
# Expected Result: No changes to server



# Test Case 7: Modify a file with an extension that should be ignored
# Expected Result: No changes to server



# Test Case 8: Delete a file with an extension that should be ignored
# Expected Result: No changes to server



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
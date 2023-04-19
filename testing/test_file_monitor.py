import os
import shutil
import pytest
from main import MyHandler


# Test Case 0: Sync the starting repo structure to the server
# Expected Results: All directories and files in the initial structure should be copied to the server.



# Test Case 1: Create a file
# Expected Result: File is created on server, program outputs list of files that were created
@pytest.fixture
def my_handler_instance(tmpdir):
    # Create a temporary folder to use as the destination folder
    destination = str(tmpdir.mkdir("destination"))
    return MyHandler()

def test_create_file(my_handler_instance):
    # Define the test file path
    file_name = "test_file.txt"
    test_file_path = os.path.join(my_handler_instance.destination, file_name)

    # Call the on_created method to create the file
    my_handler_instance.on_created(event=MockEvent(test_file_path))

    # Check that the file was created
    assert os.path.exists(test_file_path)

    # Check that the program outputs the list of files that were created
    assert my_handler_instance.list_files() == [file_name]

class MockEvent:
    def __init__(self, src_path):
        self.src_path = src_path



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
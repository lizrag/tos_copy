    # def on_created(self, event):
    #     # Replace backslashes with forward slashes in the source path.
    #     or_path = event.src_path.replace("\\", "/")
    #     print(or_path)
    #     server = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(or_path)))))
    #     print(server)
    #     # Extract the server name from the path
    #     first_dir = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(or_path))))
    #     print(first_dir)
    #     # Extract the file name from the path
    #     file_name = os.path.basename(or_path)
    #     print(file_name)
    #     # Extract the TOS dir
    #     second_dir = os.path.basename(os.path.dirname(os.path.dirname(or_path)))
    #     print(second_dir)
    #     # Extract the subdir of TOS
    #     third_dir = os.path.basename(os.path.dirname(or_path))
    #     print(third_dir)
    #     # Create a path to the target destination directory
    #     dest_file_path = os.path.join(destination,server,first_dir,second_dir,third_dir).replace("\\", "/")
    #     print(dest_file_path)
    #     ignore_dirs = ['logs', 'bin', 'archive']

    #     path_components = or_path.split(or_path)
    #     print(path_components)
    #     num_components = len([component for component in or_path.split("/") if component])
    #     print(num_components)

        # if third_dir in ignore_dirs or second_dir in ignore_dirs:
        #     logging.info(f"Ignoring directory '{third_dir}' because it's in the ignore list")
        #     return
        
        # # Creates the TOS folder if does not exist
        # subdir_parent_dir = os.path.join(destination, first_dir, second_dir).replace("\\", "/")
        # if not os.path.exists(subdir_parent_dir):
        #     os.makedirs(subdir_parent_dir, exist_ok=True)

        # # Creates the subdir folder if it doesn't exist
        # if not os.path.exists(dest_file_path):
        #     os.makedirs(dest_file_path, exist_ok=True)

        # # If the file that triggered the event has a valid extension and not an extension that should be include, copy it to the target directory
        # extension = ('.var', '.fil', '.tdr', '.txt')
        # ignore_extension = ('.log')
        # if file_name.endswith(extension) and not file_name.endswith(ignore_extension):
        #     shutil.copy2(or_path, os.path.join(dest_file_path, file_name))
        #     logging.info(f"Copied {or_path} to {dest_file_path}")
        #     print("copy")
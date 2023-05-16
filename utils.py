# import os
# import shutil
# import logging

# origin = "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/"
# destination = "C:/Users/laura.rangelroman/Documents/folder_sync_project/"

# paths_or = [

#     "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_a",

#     "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_b",

#     "C:/Users/laura.rangelroman/Documents/folder_sync_project/repository/server_c"
# ]

# paths_dest = [

#     "C:/Users/laura.rangelroman/Documents/folder_sync_project/server_a",

#     "C:/Users/laura.rangelroman/Documents/folder_sync_project/server_b",

#     "C:/Users/laura.rangelroman/Documents/folder_sync_project/server_c"
# ]

# def get_path(route, nombre=None):
#     routes = []
#     names = []
#     for root, dirs, files in os.walk(route):
#         for folder in dirs:
#             if nombre is None or nombre in folder:
#                 format_root = os.path.abspath(root).replace("\\", "/")
#                 routes.append(os.path.join(format_root, folder).replace("\\", "/"))
#                 names.append(folder)
#     return routes, names

# #print(get_path(destination))

# def routes_list(routes, names):
#     my_list = []
#     for i in range(len(routes)):
#         my_dict = {}
#         my_dict['route'] = routes[i]
#         my_dict['name'] = names[i]
#         my_list.append(my_dict)
#     return my_list

# def format_route(ruta):
#     new_route = ruta.split('\\')[:-1]
#     new_route = '\\'.join(new_route)

#     return new_route



# def sync_files(origin, destination):
#     for root, dirs, files in os.walk(origin):
#         for file in files:
#             extension = ('.var', '.fil', '.tdr')
#             if file.endswith(extension):
#                 path_a = os.path.join(root, file)
#                 path_b = os.path.join(destination, os.path.relpath(path_a, origin))
#                 if os.path.exists(path_a) and not os.path.exists(path_b):
#                     os.makedirs(os.path.dirname(path_b), exist_ok=True)
#                     shutil.copy2(path_a, path_b)
#                     print(f"The file {path_a} has been copied to {path_b}.")
#                     logging.info(f"Sync successful. The file {path_a} has been copied to {path_b}")
#                 if os.path.exists(path_a) and os.path.exists(path_b):
#                     mtime_a = os.stat(path_a).st_mtime
#                     mtime_b = os.stat(path_b).st_mtime
#                     if mtime_a > mtime_b:
#                         shutil.copy2(path_a, path_b)
#                         print(f"The file {path_a} has been updated in {path_b}.")
#                     elif mtime_b > mtime_a:
#                         shutil.copy2(path_b, path_a)
#                         print(f"The file {path_b} has been updated in {path_a}.")



#   def test_0(self, testing_setup): 
#         #Define a variable to store the watcher instance
#         watcher = testing_setup
#         #Run watcher
#         watcher.run()
#         #Access the source directory
#         src_dir = watcher.src_dir
#         #Access the destination directory
#         dst_dir = watcher.dst_dir
#         #Stop watcher, by this time both directories should be the same
#         watcher.stop()
#         #Start checking that every file and sub directory is in both directories
#         for root, dirs, files in os.walk(src_dir):
#             for dir in dirs:
#                 assert os.path.isdir(os.path.join(dst_dir, os.path.relpath(root, src_dir), dir))
#             for file in files:
#                 assert os.path.isfile(os.path.join(dst_dir, os.path.relpath(root, src_dir), file))
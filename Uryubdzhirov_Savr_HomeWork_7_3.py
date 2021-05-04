import os, shutil

dir_root = os.path.join(os.path.dirname(__file__), 'my_project')
dir_dist = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(dir_dist):
    os.makedirs(dir_dist)

for root, dirs, files in os.walk(dir_root):
    if root.count('templates'):
        for dir1 in dirs:
            if not os.path.exists(os.path.join(dir_dist, dir1)):
                os.makedirs(os.path.join(dir_dist, dir1))
        for file in files:
            file_sour = os.path.join(root, file)
            file_dist = os.path.join(dir_dist, os.path.basename(root))
            if not os.path.dirname(file_sour) == file_dist:
                shutil.copy(file_sour, file_dist)

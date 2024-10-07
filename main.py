import os
import shutil
from paths import main_disk, backup


disk = main_disk
flash = backup

n = len(disk)
m = len(flash)

dirs = set()
files = set()

for path, dirs_on_disk, files_on_disk in os.walk(disk):

    for directory in dirs_on_disk:
        dirs.add(path[n:] + '/' + directory)

    for file in files_on_disk:
        files.add(path[n:] + '/' + file)


for path, dirs_on_flash, files_on_flash in os.walk(flash):
    
    for directory in dirs_on_flash:
        new_path = path[m:] + '/' + directory

        if new_path in dirs:
            dirs.remove(new_path)
        else:
            shutil.rmtree(path + '/' + directory)
    
    for file in files_on_flash:

        new_path = path[m:] + '/' + file
        
        if new_path in files:
            files.remove(new_path)
        elif os.path.isfile(path + '/' + file):
            os.remove(path + '/' + file)

for directory in dirs:
    new_path = flash + directory
    if not os.path.isdir(new_path):
        os.makedirs(new_path)

for file in files:
    old_path = disk + file
    new_path = flash + file
    shutil.copy(old_path, new_path)
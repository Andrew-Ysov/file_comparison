import os
import shutil
from paths import MAIN_DISK, BACKUP


DISK = MAIN_DISK
FLASH = BACKUP

n = len(DISK)
m = len(BACKUP)

DIRS = set()
FILES = set()

# Собирает пути до всех файлов и папок
for path, dirs_on_disk, files_on_disk in os.walk(DISK):
    for directory in dirs_on_disk:
        DIRS.add(path[n:] + '/' + directory)

    for file in files_on_disk:
        FILES.add(path[n:] + '/' + file)

# Оставляет в DIRS, FILES только уникальные для DISK пути, которых нет в FLASH
for path, dirs_on_flash, files_on_flash in os.walk(FLASH):
    for directory in dirs_on_flash:
        new_path = path[m:] + '/' + directory

        if new_path in DIRS:
            DIRS.remove(new_path)
        else:
            shutil.rmtree(path + '/' + directory)
    
    for file in files_on_flash:
        new_path = path[m:] + '/' + file
        
        if new_path in FILES:
            FILES.remove(new_path)
        elif os.path.isfile(path + '/' + file):
            os.remove(path + '/' + file)


for directory in DIRS:
    new_path = FLASH + directory
    if not os.path.isdir(new_path):
        os.makedirs(new_path)


for file in files:
    old_path = DISK + file
    new_path = FLASH + file
    shutil.copy(old_path, new_path)

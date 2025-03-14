import os
import shutil

from paths import MAIN_DISK, BACKUP


DISK = MAIN_DISK
FLASH = BACKUP

n = len(DISK)
m = len(BACKUP)

dirs = set()
files = set()


def main(dirs, files, m, n, DISK, FLASH):
    """Collect paths to files and directories."""
    for path, dirs_on_disk, files_on_disk in os.walk(DISK):
        for directory in dirs_on_disk:
            dirs.add(path[n:] + '/' + directory)

        for file in files_on_disk:
            files.add(path[n:] + '/' + file)

    # keep only unique paths in DISK
    for path, dirs_on_flash, files_on_flash in os.walk(FLASH):
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
        new_path = FLASH + directory
        if not os.path.isdir(new_path):
            os.makedirs(new_path)


    for file in files:
        old_path = DISK + file
        new_path = FLASH + file
        shutil.copy(old_path, new_path)

if __name__ == '__main__':
    main(dirs, files, m, n, DISK, FLASH)
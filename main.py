import os
import shutil
from paths import main_disk, backup, ignor

disk_path = main_disk
flash_path = backup
seen_files = {}

for path, dirs, files in os.walk(disk_path):
    for file_name in files:
        if path.split("\\")[-1] in ignor:
            continue
        way_to = os.path.join(path, file_name)
        seen_files[way_to] = file_name


def split_with_dif_ch(s, leave_last = True):
    prev = 1
    sp = {'/', '\\'}

    result = []
    
    for i in range(len(s)):
        if s[i] in sp:
            result.append(s[prev-1:i])
            prev = i+1
    if len(s[prev:])>0:
        result.append(s[prev-1:])
    
    if leave_last == False:
        return result[:-1]
    
    return result

removed_from_flash = 0
for path, dirs, files in os.walk(flash_path):
    for file_name in files:
        if path.split('\\')[-1] in ignor:
            continue
        
        way_to = os.path.join(path, file_name)

        if file_name in seen_files.values():
            del seen_files[way_to]
        else: 
            os.remove(way_to)
            removed_from_flash += 1
        


flash = flash_path
flash_p_list = split_with_dif_ch(flash)

added_files = 0
for path in seen_files.keys():
    path_list = split_with_dif_ch(path, False)

    new_path = ''.join(flash_p_list + path_list[len(flash_p_list):])
    

    if not os.path.isdir(new_path):
        os.makedirs(new_path)

    shutil.copy(path, new_path)
    added_files += 1

# По итогу, помимо наличия одинаковых файлов как на диске, так и на флешке, 
# можно вывести количество удалённых и новых файлов


print('Удалённых файлов было: ', removed_from_flash)
print('На флешку добавили ', added_files, ' файлов')
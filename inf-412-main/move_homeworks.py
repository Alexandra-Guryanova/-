import os
import shutil

from helper import make_dirs

# 1
homework_dir = 'homeworks'
make_dirs(homework_dir)

# 2
files = os.listdir()
new_files_list = [] # список файлов которые будем перемещать

for file in files:
# 2.1 and 2.2
    if '.txt' in file and 'homework' in file:
        new_files_list.append(file)
    

# 3.2
for file in new_files_list:
    shutil.copy(file, f'{homework_dir}/{file}')

# 3.5
for file in new_files_list:    
    os.remove(file)
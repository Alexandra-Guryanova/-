# работа с файлами

import os

# информация о текущем файле
print(
    os.getcwd()
)
# s:/Проневич/inf-412-main/filesystem.py

# получить список файлов в директории
print(
    os.listdir()
)
# ['arr.py', 'dict_01.py', 'filesystem.py', 'Hello world.txt', 'main.py', 'README.md', 'str.py']

# проверка есть ли директория
print(
    os.path.isdir('homeworks')
)

for f in os.listdir():
    print(
        f'is dir: {f}', os.path.isdir(f),
    )

#os.mkdirs('home_01/work_1')
def make_dirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

# make_dirs('home_01/work_2')


# 1. проверка существования директории (папки)
# 1.1 если существует, то ничего не делать
# 1.2 если не существует, то создать
# 2 ищем файлы, которые будем переносить
# 2.1 ищем файлы с форматом .txt
# 2.1 ищем файлы название которых содержит "homework"
# 3. перемещение
# 3.1 выбор файла
# 3.2 копируем
# 3.3 переходим в директорию
# 3.4 добавляем файл
# 3.5 удаляем исходный файл

# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Файлы в операционной системе"

import os, time

directory = "."

for root, dirs, files in os.walk(directory):
    print()
    print('Дата и время\t\t', 'Родительская\t', 'Размер\t\t', 'Имя')
    print('изменения файла\t\t', 'директория\t\t', 'файла\t\t', 'файла')
    print('_____________________________________________________________')
    for file in files:

        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)

        if filesize >= 100:
            print(f'{formatted_time}\t {parent_dir}\t\t\t\t {filesize}\t {filepath}')
        else:
            print(f'{formatted_time}\t {parent_dir}\t\t\t\t {filesize}\t\t {filepath}')

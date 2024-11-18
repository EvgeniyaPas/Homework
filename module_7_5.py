import os
import time
directory = r'C:\Users\Школа 2\PycharmProjects'

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join('.', file)
    filetime = os.path.getmtime('.')
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize('.')
    parent_dir = os.path.dirname('.')
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


import os
from datetime import datetime, timedelta
import time


now = datetime.now()
vremya = now.strftime("%d-%m-%Y %H:%M:%S")


vremya1 = 'shared'
path = 'dataset'


# for filename in os.listdir(path):
#     if filename.endswith('.jpg'): # Проверяем, что это файл с расширением .jpg
#         if vremya1 not in filename:
#             print(filename)
#              # Формируем новое имя файла с добавлением слова "shared"
#             new_name = filename.replace('.jpg', '_shared.jpg')
#             # Сформируйте полный путь к старому файлу
#             old_path = os.path.join(path, filename)
#             # Сформируйте полный путь к новому файлу
#             new_path = os.path.join(path, new_name)
#             # Используйте метод rename() для переименования файла
#             os.rename(old_path, new_path)
# num = []

# col = int(len(os.listdir(path)))


# if col not in num:
#     print("Функция выполнена")
#     num.append(col)

for filename in os.listdir(path):
    print(os.path.basename(f'{path}/{filename}'))

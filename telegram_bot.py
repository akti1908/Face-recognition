import requests
import os
from datetime import datetime, timedelta
import time
from telegram import Bot, Location




def telega():
    # Указываем токен и ID чата для отправки сообщений
    TOKEN = '6173293326:AAGKmRSrouMYpx6X2stXcQsyLLWaf_jWKKw'
    CHAT_ID = '873271733'
    bot = Bot(TOKEN)
    latitude = 42.87403014910091
    longitude = 74.61993886500643

    
    shared = 'shared'
    path = 'dataset'
    photo_path = 'dataset/aktilek 02-03-2023 12:00:16.jpg'


    def send_photo_and_location(photo_path, latitude, longitude, des):
        """
        Отправляет фотографию и локацию в Telegram бота
        """
        # Открываем файл с фотографией
        (os.path.basename(f'{path}/{filename}'))
        try:
            with open(photo_path, 'rb') as photo:
                # Отправляем запрос на загрузку фотографии на сервер Telegram
                response = requests.post(
                    f'https://api.telegram.org/bot{TOKEN}/sendPhoto',
                    files={'photo': photo},
                    data={'chat_id': CHAT_ID, 'caption': f'{des}'}
                )
        except:
            print('Пока новых фотографий не найдено')

        # Отправляем локацию
        try:
            response = requests.post(
                f'https://api.telegram.org/bot{TOKEN}/sendLocation',
                data={
                    'chat_id': CHAT_ID,
                    'latitude': latitude,
                    'longitude': longitude
                }
            )
        except:
            print('Ошибка отправки локации')


    for filename in os.listdir(path):
        if filename.endswith('.jpg'): # Проверяем, что это файл с расширением .jpg
            if shared not in filename:

                photo_path = f'dataset/{filename}'
                try:
                    des = ((os.path.basename(f'{path}/{filename}'))[:-4])+" Академия OGOGO"

                    send_photo_and_location(photo_path, latitude, longitude, des)
                    
                    print('Фотография и локация успешно отправлена!')
                except:
                    print("Новых фотографий в базе нет!")
                    
# Формируем новое имя файла с добавлением слова "shared"
                new_name = filename.replace('.jpg', '_shared.jpg')
                # Сформируйте полный путь к старому файлу
                old_path = os.path.join(path, filename)
                # Сформируйте полный путь к новому файлу
                new_path = os.path.join(path, new_name)
                # Используйте метод rename() для переименования файла
                os.rename(old_path, new_path)


    
        # Удаляем файл с фотографией после отправки
        # os.remove(photo_path)

        # Проверяем, успешно ли была отправлена фотография
        



    

    # for filename in os.listdir(path):
    #     if filename.endswith('.jpg'): # Проверяем, что это файл с расширением .jpg
    #         if shared not in filename:

                

# def main():
#     telega()
        

# if __name__ == '__main__':
#     main()

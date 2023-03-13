import numpy as np
import face_recognition
import cv2
import os
from datetime import datetime, timedelta
import time
import requests
import os
from datetime import datetime, timedelta
import time
import asyncio

from telegram_bot import telega

# Асинхронная функция
# async def check_folder():
#     while True:
#         files = os.listdir('dataset')
#         # if len(files) not in num:

#         print("Функция успешна!!!!")
#         await asyncio.sleep(0.5)


# async def main():




screenshot_interval = timedelta(seconds=30)

# Определяем время последнего скриншота (для проверки интервала)
last_screenshot_time = datetime.now()

path = 'KnownFaces'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])

print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open("Attendance.csv", "r+") as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f'\n{name}, {dtString}')

encodeListKnown = findEncodings(images)
print("Декодирование закончено")

cap = cv2.VideoCapture(0)

if not os.path.exists('dataset'):
    os.makedirs('dataset')


while True:
    num = []
    telega()
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex]
            #print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

            if not os.listdir('dataset'):
                # Если папка пустая, сделать скриншот и назвать его именем
                now = datetime.now()
                dtString = now.strftime("%d-%m-%Y %H:%M:%S")
                cv2.imwrite(f"dataset/{name} {dtString}.jpg", img)
                last_screenshot_time = datetime.now()
            else:
                # Проверить, было ли уже сделано фото для этого человека
                files = [f for f in os.listdir('dataset') if os.path.isfile(os.path.join('dataset', f))]
                file_names = [os.path.splitext(f)[0] for f in files]
                if name not in file_names:
                    # Если фото еще не сделано, проверить время последнего скриншота
                    time_since_last_screenshot = (datetime.now() - last_screenshot_time).total_seconds()
                    if time_since_last_screenshot >= screenshot_interval.total_seconds():
                        # Если прошло больше времени, чем задано в интервале, сделать новый скриншот и обновить время
                        now = datetime.now()
                        dtString = now.strftime("%d-%m-%Y %H:%M:%S")
                        cv2.imwrite(f"dataset/{name} {dtString}.jpg", img)
                        last_screenshot_time = datetime.now()
                else:
                    # Если папка с набором данных заполнена, напечатается Функция отправки завершена.
                    if len(os.listdir('dataset')) >= 100:
                        print('Send function completed')
            
            # Обновить значение переменной num
            

    cv2.imshow("WebCam", img)
    cv2.waitKey(1)























# async def run():
#     task1 = asyncio.create_task(main()) # Создание задачи для main()
#     task2 = asyncio.create_task(check_folder()) # Создание задачи для check_folder()
#     await asyncio.gather(task1, task2) # Ожидание завершения обеих задач

# asyncio.run(run())

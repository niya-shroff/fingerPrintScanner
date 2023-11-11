import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# scpCommand = 'scp raspberrypi@192.168.111.169:~/Desktop/Camera/test.jpeg ./Desktop/Projects/fingerPrintScanner/backend/facialRec/ImagesAttendance'
# os.system(scpCommand)

path = 'ImagesAttendance'                                                         #image directory is taken
images = []                                                                       #list of images to import to store in the list
classNames = []                                                                   #to take the names directly from the image file name
myList = os.listdir('ImagesAttendance')                                                        #to grab the list of images in to the folder
print(myList)                                                                     #to print the list of names
for cl in myList:                                                                 #to import the images one by one
    curImg = cv2.imread(f'{path}/{cl}')                                           #to read the image with file path
    images.append(curImg)                                                         # appending images from the list to path
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                                 #to convert the image to RGB code
        encode = face_recognition.face_encodings(img)[0]                           #to encode the recognized face
        encodeList.append(encode)                                                  #to append the encoded list
    return encodeList

encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow('webcam',img)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)                                
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)                                    

    facesCurFrame = face_recognition.face_locations(imgS)                           #to locate the name list
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
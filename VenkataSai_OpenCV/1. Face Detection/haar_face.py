import numpy as np
import cv2
import requests

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
url = 'http://192.168.1.7/SnapshotJPEG?Resolution=640x480'

while 1:

    img_resp=requests.get(url)
    img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)

    img = cv2.imdecode(img_arr,1)

    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    add=[]


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('Haarcascades',img)
 
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

print(i)

cap.release()
cv2.destroyAllWindows()



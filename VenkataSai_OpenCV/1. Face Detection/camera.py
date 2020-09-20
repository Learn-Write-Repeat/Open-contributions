import cv2
import numpy as np
import requests

class VideoCamera(object):
    def __init__(self):

        self.video = cv2.VideoCapture(0)

    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        success, image = self.video.read()
        image = cv2.flip(image,180)
        faces = face_cascade.detectMultiScale(image, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            roi_color = image[y:y+h, x:x+w]
        ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()

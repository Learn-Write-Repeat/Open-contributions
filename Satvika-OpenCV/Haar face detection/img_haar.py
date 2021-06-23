import cv2
import numpy

img = cv2.imread('C:\Python\ProgramsPython\HelloWorld\\venv\OpenCV\FaceBarca.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('C:\Python\ProgramsPython\HelloWorld\\venv\OpenCV\haarcascade_frontalface_default.xml') # Path of XML file


# Arguments of the function :- (src image , scaleFactor , minNeighbours)
# We generally check with all possible values and choose the best among them
# Here, in this case, when scale factor increases and minNeighbours also increase, the face detection becomes very clumsy with multiple detections to same object
# i.e. if we observe the output, the image has multiple boxes around same face.
# Also, few faces remain undetected if minNeighbours are less.

# faces = face_cascade.detectMultiScale(gray,1.7,5) # ScaleFactor

# faces = face_cascade.detectMultiScale(gray,1.5,0) # minNeigbours
faces = face_cascade.detectMultiScale(gray,1.1,7) # minNeigbours

# print(faces)

for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

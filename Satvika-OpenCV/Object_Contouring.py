import numpy as np
import cv2

img  = cv2.imread('C:\Python\ProgramsPython\HelloWorld\\venv\OpenCV\Resources\Resources(Day-1)\Contours\Shapes.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray , 220 ,255 , cv2.THRESH_BINARY_INV)
cnts,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# print(cnts)

cv2.drawContours(img,cnts,-1,(0,255,0),2)

cv2.imshow('Image',img)
cv2.imshow('Thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()




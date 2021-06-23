# This code discussed about object contouring wherein an image consisting of different shapes is thresholded 
# and then the outlines for each shape is identified using the openCV function findContours().
# We are printing both thresholded and contoured images here.


import numpy as np
import cv2

img  = cv2.imread('C:\Python\ProgramsPython\HelloWorld\\venv\OpenCV\Contours\Shapes.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray , 220 ,255 , cv2.THRESH_BINARY_INV)
cnts,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# print(cnts)

cv2.drawContours(img,cnts,-1,(0,255,0),2)

cv2.imshow('Image',img)
cv2.imshow('Thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


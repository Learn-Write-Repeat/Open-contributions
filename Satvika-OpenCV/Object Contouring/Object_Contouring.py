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


'''
Some importtant functions in OpenCV:
•	cv2.threshold(src,thresholdvalue,maxvalue, thresholding_technique)
Returns the threshold value(ret) and the thresholded frame. Thresholding technique can be cv2.THRESH_BINARY or cv2.THRESH_BINARY_INV.
•	cv2.findContours(src,retrieval method,contour approximation method)
Returns a list of all numpy arrays which contain the x,y co-ordinates of all boundary points.
	Retrieval method – cv2.RETR_TREE or cv2.RETR_EXTERNAL
	Contour approximation – cv2.CHAIN_APPROX_SIMPLE or 	cv2.CHAIN_APPROX_NONE.
	Note: There are many more methods and they can be found in the official documentation.
•	cv2.drawContours(src,contours,contour index,color,thickness)
Draws the contours on our source image. Contours are returned from the cv2.findContours function given above. Contour index helps us in displaying only specific contours.
'''
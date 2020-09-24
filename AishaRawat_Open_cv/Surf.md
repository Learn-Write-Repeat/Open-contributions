# SURF(Speeded-up Robust Feature)
  
Speeded Up Robust Feature (SURF) is an image region descriptor and detector that is invariant with regard to scale, orientation, and illumination. It is an enhanced version of SIFT.It is faster than SIFT.




A feature descriptor is an algorithm which takes an image and outputs feature descriptors/feature vectors. Feature descriptors encode interesting information into a series of numbers and act as a sort of numerical "fingerprint" that can be used to differentiate one feature from another. Ideally this information would be invariant under image transformation, so we can find the feature again even if the image is transformed in some way.




### A feature detector detects the keypoints and a feature descriptor describes the keypoints(how does the surrounding or pixels look like)
Keypoints are points of interest in an image that can be used to compare images and perform tasks such as image alignment and image registration. 

```#import required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
#show OpenCV version
print(cv2.__version__)
#read image and convert to grayscale
image = cv2.imread('index.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#instantiate surf object
surf  = cv2.xfeatures2d.SURF_create(400)
#calculate keypoints and their orientation
keypoints,descriptors = surf.detectAndCompute(gray,None)

with_keypoints = cv2.drawKeypoints(gray,keypoints)

plt.imshow(with_keypoints)```

# SURF(Speeded-up Robust Feature)

Speeded Up Robust Feature (SURF) is an image region descriptor and detector that is constant with respect to scale, orientation, and illumination. 
To detect interest points, SURF uses an integer approximation of the determinant of Hessian blob detector, which can be computed with 3 integer operations using a precomputed integral image. Its feature descriptor is based on the sum of the Haar wavelet response around the point of interest. These can also be computed with the aid of the integral image.

<br>
<ul style="list-style-type:square;" ><li>It is an enhanced version of SIFT.</li>
        <li>It is faster than SIFT.</li>
</ul> 
</br>

  
 ### A feature detector detects the keypoints and a feature descriptor describes the keypoints(how does the surrounding or pixels look like)
Keypoints are points of interest in an image that can be used to compare images and perform tasks such as image alignment and image registration. 

A feature descriptor is an algorithm which takes an image and outputs feature descriptors/feature vectors. Feature descriptors encode interesting information into a series of numbers and act as a sort of numerical "fingerprint" that can be used to differentiate one feature from another. Ideally this information would be invariant under image transformation, so we can find the feature again even if the image is transformed in some way.
 <b>SURF descriptors have been used :</b>
  
 <ul><li>to locate and recognize objects, people or faces</li>
 <li>to reconstruct 3D scenes</li>
  <li>to track objects and to extract points of interest.</li></ul>
 </br>
 
  SURF was first published by Herbert Bay, Tinne Tuytelaars, and Luc Van Gool, 
  and presented at the 2006 European Conference on Computer Vision.
  </br>

  <b> The algorithm has three main parts:</b> 
  <ol><li> interest point detection</li>
        <li>local neighborhood description </li>
        <li>matching.</li></ol>
        
   <b>Interest Point Detection</b><br>
   SURF uses a blob detector based on the Hessian matrix to find points of interest. The determinant of the Hessian matrix is used as a measure of local change around the point    and points are chosen where this determinant is maximal.
    SURF also uses the determinant of the Hessian for selecting the scale,<
    The sum of the original image within a rectangle can be evaluated quickly using the integral image, requiring evaluations at the rectangle's four corners.
     SURF uses a blob detector based on the Hessian matrix to find points of interest. The determinant of the Hessian matrix is used as a measure of local change around the            point and points are chosen where this determinant is maximal. In contrast to the Hessian-Laplacian detector by Mikolajczyk and Schmid, SURF also uses the determinant of       the Hessian for selecting the scale, as is also done by Lindeberg. Given a point p=(x, y) in an image I, the Hessian matrix H(p, σ) at point p and scale σ, is:<br>
  ![Image](79c73bc892769b2b27218327be8af9f72fc17945.svg)
    


 How to reach me: [This is my portfolio link](https://github.com/AishaRawat/AishaRawat/blob/master/README.md) or you can mail me at rawataisha981@gmail.com  <br>







[Surf Implementation on Jupyter Notebook](https://github.com/AishaRawat/Open-contributions/blob/master/AishaRawat_Open_cv/SURF.ipynb)
(click the link , you will reach to python notebook )

 ``` #import required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
#read image and convert to grayscale
image = cv2.imread('index.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#instantiate surf object
surf  = cv2.xfeatures2d.SURF_create(400)
#calculate keypoints and their orientation
keypoints,descriptors = surf.detectAndCompute(gray,None)
with_keypoints = cv2.drawKeypoints(gray,keypoints)
plt.imshow(with_keypoints)
```


  <br>
 This is the most basic and simple explanation of surf . Enjoying Learning ! :books:
 

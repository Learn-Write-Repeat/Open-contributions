## Face and Eye detection with OpenCV

In this session,
- We will see ***face*** and ***eye*** detection using Haar Feature based Cascade classifiers.
- We will see programming on face and eye detection.


## Haar Classifier

**Face** and **Eye** detection works on the algorithm called **Haar Classifier** which is proposed by **Paul Viola** and **Michael Jones** in their paper, **"Rapid Object Detection
using Boosted Cascade of Simple Features"** in 2001.



**Haar Classifier is a ***machine learning*** based approach  where a function is trained from a lot of positive and negative images i.e with face and without face**.

Initially the algorithm needs lots of positive images(***with face***)and negative images(***without face***) to train the ***classifier***(algorithm that sorts data in categories
of information). Once all the features and details are extracted, they are stored in a file and if we get any new input image, check the feature from the file, apply it on the input image and if it passes all the stage then ***the face is detected***. So this can be done using **Haar Features**. 

So in short **Haar Classifier** is a classifier which is used to detect the object for which it has been trained for from the source.

### ***Haar Features:***
It is used to detect the presence of that feature in the image i.e face ,eyes ,mouth ,nose etc.

A single value is obtained by subtracting the sum of pixels under white rectangle and sum of pixels under black rectangle.

![image](https://opencv-python-tutroals.readthedocs.io/en/latest/_images/haar_features.jpg)



##  Program on Face and Eye detection

Before we add face and eye detection haar cascade files we need to import **OpenCV library**.

### To install OpenCV library on **anaconda prompt** execute the following commands:

                       pip install opencv-python
                       pip install opencv_contrib-python
                       
  
## REQUIREMENTS

  - Webcam system
  
  - Jupyter notebook
  
  - Python-OpenCV
  
### Code
<html>
<table>
 <tr>
  <td>
   
import cv2  
   
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')   

cap = cv2.VideoCapture(0) 

while 1:  

    ret, img = cap.read() 
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    
    for (x,y,w,h) in faces: 
    
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        
        roi_gray = gray[y:y+h, x:x+w] 
        
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)  
        
        for (ex,ey,ew,eh) in eyes: 
        
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
            
    cv2.imshow('img',img) 
    
    k = cv2.waitKey(30) & 0xff
    
    if k == 27: 
    
        break
        
cap.release() 

cv2.destroyAllWindows()   
 

</td>
</tr>
</table>
</html>
  
  
  
  ##  Explaination
   - Import Opencv library using **import cv2** statement
   - Load the required XML classifiers for face and eye detection.
   
        face_cascade=cv2.CascadeClassifier('haarcascade_frontal_face_default.xml')
        
        eye_cascade=cv2.CascadeClassifier('haarcascade_eye_default.xml')
        
        
        #### OR
        
        Specify the path where XML classifiers are stored:
        
        ***Example:***
        
          face_cascade=cv2.CascadeClassifier('F:/is setup/haarcascade_frontal_face_default.xml')
          
          eye_cascade=cv2.CascadeClassifier('F:/is setup/haarcascade_eye.xml
          
          
    
   -  Now initialize cap variable and captures the frames from the camera
    
          cap=cv2.VideoCapture(0)
          
 -  Using while loop read each frame from the camera and then perform the following steps:
                      
              ret,img=cap.read()
              
  -  Convert into gray scale image
  
              gray=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
              
      
   -   Detect faces of different sizes in the input image
   
            faces=face_cascade_detectMultiScale(gray,1.3,5)
    
            
   -   Now our work is to draw a rectangle on the face and also on the eye image using for loop
   
   
              for (x,y,w,h) in faces:
              
              cv2.rectangle(img(x,y),(x+w,y+h),(255,255,0),2)
              
              roi_gray=gray(y:y+h,x:x+w)
              
              roi_color=img(y:y+h,x:x+w)
              
              eyes=eye_cascade.detectMultiScale(roi_gray)
 
                 for (ex,ey,ew,eh) in eyes:
          
                      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
   
   - Display camere screen as output
      
          cv2.imshow(' image ',img)
          
   - Last and the final step is to break the loop by pressing **Esc** button
   
          k=cv2.waitKey(30) & 0xff
        
            if k=27;
          
              break:
        
    
  
  
  
  
  
  
  
                       

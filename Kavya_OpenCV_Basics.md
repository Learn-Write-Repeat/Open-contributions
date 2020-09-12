**OPENCV**

- **What is OpenCV**?

   OpenCV(**Open Source Computer Vision and Machine Learning Software**)is an open source library which processes images and videos to identify objects, faces ,detecting colours etc.It has wide applications in **computer vision**,
   **machine learning** and **image processing**.It also supports variety of programming languages like **Python**, **C++**, **C**. Basically it a library for **images**.
   
   ***Artificial Intelligence in OpenCV***
   
   **Computer Vision** is a branch of **Artificial Intelligence** which trains the computer to extract information from digital data like images and videos, understand them and even communicate.
   
 -   **Images**
   
   Images are collection of **pixels** and it is a binary representation of visual information such as logos, drawing pictures, graphs etc.
   
   - The image which has only two colours i.e **Black** ***and*** **white** is called **Binary image**.
     For a basic black and white image there is only one bit representation where **0** represents ***black*** and **1** represents ***white***.
     
-   **Black and white image**
   
    ![image](https://i.pinimg.com/236x/13/bc/e2/13bce226fa0d37b0ddca3ef09045d34d--monochrome-photography-black-white-photography.jpg)
   
   


 -   **Gray Scale Image**
   
   We can have image more than two levels i.e instead of having only 0 and 1 bit levels we can have range of values i.e 2^8,this will give us resolution of 256 levels where 0 will be
   **black** and 255 will be white.So basically we have 254 colours between **black** and **white**. In other words we have 254 shades of **grey**.
   
   ![image](https://i.stack.imgur.com/B2DBy.jpg)
   
-  **Coloured image**
   
   For coloured images we have three gray scale images representing the intensities of **red**,**green**,**blue**. Adding these colours together gives a us a full coloured       image.
   
  ![image](extras/red.jpg)   **+**   ![image](extras/blue.jpg)    **+**    ![image](extras/green.jpg)   =  
  
  ![image](extras/original.jpg)   
   
   
  
- **Installation of OpenCV**
   
   Installation of OpenCV has two steps to follow in **Anaconda Prompt**.
   - Open **Anaconda Prompt** 
   - Execute the following commands:
   
       - pip install opencv-python
       
       - pip install opencv-contrib-python
   
   
 After installing the Opencv package on anaconda prompt, For further usage of OpenCV in image and video processing in any python IDE it is necessary to import OpenCV library and it's functions using **import cv2** statement 
 
 
- **Basic functions in OpenCV**

  - **imread()**:
    In order to read or store image in a variable imread() function is used.
    
    First will declare a variable,then using the function imread() in cv2 package we store the image. 
       
       *syntax*:
       
          **variable_name = cv2.imread(specify_the_path_in_which_image_should_be_read_with_extensions)**
          
       *Example*:
       
           img1 = cv2.imread("extras/nature.jpeg")
          
          
          
   - **imshow()**:
            This function is used to display the image from the variable where the image is stored.
            
      *syntax*:
      
             **cv2.imshow(window_name,variable_name)**
             
     *Example*:
     
             cv2.imshow("Output",img1)
     
     
   - **videocapture()**:
               This function is used to import a video.
               
           - steps to import a video
           
              - Declare a variable and using videocapture()function import the image.
              
              - Using a infinite while loop and read()function read the frames.
              
              - Use imshow()function to display the video and break the loop using a specific key.
     
     
     *Example*: 
     
          cap=cv2.videocapture("")
          
           while true:
           
               success,img=cap.read()
               
               cv2.imshow("video",img)
               
               if cv2.waitKey(1)& 0xFF=ord('q'):
               
                   break:
                   
                   
     **Displaying multiple images**
     
       It is possible to display multiple images in a single window.
       It can be displayed either horizontly or vertically.
       we have to import numpy library as well for displaying multiple images.
       
        **import numpy as npy**
        
       *steps to display multiple images*
       - store the multiple images in different variables using imread() function.
       - concatanate image Horizontally 
       
       *syntax*:
       
         variablename=npy.concatenate((image_1,image_2),axis=1)
         
       - concatanate image Vertically
       
       *syntax*:
       
         variable_name=npy.concatenate((image1,image2),axis=0)
         
        **Here axis refers to mode of concentation.**
         
         axis=1 refers to horizontal concentation.
         
         axis=0 refers to horizontal concentation.
         
        - Display the concantenated images using imshow() function.
        
     
     
     
     
     
     
     
     
     
     
     
               
            
          
    
 
   
   
   
  
   

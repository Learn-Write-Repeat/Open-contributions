*OPENCV BASICS*

- *What is OpenCV*?

   OpenCV(*Open Source Computer Vision and Machine Learning Software*)is an open source library which processes images and videos to identify objects, faces, detecting colours etc.It has wide applications in **Computer Vision,Machine Learning** and *Image Processing*. It also supports variety of programming languages like **Python**, **C++**, **C**. Basically it a library for processing **images**.
   
   **OpenCV in Artificial Intelligence**
   
   *Computer Vision* is a branch of *Artificial Intelligence* which trains the computer to extract information from digital data like images and videos, understand them and even communicate.
   
   *Why OpenCV?*
   
   Nowadays image processing and computer vision have gained importance in every field. As Opencv has over 2500 optimized algorithms which ease image processsing and even helps in building projects like tracking movements, recognizing faces, finding similar images etc.,it makes programming easier.Reading and displaying images is simplified and through OpenCV development of programs from simpler to complex is easier. 
   
  *Application of OpenCV*
  
    - Image enchancement.
    
    - Rotating,Cropping,Resizing(using more advanced features)
    
    - Background removal.
    
    
 -   *Images*
   
     Image is collection of *pixels* and it is a binary representation of visual information such as logos, drawing pictures, graphs etc.
     
     
 -   *Black and white image*
   
     The image which has only two colours i.e *Black* **and** **white** is called *Binary image*.
     For a basic black and white image there is only one bit representation where *0* represents **black** and *1* represents **white**.
     

     ![image](https://i.pinimg.com/236x/13/bc/e2/13bce226fa0d37b0ddca3ef09045d34d--monochrome-photography-black-white-photography.jpg)
   
   


 -   *Gray Scale Image*
   
     One can have images of more than two levels i.e instead of having only 0 and 1 bit levels each pixel can have range of values i.e 2^8,this will give us resolution of 256 levels where 0 will be *black* and 255 will be *white*. So basically we have 254 colours between *black* and *white*.
   
     ![image](https://i.stack.imgur.com/B2DBy.jpg)
   
-  *Coloured image*
   
   For coloured images each pixel can have levels of *red,green,blue*. Different levels of red, green and blue give different colours to the respective pixels giving out a fully coloured image.
  
  
   ![image](extras/original.jpg)   
   
   
  
- *Installation of OpenCV*
   
   Installation of OpenCV has two steps to be followed through *Anaconda Prompt*.
   - Open *Anaconda Prompt* 
   - Execute the following commands:
   
         pip install opencv-python
       
         pip install opencv-contrib-python
   
   
 After installing the Opencv package on anaconda prompt, for further usage of OpenCV in image and video processing through python IDE, it is necessary to import OpenCV library and it's functions using *import cv2* statement.
 
 
- *Basic functions in OpenCV*

  - *imread()*:
    In order to read or store image in a variable imread() function is used.
    
    A variable is initialized to read an image, using the function imread() in cv2 package we store the image. 
       
       syntax:
       
          variable_name = cv2.imread(specify_the_path_in_which_image_should_be_read_with_extensions)
          
       Example:
       
           img1 = cv2.imread("extras/nature.jpeg")
          
          
          
   - *imshow()*:
   This function is used to display the image from the variable where the image is stored. Window name represents the name of the window on which the image is to be displayed.
            
     syntax:
      
             cv2.imshow(window_name,variable_name)
             
     Example:
     
             cv2.imshow("Output",img1)
     
     
   - *videocapture()*:
               This function is used to import a video.
               
           - steps to import a video
           
              - Initialize a variable to store the imported video.
              
              - Using an infinite while loop and read() function, read the frames.
              
              - Use imshow() function to display the video.
     
     
     Example: 
     
          cap=cv2.videocapture("specify_the_path_in_which_video_should_be_read_with_extensions")
          
           while true:
           
               success,img=cap.read()
               
               cv2.imshow("video",img)
               
               if cv2.waitKey(1)& 0xFF=ord('q'):
               
                   break:
                   
                   
    - *Displaying multiple images*
     
       It is possible to display multiple images in a single window.
       It can be displayed either horizontly or vertically.
       One has to import numpy library for displaying multiple images.
       
        *import numpy as np*
        
       steps to display multiple images
       - store the multiple images in different variables using imread() function.
       - concatenate image Horizontally 
       
       syntax:
       
         variablename=np.concatenate((image1,image2),axis=1)
         
       - concatenate image Vertically
       
       syntax:
       
         variable_name=np.concatenate((image1,image2),axis=0)
         
        *Here axis refers to mode of concatenation.*
         
         axis=1 refers to horizontal concatenation.
         
         axis=0 refers to horizontal concatenation.
         
        - Display the concatenated images using imshow() function.
        
        
        
        





  *Contact me directly on my [mail](kavyadheerendra@gmail.com)*

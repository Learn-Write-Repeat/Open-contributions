## Contours

### Contours:

Basically, **Contour** can be defined as an *outline* or a *border* of any object. *Contours* in Python is a ***list*** of contours of an object, which can be an image, a frame from a video and so on. Each *Contour* in the list *Contours* is a point represented as (x , y) which represent the position of the point with respect to the two axes. The contoural points usually have the same intensity.

### Uses of Contours:

Contours are mainly **used** in ***Object Detection***. Working with contours is very handy and have application in determining the size and shape of an object. Briefly stating, Contour finds its applications in anything that involves shape analysis, object detection and recognition. 

### Functions that are used to find the contours in OpenCV:

Determining contours involves multiple steps as the image needs to get ready for the process. After reading and storing the image in a variable, the image needs to be converted to either **hsv** or **grayscale** to ease the processing.

    variable_name = cv2.cvtColor(variable_name_that_stores_the_image , cv2.COLOR_BGR2HSV)
    
***Example***:

    hsv = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)
    
  The normal format of the image is **BGR** which represents the order of consideration of intensities of **Blue, Red** and **Green** in the image. **cv2.COLOR_BGR2HSV** converts the file to **hsv** which basically represents the level of **hue, saturation** and **lightness**. For obtaining **Grayscale** image, pass cv2.COLOR_BGR2GRAY as the parameter instead of cv2.COLOR_BGR2HSV.
  
  To find all the contoural points of the image, the syntax is as follows: 
  
  cv2.CHAIN_APPROX_NONE)
      
  Now, the **syntax** is:
  
      image , contours , hierarchy = cv2.findContours( image_variable , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
      
  ***Example***:
  
      image , contours , hierarchy = cv2.findContours( image , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
      
  The function cv2.findContours() takes 3 arguments, **source image, contour retrieval mode**, and **contour approximation method** in order. The *contour approximation* can take another value also, **cv2.CHAIN_APPROX_NONE**, but less efficient. 
  
  To obtain all the contoural points on the image, drawing the contours is necessary. To do thid the OpenCV has the drawContours() function that draws or plots all the contoural points onto the image whose **syntax** is as follows:
  
        variable_name = cv2.drawContours(image_variable , contours , -1 , (0,255,0), 3)
        
 This functions takes the arguments in the order of source image, the contours in the form of a list, and index of contours (to draw all contours, pass -1). (0,255,0) represents the colour of the contour, which here, is Green.
  
  ***Example***:
  
        image = cv2.drawContours(image , contours , -1 , (0,255,0), 3)
        
 To ensure that no noises are included, one can make use of the **for** loop to *iterate* through all the contoural points and **based on a condition**, the point can be chosen to be *plotted or discarded*.
 
 To make contouring more efficient, the **cv2.Canny()** function comes handy to ease the process for users. This function is an *integrated* function to perform all of the following tasks:
 
 - Noise Reduction
 - Finding Intensity Gradient of the image
 - Non Maximum Suppression
 - Hysteresis Thresholding
 
 This function makes the **edge detection** job done for the users so that the contouring becomes easier.
 
 **Syntax**:
 
        variable_name = cv2.Canny(image_variable , threshold_1 , threshold2) 
        
 **Example**:
 
        variable_name = cv2.Canny(image_variable , threshold_1 , threshold2) 
 
 Here, the arguments taken by the functions are **source image, first threshold for the hysteresis procedure, second threshold for the hysteresis procedure** and many more.
 
### Contouring in Video processing:

Video is undoubtedly a **series of image frames**. This concept makes video processing easier, especially when using OpenCV library. ***Contouring a video is nothing but contouring the individual frames of the video***. So, video contouring is nothing but **contouring multiple images**. To understand the *real-time application* of Contouring, contouring a webcam video is the best example.

To achieve this, 

- Access the webcam.
- Extract individual frames.
- Process the frames as if they are images to get the contours and draw them.
- Use loops wherever necessary or break statements and conditions.

*This markdown is written by: Sathyashree*. 

***Feel free to contact me on my [mailid](ksathyanrao@gmail.com).***

## Contours

### Contours:

Basically, **Contour** can be defined as an *outline* or a *border* of any object. *Contours* in Python is a ***list*** of contours of an object, which can be an image, a frame from a video and so on. Each *Contour* in the list *Contours* is a point represented as (x , y) which represent the position of the point with respect to the two axes. The contoural points usually have the same intensity.

### Uses of Contours:

Contours are mainly **used** in ***Object Detection***. Working with contours is very handy and have application in determining the size and shape of an object. Briefly stating, Contour finds its applications in anything that involves shape analysis, object detection and recognition. 

### Functions that are used to find the contours in OpenCV:

Determining contours involves multiple steps as the image needs to get ready for the process. After reading and storing the image in a variable, the image needs to be converted to either **hsv** or **grayscale** to ease the processing.

    variable_name = cv2.cvtColor(variable_name_that_stores_the_image , cv2.COLOR_BGR2HSV)
    
Example:

    hsv = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)
    
  The normal format of the image is **BGR** which represents the order of consideration of intensities of **Blue, Red** and **Green** in the image. **cv2.COLOR_BGR2HSV** converts the file to **hsv** which basically represents the level of **hue, saturation** and **lightness**. 
  
  To find all the contoural points of the image, the syntax has changed for the latest version of Python and OpenCV. 
  
  Previously, it was:
  
      _ , variable_name , _ = cv2.findContours( image_variable , cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)
      
  Now, the syntax is:
  
      image , variable_name , hierarchy = cv2.findContours( image_variable,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      
  The function cv2.findContours() takes 3 arguments, **source image, contour retrieval mode**, and **contour approximation method in order**.

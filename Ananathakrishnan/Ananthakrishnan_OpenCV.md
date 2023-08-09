# Opencv Module 2 Summary 

- This module tells us the various ways of image processing and to some new concepts like Object detection , contours , image segmentation.

- This module starts with **Image Segmentation** and then moves to **contours** and to **Shape Detection** , **Face Detection** and finaly to **flask**.

## Contours 
- First we have to convert the image into either in HSV or in grayscale using OpenCV cvtcolor() function this is necessary for easing the process because before that the image is in BGR format.
- Second then we have a function in opencv to find countors findcontours() . It takes 3 arguments, source image, contour retrieval mode, and contour approximation method in order.

## Shape Detection
- Basically Shape Detection is nothing but finding different shapes in an image and identifying them. Using OpenCV, computers can be made able to detect shapes in an image by feeding them with some information and applying certain conditions and allow them to act based on the decision. This process involves multi-steps.



## Now in this module we also learn some image processing technique now lets see one of the technique: 

## Edge Detection
- Canny Edge Detection is a popular edge detection algorithm. It was developed by John F. Canny. It is a multi-stage algorithm which involves step like

`1.Noise Reduction`

`2.Finding Intensity Gradient of the Image`

`3.Non-maximum Suppression`

`4.Hysteresis Thresholding`

## Face Detection 

### Face and Eye detection with OpenCV : Haar Classifier

- Face and Eye detection works on the algorithm called Haar Classifier which is proposed by Paul Viola and Michael Jones. In their paper, "Rapid Object Detection using Boosted Cascade of Simple Features" in 2001.

- Haar Classifier is a machine learning based approach where a function is trained from a lot of positive and negative images i.e with face and without face.

## Flask

- Flask is a web application framework written in Python. A web framework is a collection of modules and packeges which facilitates or supports the user to create dynamic web applications. 
- It facilitates creation,development and publishing of web applications. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine.
- It includes a built-in development server, unit tesing support, and is fully Unicode-enabled with RESTful request dispatching and WSGI compliance.










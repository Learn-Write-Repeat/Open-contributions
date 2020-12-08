In this module i have learnt all the Image preprocessing techniques so that we can locate, detect and identify a particular images with their respective features.
###### In this i came to know about the following:-
How Image segmentation works specially using the watershed algorithm.
Contours: Contour can be defined as an outline or a border of any object. Contours in Python is a list of contours of an object, which can be an image, a frame from a video and so on.
Finding specific patterns in image
Getting image features

###### ALSO LEARNT SEVERAL IMAGE PREPROCESSING TECHIQUES INCLUDING:-
Blending
Blurring and Smoothing
Color Mapping
Corner Detection
Edge Detection
Grid Detection

And finally creating a full fledged flask web application.

# Object Detection
Object detection is the problem of finding and classifying a variable number of objects on an image.
Object detection is a computer vision technique for locating instances of objects in images or videos. 
Object detection algorithms typically leverage machine learning or deep learning to produce meaningful results.
When humans look at images or video, we can recognize and locate objects of interest within a matter of moments. The goal of object detection is to replicate this intelligence using a computer.
The SOTA methods can be categorized into two main types: one-stage methods and two stage-methods. One-stage methods prioritize inference speed, and example models include YOLO, SSD and RetinaNet. Two-stage methods prioritize detection accuracy, and example models include Faster R-CNN, Mask R-CNN and Cascade R-CNN.

##### Practical Uses of Object Detection
Face Detection.

Counting.

Visual Search engine.

Areial Image Analysis.

### Summary

##### Image Segmentation
If we want to extract or define something from the rest of the image, eg. detecting an object from a background, we can break the image up into segments in which we can do more processing on. This is typically called Segmentation.

##### Contours
Contours are often obtained from edges, but they are aimed at being object contours. Thus, they need to be closed curves. You can think of them as boundaries (some Image Processing algorithms & librarires call them like that). When they are obtained from edges, you need to connect the edges in order to obtain a closed contour.

##### Image Preprocessing
Image pre-processing is the name for operations on images at the lowest level of abstraction whose aim is an improvement of the image data that suppress undesired distortions or enhances some image features important for further processing.
###### The steps to be taken are :
Read image.
Resize image.
Remove noise(Denoise)
Segmentation.
Morphology(smoothing edges)

##### Face Detection
Face detection is a computer technology being used in a variety of applications that identifies human faces in digital images. Face detection also refers to the psychological process by which humans locate and attend to faces in a visual scene.
With face detection, you can get the information you need to perform tasks like embellishing selfies and portraits, or generating avatars from a user's photo.

##### Integrating ML models in Flask and creating a full-fledged web-application.
In this part i understood how to integrate my model into the flask web app and exposing the API to the front end in order to get the final working model which can be accessed from anywhere around the world.


###### Anubhav Gupta
###### anubhav6864@gmail.com

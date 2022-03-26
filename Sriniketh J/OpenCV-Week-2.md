## Topics

- Segmentation - using WaterShed Algortihm
- Contours
- Extreme points in contours
- Patterns in images
- Image features
- Image Processing
> - Blending
> - Blurring and smoothing
> - Color mapping
> - Corner detection
> - Edge detection
> - Grid detection
- Face Detection
- Flask in ML

### Segmentation
Here we use a marker-based image segmentation using Watershed Algorithms.

It will use the OpenCV method ```cv2.watershed()```.

#### General Syntax
```
cv2.watershed(image, markers) -> markers
```

### Contours
Outline or border of any object.

Contours are mostly used in Object Detection

#### General Syntax
Initially convert to Gray Scale or HSV (HSV => hue, saturation, lightness)
```
cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
```

Next, we have to find all the contour points:
```
image, contours, hierarchy = cv2.findContours(image_variable, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```

### Patterns in Images
This can also be referred as Shape Detection.
Steps involved are:
- Installing pip and imutils packages.
- Importing the necessary libraries.
- Creating the ShapeDetector class.
- Loading and processing the image and finding the contours.
- Finding the center of each contour and detecting the shape.
- Displaying the output image.

#### General Syntax
Initailly we find the number of vertices.

    def detect(self, c):
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

Based on the number of vertices we predict the shape like:

3 => Triangle

4 => Square or Rectangle

5 => Pentagon etc.

### Image features
Feature detection is a method to compute abstractions of image information and making local decisions at every image point whether there is an image feature of a given type at that point or not.

Feature detection is a low-level image processing operation

Algorithms avaliable are:
- Harris Corner Detection
- Shi-Tomasi Corner Detector
- SIFT (Scale-Invariant Feature Transform)
- SURF (Speeded-Up Robust Features)
- FAST (Features from Accelerated Segment Test)
- BRIEF (Binary Robust Independent Elementary Features)
- ORB(Oriented FAST and Rotated BRIEF)

These feature detection algorithms are then used with below mentioned methods available in OpenCV to match with other images:
- FLANN based Matcher
- Brute-Force Matcher

#### General Syntax
[Refer this Example Notebook](https://github.com/AvinashMirgal/Open-contributions/blob/master/Avinash_OpenCV_Feature_Detection_and_Description.ipynb)

### Image Processing
#### [Blending](https://github.com/Learn-Write-Repeat/Open-contributions/blob/master/Neelesh_Blending-and-Pasting-Images_opencv.ipynb)
#### [Blurring and smoothing](https://github.com/Learn-Write-Repeat/Open-contributions/blob/master/Neelesh_Blurring-and-Smoothing_opencv.ipynb)
#### [Color Mapping](https://github.com/Learn-Write-Repeat/Open-contributions/blob/master/Neelesh_Color-Mappings_opencv.ipynb)
#### [Corner detection](https://github.com/Learn-Write-Repeat/Open-contributions/blob/master/Neelesh_Corner-Detection_opencv.ipynb)
#### [Edge detection](https://github.com/Learn-Write-Repeat/Open-contributions/blob/master/Neelesh_Edge-Detection_opencv.ipynb)
#### [Grid detection](https://github.com/Learn-Write-Repeat/Open-contributions/blob/master/Neelesh_Grid-Detection_opencv.ipynb)

### Face Detection
It is now becoming very famous and widespread due to current scenario, advancements in cameras, and many other reasons.

We use a HarrCascades which is a algorithm used to identify faces in images or video.

#### [Reference Notebook](https://github.com/Learn-Write-Repeat/Open-contributions/blob/master/Kavya_OpenCV_face_and_eye_detection.ipynb)

### Flask in ML
Flask is a Python Web Framework.

Initially, they were used for creating web-apps in Python.

They have grown exponentially that these can be used in ML Models so that our models don't just stay as Models but can be tested out people in real-world.

#### [Example](https://github.com/Learn-Write-Repeat/Contribution-program/tree/master/ML_models_Flask/Kumari%20Neha)

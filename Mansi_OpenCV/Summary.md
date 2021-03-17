## Summary of Module

### Image Segmentation using Watershed Algorithm
The watershed is an algorithm used for segmentation, that is, for separating different objects in an image.The watershed algorithm treats pixels values as a local topography,where high intensity denotes peaks and hills while low intensity denotes valleys. The philosophy behind this is that valleys i.e minima can be filled with different watercolors as the water rises water of different color starts to merge from different valley to prevent this barriers are build at the point where they merge.
But this gives an oversegmented result due to noise or any other irregularities in the image. So marker-based watershed algorithm is used in OpenCV where we specify which are all valley points are to be merged and which are not.
1. To remove any small white noises in the image 'morphological opening' is used. 
2. To remove any small holes in the object 'morphological closing' is used.  
3. Erosion removes the boundary pixels. That would work if objects were not touching each other. But if they are touching each other,then find the distance transform and apply a proper threshold. 
4. Erosion is used to extract sure background area. After knowing the area of foreground and Background, we create marker and label region.
5. The region we know for sure are labelled with different positive integers, the area we don't know for sure are left as zero. 
6. When the marker is ready, apply watershed. The marker will be modified.

### Contours
It is outline or border of any object. In python contours are list of contours of an image which can be an image or a frame from a video. Contours are used for shape analysis, object detection, recognition. 
But first the image need to be converted to either hsv or grayscale. To obtain contours point on image,drawing contours is necessary.To draw Contours its first argument is source image, second argument is the contours which should be passed as a Python list, third argument is index of contours. To ensure no noises included,we can use the for loop to iterate through all the contoural points. 
Canny edges are used for noise reduction,finding intensity gradient of the image, non-maximum suppression and hysteresis Thresholding. As it does edge deduction so contouring becomes easier.


### Shape Detection
It used to find different shapes in an image and identifying them. 
Installing pip and imutils packages and Importing the necessary libraries. Creating the ShapeDetector class and in it loading and processing the image and finding the contour and finding the center of each contour and detecting the shape. And displaying the output image.

### Feature Detection
Features are the vector representations of the visual content from an image. FeaturesDetection from an image plays an important role in computer vision for variety of applications including object detection, motion estimation, segmentation. Features may include edges, corners or parts of an image.
#### Various Algorithms for Feature Detection
1. Haris corner detection
2. Shi-Tomasi corner detection
3. SIFT (Scale-Invariant Feature Transform)
4. SURF (Speeded-Up Robust Features)
5. FAST algorithm for corner detection
6. ORB (Oriented FAST and Rotated Brief)

## Object Detection
Object Detection is a computer technology related to computer vision, image processing, and deep learning that deals with detecting instances of objects in images and videos.It is a technology where things, human, building, cars can be detected as object in image and videos.It is used to recognize the object with bounding box in the image.
#### Haar Classifier
Haar Cascade classifiers are used for object detection. This method was proposed by Paul Viola and Michael Jones in their paper Rapid Object Detection using a Boosted Cascade of Simple Features. Haar Cascade is a machine learning-based approach where a lot of positive and negative images are used to train the classifier.
Positive Image - These images contain the images which we want our classifier to identify. 
Negative Image - Images of everything else, which do not contain the object we want to detect.
This algorithm needs a lot of positive images and negative images to train the classifier. For each feature, it finds the best threshold which will classify it to positive and negative.
Once all the features and details are extracted, they are stored in a file and if we get any new input image, check the feature from the file, apply it on the input image and if it passes all the stage then the object is detected.
##### Face and Eye Detection
1. First we load the required XML Classifiers.
2. Then we captures the frame from camera.
3. Then using while loop we fetch each frame from the camera.
4. Convert frames into grayscales.
5. Detect face sof different sizes in input image. 
6. Then finally form the rectangle around the eye anf face of the detected image from the camera.
7. And then display the detected face and the eye. 

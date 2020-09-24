# Haar Cascade Classifiers 

## Viola Jones Algorithm
The Viola-Jones object detection framework is a machine learning approach for object detection, proposed by Paul Viola and Micheal Jones in 2001.
This framework can be trained to detect almost any object, but this primarily solves the problem of face detection in real-time. 
This algorithm has four steps: 
1. Haar Feature Selection 
2. Creating an Integral Image 
3. Adaboost Training 
4. Cascading Classifiers 

#### 1. Haar Feature Selection 
Objects are classified on very simple features as a feature to encode ad-hoc domain knowledge and operate much faster than pixel system.
The feature is similar to haar filters, hence the name 'Haar'. 
An example of these features is a 2-rectangle feature, defined as the difference of the sum of pixels of area inside the rectangle, which can be any position and scale within the original image.
3-rectangle and 4-rectangle features are also used here. 

#### 2. Integral Image Representation
The Value of any point in an Integral Image, is the sum of all the pixels above and left of that point.
An Integral Image can be calculated efficiently in one pass over the image.

#### 3. Adaboost Training 
For a window of 24x24 pixels, there can be about 162,336 possible features that would be very expensive to evaluate.
Hence AdaBoost algorithm is used to train the classifier with only the best features.

#### 4. Cascade Classifier Architecture
A cascade classifier refers to the concatenation of several classifiers arranged in successive order. It makes large numbers of small decisions as to whether its the object or not. 
The structure of the cascade classifier is of a degenerate decision tree.

## Application 
Despite the arrival of deep learning(RCNN, YOLO, etc), this method is still used in many applications for face and object detection, as this is very simple yet powerful.    
Reference: Rapid Object Detection using a Boosted Cascade of Simple Features 

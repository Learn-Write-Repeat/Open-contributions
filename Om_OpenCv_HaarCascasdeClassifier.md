# Haar Cascade Classifiers 
<p>
<b>by Om Rastogi  </b>  
<a href="https://twitter.com/OmRastogi"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg"  alt="Om's Logo" width="15" height="15"></a> 
<a href="https://medium.com/@omrastogi"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/medium.svg"  alt="Om's Logo" width="15" height="15"></a> 
<a href="https://www.linkedin.com/in/om-rastogi-a886b4b2/"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg"  alt="Om's Logo" width="15" height="15"></a> 
<a href="https://omrastogi.github.io/omrastogi/index.html"><img src="https://omrastogi.github.io/omrastogi/images/logo.png" alt="Om's Logo" width="22" height="15"></a> 
</p>

## Viola Jones Algorithm
The Viola-Jones object detection framework is a machine learning approach for object detection, proposed by Paul Viola and Micheal Jones in 2001.
This framework can be trained to detect almost any object, but this primarily solves the problem of face detection in real-time. 
This algorithm has four steps.<br><br>
<img src="https://www.researchgate.net/profile/Penousal_Machado/publication/232590123/figure/fig2/AS:300366072696842@1448624260811/Haar-features-adapted-from-20.png" alt="Viola Jones">

#### 1. Haar Feature Selection 
Objects are classified on very simple features as a feature to encode ad-hoc domain knowledge and operate much faster than pixel system.
The feature is similar to haar filters, hence the name 'Haar'. 
An example of these features is a 2-rectangle feature, defined as the difference of the sum of pixels of area inside the rectangle, which can be any position and scale within the original image. 3-rectangle and 4-rectangle features are also used here. <br><br>
<img src="https://docs.opencv.org/2.4/_images/haarfeatures.png" alt="Haar Features" >

#### 2. Integral Image Representation
The Value of any point in an Integral Image, is the sum of all the pixels above and left of that point.
An Integral Image can be calculated efficiently in one pass over the image.<br><br>
<img src="https://aishack.in/static/img/tut/integral-example-new.jpg" alt="Integral Image">


#### 3. Adaboost Training 
For a window of 24x24 pixels, there can be about 162,336 possible features that would be very expensive to evaluate.
Hence AdaBoost algorithm is used to train the classifier with only the best features.<br><br>
<img src="https://i.ytimg.com/vi/BoGNyWW9-mE/maxresdefault.jpg" alt="Boosting Algorithms" width='400' height='200'>


#### 4. Cascade Classifier Architecture
A cascade classifier refers to the concatenation of several classifiers arranged in successive order. It makes large numbers of small decisions as to whether its the object or not. The structure of the cascade classifier is of a degenerate decision tree.<br><br>
<img src="https://www.researchgate.net/publication/277929875/figure/fig9/AS:329583183319048@1455590162849/Cascade-structure-for-Haar-classifiers.png" alt="Cascade Classifier" width='600' height='200'>

## Application 
Despite the arrival of deep learning(RCNN, YOLO, etc), this method is still used in many applications for face and object detection, as this is very simple yet powerful.    

#### Reference: <a href="https://ieeexplore.ieee.org/abstract/document/990517/"> 'Rapid Object Detection using a Boosted Cascade of Simple Features'</a>, by Paul Viola and Micheal Jones in 2001  

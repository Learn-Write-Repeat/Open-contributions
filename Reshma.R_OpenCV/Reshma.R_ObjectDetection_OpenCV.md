# Object Detection in OpenCV

---

## Created by Reshma R

 Object Detection using Haar feature-based Cascade classifiers

**What is it exactly?**

This is a machine learning based approach where a cascade function is trained from a lot of positive and negative images, further used to detect objects in other images. Proposed by Paul Viola and Michael Jones in their paper, “Rapid Object Detection using a Boosted Cascade of Simple Features” in 2001, this method proves to be an effective object detection method. 

1. Firstly, the algorithm needs a lot of positive images and negative images to train the classifier. 
2. Later features have to be extracted from it, for which we use haar features.
3. Now we have all possible sizes and locations of each kernels used to calculate plenty of features. But among all these features, most of them are irrelevant. 
4. For this, we apply each and every feature on all the training images. For each feature, it finds the best threshold which will classify the faces to positive and negative. But obviously, there will be errors or misclassifications. 
5. We select the features with minimum error rate, which means they are the features that best classifies the face and non-face images.
6. Final classifier is a weighted sum of these weak classifiers. It is called weak as it alone can’t classify the image, but can do it together with others forms of strong classifier. 
7. The research paper says even 200 features provide detection with 95% accuracy. 

In an image, most of the image region is non-face region. So having a simple method to check if a window is not a face region, will be accurate. If it is not, it can be discarded in a single shot. Don’t process it again. Instead focus on region where there can be a face. This saves more time so as to check a possible face region. 

For this concept of focusing, the concept of Cascade of Classifiers was introduced. The technique is simple - instead of applying all the features on a window, group the features into different stages of classifiers and then apply one-by-one. If a window fails the first stage, it will be discarded. We don’t consider remaining features on it. If it passes, apply the second stage of features and continue the process. The window which passes all stages is a face region.

- A simple intuitive explanation of how Viola-Jones face detection works.

---

**Process for Face Detection and Eye Detection - An example**

* An image imported using OpenCV will be of the color format BGR. So it needs to be changed to grayscale in order to apply the Haar Cascade Classifier.
* The **detectMultiScale()** function is used to find the faces which returns the values in the format **(x, y, w, h)** where x is the starting x-coordinate, y is the starting y-coordinate, w is the width and h is the height.
* Further, to make it visible on the photo we use **rectangle()** function and draw rectangle around it as shown below.
  ![image](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTF9LipPzwRM-yh3DO7tNk4hHgB6MHmVKtorg&usqp=CAU)
* The part of the image consisting of the face can be taken out using **roi()** funtion, and then apply the eye cascade classifier for this part by repeating the above steps.


**Applying the above classifier for a video - Steps.**

The steps are as follows:
* First, the video capture needs to be turned on using the **VideoCapture()** function. (Enabling the webcam)
* Next, the current frame needs to be extracted using the **read** function.
* The same process, as it was done for an image, has to be repeated.


The full code is [here](https://github.com/rakshith48/Open-contributions/blob/master/Rakshith_OpenCV_ObjectDetection.ipynb)

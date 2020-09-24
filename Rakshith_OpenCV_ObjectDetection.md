# Created by Rakshith

**Get in touch with me at my LinkedIn**

[![linkedin](https://cloud.githubusercontent.com/assets/17016297/18839848/0fc7e74e-83d2-11e6-8c6a-277fc9d6e067.png)][2]

[2]: https://www.linkedin.com/in/rakshith-ramprakash-66685b198/

---

## Object Detection

In this page for Object Detection we will be using Haar feature-based Cascade classifiers.

**What is that?**

It is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, “Rapid Object Detection using a Boosted Cascade of Simple Features” in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

Initially, the algorithim need a lot of positive images and negative images to train the classifier. Then we need to extract features from it so for this we use haar features as shown the image below.Now all possible sizes and locations of each kernel s used to calculate plenty of features. But among all these features we calculated, most of them are irrelevant.For this, we apply each and every feature on all the training images. For each feature, it finds the best threshold which will classify the faces to positive and negative. But obviously, there will be errors or misclassifications. We select the features with minimum error rate, which means they are the features that best classifies the face and non-face images.Final classifier is a weighted sum of these weak classifiers. It is called weak because it alone can’t classify the image, but together with others forms a strong classifier. The paper says even 200 features provide detection with 95% accuracy. Their final setup had around 6000 features. 

![image](https://opencv-python-tutroals.readthedocs.io/en/latest/_images/haar_features.jpg)

In an image, most of the image region is non-face region. So it is a better idea to have a simple method to check if a window is not a face region. If it is not, discard it in a single shot. Don’t process it again. Instead focus on region where there can be a face. This way, we can find more time to check a possible face region. 

For this they introduced the concept of Cascade of Classifiers. Instead of applying all the 6000 features on a window, group the features into different stages of classifiers and apply one-by-one.If a window fails the first stage, discard it. We don’t consider remaining features on it. If it passes, apply the second stage of features and continue the process. The window which passes all stages is a face region.

So this is a simple intuitive explanation of how Viola-Jones face detection works.

---

**Now lets take an example like face detection and eye detection and see what are the process that needs to be done.**

* A image when we import using OpenCV it is of the color format BGR. So we need to change it to grayscale to apply the Haar Cascade Classifier.
* Now to find the faces we use the **detectMultiScale()** function and it returns values of the format **(x, y, w, h)** where x is the starting x-coordinate, y is the starting y-coordinate and w is the width and h is the height.
* Then to make it visible on the photo we use **rectangle()** function and draw rectangle around it like the below picture.
  ![image](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTF9LipPzwRM-yh3DO7tNk4hHgB6MHmVKtorg&usqp=CAU)
* Now we can jus take out the part of the image of the face using **roi()** funtion and then apply the eye cascade classifier for this part by repeating the above steps.


**We can also apply this classifier for a video as well.**

The steps are as follows:
* First the video capture needs to be turned on using **VideoCapture()** function.
* Next the current frame needs to extracted using **read** function.
* Now we need to do the same process as we did for an image.


The full code is [here](https://github.com/rakshith48/Open-contributions/blob/master/Rakshith_OpenCV_ObjectDetection.ipynb)

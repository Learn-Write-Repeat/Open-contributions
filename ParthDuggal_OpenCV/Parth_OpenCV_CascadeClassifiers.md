# Cascade Classifiers
## What are cascade classifiers ?

If you talk about the word classifier, it means something that can classify, create a boundary, make a distinction about some thing. Like we can classify between sugar and salt, tea and coffe etc. and basically we are classifying the objects into categories.
Similiarly, cascade classifiers are used to classify stuff but in terms of images. Let's say an image has a face, so a face cascade classifier can tell us if there is a face or not. Eyes , nose,etc.
### Origins
So basically this approach of calssifying things was introduced by  Paul Viola and Michael Jones in their paper [Rapid Object Detection using a Boosted Cascade of Simple Features](https://www.researchgate.net/publication/3940582_Rapid_Object_Detection_using_a_Boosted_Cascade_of_Simple_Features).
So it is a machine learning based approach where a lot of positive images(images that we want our classifier to classify) and negative images were trained in order to create cascade classifier.
### How to make your own cascade classifier ?
You can always make your own cascade classifer. The steps are as follows :
* You need a bunch of images , not a bunch but a lot of images. There should be both positive and negative images.
* You need knowledge of python and basic OpenCV and you're all set .
* Follow these links - [link1](https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/) and [link2](https://medium.com/@dikshitkathuria1803/training-your-own-cascade-classifier-detector-opencv-9ea6055242c2)
* These articles can give you a pretty good jist about creating your own cascade classifiers if you're curious. 
### Using cascade classifiers
Cascade calssifiers can be used to detect a lot of features in images or in a love video like faces, facial features, hand recognition and as you can create your own classifiers also, there is no limit to them. With a good amount of training images you can make your own and use them for future.
There are also many good classifiers available on the internet as well. You can always download them and use them for your work. 
To use cascade classifiers all you need is python in your system, OpenCV library and the .xml file. I have also created a jupyter notebook where i have shown how to use these classifiers in your programs.

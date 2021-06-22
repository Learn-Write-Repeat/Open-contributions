To elucidate an image, it is important for the computer to detect the objects and also measure their location in an image before classifying it. There are many subtasks under object detection such as face detection number plate detection, car detection, pedestrian detection which are used in autonomous cars and surveillance systems.

Object detection is done with many techniques which are classified
into modern and traditional techniques.

The traditional approach consists of 3 stages:

1. Informative region selection:
In this stage, the object is located and as the objects have different size and aspect ratios they appear at different locations as the whole image has to be scaled using a multi-scale sliding window but this is expensive.

2. feature extraction:
This is done with SIFT and HOG techniques for extracting the visual feature for recognition of the object. It provides a semantic and robust representation.

3. classification of object:
For this stage, a support vector machine (SVM) or AdaBoost is used for the classification of target objects from all other categories and to make the representation more hierarchical and informative for recognition.

Modern Approaches
This approach is used to tackle the drawbacks of traditional approaches.
This approach was able to learn more complete features.

R-CNN:
To get around the problem of the selection of a large number of the regions, Ross, Girshik, et al. proposed a way in which we use selective search to extract the 2000 areas in an image, and named them the region proposal. So now, instead of trying to classify a large number of regions, you can work with the 2000 areas. These 2000 areas are obtained by using the selective search algorithm.

Fast R-CNN:
The same author of the previous article [R-CNN) solved some of the drawbacks of R-CNN to build a faster object detection algorithm and it has been named Fast R-CNN. This approach is similar to that of the R-CNN algorithm But, instead of feeding the CNN suggestions for each region, we feed the image to the CNN to generate a convolutional feature map. The only reason this is fast is that convolutional operation is done once per image and then the feature map is generated.

SPP-NET:
SPP-Net is a convolutional neural architecture that employs spatial pyramid pooling to remove the fixed-size constraint of the network. Specifically, we add an SPP layer on top of the last convolutional layer.

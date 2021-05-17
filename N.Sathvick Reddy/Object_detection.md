Object Detection:
Object Detection is a common Computer Vision problem which deals with identifying and locating objects in the image. finding the object highlighting it can be done in many ways generally a bounding box is made around the object with name above the bounding box.

Object Detection is combination of both Image Classification(assigning class label to a image ) and object localization(drawing bounding box around objects in an image).

Object Detection Algorithms:

1)Regional Based Convolutional Neural Network

In this model we take a pre trained convolutional neural network and we retrain only the last layer based on the number of classes.Then reshape all these regions so that it matches the CNN input size.After getting the regions, SVM is trained to classify objects and background. 

For each class, we train one binary SVM.A linear regression model is trained to generate tighter bounding boxes for each identified object in the image.

In this way object detection is done in Regional Based Convolutional Neural Network

2)Fast RCNN

An input image is taken and passed to ConvNet which generates Region Of Interest.

A RoI pooling layer is applied on all of these regions to reshape them as per the input of the ConvNet.each region is passed on to a fully connected network.

A softmax layer is used on top of the fully connected network to output classes. Along with the softmax layer, a linear regression layer is also used parallely to output bounding box coordinates for predicted classes.

3)YOLO
YOLO is a convolutional neural network  for doing object detection in real-time. The algorithm applies a single neural network to the full image, and then divides the image into regions and predicts bounding boxes and probabilities for each region. These bounding boxes are weighted by the predicted probabilities.

Full form of YOLO is "You only look once " as it requires only one forward propagation pass through the neural network to make predictions.

YOLO trains on full images and directly optimizes detection performance.

YOLO is the best object detection algorithm in terms of accuracy and speed





Name:N.Sathvick Reddy
sathvicknarahari@gmail.com

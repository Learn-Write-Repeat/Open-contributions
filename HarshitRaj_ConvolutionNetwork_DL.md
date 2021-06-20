# Covalution Neural Network
  Convolution Neural Network(**CNN**) is mainly used for Computer Vission beccause it is capable of extracting the main feature of image.
  It uses **Filters** to do that and since an image will have huge amount of features to train on, so normal neural network (Straight Forward) will     take more time to train and the no. of pararmeters to train on will increase exponentially.
    For example a image is of 1080p that means it'll have 1080 * 1080 pixels. Which is equal to 1166400, that means we have to train upon 1166400         features. In this the model the input layer itself will have 1166400 nodes and then the hidden layer should have equal or more nodes to process       the image and hidden layer will obviously have five to six layers to handle that big no. of feature and train it. This will take a long time to       train the model and the parameters will be too much to handle.
  To solve this problem **CNN** came into the picture. In this network the main part is **filters** which pass trough the image and filters the         importnat features from it like (horizontal edges or vertical edges, sharpening of image, bright side of the image and etc).
  It doesn't need huge amount of parameters to detect the main features of image. It only requires filters of certain size to convolute the image. 
  For exaple, lets take a matrix which represent a part of image and that matrix presents the edge of the image and also consider  fiter of size 
  3 * 3
  ![convolution layers](https://i.stack.imgur.com/uEoXw.gif)
  

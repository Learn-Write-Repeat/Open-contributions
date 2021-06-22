**Introduction**

Since many times, Computer Vision has got a lot of importance with its offered accessibility to detect things and humans. In that, object detection has gained a lot of reputation due to its features. Before sorting an image or video, the computer must first detect the elements and accurately estimate their placement within the image/video. Face detection, motion detection, skeleton identification, and other dependencies of object detection are common use scenarios in surveillance equipment including self-driving automobiles. Object detection algorithms come in a number of different forms, with some being conventional techniques and others being more contemporary innovations. They differ from each other considering some factors such as speed, resources, and precision.

**Traditional Route:**

*It includes 3 phases. They are:*

We try to track down the object in the first level. To do so, use a multiscale sliding window to scan the entire image. In the second phase, we do the extraction of features procedure, which involves extracting visual features for object recognition utilising techniques such as SIFT and HOG. We apply Support Vector Machine (SVM) or Adaboost to classify target items in the third and the final step.

**Modern Route:**

\1. You Look Only Once (YOLO): The bounding boxes as well as class probabilities for those kind of boxes are predicted by a single neural network in YOLO. YOLO input image is divided into an SS grid, with each data point anticipating the object that is centred in that grid cell. Bounding boxes plus their related certainty scores are predicted within every grid cell.

\2. Single Shot Detector (SSD): Instead of just using preset grids like YOLO, the SSD defines a collection of predefined bounding box with variable proportions and scales to convert the output space of bounding boxes given a specified feature map. The network combines recommendations from numerous feature maps with different resolutions to manage objects of diverse dimensions.



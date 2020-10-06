# YoloV3 Algorithm
- YOLO(You Only Live Once) is an **Oject Detection Algorithm**
- A single neural network is applied to the full image. This network divides the image into regions and predicts **bounding boxes** and probabilities for each region. These bounding boxes are weighted by the predicted probabilities.
- High **Accuracy** and extremely **Fast**

![yolo architecture](https://cdn-images-1.medium.com/max/724/1*PHv_qaMpnFM21Vw9wajYuA.png)

## How to work on YoloV3:
You need to download these files:
- [yolov3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg) -> model configuration file
- [yolo.weights](https://pjreddie.com/media/files/yolov3.weights) -> pretrained model 
- [Object names](https://github.com/pjreddie/darknet/blob/master/data/coco.names) list of objects the model can detect

### Lets create a simple program to detect humans in the video

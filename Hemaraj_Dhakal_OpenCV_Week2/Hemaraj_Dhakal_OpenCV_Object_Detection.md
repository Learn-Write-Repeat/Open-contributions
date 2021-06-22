# Object Detection
## Object detection using TensorFlow frozen_inference_graph coco model and ssd_mobilenet_v3_large_coco_2020_01_14.

### Introduction
Object detection is a computer technology related to computer vision and image processing that deals with detecting instances of semantic objects of a certain class (such as humans, buildings, or cars) in digital images and videos. Well-researched domains of object detection include face detection and pedestrian detection. Object detection has applications in many areas of computer vision, including image retrieval and video surveillance.
Some of the popular algorithms used in object detection are listed below:
Fast R-CNN.
Faster R-CNN.
Histogram of Oriented Gradients (HOG)
Region-based Convolutional Neural Networks (R-CNN)
Region-based Fully Convolutional Network (R-FCN)
Single Shot Detector (SSD)
Spatial Pyramid Pooling (SPP-net)
YOLO (You Only Look Once)

### Project
This model can detect the objects are listed below:
 ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'street sign',
 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'hat', 'backpack',
 'umbrella', 'shoe', 'eye glasses', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 
 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'plate', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'mirror', 'dining table', 'window', 'desk', 'toilet', 'door',
 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'blender', 'book', 'clock', 'vase', 'scissors',
 'teddy bear', 'hair drier', 'toothbrush', 'hair brush']
 
#### Importing library
![image](https://user-images.githubusercontent.com/65659902/122662593-e833eb80-d1b3-11eb-942e-5e37b82551e5.png)

#### Getting video files from the camera and function to output video that has been capture with the threshold of 0.45.
![image](https://user-images.githubusercontent.com/65659902/122662606-06015080-d1b4-11eb-87f6-c53108e21575.png)


#### Getting the files from a local disk like coco. names that contain all the objects that it will detect. MobileNet has the configuration and the frozen graph has the weights of the model.
![image](https://user-images.githubusercontent.com/65659902/122662612-0e598b80-d1b4-11eb-9aa8-a1eacdf2806e.png)


#### Getting an image from the camera converting it in an array and detecting the objects within the camera and bounding the objects by the box with its respective detected name.
![image](https://user-images.githubusercontent.com/65659902/122662617-174a5d00-d1b4-11eb-8009-ccc72d0f0346.png)


#### We can give the video link to in this code and it will detect the objects from the video and output the video with detected objects.
![image](https://user-images.githubusercontent.com/65659902/122662620-20d3c500-d1b4-11eb-8544-fe874295b773.png)
![image](https://user-images.githubusercontent.com/65659902/122662621-28936980-d1b4-11eb-947b-ccf023df5ee1.png)

#### Testing
![image](https://user-images.githubusercontent.com/65659902/122662677-7d36e480-d1b4-11eb-9f65-5648b5710e44.png)

Thank you!!
By: Hemaraj Dhakal



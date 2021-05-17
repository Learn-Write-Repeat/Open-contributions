# Rock Paper Scissor with Keras and OpenCV

## 1.Requirements
- Keras
- os
- OpenCV
- TensorFlow
## 2.Installations
- pip install Keras
- pip install tensorflow
- pip install opencv-python

## 3.Understanding the Project

**Why** 
- Fun project but can be used to build a rock paper scissor game.

**Difficulty Level**
- Beginners

**Project is divided into two parts**

1. Training a deep neural net to detect rock, paper and scissor sign from image.
2. Deploying trained model via webcan using OpenCV.

## Flow Chart
![Flow chart](https://github.com/nakulsingh1289/Projects/blob/master/Rock%20Paper%20Scissors%20with%20AI%20using%20keras%20and%20openCV/IMG-20200918-WA0011.jpg?raw=true)

## Understanding Flowchart

- OpenCV captures image from webcam
- Then cropped image is passed to a trained deep neural network model which classifies the image into rock, paper or scissor.


### Deep Neural Net Layers
- 4 Convolution layers followed by maxpooling layers
- 2 Dense layers with activation relu
- Followed by Dropout Layers
- Final Dense layer with Softmax activation

### Author- Nakul Singh
[GitHub](https://github.com/nakulsingh1289) | 
[Kaggle](https://www.kaggle.com/nakulsingh1289) |
[LinkedIn](https://www.linkedin.com/in/nakul-singh-247205145/)

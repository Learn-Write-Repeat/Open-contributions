# Model to classify Chest X-ray images as normal or having pneumonia.


### Introduction 
The Chest X-ray data used is available on [Kaggle](https://https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia).  The data is split into two categories:

1.   Normal
2.   Pneumonia

This data can be used to train a model which can then be used to directly predict from the chest x-ray image whether a patient has pneumonia. This model can be used as a preliminary detection method for pneumonia. Also if it is directly deployed on a portable x-ray machine then instantaneous preliminary diagnosis is possible. It can also be deployed as a mobile application that can diagnose from an x-ray image.  



### Setup
The model is trained using a Google Cloud GPU in Colab. To access the training data from Colab it is uploaded to Google Drive and the drive is mounted in colab. By accessing the data through the drive, the data can be accessed without having to upload it to the environment each time the session is terminated.

### Model
The model used is built up on top a [MobileNetV2](https://ai.googleblog.com/2018/04/mobilenetv2-next-generation-of-on.html) architecture, which is used as a pre-trained feature extractor, i.e., for transfer learning. The MobileNet model is chosen as it is more compatible with mobile devices and can be deployed on devices such as a portable x-ray machine for instantaneous diagnosis.  
On top of the MobileNetV2 architecture a GlobalAveragePooling layer and a dense layer with ReLu activation is added before the final single neuron classification layer that has sigmoid activation.   



### Training and Testing

The model is trained using the data in the train folder and is evaluated using the data in the test folder with the following results:
* The final training accuracy achieved was 98.64%
* The testing precision was 0.82
* The testing recall was 0.98
* The testing f1 score was 0.89
* The testing accuracy was 0.85


### Saving the model
The trained model is saved as keras model in HDF5 format in the model folder. 

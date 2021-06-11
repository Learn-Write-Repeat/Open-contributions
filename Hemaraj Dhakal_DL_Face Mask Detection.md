Masks should be used as part of a comprehensive strategy of measures to suppress transmission and save lives; the use of a mask alone is not sufficient to provide an adequate level of protection against COVID-19.So this project helps to detect whether the person is wearing Mask or not. We can use this in live cc camera video across the street. so that we are able to know who is wearing the mask and who is not.
To do this project, I have used deep learning Binary classification for training the image and opencv for detecting the mask in live video feed. So let’s get started.
I have done this project of training the model in google colab and testing in my local machine.

In this image, I have mounted Google Drive so that I can import the files from my drive.
![image](https://user-images.githubusercontent.com/65659902/121721725-4998f200-cb04-11eb-87a1-3e533a2b1ff0.png)

In this image, I have imported the files and inside the Dataset folder there are two categories which are Mask and No_Mask and 1500 each image of people wearing masks and not masks are listed inside the dataset folder.
![image](https://user-images.githubusercontent.com/65659902/121721860-70572880-cb04-11eb-94e8-151468e1230d.png)

Imported some import packages for image pre-processing.
![image](https://user-images.githubusercontent.com/65659902/121722147-c926c100-cb04-11eb-948b-b637c4918676.png)

In this image, all the images are changed in matrix array and resized in 120,120 pixel value. After getting the matrix value of the resize image the labels and image array is appended into a data list. The data are not randomly shuffled after that image array and labels are put in different lists X and y.
![image](https://user-images.githubusercontent.com/65659902/121722003-9b417c80-cb04-11eb-9bc9-35ccd5be674b.png)

Values are divided by 255 so that we can get values in the range of 0 and 1. CNN works better in small numbers so we did this.
![image](https://user-images.githubusercontent.com/65659902/121722184-d5128300-cb04-11eb-8934-fa958f0a24f7.png)

We are using keras to train our model and importing some import keras packages for training our model.
![image](https://user-images.githubusercontent.com/65659902/121722206-dd6abe00-cb04-11eb-9b97-f959f56d3bca.png)

We are using keras sequential models for this training. We have used two convolutional layers. In the first layers I am using 128 filters, kernel size of 3,3, relu(Rectified linear unit) as our activation function and max pooling of 7,7 is used in first layers. In the second layer I am using 64 filters, kernel size of 5,5, relu(Rectified linear unit) as our activation function and max pooling of 2,2 is used in the second layer.  Flattern is also used to convert our value into a 1D array. Dropout of 0.5 is used  and 1024 and 512 neural network dense is used with relu activation function. At last 1 dense neuron is given because our output is binary with sigmoid activation function.
Binary_crossentropy is used for calculating loss and adam optimizers are also used at compilation. I used a model checkpoint to save a model of best accuracy and batch size of 8 with 20 epochs is used to train the model separating 0.1% of total data for validation.
![image](https://user-images.githubusercontent.com/65659902/121722269-f4111500-cb04-11eb-8e19-3e9cbb9866ac.png)

I didn’t get that much good accuracy because for this training idea my number of images are also low and features of images are not that much different. So, binary classification is better for two different species classification like cat and dog, man and women, etc. I will be sharing the github link of a better way of doing binary classification but that is a little more complicated than this but that has accuracy of around 98% percent. But this model also works fine in live video feed the way of implementing this in live video feed is given below:
First perform the above steps in google colab, local machines or any other platform and after that save the model that is generated from this training and try running the code below in the local machine.
Note: The model path should be given properly otherwise it won’t work and if you are using an external camera opencv.videocapture should be 1 not 0.
![image](https://user-images.githubusercontent.com/65659902/121722302-fecbaa00-cb04-11eb-99d8-7230b4a46c0f.png)

![image](https://user-images.githubusercontent.com/65659902/121722347-0e4af300-cb05-11eb-9e89-d03e7997999d.png)

![image](https://user-images.githubusercontent.com/65659902/121722379-1acf4b80-cb05-11eb-9d66-85c0fade93be.png)

The evidence of this model performance is given below:
![image](https://user-images.githubusercontent.com/65659902/121722420-27ec3a80-cb05-11eb-83fc-e9e4b3674cfe.png)

![image](https://user-images.githubusercontent.com/65659902/121722461-333f6600-cb05-11eb-857e-d07f8abdb572.png)


The github link of face recognition project which is 98% accuracy but little complicated is given here: https://github.com/Hemraj183/Face-Mask-Detection
Thank you.


# Getting Start with GAN

In this notebook, we're going to create our first generative adversarial network (GAN). we will build and train a GAN that can generate hand-written images of digits (0-9) from scratch. In this notebook we are use Torch library. We so ready in journey of adding GAN tool in your collection.



## Learning Objectives

- Build the generator and discriminator components of a GAN from scratch.
- Create generator and discriminator loss functions.
- Train your GAN and visualize the generated images.

  
## Dataset

The training images our discriminator will be using is from a dataset called [MNIST](http://yann.lecun.com/exdb/mnist/). It contains 60,000 images of handwritten digits, from 0 to 9, like these:
  
![MNIST Digits](https://images.deepai.org/custom-datasets/images/348c034a7411428ead2e04742df3d9ff/mnist-thumb.jpg)
## Generator

The first step is to build the generator component.


We will start by creating a function to make a single layer/block for the generator's neural network. Each block should include a [linear transformation] to map to another shape, a [batch normalization] for stabilization, and finally a non-linear activation function (we use a [ReLU here].

## Discriminator

The discriminator will build a neural network with 4 layers. It will start with the image tensor and transform it until it returns a single number (1-dimension tensor) output. This output classifies whether an image is fake or real. Note that you do not need a sigmoid after the output layer since it is included in the loss function. Finally, to use your discrimator's neural network you are given a forward pass function that takes in an image tensor to be classified.


![Generate](https://sthalles.github.io/assets/dcgan/GANs.png)
## Putting all together

Finally, you can put everything together! For each epoch, you will process the entire dataset in batches. For every batch, you will need to update the discriminator and generator using their loss. Batches are sets of images that will be predicted on before the loss functions are calculated (instead of calculating the loss function after each image). Note that you may see a loss to be greater than 1, this is okay since binary cross entropy loss can be any positive number for a sufficiently confident wrong guess. 

It’s also often the case that the discriminator will outperform the generator, especially at the start, because its job is easier. It's important that neither one gets too good (that is, near-perfect accuracy), which would cause the entire model to stop learning. Balancing the two models is actually remarkably hard to do in a standard GAN

## result

![output Digits](output.png)

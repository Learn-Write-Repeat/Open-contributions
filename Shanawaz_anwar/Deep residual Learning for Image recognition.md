### Deep Residual Learning for Image Recognition
By Mohammad Shanawaz

## Problem this paper is trying to solve
Adding more layers lead to model's accuracy saturating, then rapidly decaying, and higher training errors - the degradation problem. a question arose: Is learning better networks as easy as stacking more layers? An obstacle to this question was the vanishing/exploding gradients problem. The degradation of the training accuracy indicates that not all systems are similarly easy to optimize. Considering a shallower architecture and its deeper counterpart that adds more layers onto it: the added layers are identity mapping and the other layers are copied from the learned shallower model. therefore, a deeper model should produce no higher training error than its shallower counterpart.

## Solution: Deep residual learning framework

1. start with a network that performs well
2. Add additional layers that are forced to be the identity function, that is, they simply pass along whatever information arrives at them without change
3. This network is deeper, but must have the same performance as the original network by construction since the new layers do not do anything
4. Layers in a network can learn the identity function, so they should be able to exactly replicate the performance of this deep network if it is optimal

This thought experiment leads them to propose their deep residual learning architecture. They construct their network of what they call residual building blocks. The image below shows one such block. These blocks have become known as ResBlocks.

![image](https://cdn-images-1.medium.com/max/1500/1*4sO3vjCdUlYQZcRq-GNqyw.png)

## Contact
[Linkedin](https://www.linkedin.com/in/msanwar/)

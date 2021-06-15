### Weight  Initialization in Deep Learning Neural Networks

By Shanawaz Anwar:

![Neural Network](https://github.com/maaz97py/Open-contributions/blob/master/55.PNG?raw=true)



## What is Weight Initialization?

Weight initialization is a procedure to set the weights of a neural networks  to small random values that define the starting point of the optimization(learning or training) of 
neural network model.

## Different Weight Initialization Techniques

1. Zero Initialization
2. Random Initialization
3. Xavier Normal Initialization


## Zero Initialization:
Initializing all the weights with zero leads the neurons to learn same features during training.
In fact, any constant initialization scheme will perform very poorly. Consider a neural network with two hidden units, and assume we initialize all the biases to 0 and the weights with some constant α. If we forward propagate an input (x1​,x2​) in this network, the output of both hidden units will be relu(αx1​+αx2​). Thus, both hidden units will have an identical influence on the cost, which will lead to identical gradients. Thus, both neurons will evolve symmetrically throughout training, effectively preventing different neurons from learning different things.

## Random Initialization :
Assigning random values to weights is better than 0 assignment. 
We could use two statistical distributions for this: either the standard normal distribution or the uniform distribution.

Effectively, you’ll simply initialize all the weights vectors randomly. Since they then have numbers > 0, your neurons aren’t dead and will work from the start. You’ll only have to expect that performance is (very) low the first couple of epochs, simply because those random values likely do not correspond to the actual distribution underlying the data.

There’s however two types of problems that you can encouunter when you initialize your weights randomly: the vanishing gradients problem and the exploding gradients problem. If you initialize your weights randomly, two scenarios may occur:

- Your weights are very small. Backpropagation, which computes the error backwards, chains various numbers from the loss towards the updateable layer. Since 0.1 x 0.1 x 0.1 x 0.1 is very small, the actual gradient to be taken at that layer is really small (0.0001). Consequently, with random initialization, in the case of very small weights – you may encounter vanishing gradients. That is, the farther from the end the update takes place, the slower it goes. This might yield that your model does not reach its optimum in the time you’ll allow it to train.

- In another case, you experience the exploding gradients scenario. In that case, your initialized weights are very much off, perhaps because they are really large, and by consequence a large weight swing must take place. Similarly, if this happens throughout many layers, the weight swing may be large: 10**6⋅10**6⋅10**6⋅10**6=1024. Two things may happen then: first, because of the large weight swing, you may simply not reach the optimum for that particular neuron (which often requires taking small steps). Second, weight swings can yield number overflows in e.g. Python, so that the language can no longer process those large numbers. The result, NaNs (Not a Number), will reduce the power of your network.

## To prevent the gradients of the network’s activations from vanishing or exploding, we will stick to the following rules of thumb:
- The mean of the activations should be zero.
- The variance of the activations should stay the same across every layer.

## Xavier Normal Initialization :

When your neural network is Tanh or sigmoid activated, you can choose Xavier Normal method for weight initialization purpose.

![Xavier Normal]()




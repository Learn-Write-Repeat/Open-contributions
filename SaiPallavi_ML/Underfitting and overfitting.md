
# Overfitting and Underfitting 

Overfitting and Underfitting are the two main problems that occur in machine learning and degrade the performance of the machine learning models.

The main goal of each machine learning model is to generalize well. Here generalization defines the ability of an ML model to provide a suitable output by adapting the given set of unknown input. It means after providing training on the dataset, it can produce reliable and accurate output. 
Hence, the underfitting and overfitting are the two terms that need to be checked for the performance of the model and whether the model is generalizing well or not.

Before diving further let’s understand two important terms:

* Bias: Assumptions made by a model to make a function easier to learn.
* Variance: If you train your data on training data and obtain a very low error, upon changing the data and then training the same previous model you experience a high error, this is variance.

# Underfitting

Underfitting occurs when our machine learning model is not able to capture the underlying trend of the data. 
To avoid the overfitting in the model, the fed of training data can be stopped at an early stage, due to which the model may not learn enough from the training data. As a result, it may fail to find the best fit of the dominant trend in the data.

In the case of underfitting, the model is not able to learn enough from the training data, and hence it reduces the accuracy and produces unreliable predictions.

# An underfitted model has high bias and low variance.


# Overfitting 

Overfitting occurs when our machine learning model tries to cover all the data points or more than the required data points present in the given dataset
Because of this, the model starts caching noise and inaccurate values present in the dataset, and all these factors reduce the efficiency and accuracy of the model.

# The overfitted model has low bias and high variance.


A general view of both the problems :

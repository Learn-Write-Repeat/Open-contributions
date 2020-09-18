# A Gentle Introduction to XGBoost for Applied Machine Learning
## What is XGBoost

XGBoost is the leading model for working with standard tabular data (the type of data you store in Pandas DataFrames, as opposed to more exotic types of data like images and videos).       XGBoost models dominate many Kaggle competitions.

To reach peak accuracy, XGBoost models require more knowledge and model tuning than techniques like Random Forest. After this tutorial, you'ill be able to

    Follow the full modeling workflow with XGBoost
    Fine-tune XGBoost models for optimal performance

XGBoost is an implementation of the Gradient Boosted Decision Trees algorithm (scikit-learn has another version of this algorithm, but XGBoost has some technical advantages.) What is Gradient Boosted Decision Trees? We'll walk through a diagram.

<br/>![What is XGBoost](https://i.imgur.com/e7MIgXk.png)<br/>
We go through cycles that repeatedly builds new models and combines them into an ensemble model. We start the cycle by calculating the errors for each observation in the dataset. We then build a new model to predict those. We add predictions from this error-predicting model to the "ensemble of models."

To make a prediction, we add the predictions from all previous models. We can use these predictions to calculate new errors, build the next model, and add it to the ensemble.

There's one piece outside that cycle. We need some base prediction to start the cycle. In practice, the initial predictions can be pretty naive. Even if it's predictions are wildly inaccurate, subsequent additions to the ensemble will address those errors.

## XGBoost Features

The library is laser focused on computational speed and model performance, as such there are few frills. Nevertheless, it does offer a number of advanced features.

### Model Features 

The implementation of the model supports the features of the scikit-learn and R implementations, with new additions like regularization. Three main forms of gradient boosting are supported:

    Gradient Boosting algorithm also called gradient boosting machine including the learning rate.
    Stochastic Gradient Boosting with sub-sampling at the row, column and column per split levels.
    Regularized Gradient Boosting with both L1 and L2 regularization.

### System Features

The library provides a system for use in a range of computing environments, not least:

    Parallelization of tree construction using all of your CPU cores during training.
    Distributed Computing for training very large models using a cluster of machines.
    Out-of-Core Computing for very large datasets that don’t fit into memory.
    Cache Optimization of data structures and algorithm to make best use of hardware.

## Why Use XGBoost?

The two reasons to use XGBoost are also the two goals of the project:

    Execution Speed.
    Model Performance.
    
XGBoost and Gradient Boosting Machines (GBMs) are both ensemble tree methods that apply the principle of boosting weak learners (CARTs generally) using the gradient descent architecture. However, XGBoost improves upon the base GBM framework through systems optimization and algorithmic enhancements.


<br/>![What is XGBoost](https://miro.medium.com/max/875/1*FLshv-wVDfu-i54OqvZdHg.png)<br/>



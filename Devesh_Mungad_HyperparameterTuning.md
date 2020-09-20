##What are hyperparameters and how do they differ from parameters?

To understand hyperparameters and their significance in a Machine Learning or Deep Learning model, we need to understand how they differ from model parameters. Model parameters are the sets of values that are are determined by processing the training data through the ML algorithm. They vary based on the data and are determined internally i.e. we do not set these parameters manually. Model parameters include the weights and biases in neural networks, word frequency and lexical diversity in NLP, coefficients of variables in regression and nodes in a decision tree to name a few.
Model Hyperparameters, unlike parameters are external factors that regulate the architecture of the ML model and in turn modify the parameters. Hyperparameters are not affected by the data as they are used fundamentally to define the structure of the ML model itself. Model hyperparameters include penalty and max iterations in regression, weight decay and momentum in neural networks, maximum depth and class weight in decision trees. These parameters and hyperparameters define the different aspects of the tree and vary from one model to another and from one algorithm to another respectively.

##The need for hyperparameter tuning

The need for hyperparameter tuning arises as we want to specify how our model works. Simpler models like linear regression do not have many hyperparameters and therefore tuning is not a requisite. However, complex ML models like DNN (Deep Neural Network) and Ensemble Learning algorithms have a multitude of model hyperparameters which when altered, can impact the results noticeably. Hyperparamter optimization can be implemented to tailor the model to suit our use case. Optimization of the structure of ML models has many advantages like increase in acuuracy, prescision and other metrics. It can be used to avoid over and underfitting the model so as to generalize the model even more. In case of resource intesive algorithms, we can limit the time, memory and computation required to generate the model by tweaking the relevant hyperparameters. All in all, optimal hyperparameters give us control over our models.

##How to tune hyperparameters

Before getting into hyperparameter optimization for any ML model, we must first understand the hyperparameters themselves and how they

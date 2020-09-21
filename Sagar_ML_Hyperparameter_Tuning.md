## What is Hyperparameter Tuning?

* First we have to know about the Hyperparameter, There are a lot of different machine learning models. They all are different in some way or the other, but what makes them different is nothing but input parameters for the model. These input parameters are called as **Hyperparameters**.
* Often, We are not aware of optimal values for hyperparameters which would generate the best model output. So, what we tell the model is to explore and select the optimal model architecture automatically. This selection process for hyperparameter is known as **Hyperparameter Tuning**.

## Why do we need Hyperparameter Tuning?

* If you feel while training the model that what happened with my model or you are not getting good accuracy, even you did better work in feature engineering then hyperparameter tuning can help you.
* we used it to minimize the losses and get those parameters which are really helping to get the desired accuracy.

## What are the types of hyperparameter tuning techniques?
### Manual Search
In Manual Search, we choose some model hyperparameters based on our judgment. then we train the model, evaluate its accuracy and start the process again. This loop is repeated until we get the satisfactory accuracy.

### Grid Search
In Grid Search, we set up a grid of hyperparameters then we fed to the GridSearchCV function and train our model on each of the possible combinations. **Grid Search** is slower compared to **Random Search** but it can be overall more effective because it can go through the whole search space.

### Random Search
In Random Search, we do the same only the grid of hyperparameters will fed to the RandomizedSearchCV function. **Random Search** is faster compared to **Grid Search** but it can lead to miss some informations due to take random spaces.

### Bayesian Optimization
Bayesian optimization uses probability to find the minimum of a function. The final aim is to find the input value to a function which can give us the lowest possible output value. It has been proved to be more efficient than **Random Search**, **Grid Search** or **Manual Search**. It can lead to better performance in the testing phase and reduced optimization time.

### Artificial Neural Network Tuning
Using **KerasClassifier** or **KerasRegressor** wrapper, it is possible to apply **Grid Search** and **Random Search** for Deep Learning models in the same way it was done by using scikit-learn Machine Learning models. it will try to optimize some of our ANN parameters eg. how many neurons to use in each layer and which activation function and optimizer to use. 

## How can we implement these techniques
click here on this link: https://github.com/sagarbadki/Open-contributions/blob/master/Sagar_ML_Hyperparameter_Tuning.ipynb

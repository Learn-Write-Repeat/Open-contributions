## What are hyperparameters?

To understand hyperparameters and their significance in a Machine Learning or Deep Learning model, we need to understand how they differ from model parameters. Model parameters are the sets of values that are determined by processing the training data through the ML algorithm. They vary based on the data and are determined internally i.e. we do not set these parameters manually. Model parameters include the weights and biases in neural networks, word frequency and lexical diversity in NLP, coefficients of variables in regression and nodes in a decision tree to name a few.

Model Hyperparameters, unlike parameters are external factors that regulate the architecture of the ML model and in turn modify the parameters. Hyperparameters are not affected by the data as they are used fundamentally to define the structure of the ML model itself. Model hyperparameters include penalty and max iterations in regression, weight decay and momentum in neural networks, maximum depth and class weight in decision trees. These parameters and hyperparameters define the different aspects of the tree and vary from one model to another and from one algorithm to another respectively.

## The need for hyperparameter tuning

The need for hyperparameter tuning arises when we want to specify how our model works. Simpler models like linear regression do not have many hyperparameters and therefore tuning is not a requisite. However, complex ML models like DNN (Deep Neural Network) and Ensemble Learning algorithms have a multitude of model hyperparameters which when altered, can impact the results noticeably. Hyperparamter optimization can be implemented to tailor the model to suit our use case. Optimization of the structure of ML models has many advantages like increase in accuracy, precision and other metrics. It can be used to avoid over and underfitting the model so as to generalize the model even more. In case of resource intensive algorithms, we can limit the time, memory and computation required to generate the model by tweaking the relevant hyperparameters. Overall, tuning hyperparameters give us control over our models.

## How to tune hyperparameters

Before getting into hyperparameter optimization for any ML model, we must first understand the hyperparameters themselves and how they transform our model. For many hyperparameters, like splitter and random state in the decision tree model, tuning is not necessary and default values provide the best output while some do not have considerable effect on the output. Once the hyperparameters that are to be optimized have been identified, there are four widely used approaches for optimization:

1. **Manually changing the hyperparameters:**

    As the name suggests, in this method we choose initial values based on our best estimation of the optimal values. Then we analyze the evaluation metrics of the model and change the hyperparameters as per our requirements. This method is generally not used as it is inefficient and we can only check one configuration of values at a time (unless we train multiple models).
    
    Code:
    ```python
    model=RandomForestClassifier(n_estimators=150,
                                 max_depth=10,
                                 min_samples_split=4, 
                                 max_features=3)
    model.fit(X, y)
  
 2. **Grid Search:**
 
     In the grid search method we create a dictionary containing the hyperparameters we want to optimize as keys and an array containing multiple discrete values (of that hyperparameter) as the value (of that key). Then we use the GridSearchCV() from the sklearn.model_selection package to go through all the possible combinations of the discrete values in the dictionary. Some important parameters of the GridSearchCV() function are:
     * estimator - The model being used for fitting.
     * param_grid - The dictionary containing the values of the hyperparameters.
     * scoring - The metric that we use to evaluate the model like accuracy, roc_auc for classification, homogeneity_score for clustering, explained_variance and r2 for regression.
     * n_jobs - Number of jobs that can run in parallel.
     * cv - We can set the K in Kfold cross validation using this parameter.
     * verbose - This can be used to set the verbosity or the number of messages created.
     
     Code:
     ```python
     model=GradientBoostingClassifier()
     hpdict={'learning_rate': [0.01,0.05,0.1,0.2],
             'n_estimators': [20,50,100,200,500],
             'subsample': [0.6,0.7,0.8,0.9,1]
            }        
     gs=GridSearchCV(estimator=model, param_grid=hpdict, scoring='precision', n_jobs=-1, cv=4, verbose=True)
     gs.fit(X, y)
     
3. **Random Search:**

    Random search creates models with random values of hyperparameters where we can specify the range of values. This method can be more efficient as compared to Grid search as it is less resource intensive and can provide better results in the same number of iterations. This is because the number of models that grid search creates is much larger as it goes through all the possible combinations to find the best fit. Random search is best used when the dataset is large and there are some important and some not so important hyperparameters. Grid search is best used for small datasets and where finding the best performing model is worth the resource tradeoff. For implementation, RandomizedSearchCV() from the sklearn.model_selection package is used. Like Grid Search, we also create a dictionary containing values of hyperparameters. Some important parameters of the GridSearchCV() function are:
    * estimator - The model being used for fitting
    * param_distributions - The dictionary containing the values of the hyperparameters.
    * scoring - The metric that we use to evaluate the model like accuracy, roc_auc for classification, homogeneity_score for clustering, explained_variance and r2 for regression.
    * n_iter - Number of iterations i.e. random combinations that Random Search will go through.
    * cv - We can set the K in Kfold cross validation using this parameter.
    * n_jobs - Number of jobs that can run in parallel.
    * verbose - This can be used to set the verbosity or the number of messages created.
    
    Code:
    ```python
    model=xgb.XBGClassifier()
    hpdict={'eta':random.uniform(0.01, 0.2),
            'subsample': random.uniform(0.25, 1),
            'n_estimators' : [20,50,100,200,500]
           }
    rs=RandomizedSearchCV(estimator=model, param_distributions=hpdict, scoring='precision', n_iter=20, cv=4, n_jobs=-1, verbose=True)
    rs.fit(X, y)
    
4. **Automatic Hyperparameter Tuning:**

    Hyperparameter tuning can be automated by either automating the entire process using libraries like h2o and tpot or by using bayesian optimization algorithm. h2o is an open source AI and ML platform for python and R. Its AutoML package can generate and rank multiple models with different algorithms and configurations. TPOT is another open source library that can create and evaluate various pipelines that process the raw data and construct models. These libraries can be really convenient to use for relatively simple machine learning use cases.
    
    skopt (Scikit-Optimize) and hyperopt are libraries that adopt the latter method i.e. using optimization algorithms for a particular model that we create. Bayesian optimization is more efficient as it changes the values of hyperparameters based on past results (unlike Grid and Random Search which are uniform), thereby coming closer to the optimal configuration with increasing iterations. Bayesian optimization utilizing Gaussian Processes surrogate model can be performed using skopt.gp_minimize. Bayesian optimization utilizing TPE (Tree Parzen Estimator) surrogate model can be implemented by importing and using tpe method from the hyperopt library.
    
    
    
    
The image below illustrates the difference between the three methods. The grid represents the combinations of two hyperparameters (x-hp1, y-hp2) and the optimal configuration lies somewhere in the grid. Bayesian algorithm can traverse the grid more efficiently than random search which in turn can traverse it more efficiently than grid search.

![Image comparing different methods](https://github.com/Choronzon13/Open-contributions/blob/master/hptuning.png?raw=true)

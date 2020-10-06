# CLASSIFICATION IN MACHINE LEARNING

## What is Classification?

<img src = "https://cdn.analyticsvidhya.com/wp-content/uploads/2020/01/cifar-10-classification.jpg" width="70%">

**Classification** is a process of categorizing a given set of data into classes. 
It can be performed on both **structured** or **unstructured data**. 
The process starts with predicting the class of given data points. 
The classes are often referred to as **target**, **label** or **categories**.

The classification predictive modeling is the task of approximating the mapping function from input variables to discrete output variables. 
The main goal is to identify which class/category the new data will fall into.

<img src = "https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/11/classification.png">

## Classification Terminologies In Machine Learning

- **Classifier** – It is an algorithm that is used to map the input data to a specific category.
- **Classification Model** – The model predicts or draws a conclusion to the input data given for training, it will predict the class or category for the data.
- **Feature** – A feature is an individual measurable property of the phenomenon being observed.
- **Binary  Classification** – It is a type of classification with two outcomes, for eg – either true or false.
- **Multi-Class Classification** – The classification with more than two classes, in multi-class classification each sample is assigned to one and only one label or target.
- **Multi-label Classification** – This is a type of classification where each sample is assigned to a set of labels or targets.
- **Initialize** – It is to assign the classifier to be used for the
- **Train the Classifier** – Each classifier in sci-kit learn uses the fit(X, y) method to fit the model for training the train X and train label y.
- **Predict the Target** – For an unlabeled observation X, the predict(X) method returns predicted label y.
- **Evaluate** – This basically means the evaluation of the model i.e classification report, accuracy score, etc.

# Classification Algorithms

## Logistic Regression

It is a classification algorithm in machine learning that uses one or more independent variables to determine an outcome. The outcome is measured with a dichotomous variable meaning **it will have only two possible outcomes**.
The goal of logistic regression is to find a best-fitting relationship between the dependent variable and a set of independent variables. It is better than other binary classification algorithms like nearest neighbor since it quantitatively explains the factors leading to classification.

<img src = "https://machinelearningmind.files.wordpress.com/2019/11/screenshot-2019-11-25-at-7.02.08-am.png">

### Use Cases

- Identifying risk factors for diseases
- Word classification
- Weather Prediction
- Voting Applications

## Naive Bayes Classifier

It is a classification algorithm based on **Bayes’s theorem** which gives an assumption of independence among predictors. In simple terms, a Naive Bayes classifier assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature.
Even if the features depend on each other, all of these properties contribute to the probability independently. Naive Bayes model is easy to make and is particularly useful for comparatively large data sets. Even with a simplistic approach, Naive Bayes is known to outperform most of the classification methods in machine learning. Following is the Bayes theorem to implement the Naive Bayes Theorem.

<img src = "https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/11/naive.png">

### Use Cases

- Disease Predictions
- Document Classification
- Spam Filters
- Sentiment Analysis

## K-Nearest Neighbor

It is a lazy learning algorithm that **stores all instances corresponding to training data in n-dimensional space**. It is a **lazy learning algorithm** as it does not focus on constructing a general internal model, instead, it works on storing instances of training data.

<img src = "https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/11/knn.png">

### Use Cases

- Industrial applications to look for similar tasks in comparison to others
- Handwriting detection applications
- Image recognition
- Video recognition
- Stock analysis

## Decision Tree

The decision tree algorithm builds the classification model in the form of a **tree structure**. It utilizes the if-then rules which are equally exhaustive and mutually exclusive in classification. The process goes on with breaking down the data into smaller structures and eventually associating it with an incremental decision tree. The final structure looks like a tree with nodes and leaves. The **rules are learned sequentially** using the training data one at a time. Each time a rule is learned, the tuples covering the rules are removed. The process continues on the training set until the termination point is met.

<img src = "https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/11/decision.png">

### Use Cases

- Data exploration
- Pattern Recognition
- Option pricing in finances
- Identifying disease and risk threats

## Random Forest

Random decision trees or random forest are an **ensemble learning method** for classification, regression, etc. It operates by constructing a multitude of decision trees at training time and outputs the class that is the mode of the classes or classification or mean prediction(regression) of the individual trees.

<img src = "https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/11/random.png">

### Use Cases

- Industrial applications such as finding if a loan applicant is high-risk or low-risk
- For Predicting the failure of  mechanical parts in automobile engines
- Predicting social media share scores
- Performance scores

## Support Vector Machines

An SVM model is basically a representation of different classes in a hyperplane in multidimensional space. The hyperplane will be generated in an iterative manner by SVM so that the error can be minimized. The goal of SVM is to divide the datasets into classes to find a maximum marginal hyperplane (MMH).

<img src = "https://www.tutorialspoint.com/machine_learning_with_python/images/working_of_svm.jpg">

### Use Cases

- Face detection
- Text and hypertext categorization
- Classification of images
- Bioinformatics
- Handwriting recognition


# Classifier Evaluation

## Classification Report

A classification report will give the following results, it is a sample classification report of an SVM classifier using a cancer_data dataset.

<img src = "https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/11/accuracy-2.png">

* **Accuracy**
   * Accuracy is a ratio of correctly predicted observation to the total observations
   * True Positive: The number of correct predictions that the occurrence is positive.
   * True Negative: Number of correct predictions that the occurrence is negative.
* **F1- Score**
   * It is the weighted average of precision and recall
* **Precision And Recall**
   * Precision is the fraction of relevant instances among the retrieved instances, while recall is the fraction of relevant instances that have been retrieved over the total number of instances. They are basically used as the measure of relevance.

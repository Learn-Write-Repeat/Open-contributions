### In the module we have learnt about:

- **Supervised Learning**

It is the use of labeled datasets to train algorithms that to classify data or predict outcomes accurately. As input data is fed into the model, it adjusts its weights until the model has been fitted appropriately, which occurs as part of the cross validation process. 

- **Unsupervised learning**

Unsupervised learning is the training of a machine using information that is neither classified nor labeled and allowing the algorithm to act on that information without guidance. Here the task of the machine is to group unsorted information according to similarities, patterns, and differences without any prior training of data. 

- **Regression**

Regression falls under supervised learning wherein the algorithm is trained with both input features and output labels. Linear regression approach is used to perform regression on data. Linear regression finds the linear relationship between the dependent variable and one or more independent variables using a best-fit straight line. 

- **Classification** 

Classification is a supervised learning approach in which the computer program learns from the data given to it and make new observations or classifications.

- **Bias** 

Bias is the difference between our actual and predicted values. Bias is the simple assumptions that our model makes about our data to be able to predict new data. High bias indicates model underfitting.

- **Variance**

Variance is a is a type of error that occurs due to a model's sensitivity to small fluctuations in the training set. High variance would cause an algorithm to model the noise in the training set and result in overfitting.

- **ROC score**

ROC-AUC is indicative of degree of separability /distinction or intermingling /crossover between the predictions of the two classes. Higher the score, higher the distinction and lower the crossover of the predictions of the two classes. 

- **Confusion matrix**

A confusion matrix is a performance measurement technique for Machine learning classification. It is a kind of table which helps you to the know the performance of the classification model on a set of test data for that the true values are known. 
The outcomes of the confusion matrix are:

- TP: True Positive: Predicted values correctly predicted as actual positive
- FP: Predicted values incorrectly predicted an actual positive. i.e., Negative values predicted as positive
- FN: False Negative: Positive values predicted as negative
- TN: True Negative: Predicted values correctly predicted as an actual negative

- **Accuracy**

It is determined by the total number of correct predictions divided by total number of predictions made for a dataset.

                                         total number of correct predictions 
                             Accuracy = ----------------------------------------  
                                            total number of predictions 


- **Precision**

Precision is defined as the ratio of True Positives to all the positives predicted by the model.

                         TP 
        Precision = --------------
                       TP + FP 
                       
- **Recall**

It is the ratio of True Positives to all the positives in your dataset.

                   TP 
      Recall = -----------
                 TP + FN  
               
 - **F1-Score**

The F1 score is the harmonic mean of precision and recall.

                                          1                        2 * precision * recall 
             F1-score = 2 * -----------------------------  =   -----------------------------
                               1/precision + 1/recall               precision + recall
               
## Analysis of Algorithms

- **Linear Regression**

Linear regression is one of the very basic forms of machine learning where we train a model to predict the behaviour of your data based on some variables. In the case of linear regression as you can see the name suggests linear that means the two variables which are on the x-axis and y-axis should be linearly correlated.

Mathematically the relationship can be represented with the help of following equation −

Y = mX + b

Here, Y is the dependent variable we are trying to predict

X is the dependent variable we are using to make predictions.

m is the slop of the regression line which represents the effect X has on Y

b is a constant, known as the Y-intercept. If X = 0,Y would be equal to b.

<img src = "https://github.com/Soumayan-pal01/Open-contributions/blob/master/Soumayan_Pal_ML/Images/regression.png" width = '500'>

- **Logistic regression**

Logistic regression is a classification algorithm used to assign observations to a discrete set of classes. Unlike linear regression which outputs continuous number values, logistic regression transforms its output using the logistic sigmoid function to return a probability value which can then be mapped to two or more discrete classes. The types of Logistic regression are: Binary Class, Multi Class ,Ordinal (Low, Medium, High)

<img src = "https://github.com/Soumayan-pal01/Open-contributions/blob/master/Soumayan_Pal_ML/Images/logistic_regression.png" width = '500'>

- **Random forest** 

Random forest regression is an ensemble learning technique.In ensemble learning, you take multiple algorithms or same algorithm multiple times and put together a model that’s more powerful than the original.Prediction based on the trees is more accurate because it takes into account many predictions. This is because of the average value used. These algorithms are more stable because any changes in dataset can impact one tree but not the forest of trees.

This is a four step process and our steps are as follows:

- Pick a random K data points from the training set.
- Build the decision tree associated to these K data points.
- Choose the number N tree of trees you want to build and repeat steps 1 and 2.
- For a new data point, make each one of your Ntree trees predict the value of Y for the data point in the question, and assign the new data point the average across all of the - predicted Y values.

Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and takes the average to improve the predictive accuracy of that dataset.The greater number of trees in the forest leads to higher accuracy and prevents the problem of overfitting.

Advantages of Random Forest:
- Random Forest is capable of performing both Classification and Regression tasks.
- It is capable of handling large datasets with high dimensionality.
- It enhances the accuracy of the model and prevents the overfitting issue.

<img src = "https://github.com/Soumayan-pal01/Open-contributions/blob/master/Soumayan_Pal_ML/Images/random_forest.png" width = '500'>

- **Support Vector Classifier**

The support vector classifier aims to create a decision line that would class a new observation as a violet triangle below this line and an orange cross above the line.
SVC aims to maximise the gap between the two classes.The objective of SVC algorithm is to find a hyperplane in an N-dimensional space that distinctly classifies the data points.SVM chooses the extreme points/vectors that help in creating the hyperplane. These extreme cases are called as support vectors, and hence algorithm is termed as Support Vector Machine.

<img src = "https://github.com/Soumayan-pal01/Open-contributions/blob/master/Soumayan_Pal_ML/Images/SVC.png" width = '500'>

- **Naive Bayes Classifier**

Naïve Bayes algorithm is a supervised learning algorithm, which is based on Bayes theorem and used for solving classification problems. It is mainly used in text classification that includes a high-dimensional training dataset. Naïve Bayes Classifier is one of the simple and most effective Classification algorithms which helps in building the fast machine learning models that can make quick predictions. It is a probabilistic classifier, which means it predicts on the basis of the probability of an object.
   It is fine-tuned for big data sets that include thousands or millions of data points and cannot easily be processed by human beings. This algorithm works by analyzing a point in a dataset with a number of different criteria. The criteria involved include attributes and thresholds that are associated with a category.

<img src = "https://github.com/Soumayan-pal01/Open-contributions/blob/master/Soumayan_Pal_ML/Images/NBclassifier.png" width = '500'>

- **K-nearest neighbor**

K-nearest neighbor creates an imaginary boundary to classify the data. When new data points come in, the algorithm will try to predict that to the nearest of the boundary line. It is a non-parametric algorithm, which means it does not make any assumption on underlying data. KNN algorithm at the training phase just stores the dataset and when it gets new data, then it classifies that data into a category that is much similar to the new data.

Advantages of KNN Algorithm:
- It is simple to implement.
- It is robust to the noisy training data
- It can be more effective if the training data is large.

<img src = "https://github.com/Soumayan-pal01/Open-contributions/blob/master/Soumayan_Pal_ML/Images/knn.png" width = '500'>

- **Decision Tree**

Decision Tree is a decision-making tool that uses a flowchart-like tree structure or is a model of decisions and all of their possible results, including outcomes, input costs and utility. Decision-tree algorithm falls under the category of supervised learning algorithms. It works for both continuous as well as categorical output variables. It is a tree-structured classifier, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome.

<img src = "https://github.com/Soumayan-pal01/Open-contributions/blob/master/Soumayan_Pal_ML/Images/dt.png" width = '500'>

Name - Soumayan pal

E-mail - soumayan.pal@gmail.com

Github - https://github.com/Soumayan-pal01

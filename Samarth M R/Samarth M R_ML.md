# Machine Learning Topics

Following are the list of topics I know in **Machine Learning**.

1. **Regression**
    * Linear
    * Multiple Linear
    * Polynomial
    * Logistic
    
2. **Classification**
    * K-Nearest Neighbour
    * Support Vector Machine
    * Naive Bayes
    * Decision Tree
    * Random Forest
    
3. **Clustering**
    * K-Means
    * Hierarchical
    
4. **Dimentionality Reduction**
    * PCA 
    * LDA
    
5. **Deep Learning**
    * Artificial Neural Networks
    * Backpropagation
    * Convolutional Neural Network
    * Transfer Learning
    
6. **Ensemble Learning**

7. **Cross Validation**
    * K-Fold
    
8. **Performance Metrics**
    * For Regression
      * MAE
      * RMSE
    * For Classification
      * Accuracy
      * Precision
      * F1-score

# Introduction to supervised learning

Supervised Learning is the process of making an algorithm to learn to map an input to a particular output. This is achieved using the labelled datasets that you have collected.  Supervised Learning algorithms can help make predictions for new unseen data that we obtain later in the future. 

Supervised learning provided with two sets of data(if dataset is smaller), a training set and a validation set
and test set. but provide three sets of data(if dataset is greater) , a training set , a validation set and test set.

![supervised learning](https://user-images.githubusercontent.com/64517073/95315428-1b497f80-08b0-11eb-9847-db8cb9ff88b7.jpg)

The idea is for the model to “learn” from a set of labeled examples in the training set so that it can
identify unlabeled examples in the test set with the highest possible accuracy.

There are many different approaches that attempt to build the best
possible method of classifying examples of the test set by using the data given in
the training set.

In supervised learning, the training set consists of n ordered pairs (x1, y1),
(x2, y2), ...,(xn, yn), where each x1 is some parameters of data,
and y1 is the label for that data .

For example, an x might be a group of five parameters for a patient in a hospital including height, weight, temperature, blood sugar
level, and blood pressure. 
The corresponding yi might be a classification of the patient as “healthy” or “not healthy”.

Supervised learning can be done in two ways:
## 1. Regression  

Regression analysis helps us to understand how the value of the dependent variable is changing corresponding to an independent variable when other independent variables are held fixed. It predicts continuous/real values such as temperature, age, salary, price, etc.

It is a statistical method used in finance, investing, and other disciplines 
that attempts to determine the strength and character of the relationship between 
a series of other variables and one dependent variable.

![regresision](https://user-images.githubusercontent.com/64517073/95163106-cd0b8200-07c4-11eb-8471-afb1f8f03015.png)

 ### Types of Regression : 

Linear Regression

Logistic Regression

Support Vector Regression

Decision Tree Regression



### Linear regression :

We aim to predict a target variable using some given data variables. What we can do is to pass a line from the data set fitting the data set as shown.
To generalise, you draw a straight line such that it crosses through the maximum number of points. Once we have done that, we can predict the target value using that line as the hypothesis function.
<br/>![linear regression](https://www.researchgate.net/profile/Hieu_Tran33/publication/333457161/figure/fig3/AS:763959762247682@1559153609649/Linear-Regression-model-sample-illustration.ppm)<br/>
The only problem is how to define the values of slop and intercept of the line.
<br/>![linear regression intuition](https://miro.medium.com/max/656/1*4nBp-NeOFGBc-nNzP-VG3w.png)<br/>
We can use calculus to get the minimum values of slope and intercept such that the line passes through maximum number of points. More commonly, gradient descent is used for updating parameters at each step. [Gradient descent](https://machinelearningmastery.com/linear-regression-tutorial-using-gradient-descent-for-machine-learning/#:~:text=Gradient%20Descent%20is%20the%20process,downhill%20towards%20the%20minimum%20value.), [more details.](https://en.wikipedia.org/wiki/Linear_regression#:~:text=In%20statistics%2C%20linear%20regression%20is,is%20called%20simple%20linear%20regression.)
We will not go into detailed mathematics because this note just provides intuition for the algorithms.

## Algorithms :

This flowchart helps in choosing the appropriate machine learning algorithm from numerous algorithms to solve the specific problems.

![ML Algorithms Flowchart](https://github.com/AmanKalwar/AmanKalwar/blob/master/Aman%20ML%20Flowchart.png)

## Conclusion :
 
![machine learning](https://user-images.githubusercontent.com/64517073/95162408-44d8ad00-07c3-11eb-99a1-61ff51ddeb46.jpg)
 
Machine Learning is a technique of training machines to perform the activities a human brain can do, albeit bit faster and better than an average human-being. Today we have seen that the machines can beat human champions in games such as Chess, AlphaGO, which are considered very complex.
 
Machine Learning can be a Supervised or Unsupervised. If you have lesser amount of data and clearly labelled data for training, opt for Supervised Learning.

Machine Learning is a technique of training machines to perform the activities a human brain can do, albeit bit faster and better than an average human-being. Today we have seen that the machines can beat human champions in games such as Chess, AlphaGO, which are considered very complex.


This is my understanding so far in Supervised Machine Learning (Linear Regression and Algorithms).

### Thank you

Name: Samarth M R

You can contact me on this email - mrsamarth18@gmail.com.

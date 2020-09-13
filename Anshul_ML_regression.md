# Concrete Compressive Strength Prediction using Machine Learning 😎😎
-Anshul Sharma, IIT Kharagpur
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20%40thevoxium)](https://twitter.com/thevoxium) [![GitHub followers](https://img.shields.io/github/followers/tterb.svg?label=Github)](https://github.com/thevoxium)

[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


Cement is one of the components of concrete. Mixing of required substances in required amount produces concrete. The strength of concrete may be influenced by:
1. Ratio of cement to water
2. Size of aggregate
3. Texture, stiffness of particles

In this project, we aim to determine the compressive strength of concrete given some data about cement.The data set
for this project is acquired from the [UCI ML repository](https://archive.ics.uci.edu/ml/datasets/concrete+compressive+strength)

The data set has the following attributes:
1.  Cement 
2.  Blast Furnace Slag 
3.  Fly Ash 
4.  Water 
5.  Superplasticizer 
6.  Coarse Aggregate 
7.  Fine Aggregate 
9.  Age 
10. Concrete compressive strength 

### Prerequisites
You should have the following softwares/libraries installed:
```
Python3
Scikit-learn
Jupyter notebook
Scipy
Numpy
Pandas
Matplotlib
Seaborn
```

## Important Machine Learning Algorithms

Good understanding of the following algorithms is required.

### Linear regression

We aim to predict a target variable using some given data variables. What we can do is to pass a line from the data set fitting the data set as shown.
To generalise, you draw a straight line such that it crosses through the maximum number of points. Once we have done that, we can predict the target value using that line as the hypothesis function.
<br/>![linear regression](https://www.researchgate.net/profile/Hieu_Tran33/publication/333457161/figure/fig3/AS:763959762247682@1559153609649/Linear-Regression-model-sample-illustration.ppm)<br/>
The only problem is how to define the values of slop and intercept of the line.
<br/>![linear regression intuition](https://miro.medium.com/max/656/1*4nBp-NeOFGBc-nNzP-VG3w.png)<br/>
We can use calculus to get the minimum values of slope and intercept such that the line passes through maximum number of points. More commonly, gradient descent is used for updating parameters at each step. [Gradient descent](https://machinelearningmastery.com/linear-regression-tutorial-using-gradient-descent-for-machine-learning/#:~:text=Gradient%20Descent%20is%20the%20process,downhill%20towards%20the%20minimum%20value.), [more details.](https://en.wikipedia.org/wiki/Linear_regression#:~:text=In%20statistics%2C%20linear%20regression%20is,is%20called%20simple%20linear%20regression.)
We will not go into detailed mathematics because this note just provides intuition for the algorithms.

### Polynomial Regression
Sometimes the line may not fit the data because of the data might have a high dimensional polynomial nature. So a line won't be enough. For this we need to increase the degee of attibutes (which can be done using the scikit-learn library).
Check the below figure for linear regression.
<br/>![linear regression](https://miro.medium.com/max/875/1*US9Nk7SxtBlwvAswpXehng.png)<br/>
As you can see in the figure, the given line can fit the data almost perfectly. Simple linear regression is fine in this case.
Now look at this figure.
<br/>![polynomial regression](https://miro.medium.com/max/875/1*MhTfu8jmERKpstkYCc7n3w.png)<br/>
The line for predicted speeds is not able to fit the ground truth perfectly. The data is too complex for simple linear regression to make predictions. We need to have high degree attributes.
Now look at this figure.
<br/>![polynomial regression](https://miro.medium.com/max/875/1*866wXGUKYkkwgguk3o-8Gg.png)<br/>
This hypothesis function fits the data almost perfectly. So to decide between linear and polynomial regression, you have to visualize the data. Use python's seaborn for better aid in visualization.
For detailed mathematics behind polynomial regression, [Click Here](https://en.wikipedia.org/wiki/Polynomial_regression)

### Random Forest Regression
First let's look at Ensemble Learning. Ensemble learning is a technique that combines the predictions from multiple weak machine learning algorithms together to make more accurate predictions. Since the model is comprised of many models, it is called an Ensemble model. Look at the image below for better understanding.
<br/>![ensemble](https://miro.medium.com/max/434/0*IsQCuCZCTX_zc7Xy.png)<br/>
Random forest is an supervised machine learning that can be used for classification and regression. It has trees which have no interaction in between them, they are completely independent from each other. Each tree acts as an independent model, which can be combined with others to form an ensemble. Each tree uses random data from the original data set when generating its splits, adding randomness to prevent overfitting. For many data sets, it produces a highly accurate classifier. It gives estimates of what variables that are important in the classification therefore, can be used for feature selection. It has an effective method for estimating missing data while maintaining accuracy.
<br/>![random forests](https://miro.medium.com/max/656/0*f_qQPFpdofWGLQqc.png)<br/>

### Support Vector Regression
SVM is one of the most powerful machine learning algorithm available today. A linear regression is only able to generate a line to predict the data points, while a support vector regression can also generate a hyperplane. In SVM, Margin is the perpendicular distance between the hyperplane and the closest points. SVM tries to maximise this margin, no penalty region in built by SVM in the muti dimensional data.
<br/>Look at the image.<br/>
![SVM](https://miro.medium.com/max/875/0*uwRVvFVLmKi3T9pS.png)<br/>
Making a hyperplane to fit this data is very difficult, specially it it's high dimensional. SVM does this task perfectly. SVR tries to have as many support vectors as possible within the margin, thus it keeps the error within the threshold.
A major difference between Linear regression and SVR lies on the fact that Linear regression tends to minimize the error and SVR tends to keep it within a threshold.
For further information visit [Sklearn SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html)

## When to use what? 😕😕
Linear regression is a linear model, which means it works really great with data with linear properties. But, linear model cannot capture the non-linear features. So in this case, you can use the decision trees or random forests which do a better job at capturing the non-linearity in the data by dividing the space into smaller sub-spaces.
Random forests behave like ensemble models, making decision trees even more robust to deal with noisy data, whereas standard regression methods can get easily confused by noise and will result in high error. 
Normally, Support Vectors models perform better on sparse data than RF. Moreover, Decision trees work faster, non-linear data are handled well . Also they train faster but they have tendency to overfit.

### Now pat your back!! You have successfully completed this module. 🏆 🏆 
## Author

* **Anshul Sharma** - [Github](https://github.com/thevoxium), [Linkedin](https://www.linkedin.com/in/anshul-sharma-38aa481b4/), [Instagram](https://www.instagram.com/anshul_1923/),  [Facebook](https://www.facebook.com/profile.php?id=100039009814742), 
## Acknowledgments
- DevIncept Mentor
- Google for images
- Medium blog posts
- Wikipedia
- UCI Machine learning datset repository

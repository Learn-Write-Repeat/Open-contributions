After the data is processed and cleaned, we must find the suitable ML algorithms to apply on it.
This topic covers 8 subtopics including an assignment:
1. Supervised Learning
2. Unsupervised Learning
3. Regression Problem
4. Classification Problem
5. Performance Measure
6. Linear Regression Notebook
7. Assignment

## Summary of the Module (100 Words)
In Machine Leaning, basically, we make use of historic data to make future decisions of make our present decisions better.
Expert systems stimulate the human experts or organizations who are expert in a particular field. They interpret the historic data and to solve a particular problem. This field is a combination of Computer Science, Engineering and Statistics and a subset of Artificial Intelligence. 
Machine Learning algorithms work on datasets which are a collection of information. There are three types of datasets:

1.	Training 
2.	Validation
3.	Testing

The training data set is what you initially feed into the Machine Learning Model. The validation dataset is the data held back from the training data set which is used to check the estimated accuracy of prediction. The validation dataset is not required although the model can be better tuned if we use this approach.
The testing dataset is the final dataset you test your model on which tells you how accurate your model is.
Target variables are those variables which are going to be predicted by running the machine learning model on other variables.
There are three types of Machine Learning:

1.	Supervised Learning
2.	Unsupervised Learning
3.	Reinforcement Learning

In supervised learning, labels are provided to the model and there is an understanding about what your model wants to achieve. Labelled data means, you know what is going to be the output to a certain input. For example, for a square function, that takes a value and gives the square of it, you know the input variables and you know that the output is itself multiplied by itself. Such kind of data is called labelled data, and this is used in supervised machine learning.

<img src=https://user-images.githubusercontent.com/50140975/122704296-04499280-d271-11eb-95e0-61b55ba25e24.png>

This type of model can now be further used to predict the output of data which is unlabelled.
Supervised learning is useful in various domains like face recognition, cyber security, weather, and sales forecasting, etc.
There are 2 types of supervised learning:

1.	Regression 
2.	Classification

There are two types of regressions, linear and logistic regression. These are used to generate best-fit line to fit the shape of several points.

1.	Linear regression attempts to find the dependent variable based on independent variable. The general equation is in the form of, Y = B1X + B0

![image](https://user-images.githubusercontent.com/50140975/122704395-4541a700-d271-11eb-835e-5a6833ae607c.png)

2.	B0 is the intercept where the graph cuts Y axis.
3.	The B1X gives the slope of the graph.

It is one of the most well known and well understood algorithms in statistics and machine learning.
Logistic regression, on the other hand, is used to model probability.
For example, consider the following table,
![image](https://user-images.githubusercontent.com/50140975/122704438-5d192b00-d271-11eb-9274-f82a694f5484.png)

![image](https://user-images.githubusercontent.com/50140975/122704443-60141b80-d271-11eb-962d-28859893301a.png)
 
The graph above shows the probability of passing the exam vs the number of hours studied.
This indicates that, as the student studies for more hours, the probability of passing the exam increases. 
Logistic regression can be binomial, ordinal, or multinomial. Binomial or binary logistic regression deals with the situations where there are two possible outputs.
Multinomial logistic regression deals with the models where more than two outcomes are there. For example, when there are 3 types of possible diseases.
In unsupervised learning, labels are not provided, and the problem statement is also not clear. The model would then have to understand from the patterns that exist in the data.
In reinforcement learning, there is no dataset, and one must interact with the model during the training process. If the model gives correct output, you give it a reward. In this manner the model learns to give correct output.

# Linear Regression

![image](https://user-images.githubusercontent.com/50140975/122704481-73bf8200-d271-11eb-9810-6ec099450873.png)

The graph above is also an example of linear regression.
Types of linear regression,

1.	Simple
2.	Multiple


## Simple Linear Regression
*	Finding relationship between two continuous variables

*	One is predictor, or independent variable

*	Other is response, or dependent variable

The value of the dependent variable, as the name suggests, depends upon the value of the independent variable.
The aim is to obtain a best fit line. A best fit line is that line, for which the total prediction error summed up including every data point is the lowest. The error is found by calculating the perpendicular distance between the line and the point for which the error is being calculated.


Formula:

![image](https://user-images.githubusercontent.com/50140975/122704598-a9fd0180-d271-11eb-928d-5df76ea9f198.png)

![image](https://user-images.githubusercontent.com/50140975/122704609-aec1b580-d271-11eb-9e61-8afed88d5cdb.png)

The **2 indicates exponent raised to the power of 2.




<hr>

### by <font>Samnit Mehandiratta

<a href="https://www.linkedin.com/in/lankabhedi"><img width="100px" src="https://user-images.githubusercontent.com/50140975/122695391-d9a20e80-d25d-11eb-8957-b8458b8a95e9.png"/></a>

<hr>
  
Thanks to <a href="https://www.freepnglogos.com/images/linkedin-logo-png-1840.html">FREEPNGLOGOS</a> for LinkedIn logo.

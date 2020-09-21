#       LOGISTIC REGRESSION



## What is Logistic Regression?


Logistic Regression is a Predictive Analysis. It is used to define relationship between an independent variable and a binary dependent variable. It is mostly used method for binary classification problems. It is used to estimate the probability of occurrence of an event, given some data which has only two possibilities, either the event happens(1) or the event doesn't happen(0). Such a variable is known as "dichotomous" or "binary" variable. The main drawback of logistic regression is its assumption of linearity between dependent and independent variable. Generally, we don't get such data in which we can divide the dependent variable into just two categories. Usually, the data we get are a lot messier. Logistic regression uses some logistic functions to derive the value.





## Why do we use Logistic Regression?


We use Logistic Regression only when the output we want is to be divided into two categories only. As compared to linear regression, logistic regression is quick and easy to implement and very efficient to train. Also, logistic regression is less likely to overfitting, given the data set is not high dimensional. We should use logistic regression only when the dependent variable takes only two values, but there is no any restriction for independent values. 


#### To understand the concept of Logistic Regression, it is important to understand the concept of  Odd Ratio (OR), Logit function, Sigmoid function or Logistic function. 



### Odds Ratio (OR)
Odds Ration (OR) is the odds in favor of a particular event. It is a measure of association between exposure and outcome.
Lets X is the probability of subjects affected and Yis a probability of subjects not affected, then, **ODDS = X/Y**


### Logit Function
Logit function is the logarithm of the Odd Ratio (log-odds). It takes input values in the range 0 to 1 and then transforms them to value over the entire real number range.

Let’s take P as probability, then P/(1-P) is the corresponding odds; the logit of the probability is the logarithm of the odd given below:
  **logit(P) = log(P/(1-P))**
 
 
### Logistic function or Sigmoid function
The inverse of the logit function is called the logistic function or Sigmoid function. It is named as Sigmoid function due to its characteristic shape.

The equation of the Sigmoid function (from logit function): **Φ = 1/(1+ e^-z)**  



# Conclusion
The base of Logistic Regression is dependent on different probabilistic equations like Odds Ration, Sigmoid function, etc. This classification model is very easy to implement and performs very well in linearly separable classes.



##### This markdown file is created by Riddhima Singh. 

<b>LINEAR REGRESSION</b>

Linear regression is a basic predictive analytics technique that uses historical data to predict an output variable. It is popular for predictive modelling because it is easily understood and can be explained using plain English.
Python has an array of packages for linear regression modelling.

Why should we use this?
 widely used
 runs fast
 easy to use (not a lot of tuning required)
 highly interpretable
 basis for many other methods


There are two kinds of variables in a linear regression model:
The input or predictor variable is the variable(s) that help predict the value of the output variable. It is commonly referred to as X.
The output variable is the variable that we want to predict. It is commonly referred to as Y.
To estimate Y using linear regression, we assume the equation:
Yₑ = α + β X
where Yₑ is the estimated or predicted value of Y based on our linear equation.
Our goal is to find statistically significant values of the parameters α and β that minimise the difference between Y and Yₑ.If this satifies then line of best fit can be determined.
 
<b>MULTIPLE LINEAR REGRESSION</b>
Simple linear regression can easily be extended to include multiple features. This is called multiple linear regression:

y = β0 + β1x1 + ... + βnxn

Each x represents a different feature, and each feature has its own coefficient. 


Model Evaluation Metrics for Regression
For classification problems, we have only used classification accuracy as our evaluation metric. What metrics can we used for regression problems?

Mean Absolute Error (MAE) is the mean of the absolute value of the errors


Mean Squared Error (MSE) is the mean of the squared errors


Root Mean Squared Error (RMSE) is the square root of the mean of the squared errors


Applications:
1.Stock price Prediction
2.Analysis of tobacco smokers in country

Disadvantage:
Linear regression is a linear model, which means it works really great with data with linear properties. But, linear model cannot capture the non-linear features.




Written by Yashaswini D Pai 

Contact me @yashaswinidpai@gmail.com

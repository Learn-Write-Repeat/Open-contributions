# Linear Regression

Let's learn about linear regression and implement it. Linear Regression is supervised algorithm which is used to predict continuous variable like house price. Let's start from understanding regression.

### Let's understand what regression is

Regression analysis is a form of predictive modelling technique which investigates the relationship between a dependent and independent variable.

Uses of regression are as follows:

* Forecasting an effect :snowflake:
* Time series modeling

### Types of Regression

|Linear Regression|Logistic Regression|
|-----------------|-------------------|
|The data model uses straight line.|It uses sigmoid function.|
|Used with continuous variable.|Used with categorical variable.|
|Predicts value.|Classifies the object|

### Linear Regression Algorithm

Linear Regression uses is an equation that combines a specific set of input values (x) the solution to which is the predicted output for that set of input values (y). As such, both the input values (x) and the output value are numeric. Where (x) is independent variable and (y) is indepedent variable.

The linear equation assigns one scale factor to each input value or column, called a coefficient and represented by the capital Greek letter Beta (B). One additional coefficient is also added,called the intercept or the bias coefficient.

In a simple regression problem (a single x and a single y), the form of the model would be:
-------
## |y = B0 + B1* x|
-------

After applying Linear Regression on the model: 
<table align="center">
    <tr>
        <td><img src="https://github.com/anamikarpp/Open-contributions/blob/master/AnamikaPatel_ML/images/linear regression.png" width=600 height=300></td>
    </tr>
    
</table>

Once we know the value of coefficient and intercept we can easily predict dependent variable (y) give indepent variable (x).

## Linear Regresion using Scikit learn Library

We can easily implement Linear Regression in python using scikit learn library.The steps to be followed are as follows:

* Step 1 : Import Linear Regression from sklearn.
* Step 2 : Load model.
* Step 3 : Fit the model on given independent variable(x) and dependent variable (y).
* Step 4 : Plot the model
* Step 5 : Make prediction. 
And yeah :wink: it's done.

## Python code:

```python
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X,y)
model.coef_  #printing coeficent
model.intercept_ #printing intercept

#plotting the linear model we got
plt.figure(figsize=(12,8))
sns.regplot(X,y)
plt.xlabel('Independent variable')
plt.ylabel('Dependent variable')
```
Implementation of linear regression on boston dataset is done in python notebook, have a look. Thankyou 😃 

# Boston House Price Prediction

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>

The problem that we are going to solve here is that given a set of features that describe a house in Boston, our machine learning model must predict the house price. To train our machine learning model with boston housing data, we will be using scikit-learn’s boston dataset.

The data set for Boston housing prediction is already present in the sklearn module.

## Short Overview

Here we are going to implementing a model for predicting the house price prediction using some of the regression techniques based of some of features in the dataset which is called Boston House Price Prediction. There are some of the processing techniques for creating a model.

## Problem Statement

Housing prices are an important reflection of the economy, and housing price ranges are of great interest for both buyers and sellers. Ask a home buyer to describe their dream house, and they probably won’t begin with the height of the basement ceiling or the proximity to an east-west railroad. But this playground competition’s data-set proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.

## Dataset

In this project, house prices will be predicted given explanatory variables that cover many aspects of residential houses. The goal of this project is to create a regression model that is able to accurately estimate the price of the house given the features.

1. _**CRIM**_ per capital crime rate by town

2. _**ZN proportion**_ of residential land zoned for lots over 25,000 sq.ft.

3. _**INDUS**_ proportion of non-retail business acres per town

4. _**CHAS**_ Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)

5. _**NOX**_ nitric oxides concentration (parts per 10 million)

6. _**RM**_ average number of rooms per dwelling

7. _**AGE**_ proportion of owner-occupied units built prior to 1940

8. _**DIS**_ weighted distances to five Boston employment centers

9. _**RAD**_ index of accessibility to radial highways

10. _**TAX**_ full-value property-tax rate per 10,000 USD

11. _**PTRATIO**_ pupil-teacher ratio by town

12. _**Black 1000(Bk — 0.63)²**_ where Bk is the proportion of blacks by town

13. _**LSTAT**_ % lower status of the population


## Algorithm 

Here Linear Regression is used to create the model for **Boston House Price prediction** 

Steps To be followed for creating the linear Regression

- Loading the dataset from the sklearn module
  ```python
  from sklearn.datasets import load_boston
  ```
- Importing the required modules. Modules needed for data analysis are
  ```python
  import numpy as np
  import pandas as pd
  ```
- Download the dataset from [Kaggle](https://www.kaggle.com/altavish/boston-housing-dataset) 

- _Data Processing_ : In this Boston Dataset we need not to clean the data. The dataset already cleaned when we download from the Kaggle.

- _Exploratory Data Analysis_ : In statistics, exploratory data analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often with visual methods. A statistical model can be used or not, but primarily EDA is for seeing what the data can tell us beyond the formal modeling or hypothesis testing task.

- _Feature Observation_ : Finding out the correlation between the features
  ```python
  corr = df.corr()
  ```
  
- Checking the null values using **heatmap**. There is any null values are occupyed here.

- Crreate X and Y value from the above dataset
  ```pthon
  X = data.drop(['PRICE'], axis = 1)
  y = data['PRICE']
  ```

- Create xtrain, xtest, ytrain, ytest for the boston data
  ```python
  from sklearn.model_selection import train_test_split
  ```

- Create the model using LinearRegression
  ```python
  from sklearn.linear_model import LinearRegression
  ```
  
- Then find the intercept and correlation values 

- By sklearn.metrics we can find the mean squared error and r2 error
  ```python
  from sklearn.metrics import mean_squared_error and r2_error
  ```
  
- We can the predict the value and also check the accuracy. 

## Author

Rammya Dharshini K

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

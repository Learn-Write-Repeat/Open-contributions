# Data Preprocessing in Machine Learning

## What is Data Preprocessing?

 Data Preprocessing is a technique that is used to convert the raw data into a clean data set. It is the most important step to oraganize the data into meaningful manner. Its   main aim is to produce clean and efficient code so that it can be easily be understood by machine.
 It also helps to reduce the time while analyzing the data and also improves to understand the code and increase readability.

## Why Data Preprocessing?

 Since now-a-days thw world highly depends upon data and the data needs to be organised in appropriate manner.Data preprocessing helps in the real-world data to store efficiently and thereby making it ready-to-go for Machine Learning Models.
 It also helps to select the most efficient model in Machine Learning.

# Various Steps in Data Preprocessing in Machine Learning.

## 1. Importing the libraries.

  #### The predefined Python libraries can perform specific data preprocessing jobs.
  #### The three core Python libraries used for this data preprocessing in Machine Learning are:

## a. Numpy
   
    import numpy as np
   
  It is the fundamental library which is used for the scientific calculations and is widely used. 
  It is mainly used to deal with large multidimensional arrays and matrices in the code.
   
## b. Matplotlib
   
    import matplotlib.pyplot as plt
    
   It is a library which is used to plot any type of charts and graphs across any platform like: 
   Jupyter Notebook or Web Application Servers.
   It helps to easily visualize the data.
    
## c. Pandas
    
    import pandas as pd
     
   Pandas is an excellent open-source Python library for data manipulation and analysis. 
   It is extensively used for importing the Dataset and also create matrix of features and dependent variables.
    
## 2. Importing the Dataset

  Here we need to import the datasets which we have collected for our machine learning project.
  
  read_csv() function:
  
  Now to import the dataset, we will use read_csv() function of pandas library, which is used to read a csv file and performs various operations on it. 
  read_csv() function can be used as follows:
  
    dataset= pd.read_csv("Name of the data.csv")
    
### Extracting Dependent and Independent Variable
  
   Extracting Independent Variable: Here in order to extract the variable iloc[] method of pandas library is used and extract rows and columns of the data set.
    
    X= dataset.iloc[:,:-1].values
    
   Extracting Dependent Variable: Here in order to extract the variable again iloc[] method of pandas library is used.
   
    Y= dataset.iloc[:,:-1].values
    
 ## 3. Handling missing Data
 
   It is the most important step in data preprocessing, since if any of the data is missing in data set it will create a huge problem.
   
   There are mainly two ways to handle missing data, which are:

   **By deleting the particular row:** The first way is used to commonly deal with null values. In this way, we just delete the specific row or column which consists of null values. But this way is not so efficient and removing data may lead to loss of information which will not give the accurate output.

   **By calculating the mean:** In this way, we will calculate the mean of that column or row which contains any missing value and will put it on the place of missing value. This strategy is useful for the features which have numeric data such as age, salary, year, etc. Here, we will use this approach.

   To handle missing values, we use Scikit-learn library in our code, which contains various libraries for building machine learning models. Lets see how to use it. 
   
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
    imputer.fit(X[:,1:3])
    X[:,1:3]=imputer.transform(X[:,1:3])  
    print(X)
    
  ## 4. Encoding Categorical Data
  
   Now since the machine learning model deals only with the numerical data, but it can happen that our data set contains data other then numbers.
   So it would create a problem since machine cannot understand words. Hence in order to deal with this situation we need to convert this data into numbers.
   

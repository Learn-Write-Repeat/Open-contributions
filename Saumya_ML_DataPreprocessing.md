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

<img src="https://miro.medium.com/max/400/1*eWtGdqsEXCnX_ZiVw2Ba0g.png">

  Here we need to import the datasets which we have collected for our machine learning project.
  
  **Steps for Importing Data set in Jupyter notebook**
  
  1. Click on upload to upload the data from our pc.
  2. Make sure your file has .csv extention (**i.e. Data.csv**)
  3. The file should be uploaded in the same folder as that of source code.
  4. Now save the file in the same directory where all the other files have been stored.
  
  <img src="https://i.stack.imgur.com/wTjKQ.png" height="500" width="700">
  
  read_csv() function:
  
  Now to import the dataset, we will use read_csv() function of pandas library, which is used to read a csv file and performs various operations on it. 
  read_csv() function can be used as follows:
  
    dataset= pd.read_csv("Name of the data.csv")
    
### Extracting Dependent and Independent Variable
   
   **Independent Variable:** Independent variables are the input for a process that is being analyzes basically referred as Features and here we are denoting it by **x**.
   
   **Dependent Variables:** Dependent variables are the output of the process, like for example whether we have purchased the product or not and here we are denoting it by **y**.
   
   **Extracting Independent Variable:** Here in order to extract the variable iloc[] method of pandas library is used and extract rows and columns of the data set.
    
    x= dataset.iloc[:,:-1].values
    
   **Extracting Dependent Variable:** Here in order to extract the variable again iloc[] method of pandas library is used.
   
    y= dataset.iloc[:,:-1].values
    
 ## 3. Handling missing Data
 
   It is the most important step in data preprocessing, since if any of the data is missing in data set it will create a huge problem.
   
   There are mainly two ways to handle missing data, which are:

   **By deleting the particular row:** The first way is used to commonly deal with null values. In this way, we just delete the specific row or column which consists of null values. But this way is not so efficient and removing data may lead to loss of information which will not give the accurate output.

   **By calculating the mean:** In this way, we will calculate the mean of that column or row which contains any missing value and will put it on the place of missing value. This strategy is useful for the features which have numeric data such as age, salary, year, etc. Here, we will use this approach.
   
   <img src="https://mk0analyticsindf35n9.kinstacdn.com/wp-content/uploads/2018/02/missing-values.png">

   To handle missing values, we use Scikit-learn library in our code, which contains various libraries for building machine learning models. Lets see how to use it. 
   
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
    imputer.fit(x[:,1:3])
    x[:,1:3]=imputer.transform(x[:,1:3])  
    print(x)
    
  ### Now the Missing data can also be handled using one of the pandas library method i.e. **fillna method**. 
   
   **The fillna() function is used to fill NA/NaN values using the specified method.**
   
   **For example-**
   
   *Suppose we have a data set-*
   
|      |Date     |Temperature|Windspeed|Event    | 
|------|---------|---------- |---------|---------|
|  0   |07-09-20 |  32.0     | 6.0     |   Rain  |
|  1   |08-09-20 |   NaN     |  9.0    |   Sunny |
|  2   |09-09-20 |   28.0    |  NaN    |   Snow  |
|  3   |10-09-20 |  NaN      |  7.0    |    NaN  |
|  4   |11-09-20 |   32.0    |  Nan    |    Rain |

Now by using different parameters-

  1. **df.fillna(0)** - To fill the NaN values by a specified value.
  
          newData = df.fillna(0)
          newData
  
 |      |Date     |Temperature|Windspeed|Event    | 
 |------|---------|---------- |---------|---------|
 |  0   |07-09-20 |  32.0     | 6.0     |   Rain  |
 |  1   |08-09-20 |   0.0     |  9.0    |   Sunny |
 |  2   |09-09-20 |   28.0    |  0.0    |   Snow  |
 |  3   |10-09-20 |  0.0      |  7.0    |    0.0  |
 |  4   |11-09-20 |   32.0    |  0.0    |    Rain |

 2. **df.fillna({dictionary})** - Here we can pass any dictionary and the columns will change accordingly.
 
        newData = df.fillna({
           'Temperature' : 0,
           'Windspeed' : 0,
           'Event' : 'No Event'
        })
        newData
        
|      |Date     |Temperature|Windspeed|Event    | 
|------|---------|---------- |---------|---------|
|  0   |07-09-20 |  32.0     | 6.0     |   Rain  |
|  1   |08-09-20 |   0.0     |  9.0    |   Sunny |
|  2   |09-09-20 |   28.0    |  0.0    |   Snow  |
|  3   |10-09-20 |  0.0      |  7.0    | No Event|
|  4   |11-09-20 |   32.0    |  0.0    |    Rain |

3. **df.fillna(method="")** - This method fills the *previous row's* value.

       newData = df.fillna(method= "ffill")
       newData
       
|      |Date     |Temperature|Windspeed|Event    | 
|------|---------|---------- |---------|---------|
|  0   |07-09-20 |  32.0     | 6.0     |   Rain  |
|  1   |08-09-20 |   32.0    |  9.0    |   Sunny |
|  2   |09-09-20 |   28.0    |  9.0    |   Snow  |
|  3   |10-09-20 |  28.0     |  7.0    | Snow    |
|  4   |11-09-20 |   32.0    |  7.0    |    Rain |


4. **df.fillna(method="")** - This method fills the *next row's* value.

       newData = df.fillna(method= "bfill")
       newData
       
|      |Date     |Temperature|Windspeed|Event    | 
|------|---------|---------- |---------|---------|
|  0   |07-09-20 |  32.0     | 6.0     |   Rain  |
|  1   |08-09-20 |   28.0    |  9.0    |   Sunny |
|  2   |09-09-20 |   28.0    |  7.0    |   Snow  |
|  3   |10-09-20 |  32.0     |  7.0    | Rain    |
|  4   |11-09-20 |   32.0    |  0.0    |    Rain |


Now we also have **axis** parameter - It copies values horizontally.

**For example-**

        newData = df.fillna(method= "bfill", axis= "columns")
        newData
        
|      |Date     |Temperature|Windspeed|Event    | 
|------|---------|---------- |---------|---------|
|  0   |07-09-20 |  32.0     | 6.0     |   Rain  |
|  1   |08-09-20 |   9.0     |  9.0    |   Sunny |
|  2   |09-09-20 |   28.0    |  28.0   |   Snow  |
|  3   |10-09-20 |  7.0      |  7.0    |    NaN  |
|  4   |11-09-20 |   32.0    |  32.0   |    Rain |

The next parameter is **limit**

Lets see the examples-

As we have seen above **method="ffill"** fill the next row according to previous data.
But by using **limit** method we can fill the row according to our choice.

       newData = df.fillna(method= "ffill",limit="1")
       newData

|      |Date     |Temperature|Windspeed|Event    | 
|------|---------|---------- |---------|---------|
|  0   |07-09-20 |  32.0     | 6.0     |   Rain  |
|  1   |08-09-20 |   32.0    |  9.0    |   Sunny |
|  2   |09-09-20 |   28.0    |  9.0    |   Snow  |
|  3   |10-09-20 |  28.0     |  7.0    | Snow    |
|  4   |11-09-20 |   32.0    |  7.0    |    Rain |


 
  ## 4. Encoding Categorical Data
  
   Now since the machine learning model deals only with the numerical data, but it can happen that our data set contains data other then numbers.
   So it would create a problem since machine cannot understand words. Hence in order to deal with this situation we need to convert this data into numbers.
   
   Here we importt **LabelEncoder** class of **sklearn library**.Now if their the three variables in our data set so the variables will be encoded as 0,1,2.By these values, 
   the machine learning model may assume that there is some correlation between these variables which will produce the wrong output. So to remove this issue, **dummy encoding** is used.
   Dummy variables are those variables which have values 0 or 1. The 1 value gives the presence of that variable in a particular column, and rest variables become 0. With dummy
   encoding, the number of columns is equal to the number of categories.
   
   
   **For Example-**
   
   Let’s consider the case of gender having two values male (0 or 1) and female (1 or 0). Including both the dummy variable can cause redundancy because if a person is not male in such case that person is a female, hence, we don’t need to use both the variables in regression models. This will protect us from dummy variable trap.
   
   For Dummy Encoding, **OneHotEncoder** class of preprocessing library is used.
   
   <img src="https://hackernoon.com/photos/4HK5qyMbWfetPhAavzyTZrEb90N2-3o23tie">
   
   **Encoding the Independent Variable**
   
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder
    ct=ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough")
    x=np.array(ct.fit_transform(x))
    print(x)
    
  **Encoding the Dependent Variable**
    
    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    y=le.fit_transform(y)
    print(y)
    
    
  ## 5. Splitting the Dataset into the Training set and Test set
  
  <img src="https://miro.medium.com/max/948/1*4G__SV580CxFj78o9yUXuQ.png" width="800" height="500">
  
  This is one of the crucial step in data preprocessing where we divide dataset into training set and test set.
  In **training set** we train the machine learning model on exisiting observations. In **test set** we evaluate the performance of our model on new observations, and these new observations are completely like the future data which we can get and on the basis of which we  will deploy the machine learning model.
  
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
    print(x_train)
    print(x_test)
    print(y_train)
    print(y_test)
    
  ## 6. Feature Scaling
  
  Feature scaling is the final step of data preprocessing in machine learning. It simply means to scale all the variables i.e. the features and make sure they all take up values in the same scale. This is done to prevent so that one feature don't dominate on other.
  A machine learning model is based on Euclidean distance, and if we do not scale the variable, then it will cause some issue in our machine learning model.
  
  **Euclidean distance is given by:**
  
  <img src="https://static.javatpoint.com/tutorial/machine-learning/images/data-preprocessing-machine-learning-8.png">
  
  ***There are two ways to perform feature scaling in machine learning:***
  
  <img src="https://static.javatpoint.com/tutorial/machine-learning/images/data-preprocessing-machine-learning-9.png">
  
  <img src="https://static.javatpoint.com/tutorial/machine-learning/images/data-preprocessing-machine-learning-10.png">
  
  For feature scaling, **StandardScaler** class of sklearn.preprocessing library is imported as:
  
    from sklearn.preprocessing import StandardScaler
    sc=StandardScaler()
    x_train[:,3:]=sc.fit_transform(x_train[:,3:])
    x_test[:,3:]=sc.transform(x_test[:,3:])
    print(x_train)
    print(x_test)

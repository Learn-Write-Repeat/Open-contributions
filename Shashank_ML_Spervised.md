# Supervised learning

###### So before we start about Supervised learning first of all know about some basics
so first things first
What is data and what are the types of data
* DATA
  1. Data is difined as a raw material but when you process a particular data it becames Information
  2. Data are characteristics or information, usually numerical, that are collected through observation. In a more technical sense, 
     data are a set of values of qualitative or quantitative variables about one or more persons or objects, while a datum is a single value of a single variable    


* Data and its types
1. Categorical data
   * This refers to data that can be classified in seprate group
   * This kind of data represent Characterstics
   * Its also called Qualitative data
   
 * For Ex. 
  1. Gender of a person can be **male** and **Female**
  2. It can also have Numerical value like **1** for **Male** and **0** for **Female**
  
* Categorical Data is further classified into two types
  1. Nominal Data
  2. Ordinal Data


|      NOMINAL DATA            |          ORDINAL DATA          |
|------------------------------|--------------------------------|
|Place holder                  | Place holder                   |
|------------------------------|--------------------------------|
| Gender                       | Ranking of product             |
|------------------------------|--------------------------------|
| MALE         |   0           | BAD           | 0              |
|------------------------------|--------------------------------|
| FEMALE       |   1           | GOOD          | 1              |
|------------------------------|--------------------------------|
| T . G        |   2           | EXCELLENT     | 3              |

  2. Quantitative Data OR Numerical Data
     * Nominal data is defined as data that is used for naming or labelling variables, without any quantitative value.
      It is sometimes called “named” data - a meaning coined from the word nominal. There is usually no intrinsic ordering to nominal data.
      
      * Types of Quantitative data
         1. continious data :
           1.Here we can work with measureable quantities
             * Ex. Profit, GDP, Height of a person
         2. DEscrete Data: 
           1. Here we will be working with countable values.If the value is clearly Swprated from each other then it is discrete data.
             * EX. No. of children
             
             
#### Now we are going to start **SUPERVISED LEARNING**
 * Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs.
   It infers a function from labeled training data consisting of a set of training examples.[2] In supervised learning, each example is a pair
   consisting of an input object (typically a vector) and a desired output value (also called the supervisory signal).
   A supervised learning algorithm analyzes the training data and produces an inferred function, which can be used for mapping new examples.
   An optimal scenario will allow for the algorithm to correctly determine the class labels for unseen instances.
  
 * Supervised learning have **LABEL DATA** means Y variable or Target Variable is Present in the data set 
 * If Y variable is not peresent in the data set then its a UnSupervised learning approach
 
 **How does supervised learning work?**
 
  * Like all machine learning algorithms, supervised learning is based on training. The system is fed with massive amounts of data during its training phase,
    which instruct the system what output should be obtained from each specific input value.
    
  * The trained model is then presented with test data to verify the result of the training and measure the accuracy.
  
  * To avoid overfitting, it is important that the test data is different from the training data to ensure the model is not drawing answers from its previous
    experience, but instead that the model's inference is generalized.

  * The training data must also be balanced and cleaned. Garbage or duplicate data will skew the AI's understanding
    hence data scientists must be careful with the data the model is trained on.

  * The diversity of the data determines how well the AI will perform when presented with new cases
    if there are not enough samples in the training data set, the model will falter and will fail to yield any reliable answers.

  * The algorithm, on the other hand, determines how that data can be put in use. For instance, deep learning algorithms can be trained to extract billions of
    parameters from their data and reach unprecedented levels of accuracy

  **TYPES**
   1. Classification
   2. Regression
  
  **Classification Supervised Learning**
   * Supervised learning is about learning a function appropriate to the problem. This function takes an input (X) and maps it to output (Y)
     If we represent this definition in a simple equation, then it will be Y = f(X)
     The dataset which is used, split into two groups training dataset and testing/validation dataset

   * Classification is a problem that is used to predict which class a data point is part of which is usually a discrete value
  
   * Supervised learning requires that the data used to train the algorithm is already labeled with correct answers. For example,
     a classification algorithm will learn to identify animals after being trained on a dataset of images that are properly labeled with the
     species of the animal and some identifying characteristics.
 
   * Classification is a type of supervised learning. It specifies the class to which data elements belong to and is best used when the output has finite and discrete values
     It predicts a class for an input variable as well
     
  **Regression Supervised Learning** 
   * Regression analysis is a subfield of supervised machine learning. It aims to model the relationship between a certain number of features and a continuous target variable.
   
   * Regression analysis consists of a set of machine learning methods that allow us to predict a continuous outcome variable (y) based on the value of one or
     multiple predictor variables (x)
             
   ### The most important point to be noted here is how do we get to know whether it Regression or Calssification Problem
     * If the targeted variable or Y variable have class like 1,0,1,0 or pass, fail then it is Classificational problem
     * And if it the targeted variable or Y variable is continious in nature then it a Regression problem
    
             
  **Algorithms**
  
   * The most widely used learning algorithms are:
     * Support Vector Machines
     * linear regression
     * Logestic Regression
     * Naive Bayes
     * Decission Tree
     * K-nearest neighbor 
     


             
             
             
             
             
             
             
             
             
           

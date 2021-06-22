**SHASHANK**

# MACHINE LEARNING
Machine learning is a form of AI that enables a system to learn from data rather than through explicit programming.However,machine learning is not a simple process.
Machine learning uses a variety of algorithms that iteratively learn from data to improve, describe data, and predict outcomes. 
As the algorithms ingest training data, it is then possible to produce more precise models based on that data. A machine learning model is the output generated when you train your machine 
learning algorithm with data.After training, when you provide a model with an input, you will be given an output. 
# WHY MACHINE LEARNING?
1. Reduce Time Programming
2. Customize and Scale Products
3. Completely seeemingly "unprogrammable" tasks
4. Changes the way you think about problem
# APPLICATIONS OF MACHINE LEARNING
* Spam filtering
* Credit card fraud detection
* Digit recognition on checks, zip codes
* Detecting faces in images
* MRI image analysis
* Recommendation system
* Search engines
* Handwriting recognition
* Scene classification
# INTERDISCIPLINARY FIELD
 <a href="https://ibb.co/6YJQX4P"><img src="https://i.ibb.co/PxzkD5h/Screenshot-67.png" alt="Screenshot-67" border="0" width="400"></a><br /><a target='_blank' href='https://imgbb.com/'></a>
# TYPES OF ML:-
 <a href="https://ibb.co/HFyPGmz"><img src="https://i.ibb.co/2nrMcXt/mL-TYPES.png" alt="mL-TYPES" border="0"></a>
1. SUPERVISED LEARNING
2. UNSUPERVISED LEARNING
3. REINFORCEMENT LEARNING

# SUPERVISED LEARNING
<a href="https://ibb.co/5sBNmYS"><img src="https://i.ibb.co/fr4hf8y/supervised-learning.png" alt="supervised-learning" border="0"></a>

Supervised learning is the types of machine learning in which machines are trained using well "labelled" training data, and on basis of that data, machines predict the output.
In this type of ML,you have to input variables (x) and an output variable (Y) and you use an algorithm to learn the mapping function from the input to the output.

                                              Y = f(X)
As the training period progresses, the algorithm is able to identify the relationships between the two variables such that we can predict a new outcome.
It is called supervised learning because the process of an algorithm learning from the training dataset can be thought of as a teacher supervising the learning process.

## WHY SUPERVISED LEARNING?
* Pedicts accurate output on the basis of prior experiences.
* Data goes through cross validation process.
* Helps to solve many real world problems such as Fraud Detection,spam filtering,etc.

## EXAMPLE
1. **HOUSE PRICES-->**
First, we need data about the houses: square footage, number of rooms, features, whether a house has a garden or not, and so on. We then need to know the prices of these houses,
i.e. the corresponding labels. By leveraging data coming from thousands of houses, their features and prices, we can now train a supervised machine learning model to predict
a new house’s price based on the examples observed by the model.
2. **SENTIMENT ANALYSIS-->**
This comes under text classification where supervised learning helps to predict the sentiment of a piece of text, like a tweet or a product review.
This is widely used in the e-commerce industry to help companies to determine negative comments made by customers.

## TYPES OF SUPERVISED LEARNING:-
1. **CLASSIFICATION**
We use the training dataset to get better boundary conditions which could be used to determine each target class. Once the boundary conditions are determined, 
the next task is to predict the target class. The whole process is known as classification.Classification algorithms are used when the output variable is categorical,
which means there are two classes such as Yes-No, Male-Female, True-false, etc.

<a href="https://ibb.co/xL37W3s"><img src="https://i.ibb.co/mTSckSB/Screenshot-74.png" alt="Screenshot-74" border="0"></a>

Below are some popular Classification algorithms which come under supervised learning:
* Random Forest
* Decision Trees
* Logistic Regression
* Support vector Machines

## **Logistic Regression**
Logistic Regression is a classification and not a regression algorithm. It estimates discrete values (Binary values like 0/1, yes/no, true/false) based on a given set of independent variable(s).
It basically predicts the probability of occurrence of an event by fitting data to a logit function. Hence, it is also known as logit regression.
The values obtained would always lie within 0 and 1 since it predicts the probability.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/s5vQRqM/Logistic-Regression.png" alt="Logistic-Regression" border="0"></a>

**Example-->**
Let’s say there’s a sum on your math test. It can only have 2 outcomes, right? Either you solve it or you don’t (and let’s not assume points for method here).
Now imagine, that you are being given a wide range of sums in an attempt to understand which chapters have you understood well.
The outcome of this study would be something like this – if you are given a trigonometry based problem, you are 70% likely to solve it.
On the other hand, if it is an arithmetic problem, the probability of you getting an answer is only 30%. This is what Logistic Regression provides you.
If I had to do the math, I would model the log odds of the outcome as a linear combination of the predictor variables.

odds= p/ (1-p) = probability of event occurrence / probability of event occurrence ln(odds) = ln(p/(1-p)) logit(p) = ln(p/(1-p)) = b0+b1X1+b2X2+b3X3....+bkXk)

In the equation given above, p is the probability of the presence of the characteristic of interest. It chooses parameters that maximize the likelihood of observing the sample values rather than that minimize the sum of squared errors (like in ordinary regression).

2. **REGRESSION**
Regression algorithms are used if there is a relationship between the input variable and the output variable.
It is used for the prediction of continuous variables, such as Weather forecasting, Market Trends, etc.
Below are some popular Regression algorithms which come under supervised learning:
* Linear Regression
* Regression Trees
* Non-Linear Regression
* Bayesian Linear Regression
* Polynomial Regression

<a href="https://imgbb.com/"><img src="https://i.ibb.co/jh699Lw/linear-regression-in-machine-learning.png" alt="linear-regression-in-machine-learning" border="0"></a>
<p float="left">
  <a href="https://imgbb.com/"><img src="https://i.ibb.co/DG7CBRJ/Screenshot-78.png" alt="Screenshot-78" width="300" border="0"></a>
  <a href="https://imgbb.com/"><img src="https://i.ibb.co/VpzWhLH/Screenshot-79.png" alt="Screenshot-79" width="300" border="0"></a>
  <a href="https://imgbb.com/"><img src="https://i.ibb.co/6cQCGQG/Screenshot-80.png" alt="Screenshot-80" width="300" border="0"></a>
</p>

# UNSUPERVISED LEARNING
<a href="https://ibb.co/d6JmR2m"><img src="https://i.ibb.co/vmvXSPX/unsupervised-learning.png" alt="unsupervised-learning" border="0"></a>

Unsupervised learning is a machine learning technique in which models are not supervised using training dataset. Instead, models itself find the hidden patterns and insights from the given data.
It can be compared to learning which takes place in the human brain while learning new things.
In this type of ML,you only have input data (X) and no corresponding output variables.

The goal for unsupervised learning is to model the underlying structure or distribution in the data in order to learn more about the data.
These are called unsupervised learning because unlike supervised learning above there is no correct answers and there is no teacher.
Algorithms are left to their own devises to discover and present the interesting structure in the data.

Below is the list of some popular unsupervised learning algorithms:
* K-means clustering
* KNN (k-nearest neighbors)
* Hierarchal clustering
* Anomaly detection
* Neural Networks
* Principle Component Analysis
* Independent Component Analysis
* Apriori algorithm
* Singular value decomposition

## WHY UNSUPERVISED LEARNING?
* It is helpful for finding useful insights from the data.
* It is useful in handling complex tasks.
* It is much similar as a human learns to think by their own experiences, which makes it closer to the real AI.
* In real-world, we do not always have input data with the corresponding output so to solve such cases, we need unsupervised learning.

## EXAMPLE
1. **FINDING CUSTOMER SEGMENTS-->**
Clustering is an unsupervised technique where the goal is to find natural groups or clusters in a feature space and interpret the input data. 
There are many different clustering algorithms. One common approach is to divide the data points in a way that each data point falls into a group that is similar to other data points in the same group based on a predefined similarity or distance metric in the feature space.

Clustering is commonly used for determining customer segments in marketing data.
Being able to determine different segments of customers helps marketing teams approach these customer segments in unique ways.
(Think of features like gender, location, age, education, income bracket, and so on.)

2. **FEATURE SELECTION-->**
Even though feature selection and dimensionality reduction aim towards reducing the number of features in the original set of features, understanding how feature selection works helps us get a better understanding of dimensionality reduction.
Assume that we want to predict how capable an applicant is of repaying a loan from the perspective of a bank.
Here, we need to help the bank set up a machine learning system so that each loan can be given to applicants who can repay the loan.
We need a lot of information about each application to make predictions. 
A few important attributes about applicants are the applicant’s average monthly income, debt, credit history, and so on. 
<br>
<br>

**do visit me** :point_down:

<a href="https://www.linkedin.com/in/shashank-a12a851a0/">
  <img align="left"  width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://github.com/Shashankkrj"> <img align="left"  width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" />
</a>
<a href="https://www.instagram.com/shashank_krj/">
  <img align="left"  width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
<a href="https://m.facebook.com/">
 <img align="left"  width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/facebook.svg" />
</a>

***thanks for reading*** :heart:

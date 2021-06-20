## Introduction to Machine Learning

**Machine Learning**

It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention.

## Types of  Machine Learning 

* **Supervised Learning**  
* **UnSupervised Learning**  
* **Reinforcement Learning**


**Supervised learning**   algorithms are trained using labeled examples, such as an input where the desired output is known. For example, a piece of equipment could have data points labeled either “F” (failed) or “R” (runs). The learning algorithm receives a set of inputs along with the corresponding correct outputs, and the algorithm learns by comparing its actual output with correct outputs to find errors. It then modifies the model accordingly.

**UnSupervised Learning** is used against data that has no historical labels. The system is not told the "right answer." The algorithm must figure out what is being shown. The goal is to explore the data and find some structure within. Unsupervised learning works well on transactional data . 

**Reinforcement learning** is often used for robotics, gaming and navigation. With reinforcement learning, the algorithm discovers through trial and error which actions yield the greatest rewards. This type of learning has three primary components: the agent (the learner or decision maker), the environment (everything the agent interacts with) and actions (what the agent can do). The objective is for the agent to choose actions that maximize the expected reward over a given amount of time. The agent will reach the goal much faster by following a good policy. So the goal in reinforcement learning is to learn the best policy.

## Types of Supervised Learning 

* **Regression**
* **Classification**

### Regression : 

Regression analysis may be kind of predictive modelling technique which investigates the connection between a dependent and independent variable . 

![download.jpg](attachment:download.jpg)  

### Types of Regression 

1. Linear Regression 
* Linear regression is used to predict the continuous dependent variable using a given set of independent variables.
* In linear regression, we find the best fit line, by which we can easily predict the output.
* In Linear regression, it is required that relationship between dependent variable and independent variable must be linear.

2. Logistic Regression 
* Logistic Regression is used to predict the categorical dependent variable using a given set of independent variables.
* In Logistic Regression, we find the S-curve by which we can classify the samples.
* In Logistic regression, it is not required to have the linear relationship between the dependent and independent variable.

### Classification : 

In machine learning, classification refers to a predictive modeling problem where a class label is predicted for a given example of input data.

Examples of classification problems include:

 * Given an example, classify if it is spam or not.
 * Given a handwritten character, classify it as one of the known characters.
 * Given recent user behavior, classify as churn or not.
 

### Classification  Algorithm 

1. Decision tree.
2. Logistic Regression.
3. Artificial Neural Network.
4. Random Forest.
5. Stochastic Gradient Descent.
6. Naive Bayes.
7. Support Vector Machine.
8. K-Nearest Neighbor.


## Type of Unsupervised Learning 

1. Clustering 

It involves automatically discovering natural grouping in data. Unlike supervised learning (like predictive modeling), clustering algorithms only interpret the input data and find natural groups or clusters in feature space.

2. Hierarchical clustering

**Hierarchical clustering**, also known as **hierarchical cluster analysis**, is an algorithm that groups similar objects into groups called clusters. The endpoint is a set of clusters, where each cluster is distinct from each other cluster, and the objects within each cluster are broadly similar to each other.

## Classification Problem Evaluation Metrics 


1. Accuracy 

Accuracy is the proportion of true results among the total number of cases examined.

Accuracy = (TP+TN)/(TP+FP+FN+TN)

**When to use?** 

Accuracy is a valid choice of evaluation for classification problems which are well balanced and not skewed or No class imbalance.

2. Precision 

Precision = (TP)/(TP+FP)

Precision is a valid choice of evaluation metric when we want to be very sure of our prediction.

3. Recall

Recall = (TP)/(TP+FN)

Recall is a valid choice of evaluation metric when we want to capture as many positives as possible.


4. F1 Score 

The F1 score is a number between 0 and 1 and is the harmonic mean of precision and recall.

We want to have a model with both good precision and recall.



Thankyou 
**Sakshi Kukreja**
**sakshikukreja2799@gmail.com**


```python

```

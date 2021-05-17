# Support Vector Machine

## Introduction

* Support vector machine (SVM) is supervised machine learning algorithm which can be used both for classification and regression problems. But generally, it is used in classification problems.
* In 1960s, SVMs were first introduced but later they got refined in 1990. SVMs have their unique way of implementation as compared to other machine learning algorithms. Lately, they are extremely popular because of their ability to handle multiple continuous and categorical variables.
* An SVM model is basically a representation of different classes in a hyperplane in multidimensional space.
* The hyperplane will be generated in an iterative manner by SVM so that the error can be minimized.
* The goal of SVM is to divide the datasets into classes to find a maximum marginal hyperplane (MMH).

<br/>![Support Vector Machine](https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm.png)<br/>

### **The followings are important concepts in SVM −**

* **Support Vectors** − Datapoints that are closest to the hyperplane is called support vectors. Separating line will be defined with the help of these data points.

* **Hyperplane** − As we can see in the above diagram, it is a decision plane or space which is divided between a set of objects having different classes.

* **Margin** − It may be defined as the gap between two lines on the closet data points of different classes. It can be calculated as the perpendicular distance from the line to the support vectors. Large margin is considered as a good margin and small margin is considered as a bad margin.

### The main goal of SVM is to divide the datasets into classes to find a maximum marginal hyperplane (MMH) and it can be done by the following two steps −

* First, SVM will generate hyperplanes iteratively that segregates the classes in best way.
* Then, it will choose the hyperplane that separates the classes correctly.

**Example:** SVM can be understood with the example that we have used in the KNN classifier. Suppose we see a strange cat that also has some features of dogs, so if we want a model that can accurately identify whether it is a cat or dog, so such a model can be created by using the SVM algorithm. We will first train our model with lots of images of cats and dogs so that it can learn about different features of cats and dogs, and then we test it with this strange creature. So as support vector creates a decision boundary between these two data (cat and dog) and choose extreme cases (support vectors), it will see the extreme case of cat and dog. On the basis of the support vectors, it will classify it as a cat. Consider the below diagram:
<br/>![Image Classification](https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm2.png)<br/>

* SVM algorithm can be used for **Face detection**, **image classification**, **text categorization**, etc.

## Types of SVM
### SVM can be of two types:

* **Linear SVM:** Linear SVM is used for linearly separable data, which means if a dataset can be classified into two classes by using a single straight line, then such data is termed as linearly separable data, and classifier is used called as **Linear SVM classifier**.

* **Non-linear SVM:** Non-Linear SVM is used for non-linearly separated data, which means if a dataset cannot be classified by using a straight line, then such data is termed as non-linear data and classifier used is called as **Non-linear SVM classifier**.

## How does SVM works?
### Linear SVM:
* Lets take an example to understand the working of Linear SVM. Suppose we have a dataset that has two tags (green and blue), and the dataset has two features x1 and x2. We want a classifier that can classify the pair(x1, x2) of coordinates in either green or blue. Consider the below image:
<br/>![Linear SVM](https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm3.png)<br/>

* So as it is 2-d space so by just using a straight line, we can easily separate these two classes. But there can be multiple lines that can separate these classes. you can consider the below image:
<br/>![Linear SVM](https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm4.png)<br/>

* Hence, the SVM algorithm helps to find the best line or decision boundary; this best boundary or region is called as a **hyperplane**. SVM algorithm finds the closest point of the lines from both the classes. These points are called **support vectors**. The distance between the vectors and the hyperplane is called as **margin**. And the goal of SVM is to maximize this margin. The hyperplane with maximum margin is called the **optimal hyperplane**.
<br/>![Linear SVM](https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm5.png)<br/>

### Non-Linear SVM:

* If data is linearly arranged, then we can separate it by using a straight line, but for non-linear data, we cannot draw a single straight line. below image will give you the exact picture:
<br/>![Linear SVM](https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm6.png)<br/>

* So to separate these data points, we need to add one more dimension. For linear data, we have used two dimensions x and y, so for non-linear data, we will add a third dimension z. It can be calculated as: **z=x2 +y2**
* By adding the third dimension, the sample space will become as below image:
<br/>![Linear SVM](https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm7.png)<br/>

* So now, SVM will divide the datasets into classes in the following way. Consider the below image:
<br/>![Linear SVM](https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm8.png)<br/>

* Since we are in 3-d Space, hence it is looking like a plane parallel to the x-axis. If we convert it in 2d space with z=1, then it will become as:
<br/>![Linear SVM](https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm9.png)<br/>

* We can see how the non linear data seperated.

## Implementation in Python:
https://github.com/sagarbadki/Open-contributions/blob/master/Sagar_ML_Support_Vector_Machine.ipynb

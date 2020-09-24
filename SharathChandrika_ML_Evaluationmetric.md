# What is Evaluation metric? 
 * Evaluation metrics are used to measure the quality of the machine learning model, quantifies the performance of a predictive model.
 * Selecting a model,  the data preparation methods together are a search problem which guided by the evaluation metric. 
 * Experiments are performed with different models and the outcome of each experiment is quantified with a metric. 
 * This typically involves training a model on a dataset, using the model to make predictions on a test dataset, then comparing the predictions to the expected values in the test dataset.
 * For classification problems, metrics involve comparing the expected class label to the predicted class label or interpreting the predicted probabilities for the class labels for the problem. 
 *  Evaluation of machine learning models or algorithms is needed for any project. 
 *  Standard metrics works on most of the problems, that is why they are widely adopted.But all metrics make assumptions about the problem or about what is important in the problem.
 * Therefore, an evaluation metric must be chosen according to the type of dataset and the model built on the dataset, which makes choosing model evaluation metrics challenging. 
 *  This challenge is made difficult when there is a skew in the class distribution. 
 *  The reason for this is that many of the standard metrics become unreliable or even misleading when classes are imbalanced, or severely imbalanced. 

# Why is this Useful? 

* We need to use multiple evaluation metrics to evaluate your model, which is very important because a model may perform well using one measurement from one evaluation metric, but may perform poorly using another measurement from another evaluation metric.
* Evaluation metrics are critical in ensuring that model is operating correctly and optimally. There are many different types of evaluation metrics are available to test a model. 

## 1. Confusion Matrix 
<ul type="square">
<li> A confusion matrix is a table with four different combinations of predicted and actual values.</li> 
<li> This is a good way to visualize the different outputs and to calculate the Precision, Recall, Accuracy, and F-1 Score as well as the AUC-ROC. First will discuss about TP, FP, FN, and TN in a confusion matrix. </li> </ul>

![confusion_matrix_1](https://user-images.githubusercontent.com/63340338/93612837-a5a76d80-f9ed-11ea-9c05-44d2a749a8a7.png)
<ul type="square">
  <li> True Positives (TP) : The number of times our model predicted TRUE and the actual output was also TRUE. </li>

  <li> True Negatives (TN): The number of times our model predicted FALSE and the actual output was FALSE. </li>

  <li> False Positives (FP): The number of times our model predicted TRUE and the actual output was FALSE. This is known as a Type 1 Error.</li> 

   <li>  False Negatives (FN): The number of times our model predicted FALSE and the actual output was TRUE. This is known as a Type 2 Error.</li></ul>
  
  ![Type-I-and-II-errors1-625x468](https://user-images.githubusercontent.com/63340338/93614473-d12b5780-f9ef-11ea-8255-0908121fb3e8.jpg)

#### To understand this concept in a better way, let us see a small story: 

 A shepherd boy gets bored tending the town's flock. To have some fun, he cries out, "Wolf" even though there was no wolf is in sight. The villagers run to protect the flock, but then they get angry when they realize the boy was playing a joke on them. Boy repeats this many times. One night, the shepherd boy sees a real wolf approaching the flock and calls out, "Wolf" The villagers thought it is a joke again and decided to stay back in their houses. The hungry wolf turns the flock into lamb chops.  

 *Let us consider the following definitions:*

##### *"Wolf" is a positive class.*
##### *"No wolf" is a negative class.*

  *Story can be visualised as our "wolf-prediction" model using a 2x2 confusion matrix that depicts all four possible outcomes:*
  ![story](https://user-images.githubusercontent.com/63340338/93613683-d0de8c80-f9ee-11ea-876a-013c3ea4cdc4.jpeg)


## 2. Precision  
<ul type="disc">
<li> What ratio of positive identifications was actually correct? Answer for this question is Precision. </li>

<li>Precision can be described as the fraction of relevant instances among the retrieved instances.</li></ul>
The formula is as follows:

![2](https://user-images.githubusercontent.com/63340338/93614096-53ffe280-f9ef-11ea-9907-2498878c1c2f.png)

* In the terms of confusion matrix, the equation can be represented as: 

![1](https://user-images.githubusercontent.com/63340338/93614161-6da12a00-f9ef-11ea-960c-9e4df0e2bdf4.png) 

* Precision expresses the proportion of the data points our model says correct and actually were correct. 

## 3. Recall 
<ul type="square">
 <li> This answers the question “What proportion of actual positives was classified correctly?”</li> 
  <li>Also known as sensitivity. </li></ul>
  This can be represented by the following equation:

![3](https://user-images.githubusercontent.com/63340338/93614245-7abe1900-f9ef-11ea-8c13-33fd63cde835.png)

In our confusion matrix, it would be represented by: 

![4](https://user-images.githubusercontent.com/63340338/93614274-8a3d6200-f9ef-11ea-9659-1820fcaa8138.png)

<ul type="square">
 <li> Recall expresses which instances are relevant in a data set. </li>
<li> It is important to examine both the Precision AND Recall when evaluating a model because they often have an inverse relationship.</li>
 <li> When precision increases, recall tends to decrease and vice versa.</li> </ul> 

## 4. Accuracy 
* Accuracy is determining out of all the classifications, how many did model classify correctly.This can be represented mathematically as: 

![5](https://user-images.githubusercontent.com/63340338/93614316-988b7e00-f9ef-11ea-918a-e5076fa38b69.png)

* Using our confusion matrix terms, this equation is written as: 

![6](https://user-images.githubusercontent.com/63340338/93614355-a6d99a00-f9ef-11ea-9ca7-33d2e9162ca8.png)

* We want the accuracy score to be as high as possible. 
* It is important to note that accuracy may not always be the best metric to use, especially in cases of a class-imbalanced data set. This is when the distribution of data is not equal across all classes. 
* For example, say that we are looking to build a model to help diagnose people with lung cancer. If our model just classified every single person as not having lung cancer, we would be correct the overwhelming majority of the time, but the cost of someone not being diagnosed when they do, in fact, have brain cancer is devastating. Depending on the industry, these costs may outweigh the accuracy of the model. In imbalanced cases like these, it is better to use the F1-Score instead. 

## 5. F1-Score 
<ul type="circle">
 <li> The F1 Score is a function of precision and recall.</li> 
 <li> It is used to find the correct balance between the two metrics.</li>
<li> It determines how many instances your model classifies correctly without missing a significant number of instances.</li>
 <li> This score can be represented by the following equation:</li> </ul>

![7](https://user-images.githubusercontent.com/63340338/93614395-b658e300-f9ef-11ea-82e1-d885ac8f71bf.png)

<ul type="circle">
<li> Having an imbalance between precision and recall, such as a high precision and low recall, can give you an extremely accurate model, but classifies difficult data incorrectly.</li> 
 <li> We want the F1 Score to be as high as possible for the best performance of our model.</li></ul> 

## 6. AUC (Area Under Curve) ROC(Receiver Operating Characteristics) Curve 

* The AUC ROC curve is a graph which shows the performance of a classification model at all thresholds.
* ROC is a probability curve and AUC represents degree of separability. ROC plots the following parameters: 
  * True Positive Rate (TPR),  known as recall or sensitivity,  
  * False Positive Rate (FPR),  known as Fall-out, the ratio of the false positive predictions compared to all values that are actually negative. 

![9](https://user-images.githubusercontent.com/63340338/93614571-f324da00-f9ef-11ea-84fa-bb8ca0a40a13.png)
![10](https://user-images.githubusercontent.com/63340338/93614618-fe780580-f9ef-11ea-857b-3f7dcaa308d4.png)

* Both the RPR and FPR are within the range [0, 1].
* The curve is the FPR vs TPR at different points in the range [0, 1]. 
* The best performing classification models will have a curve similar to the green line in the graph below. 
* The green line has the largest Area Under the Curve.
* The higher the AUC, the better your model is performing. 
* A classifier with only 50–50 accuracy is realistically no better than randomly guessing, which makes the model worthless (red line). 
* The biggest advantage of using ROC curve is that it is independent of the change in proportion of responders. 
![11](https://user-images.githubusercontent.com/63340338/93614669-0d5eb800-f9f0-11ea-8898-5075816dc8d9.png)

## These are the frequuently used evaluation metric in Classification problems.
## Happy learning!!

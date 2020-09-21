### **What is KNN?**
* KNN is a supervised machine learning algorithm. KNN means a K Nearest Neighbor where k represents numbers from 1-n.
* KNN can be used for both classification and regression problems but it is mainly used for classification predictive analysis. It classifies a datapoint based on how its neighbors are classified.
* KNN is a simple algorithm that stores all the available cases and classifies the data based on a similar measure.

### **There are two properties of KNN:**
1. It is a **Lazy Learning Algorithm**, means it does not have a specialized training phase and uses all the data for training while classification. In other words, lazy algorithm means it does not need any training data points for model generation. All training data used in the testing phase. This results in training faster and testing phase slower and costlier. Costly testing phase means time and memory. Sometimes, KNN needs more time to scan all data points and scanning all data points will require more memory for storing training data.

2. It is **Non-parametric Learning Algorithm** because it doesn’t assume anything about the underlying data. Means the model structure is determined from the dataset. It is useful when most of the real-world datasets do not follow mathematical theoretical assumptions.

### **Work Flow Of KNN:**
Let us understand the work flow of KNN through the following steps:

**Step 1:** To perform any Machine Learning algorithm on a dataset first we need to check whether the data is ready to deal with ML algorithms or not. So first prepare your data data so that we can perform ML algorithms on it.

**Step 2:** Next, we need to decide or K value i.e. the nearest data points. It can be any integer.

**Step 3:** Calculate the distance with the help of some methods like Euclidean, Manhattan or Hamming distance. Generally, Euclidean distance is the most common method used.

**Step 4:** Now, Find the closest neighbors

**Step 5:** Vote for labels i.e. it will assign a class based on most frequent class of these rows.



### **Let us take an example:**
Suppose we have a dataset which can be plotted as follows –

![](https://www.tutorialspoint.com/machine_learning_with_python/images/concept_of_k.jpg)

Now, we need to classify new data point with black dot (at point 60,60) into blue or red class. We are assuming K = 3 i.e. it would find three nearest data points. It is shown in the next diagram −

![](https://www.tutorialspoint.com/machine_learning_with_python/images/knn_algorithm.jpg)

We can see in the above diagram the three nearest neighbors of the data point with black dot. Among those three, two of them lies in Red class hence the black dot will also be assigned in red class.

### **Curse Of Dimensionality:**
* KNN performs well with lower number of features. Because when the number of features increases this results in the increase of data. When there is an increase in data means when the dimensionality increases it may lead to overfitting problem. To solve this problem, the needed data will need to grow exponentially as you increase the number of dimensions and this problem of higher dimension is known as the **Curse of Dimensionality**.

* To solve the problem of curse of dimensionality, you need to perform Principal Component Analysis (PCA) or you can use feature selection approach. Euclidean distance is not useful anymore for large dimension. So, you can prefer other measures such as cosine similarity, which get decidedly less affected by high dimension.

### **How to choose K value?**
No optimal number of neighbors suits all kind of data sets because each dataset has it's own requirements. The noise will have a higher influence on the result, in the case of a small number of neighbors,  and a large number of neighbors make it computationally expensive. A large number of neighbors will have a smoother decision boundary which means lower variance but higher bias and a small amount of neighbors are most flexible fit which will have low bias but high variance. Mostly, we choose an odd number if the number of classes are even.


### **Finding the optimum value for K (Parameter Tuning)**
We can find the optimum value of K by using the k-fold cross-validation. It estimates the test error rate by holding out a subset of the training set from the fitting process.

|Parameter|Description|
|---------|---------|
|n_neighbors|Number of neighbors to use.|
|**weights**  |  weight function used in prediction. Possible values:	**‘uniform’** ,**‘distance’**,**[callable]**   | 
| **algorithm**  |  Algorithm used to compute the nearest neighbors: **‘ball_tree’** will use BallTree,**‘kd_tree’** will use KDTree,**‘brute’** will use a brute-force search,**‘auto’** is used to decide the most appropriate algorithm based on the values passed to fit method.**Note:** If we use fitting on sparse input will override the setting of this parameter, using brute force. |  
|**leaf_size**  | This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.  |  
|  **pint**   |  Power parameter for the Minkowski metric. When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2. For arbitrary p, minkowski_distance (l_p) is used.   |  
| **metric**  |  Dthe distance metric to use for the tree. The default metric is minkowski, and with p=2 is equivalent to the standard Euclidean metric.   |  


### **Pros:**
* Simple to understand and interpret
* As there is no assumption of data, it is useful for non-linear data.
* It is versatile.
### **Cons:**
* As it stores all the training data, it expensive.
* Required high storage.
* For large data the prediction, it takes huge amount of time.

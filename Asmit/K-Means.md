# K-Means Clustering
To understand K-Means Clutering, let us first understand a few basic concepts about it. 

So first, lets start with
## What is Clustering?
* To state it directly, **clustering is the process of dividing the items/dataset into groups, consisting of similar data-points**.
* And these groups are **called clusters**.
* The points in the same cluster are as similar as possible while the points in diffent clusters are as dissimilar as possible.

Let me explain by giving an example.
When you go to the supermarket, you see that **the similar things**, such as apple, banana, orange,etc, **are grouped together** in the fruit section. Similarly, potato, onion, garlic, etc are grouped together in the vegetable section. So we can say that these sections **are cluster of similar type** of things, and as mentioned above, **this process of creating clusters is called clustering**.
___
So now that you have basic understanding about clusters, lets us see **where clustering can be used**.
* On shopping sites, **clustering is used to recommend certain products** to the customers based on his/her past purchase history.
* It is used in banking **to divide customers into various clusters** and then give specific offer to specific group based on their account usage, balance,  or particular interests.
* Netflix, Amazon Prime, Disnep+ Hostar and various entertainment sites like these uses **clustering to suggest a new show/movie** to the person based on this watch history.

These are some simple uses of clustering.

Also talking about clustering, there are **mainly three different types of clustering**.

**1. Exclusive Clustering** 
  * Also known as Hard Clustering, in this tye of clustering **data point or items belongs exclusively to one cluster**. 
  * The **K-Means algorithm** belongs to this type of clustering.
  
  <p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/EC.PNG">
  </p>

**2. Overlapping Clustering**
  * Also known as Soft Clustering, in this type of clustering **data point or items belongs to multiple cluster**.
  * An example of this type of clustering are **Fuzzy C-Means Clustering**.
  
  <p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/OC.PNG">
  </p>

**3. Hierarchical Clustering**
  * In Hierarchical Clustering, **the aim is to produce a hierarchical series of nested clusters**.
  * A diagram called Dendrogram graphically represents this hierarchy and is an inverted tree that describes the order in which factors are merged (bottom-up view) or cluster are break up (top-down view).
  
<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/HC.PNG">
</p>
<hr>

## What is K-Means Clustering?

* So now back to **K-Means Clustering**, it **is an unsupervised learning algorithm**.

* From the above explanation, you must have understand that in clustering, **we do not have a target to predict**.
* We look at the data and then try to club similar observations and form different groups.
* Hence it is an unsupervised learning problem in which we do not have any fixed target/dependent variable, **we only have the independent variables**.

* The **K** in the k-means stands for **the number of clusters required**.
* K-means is a **centroid-based algorithm**, or **a distance-based algorithm**, where we calculate the distances to assign a point to a cluster.
* In K-Means, each cluster is associated with a centroid.
*  The main objective of the K-Means algorithm is to minimize the sum of distances between the points and their respective cluster centroid.

Following are the steps for applying K-Means algorithm and let us understand with the help of an example.

### Step 1: Select the total number of clusters to be identified.

<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s1.PNG">
</p>

* Let us consider the above data.
* By looking at the figure, we can say that taking three clusters would be suitable for this data.

### Step 2: Randomly select k distinct points.

<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s2.PNG">
</p>

* Now we will randomly select k different points in the data.
* In our case, since k=3, we will select 3 different points randomly.
* And these points will be the clusters itself.

### Step 3: Start measuring the distance between the point and selcted k clusters.
<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s3.PNG">
</p>

* So now we will measure the distance between each point and the cluster centroid.
* Initially, since there is only one point, the point itself will be the cluster centroid.

### Step 4: Assign the point to the nearest cluster.
<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s4.PNG">
</p>

* As we can see, the first point is closest to the red cluster, so it will be assigned to it.

### Step 5: Calculate the mean including the new point for the cluster.
<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s5.PNG">
</p>

* Now there are two points and so the centroid value will be changed.
* So, we will find the centroid value by simply just taking the mean of the data.
* As you can see above, the red line in the centre is the new centroid now, and for the next point we will use this to calcute the required distance.

### Step 6: Continue the same procedure for all the data points.
<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s6.PNG">
</p>

* After completion of all the points, we will get a figure like this one above.
* To check whether the algorithm did good or not, we will see the total variation within the cluster.
* Below here is the variation for this particular iteration.

<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s8.PNG">
</p>

### Step 7: Iterate over all the data again.

* So now for the next iteration, lets us take another 3 random variable.

<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s9.PNG">
</p>

* After performing all the above steps, the algorithm will create clusters of the data as follow.

<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s10.PNG">
</p>

* But the algorithm can still do better, so we will iterate once again.

<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s12.PNG">
</p>

* Taking the above three new points as the new clusters for iteraton, we will get the final clusters as shown in below image.

<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s13.PNG">
</p>
 
 * So, now if we compare the variation within the three clusters, we will see that the last iteration has the lowest value of variation for k=3.
 
 <p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s15.PNG">
</p>

* Now, no matter how many time you run this algorithm, the variation won't be lesser than the third iteration.
* So, the final output will be:

<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s7.PNG">
</p>

So that is how a simple k-means algoritm works.

Now, let me explai some few  questions.

### What is the stopping criteria for algorithm?
  
There are mainly three stopping criteria for the K-means algorithm:

**1. Centroids of newly formed clusters do not change.**
 * We can stop the algorithm if the centroids of newly formed clusters are not changing.
 * Even after multiple iterations, if we are getting the same centroids for all the clusters, we can say that the algorithm is not learning any new pattern and it is a sign to stop the training.
 
**2. Points remain in the same cluster**
 * Another clear sign that we should stop the training process if the points remain in the same cluster even after training the algorithm for multiple iterations.
 
**3. Maximum number of iterations are reached**
 * Finally, we can stop the training if the maximum number of iterations is reached.
 * Suppose if we have set the number of iterations as 50. The process will repeat for 50 iterations before stopping.
 
 ### How to choose the optimum value of k?
 
 * Sometimes, the value of k can be obviously seen by visualization of the data.
 * But sometimes it is not that easy to jugde or guess the number of cluster manually.
 
 * Well, one of the option to decide the value of k is the hit-and-trial method where you just try different values of k.
 * Also, note that k=1 is the worst case scenario as it has the highest variation.
 * And as you keep on increasing and trying different values of k, you will notice that each time you increase the cluster, the variation decreases.
 * And if number of cluster is equal to number of data points, then the total variation will be zero.
 * So we can say that the number of clusters is indirectly propotional to total variation.
 
 * Finally, when we plot the reduction in variance for per value of k, we will get a graph like below where on the X-axis we have the number of cluster-k, and on the Y-axis we have reduction in variance.
 
<p align="center">
  <img src="https://github.com/patelkishan9286/Kishan_ML_K-MeansClustering/blob/master/s16.PNG">
</p>

* On the graph, you can see that there is a huge reduction in variance with k=3, but after that there is no such steep change in the variation.
* This point of change is known as the elbow point and the value of thi point is the one which decides the value of k.
* So in order to find the optimum value of k, we need to find the elbow point from the elbow plot.


So thats it, now you've got a basic understanding of the working of the k-means clustering algorithm.

Now lets move on to the coding part where we will implement it.

# Clustering Algorithms
 
Clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense) to each other than to those in other groups.
## Clustering Algorithms
### K-Means clustering
The KMeans algorithm clusters data by trying to separate samples in n groups of equal variance.
The k-means algorithm divides a set of  samples  into  disjoint clusters , each described by the mean 
of the samples in the cluster. The means are commonly called the cluster “centroids”.

In K-Means we first choose centroids(the number is specified by the programmer).The points are assigned to the nearest centroids.We then find the mean of the cluster formed
and assign it as a new centroid.The difference between the new and the old centroid is found and the process is repeated untill the difference is less than a minimum threshhold.

<img src="kmeans1.png" alt="drawing" width="400"/>

*X represents centroids and the circles represent the data*
We find the Within-Cluster-Sum-of-Squares(WCSS).The idea is to minimise the sum.
<img src="wcss.png" alt="drawing" width="400"/>


**How to choose the number of clusters from a WCSS vs clusters graph?**


To determine the optimal number of clusters, we have to select the value of k at the “elbow” ie the point after which the WCSS start decreasing in a linear fashion.

<img src="elbow.jpg" alt="drawing" width="400"/>

*The elbow here is at number of clusters=5*


### Hierarchial Clustering
Hierarchical clustering is a general family of clustering algorithms that build nested clusters by merging or splitting them successively.This hierarchy of clusters is represented as a tree (or dendrogram).
Hierarchical clustering starts by treating each observation as a separate cluster. Then, it repeatedly executes the following two steps:
(1) identify the two clusters that are closest together, and (2) merge the two most similar clusters. This iterative process continues until all the clusters are merged together.
the distance between two clusters has been computed based on the length of the straight line drawn from one cluster to another.

<img src="clustergram.png" alt="drawing" width="400"/>


**How to choose the number of clusters from a dendrogram?**


For this algorithm to need to find the optimal number of clusters from a dendrogram.Now there isn't a fixed approach but intuitively you take the largest vertical segment which is not cut by any extended horizontal segment ,pass a horizontal line(H1) through it and the number of vertical segments H1 crosses is the optimum number of clusters.
Consider the following dendrogram.Here we can see the segment with yellow light cannot be choosen even if it has the largest length as the horizontal segments 1,2 passes through it(similarly for other segments), hence we take the verticalsegment with red highlight as the largest since no horizontal segments pass through it.

<img src="dendo.jpg" alt="drawing" width="400"/>
Now the horizontal segment in the line passes through 5 clusters which is the optimum number of clusters that you will see in the implementation file.
<img src="dendo1.jpg" alt="drawing" width="400"/>

## Happy Learning!

### **Sakshi Kulkarni**

**[sakvpms@gmail.com](mailto:sakvpms@gmail.com)**

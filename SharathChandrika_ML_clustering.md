## What is clustering?
* Clustering is the task of dividing the data points into a number of groups such that data points in the same groups are more similar to other data points in the same group and dissimilar to the data points in other groups. 
* It is basically a collection of objects on the basis of similarity and dissimilarity between them.
* For example- The data points in the graph below clustered together can be classified into one single group. We can distinguish the clusters, and we can identify that there are 3 clusters in the below picture.
![1](https://user-images.githubusercontent.com/63340338/93751163-47130700-fc1a-11ea-8e50-cccf0d71fde6.jpg)
## Why Clustering ?
1. Clustering is very much important as it determines the intrinsic grouping among the unlabeled data present. 
2. There are no criteria for a good clustering. 
3. It depends on the user, what is the criteria they may use which satisfy their need. 
4. This algorithm must make some assumptions which constitute the similarity of points and each assumption make different and equally valid clusters.
## Clustering Methods :
#### 1. Density-Based Methods :
  * These methods consider the clusters as the dense region having some similarity and different from the lower dense region of the space. 
  * These methods have good accuracy and ability to merge two clusters.
  * Example DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
#### 2. Hierarchical Based Methods : 
 * The clusters formed in this method forms a tree-type structure based on the hierarchy. 
 * New clusters are formed using the previously formed one. It is divided into two category
    * Agglomerative (bottom up approach)
    * Divisive (top down approach)
#### 3. Partitioning Methods : 
  * These methods partition the objects into k clusters and each partition forms one cluster. 
  * This method is used to optimize an objective criterion similarity function such as when the distance is a major parameter example K-means.
#### 4.Grid-based Methods : 
  * In this method the data space is formulated into a finite number of cells that form a grid-like structure. 
  * All the clustering operation done on these grids are fast and independent of the number of data objects example STING (Statistical Information Grid), wave cluster, CLIQUE (CLustering In Quest) etc.
<ul type="square">
  <li>  We shall discuss the most used clustering algorithms in detail.</li></ul>
 
 **1. K-means Clustering**

**2.Agglomerative Hierarchical Clustering**
 
 **3.DBSCAN**

## 1. K-means Clustering

* It is the simplest unsupervised learning algorithm that solves clustering problem.

* K-means algorithm partition n observations into k clusters where each observation belongs to the cluster with the nearest mean serving as a prototype of the cluster .

#### Steps involved in K-means clustering algorithm:

**Step 1** : Choose the number K of clusters.Here we choose K=2

![1 1](https://user-images.githubusercontent.com/63340338/93751220-5b570400-fc1a-11ea-8fd9-b0bdb04e2439.jpg)

**Step 2** : Select at random K points the centroids(not necessarily from dataset)

![1 2](https://user-images.githubusercontent.com/63340338/93751267-70cc2e00-fc1a-11ea-819e-9acd2ebc604e.jpg)

**Step 3** : Assign each data point to the closest centroid.(They form K clusters)

![1 3](https://user-images.githubusercontent.com/63340338/93751303-7fb2e080-fc1a-11ea-9c42-216839ac4638.jpg)

**Step 4** :Compute and place the new centroid of each cluster.

![1 4](https://user-images.githubusercontent.com/63340338/93751334-8e999300-fc1a-11ea-9e62-2c76a3b571e5.jpg)

**Step 5** : Reassign each data point to new closest centroid.if any reassignment took place, go to **Step 4**, if not model is **FINISHED**.,Here reassignment took place so we go back to **Step 4**.

![1 5](https://user-images.githubusercontent.com/63340338/93751364-9d804580-fc1a-11ea-8685-1bed233afa5c.jpg)

Repeat Step 5 until no reassignment, here reassignment doesnt take place,therefore model is completed.

![1 6](https://user-images.githubusercontent.com/63340338/93751403-aec95200-fc1a-11ea-9798-8ffe706f3c14.jpg)

### How to choose optimal value of  number of clusters:
##### Elbow Method:
 * First we calculate WCSS(Within-Cluster-Sum-of-Squares).
 * WCSS is illustrated in the below example.
 ![cluster](https://user-images.githubusercontent.com/63340338/93756360-9b21e980-fc22-11ea-82c7-12db36f99a9a.jpeg)
*  After calculating WCSS , we plot a graph between number of clusters and WCSS.

![elbowmethod](https://user-images.githubusercontent.com/63340338/93755714-61041800-fc21-11ea-80b8-f68af91e3b57.png)

* From the above graph we can observe that after a certain point WCSS values keep on decreasing and it formed a **elbow** shape .
* Which is the optimal value of clusters that can be choosen for the given dataset, here elbow is formed at number of clusters=3 ,
therefore the optimal number of clusters for that dataset are 3.
## 2. Agglomerative Hierarchical Clustering
 * Steps involved in Agglomerative Hierarchical Clustering:
   **Step 1** :Make each data point a single-point cluster( Which forms N clusters.)

![2 1](https://user-images.githubusercontent.com/63340338/93751475-c6a0d600-fc1a-11ea-8b29-7077a22cc779.jpg)
     
   **Step 2** :Take the two closest data points and make them one cluster.(Which forms N-1 clusters)
To choose the distance between clusters there are few methods ,they are:

**Complete linkage:** similarity of the farthest pair. One drawback is that outliers can cause merging of close groups later than is optimal.

**Single-linkage:** similarity of the closest pair. This can cause premature merging of groups with close pairs, even if those groups are quite dissimilar overall.

**Group average:** similarity between groups.

**Centroid similarity:** each iteration merges the clusters with the most similar central point

![2 2](https://user-images.githubusercontent.com/63340338/93751519-d7e9e280-fc1a-11ea-9759-fb35247be41f.jpg)
   
   **Step 3** :Take the two closest clusters and make them one cluster(Which forms N-2 clusters)

![2 3](https://user-images.githubusercontent.com/63340338/93751567-e801c200-fc1a-11ea-9a8e-24655c974cb6.jpg)
    
  **Step 4** : Repeat **Step 3** until there is only one cluster, **Finsihed**.
   
   ![2 4](https://user-images.githubusercontent.com/63340338/93751659-0f588f00-fc1b-11ea-86fb-13c4733781e7.jpg)
 
 ![2 4 1](https://user-images.githubusercontent.com/63340338/93751609-f6e87480-fc1a-11ea-878f-d8d950b0b8bb.jpg)
 
 ![2 5](https://user-images.githubusercontent.com/63340338/93751702-239c8c00-fc1b-11ea-81c5-971c905d38ea.jpg)

* We choose number of clusters in Agglomerative Hierarchical Clustering using dendograms

![dendrogram2](https://user-images.githubusercontent.com/63340338/93751736-31eaa800-fc1b-11ea-82c7-dedcfb134349.png)

## 3. DBSCAN
 * Partitioning methods (K-means, PAM clustering) and hierarchical clustering work for finding spherical-shaped clusters or convex clusters., they are suitable only for compact and well-separated clusters. 
 * They are also severely affected by the presence of noise and outliers in the data.
 * Real life data may contain irregularities, like –
 i) Clusters can be of arbitrary shape such as those shown in the figure below.
 ii) Data may contain noise.
 * To overcome these disadvantages of mentioned algorithms DBSCAN algorithm is used.
 * The DBSCAN algorithm is based on this intuitive notion of “clusters” and “noise”. 
 * The key idea is that for each point of a cluster, the neighborhood of a given radius has to contain at least a minimum number of points.
#### Steps involved in DBSCAN algorithm  –

**Step 1** : Find all the neighbor points within eps and identify the core points or visited with more than MinPts neighbors.

**Step 2** : For each core point if it is not already assigned to a cluster, create a new cluster.

**Step 3** : Find recursively all its density connected points and assign them to the same cluster as the core point.
 A point a and b are said to be density connected if there exist a point c which has a sufficient number of points in its neighbors and both the points a and b are within the eps distance. This is a chaining process. So, if b is neighbor of c, c is neighbor of d, d is neighbor of e, which in turn is neighbor of a implies that b is neighbor of a.

**Step 4** : Iterate through the remaining unvisited points in the dataset. Those points that do not belong to any cluster are noise

![dbscan](https://user-images.githubusercontent.com/63340338/93751787-43cc4b00-fc1b-11ea-93d0-9c2771c7b206.jpeg)

### Happy Learning !!
-----------
### Avvaru Sharath Chandrika
[My linkedin](https://www.linkedin.com/in/sharath-chandrika-avvaru-715421160/)

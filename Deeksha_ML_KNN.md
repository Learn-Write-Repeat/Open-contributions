# K nearest Neighbours

## Introduction
KNN is a baseline algorithm in ML. It follows brute force approach and any other algorithm that is devised should have accuracy greater than that of KNN to be accepted as correct.

<b>The output in KNN is predicted as the majority of the K nearest points to our query point.</b>
<br>
<img src="https://www.edureka.co/blog/wp-content/uploads/2018/07/KNN-Algorithm-k3-edureka-437x300.png" width="500px">

Here the query point is shown as a star and there are 2 different classes, A(Blue) and B(Orange). <br>
The chosen value of <b>k=3, which means we consider the 3 closest neighbours to our query point</b> <br>
Here, the distribution of the neighbours is A->1 and B->2 <br>
Since <b>B neighbours are present in majority</b>, the query point will be <b>predicted to be of class B</b> <br>

## Algorithm
### 1. Finding the K Nearest Neighbours
<b>We compute the distance of each point from our query point.</b> <br>
The distance used is the Euclidean distance <br>
<img src="https://datavedas.com/wp-content/uploads/2018/04/image001-4.png" width="500px">
<br>
### 2. After computing the distances, they are arranged in ascending order and the first K points are chosen
### 3. Then we compute the majority vote out of these K neighbours.
<br>

## Key Points
- Simplest Algorithm in Machine Learning
- Used for classification and regression both
- Comes under supervised learning
- Non parametric
- Value of k is kept odd- because if it is even there are greater chances of both classes being present in equal numbers when taking majority vote
- No training is required as all work is done in query time

# Support Vector Machines (*aka 'SVM'*)

This file explains in a subtle way the 'What?' and 'Why?' of **Support Vector Machines**, commonly known as SVMs , which are widely used as a supervised machine learning
algorithm as they are more accurate and robust to outliers. They can train on linear as well as non-linear data also consume less computational power. 
SVMs can be used for both regression and classification tasks but are mainly used for classification. 

Here we will look at its example for Binary Classification.

Suppose we have a 2-dimensional space (our Cartesian Plane of x and y coordinate system) filled with our data points on the x1 and x2 axis.
We need to classify these points into eitheir of the two groups, blue or red.

- Every data point is assumed to be represented (or simply plotted) in an N-dimensional space (here, 2-dimensional space). For classification of these data points, 
the SVM algorithm finds an **'optimal line'** (among many possible lines) which creates a **'good'** boundary between the two classses to make them seperable.

Here is our problem representation as follows before the algorithm implementation:

![](https://miro.medium.com/max/300/0*9jEWNXTAao7phK-5.png)

Now the question is, how to define the **'optimal line'** and the **'good'** boundary for the algorithm to work?

- In SVM terminology, this optimal line is called as the **hyperplane**. Hyperplanes are decision boundaries that help classify the data points. 
Data points falling on either side of the hyperplane can be attributed to different classes. Also, the dimension of the hyperplane depends upon the number of features. 
If the number of input features is 2, then the hyperplane is just a line. 
If the number of input features is 3, then the hyperplane becomes a two-dimensional plane.

- The 'good' boundary for our hyperplane will be when its distance from both the sides of the two classes would be maximum. This distance is called as the **margin**.
The margin distance should be maximum so as to maintain a good balance between two boundaries of our classes and avoid missclassification. 

Here is an image to understand the difference between a small and large margin.

![](https://miro.medium.com/max/700/0*ecA4Ls8kBYSM5nza.jpg)

So coming back to our problem, our SVM algorithm will generate a hyperplane like this:

![](https://miro.medium.com/max/300/0*0o8xIA4k3gXUDCFU.png)

- The generic SVM algorithm can then be vieved as:
  - Represent all the instances (data points) in an N-dimensional space.
  - Generate hyperplanes iteratively that segregates the data points into classe.
  - Choose the hyperplane that separates the classes correctly and keeps a maximum margin.

The data points from both the classes that are close to the hyperplane arecalled **Support Vectors**. These determine the orientation and position of our hyperplane.
If these points are changed, the resulting hyperplane will change too. Hence the name 'Support Vector Machines' owing to the important role the support vectors play 
in the algorithm.


### References and further reading:
https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47

### Written By:
Inziya Dossa        
https://www.linkedin.com/in/inziya-dossa/





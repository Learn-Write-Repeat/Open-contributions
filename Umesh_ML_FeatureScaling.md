# Name: Umesh Singh

# What is Feature Scaling?
=> In machine learning algorithms, to bring all features in same standing, we need to do scaling so that one significant number does not impact the model
because of their larger magnitude. **Feature Scaling is a technique to standardize the independent features present in the data in the fixed range**.
Feature scaling is one of the most critical steps performed while data preprocessing. Scaling can make a difference in weak machine learning algorithm and
better one. In short any algorithm which is distance based is affected by feature scaling. We can understand feature scaling like in wrestling in some category
two persons of same weight wrestle.
Feature scaling is done in two ways:

1.Mean Normalization:
**Normalization is a scaling technique in which values are shifted and rescaled so that they end up ranging between 0 and 1** . 
It is also known as min-max scaling.
![Formula](https://media.geeksforgeeks.org/wp-content/uploads/min-max-normalisation.jpg)
![Normalization](https://static.packt-cdn.com/products/9781789347999/graphics/84d43825-8e4e-47e2-a1c9-63cff1c41aca.png)

2.Standardization:
**Standardization is another scaling technique where the values are standard around mean with a unit standard deviation**.
![Formula](https://media.geeksforgeeks.org/wp-content/uploads/standardisation.jpg)
![Standardization](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_001.png)
![Feature-Scaling](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/03/NormVsStand_box_plots-1.png)

# When to use Normalization and Standardization?
=> 1.Normalization is good to use when you know the distribution of data does not follow gaussian distribution while on other hand when data follows gaussian 
distribution standardization is used. Standardization does not have specific ranges while Normalization has range between 0-1.
2. Normalization is performed when scale of feature is irrelvent or misleading and not should not normalize when scale is meaningful.


# Why Feature Scaling is Important?
=> 1.Some machine learning algorithm like kNN are sensitive to features because if they are not in the same range we can get ambiguous result. To avoid ambuguity
feature scaling is used.
2. Some algorithms which uses gradient descent like linear regression, logistic regression, neural networks,etc. for optimization. They require data to be scaled.
The presence of feature value will affect the step size of gradient descent.

# When to use feature scaling?
=> 1.K-means: uses the euclidian distance where the feature scaling matters.
   2.K-Nearest-Neighbours: also requires features scaling.
   3.Principal component analysis(PCA): Tries to get feature with maximum variance, here too feature scaling is required.
   4.Gradiant Descent: Calculation speed increases where Theta calculation becomes faster after feature scaling.
   
# Author :bowtie:
**Umesh Singh** : [LinkedIn](https://www.linkedin.com/in/umesh-singh-35629418b)

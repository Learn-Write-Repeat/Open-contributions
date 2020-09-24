# **Random forest Algorithm**
 It is supervised machine learning algorithm which is used in both regression and classification problems. this algorithm always provides best result in terms of precision and recall as it is an ensemble technique used to get more accuracy.
 
## Algorithm-
 Random forest builds multiple decision trees and merges them together to get a more accurate and stable prediction.
* We randomly select m features from total T features; m<<T. 
* Then make decision trees by taking these m features. n_estimators is simply the number of trees. The more uncorrelated trees in our forest, the closer their individual errors get to averaging out.
* Repeat above two steps to construct n number of trees.

![DevIncept logo image](https://miro.medium.com/max/574/0*a8KgF1IINziv7KIQ.png)

## Key terms related -
* *Entropy*- Entropy is measure of randomness or unpredictability in dataset.
* *Information gain*- It is measure of decrease in entropy after dataset is split.
* *Leaf node*- It contains classify item.
* *Root node*- Top most node.

   **In classification-** take voting majority based on different decision tree.
   **In regression-** take average of all output values to get result.
 
### Advantages -
* Random forest algorithm provides randomness to model means that while growing the trees. Instead of searching for the most important feature while splitting a node, it searches for the best feature among a random subset of features.
* As decision tree gives high variance result. but it provides low variance output.[**As Random forest is ensemble bagging technique where different high variance and low bias decision tree are aggregated to get low bias and low variance random forest to avoid over fitting. As random forest are low bias also,so underfiiting also not occur.**]
![DevIncept logo image](https://miro.medium.com/max/492/1*kADA5Q4al9DRLoXck6_6Xw.png)



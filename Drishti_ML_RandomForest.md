# Random Forest Classifier  :national_park:

#### When you hear of this term, what actually comes to your mind:question: :thinking:
Let me tell you what it is. <br>
Random forest means a forest consisting of many trees :deciduous_tree:, trees that take decision for predicting the outcome. 

**Real Definition** - It is a supervised algorithm which constructs multiple decision trees on the subsets in training datasets and uses the mean/mode of the decision trees in order to predict a particular outcome. 
It is used for regression and mainly for classification. 

:warning: **Note** : Supervised algorithms are based on supervised learning where we know input and output and derive a function that can map them whereas 
in unsupervised learning there is only input data and it learns more from the data to make predictions.

It is also called as an **Ensemble Method** as it combines multiple decision trees in order to solve complexity of the problem and improve it's accuracy.

Let's get to know more about it.

### How does it work:question:

![Image](https://static.javatpoint.com/tutorial/machine-learning/images/random-forest-algorithm2.png)

Consider this as an example of random forest.
Basically we know that random forest is made of multiple decision trees and the main intuition behind decision tree is selecting a criteria/feature to make 
different branches of a tree.<br>

In this case we have multiple fruits and in order to predict a new fruit it performs in following ways.

:small_red_triangle: Tree 1 : It is passed through it and with the help of decision tree predicts a particular kind which in this case is :apple:. <br>
:small_red_triangle: Tree 2 : This tree also predicts it as :apple:. <br>
. <br>
. Similarly all the trees one by one predicts its kind. <br>
. <br>
:small_red_triangle: Tree N : This also in the same way predicts it as :banana:. <br>

Now after all these decisions are made, in this case majority of the kind is taken and referred to as final class which is :apple:. Or sometimes in other cases
mean of all is taken as the final class.

Now let me state an analogy to understand more clearly.

:small_red_triangle_down: There was a guy named Chris who wanted to decide where to go for summer vacation so he asked people who knew him for suggestions. <br>
:small_red_triangle_down: His first friend asked about his likes and dislikes and based on that gives him a suggestion. <br>
&nbsp;&nbsp;:warning: **Note** - This is a single decision tree where his friend on the basis of questions makes rules and provides a suggestion. <br>
:small_red_triangle_down: In the similar way Chris asks many of his friends where each friend will act as a decision tree. <br>
:small_red_triangle_down: Finally Chris on the basis of majority of places suggested to him chooses it for summer vacation. <br>

Now time to come to **real-deal** :joy:

### Algorithm

I'll be explaining random forest as a regression method and classsification method both.

:one: Pick N random records from the dataset. <br>
:two: Build a decision tree based on these N data points. <br>
:three: Choose the number of decision trees you want and repeat steps :one: and :two: for all. <br>
:four: i) Random Forest for **Regression** - For an input each tree predicts an output and then the mean of all the decisions taken is considered to be final outcome. <br>
&nbsp;&nbsp; ii) Random Forest for **Classification** - Each tree predicts the category/class to which the output belongs and then the majority of the class is taken as final outcome. <br><br>

Now if we talk about comparing **Decision Tree** and **Random Forest** then what difference could one think offff :thinking:. Because both of them are similar in working, aren't they :question:

So one difference we know between them is that random forest has multiple decision trees and that's where it has an advantage over single decision tree. Let's see how.


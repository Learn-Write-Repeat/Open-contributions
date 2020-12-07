# Machine Learning
Machine Learning is a field of study that gives computers the ability to learn and solve problems by themselves without being programmed.
By specifying some set of rules or algorithms we can train a model which takes in some form of input whether it be numerical, text or image data
and gives outputs as predictions for any future data. This prediction is given by the model which is trained on the input data.

# Types of Machine Learning
There are 3 basic types or approaches of Machine Learning
* ***Supervised Machine Learning***
  * In Supervised Machine Learning we have a labelled dataset and we know how our output should look like.
  * In short, we have target variables which we have to predict for our input data. So we know what inputs needs to be mapped to what output.
  * The two main types of problems in Supervised Learning is **Regression** and **Classification**.
  
* ***Unsupervised Machine Learning***
  * In Unsupervised Learning we have an unlabelled dataset, which means we don't know what our output should look like.
  * So it basically depends on deriving structures or relations from the data where we necessarily don't know effect of the variables.
  * Main problem in Unsupervised Learning is **Clustering**.
  
* ***Reinforcement Learning***
  * Reinforcement Learning is a little different from Supervised and Unsupervised Learning as it does not have a dataset and a particular algorithm involved in it.
  * In this we train a model that interacts with the environment and gets rewards based on its action.
  * If the model does a job which leads it to finishing a task it is given a positive reward and if it does something wrong it is rewarded negatively.
  * Thus depending on the action taken by the model it is rewarded until if finishes a task.
  
# Supervised Machine Learning
  * Supervised Learning as the name suggests, works under supervision.
  * In this we have data which has some input variables also called as 'features' and output variable also called as 'target' variable.
  * We have to map the input to the output using models trained on algorithms 
  * There are 2 main types of Supervised Learning 
  
  ### Regression
   * In regression we have some continuous target variable that we are trying to predict.
   * It tries to map the input to a function
   * In this we try to fit a curve or any line to the input data so that any new input can be predicted based on the curve that is fit over the data
   * It has 2 main algorithms.
   
   * Linear Regression
     * In this we try to fit a line to the existing data which is of the form y = B0 + B1X.
     * The input and output variables are plotted against each other and a line is tried to fit to the plotted input data
     
   * Logistic Regression
     * In this we try to map all input greater than a particular value as 1 and less than that as 0.
     * It can be used better for Classificiation problem than Regression.
    
  ### Classification
   * In classification we try to seperate or categorize the data into different classes whch can also be refereed to as labels.
   * It is mainly used when we have different classes of data as output and not continuous form od output.
   * It can be of many types - Binary classification, Multiclass classification and more.
   * Many algorithms are used in this namely:
   1. Decision tree.
   2. Logistic Regression.
   3. Artificial Neural Network.
   4. Random Forest.
   5. Naive Bayes.
   6. Support Vector Machine.
   7. K-Nearest Neighbor.

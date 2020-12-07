Topics covered in this module are about types of Machine Learning

1.Supervised  Learning
2.Unsupervised  Learning
3.Reinforcement Learning

Supervised  Learning-In this learning,we already have the input data and the output data.These are given to the model to predict the accuracy.Example:Classification of mails

Types:Classification-It is the process of categorizing the data into classes Eg:breast cancer detection
      Regression-This model finds a connection between the dependent and independent variable.
      Types of regression models:Logistic Regression,Linear Regression
      
Classification Problem Evaluation Metrics-This is used to measure how efficient our model is.

1.Confusion Matrix:Any  model generates four types of values:True Positive,False Positive,True Negative,false Negative

2.Accuracy:It is determined by the total number of correct predictions divided by total number of predictions made for a dataset.

                  TP + TN
     Accuracy = -------------------------- 
               TP + FP + FN + TN     
3.Precision:It is the ratio of True positive by all positives predicted by model.

               TP 
Precision = --------------
               TP + FP   
               
4.Recall (Senstivity):It is  the ratio of True Positives to all the positives in the dataset.

          TP 
Recall = -----------
           TP + FN  
           
5.F1-score:It is the harmonic mean of precision and recall.

F1-score =      2 * precision * recall 
            -----------------------------
                precision + recall
6.Specificity:It is the ability of a model to predict correctly the True Negative cases.
 
               TN 
Specificity = -----------
               TN + FP   
               
7.Logarithmic Loss:It is used to compare models not only on the basis of outputs but their probabilistic outcomes.

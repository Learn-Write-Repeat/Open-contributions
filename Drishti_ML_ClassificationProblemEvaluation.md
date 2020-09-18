# Classification Problem Evaluation Metrics 

When building a classification model, in order to check how efficiently the model performs we can evaluate it with metrics . The evaluation metrics compares how accurately the predicted classes match the actual classes for classification problems.
As we know that there are several types of datasets and classification can also be binary or multiclass, based on that different evaluation matrix which are listed below can be applied in different scenarios.

1. **Confusion Matrix** :confused:

It can be generally used while dealing with multiclass classification. It is not like any other type of metrics in which we will get an integer to decide 
how efficient the model is, rather we deal with four set of values which are True Positive (TP), True Negative (TN), False Positive (FP), False Neagtive (FN).

<table>
<tbody>
<tr>
<td>&nbsp;</td>
<td>Positive</td>
<td>Negative</td>
</tr>
<tr>
<td>Positive</td>
<td>True Positive (TP) :heavy_check_mark:</td>
<td>False Positive (FP) :x:</td>
</tr>
<tr>
<td>Neagtive</td>
<td>False Negative (FN) :x:</td>
<td>True Neagtive (TN) :heavy_check_mark:</td>
</tr>
</tbody>
</table>
<br> Let us take an example so as to not confuse.:joy: <br>

Consider a dataset of pregnancy tests of a woman in which there are two classes : pregnant or not pregnant 

:small_orange_diamond: TP  It indicates that the woman is actually pregnant and the model also predicts it correctly.<br>
:small_orange_diamond: FP  It indicates that the woman is actually not pregnant but the model predicts as pregnant.<br>
:small_orange_diamond: FN  It indicates that the woman is acutally pregnant but the model predicts as not pregnant.<br>
:small_orange_diamond: TN  It indicates that the woman is not pregnant and the model predicts it correctly as not pregnant.<br>

Sometimes the cost of FN can be higher and sometimes the cost of FP can be higher.<br>


![Image](https://miro.medium.com/max/1400/1*JJ_AEptV8jF7bu17zuVxLg.png) <br><br>
Imagine that if we predict COVID-19 residents as healthy patients and they do not need to quarantine, there would be a massive number of COVID-19 infections. Hence the cost of false negatives is much higher than the cost of false positives. <br><br>
![Image](https://miro.medium.com/max/1400/1*uLbVblrwaqf1-sVT5A4TRg.png) <br>
Well, since missing important emails will clearly be more of a problem than receiving spam, we can say that in this case, FP will have a higher cost than FN.<br>

Since we now know that FP and FN can leads to false predictions we need to minimize it.


2. **Accuracy**

It is one of the most simple and common classification metrics. It is determined by the total number of correct predictions divided by total number of predictions made for a dataset. <br>
<pre>             total number of correct predictions 
Accuracy = ----------------------------------------  
               total number of predictions     </pre>
In terms of confusion matrix, accuracy can be defined as
<pre>                  TP + TN
Accuracy = -------------------------- 
               TP + FP + FN + TN     </pre>
But this metric has a disadvantage which is it cannot be used for imbalanced class datasets.

:warning: **Note :** Balanced class datasets are those in which classes are equally distributed whereas in imbalanced dataset there is always a majority present of a particular class.
<br>For example, if fraud detection dataset consists of 95% of non-fraud classes and only 5% of fraud classes then it is called an imbalanced dataset.
In this case the classification model will be showing 95% accuracy as it trained with the majority non-fraud class only. And when given a fraud case to predict, it will predict it as non-fraud class based on training.
<br> And hence accuracy sometimes can be misleading in a way which would increase our hopes about model or also it may cost life of a person if predicted for a particular disease with imbalanced dataset.<br>

3. **Precision**

In terms of confusion matrix, precision is defined as the ratio of True Positives to all the positives predicted by the model.

<pre>                 TP 
Precision = --------------
               TP + FP   </pre>
The more False Positive the model predicts, the lower is it's precision value.

4. **Recall (Senstivity)**

This is defined as the ratio of True Positives to all the positives in your dataset.
<pre>             TP 
Recall = -----------
           TP + FN   </pre>
The more False Negatives the model predicts the lower the recall. <br>

The idea of recall and precision seems to be abstract. Let me illustrate the difference with the help of an example.

Let's say that we have dataset of bank loans with the confusion matrix given below<br>


<table>
<tbody>
<tr>
<td>&nbsp;</td>
<td>Positive</td>
<td>Negative</td>
</tr>
<tr>
<td>Positive</td>
<td>:heavy_check_mark: TP-599 </td>
<td>:x: FP-0 </td>
</tr>
<tr>
<td>Negative</td>
<td>:x: FN-33 </td>
<td>:heavy_check_mark: TN-22 </td>
</tr>
</tbody>
</table>

Precision : Out of the loan that is predicted aas a bad loan, how many did we classify correctly:question: 
 
<pre>                 599 
Precision = --------------  = 100%
               599 + 0   </pre>
               
Recall : Out of the actual bad loan, how many did we correctly predict as bad loan:question:

<pre>             599 
Recall = -----------  =  94.5%
           599 + 33   </pre>         
####Precision vs Recall       <br>
![Image](https://miro.medium.com/max/700/0*uhuG2rhX6XzNC43X.png)     <br>     

For a particular model, instead of using either precision or recall we can combine both of them to obtain **F1-score**.

5. **F1-score**

For some models, sometimes the recall would be high and sometimes precision would be high. We cannot even take mean of these two values as that also would be insignificant measure for evaluating model. Hence we use harmonic mean of precision and recall which is termed as F1-score. F1-score balances out the both he precision and recall in one integer. An F1 score is considered perfect when it’s 1, while the model is a total failure when it’s 0.

<pre>                         1                            2 * precision * recall 
F1-score = 2 * -----------------------------  =   -----------------------------
                   1/precision + 1/recall               precision + recall
                
</pre>  
In the above example of bank loans, F1-score will be
<pre>                 2 * 1 * 0.945 
F1-score =   ------------------------  =   0.971
                   1 + 0.945               
                
</pre> 

# Introduction To Machine Learning

Machine learning (ML) is a branch of Artificial Intelligence.It fouses mainly on the designing of systems,thereby allowing them to learn and make predictions based on some experience which is data in case of machines.

### Key Points :-

* Data is in the form of Information.
* Problem solving tool.
* Combination of CS(Computer Science),Engineering & Statistics.
* Interprets data & act on it.
* Optimize performance using past experience.

### Key Terminologies :-

1. Expert System.
2. Training DataSet.
3. Validation DataSet.
4. Test DataSet.
5. Target Variable.
6. Classification.
7. Regression.
8. Feature.

### Types Of Machine Learning :-

Machine learning is categorized by how an program/software learns to become more accurate & precise in its predictions. There are three basic approaches of ML :

<img src="https://miro.medium.com/max/787/0*XuT17hUnXWXh8EmO" alt="tree diagram" width="60%" height="60%">


* **Supervised Learning** :- Supervised Learning works under supervision.the dataset that you have collected here is labelled and so you know what input needs to be mapped to what output. This helps you correct your program if there is some mistake.

* **Unsupervised Learning** :-  the info collected here has no labels and you're undecided about the outputs. So you model your program such it can understand patterns from the input file and provides the desired answer(output).

* **Reinforcement Learning** :- there's no dataset during this quite learning, not does one teach the algorithm anything. You model the program ,it interacts with the environment and if the algorithm does an honest job, you reward it.It's kind of like our life like parents make a deal(if you get good marks i'll buy you new i-phone).
* ## What is Supervised Learning?:-

* Supervised Learning works under supervision.
* In supervised learning, you train your model on a labelled dataset that means we have both  input data as well as output data. We split our data into a training dataset and test dataset where the training dataset(like **If shape of object is rounded and depression at top having color Red then it will be labeled as Apple.**) is used to train our network whereas the test dataset acts as new data for predicting output or to see the accuracy of our model.

<img src="https://cdn.educba.com/academy/wp-content/uploads/2019/08/What-is-supervised-learning.jpg" alt="tree diagram" width="60%" height="60%">

* In this image above you can see that we are feeding inputs as an image of apples and bananas to the algorithm as a part of the algorithm we have a supervisor who keeps on checking and correcting the machine or who keeps on training the machines or keeps on telling him that yes it is an apple or  it is an banana , things like teacher teaches his students because the teacher already knows the results.
* It is used for predicting the classification of other unlabled data through the use of supervised learning.

### Why Supervised Learning is important ?  :-

* Supervised learning helps to solve various types of real-world problems.(for eg.Facebook uses face recognition when we try to tag someone,forecasting sales,weather detection).
* Supervised learning use for classification problem.
* Supervised learning is very useful in cyber-security.

### Types of Supervised Learning? :-

* **Regression**.
* **Classification**.

### Disadvantages :-

* Classifying big data is challenging.
* training a SL requireds lots of data & lots of time.
* We required lots of train data for good examples.

### Application of supervised learning :-

* ***Spam Filtration:***  Detecting spam emails is a very helpful application, this spam filteration technique easily detect any virus ,malware. In recent studies, it was found that about **56.87%** of all emails revolving around the internet were spam in March 2017 which was a major drop from April 2014's **71.1%** spam share.
<img src="https://miro.medium.com/max/1840/1*hsyCZOYoGrX6BJsj4Lgrhg.png" alt="spam filtration" width="40%" height="40%">

* ***Sentiment Analysis:*** It's a language processing technique during which we check & categorize some meaning out of the given text data. for instance, if we are analyzing messages of individuals and wish to predict whether a message could be a query, complaint, suggestion or opinion, we are going to simply use sentiment analysis.
<img src="https://www.upgrad.com/blog/wp-content/uploads/2019/04/70862042.png" width="40%" height="40%">

* ***Speech Recognition*** : Lots of people know about speech recognition,that you teach algorithm about voice system recognize it. The most well-known example such as Google Assistant and Siri or samsung assistant bixby.whatever information just tell them 'Hey siri'.
<img src="https://image.slidesharecdn.com/sr-170427000436/95/speech-recognition-system-1-638.jpg?cb=1494239334" width="30%" height="30%">

### What Is Regression? :-

* Regression analysis may be kind of predictive modelling technique which investigates the connection between a dependent and independent variable.
* A regression analysis involves graphing a line over a group of information points that the majority closely fits the general shape of the info or regression showes the changes in variable on y-axis to changes within the variable quantity on the x-axis.
<img src="https://static.javatpoint.com/tutorial/machine-learning/images/linear-regression-vs-logistic-regression.png" alt="Regression" height="70%" width="70%">  

### Types Of Regression :-

1. **Linear Regression** :-
* A Linear Regression is one of the easiest algorithm in ML. is a stastical model that attempts to indicate the link between the 2 variable,input(X) & output(Y) with the equation.The Input variable is called the Independent Variable and the Output variable is called the Dependent Variable.When unseen data is passed to the algorithm, it uses the function, calculates and maps the input to a continuous value for the output.
* The equation has the form Y= B0 + B1X, where Y is the dependent variable (that's the variable that goes on the Y axis), X is the independent variable (i.e. it is plotted on the X axis), B1 is the slope of the line and B0 is the y-intercept.
<img src="https://nextjournal.com/data/QmfPuPp4V74FyvTTojMj6ix9T8Skj1ji4GhX5Pr6zK8w4N?filename=linear-regression.png&content-type=image/png" alt="linear regression">

2. **Logistic Regression** :-
* Logistic Regression could be a method wont to predict a variable,given a collection of independent variables,such that the variable is categorical.It does the prediction by mapping the unseen data to the logit function that has been programmed into it. The algorithm predicts the probability of the new data then it’s output lies between the range of 0 and 1.
* The equation has the shape log(Y/1-Y)=B0+B1X1+B2X2+....,where Y is that the variable (that's the variable that goes on the Y axis), X is that the variable quantity (i.e. it's plotted on the X axis).The output curve is understood as Sigmoid 'S' Curve.
logistic regression
<img src="https://miro.medium.com/max/499/0*ENkZ5v28CDzuaoYU.png" height="35%" width="35%" alt="logistic regression">

**difference between Linear regression and logistic regression:-**

<img src="https://miro.medium.com/max/1450/1*rsNiQDB2HZBzlihOwyi42A.png" height="50%" width="50%" >

# CLASSIFICATION IN MACHINE LEARNING

## What is Classification?

<img src = "https://cdn.analyticsvidhya.com/wp-content/uploads/2020/01/cifar-10-classification.jpg" width="70%">

**Classification** is a process of categorizing a given set of data into classes. 
It can be performed on both **structured** or **unstructured data**. 
The process starts with predicting the class of given data points. 
The classes are often referred to as **target**, **label** or **categories**.

The classification predictive modeling is the task of approximating the mapping function from input variables to discrete output variables. 
The main goal is to identify which class/category the new data will fall into.

<img src = "https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/11/classification.png">

## Classification Terminologies In Machine Learning

- **Classifier** – It is an algorithm that is used to map the input data to a specific category.
- **Classification Model** – The model predicts or draws a conclusion to the input data given for training, it will predict the class or category for the data.
- **Feature** – A feature is an individual measurable property of the phenomenon being observed.
- **Binary  Classification** – It is a type of classification with two outcomes, for eg – either true or false.
- **Multi-Class Classification** – The classification with more than two classes, in multi-class classification each sample is assigned to one and only one label or target.
- **Multi-label Classification** – This is a type of classification where each sample is assigned to a set of labels or targets.
- **Initialize** – It is to assign the classifier to be used for the
- **Train the Classifier** – Each classifier in sci-kit learn uses the fit(X, y) method to fit the model for training the train X and train label y.
- **Predict the Target** – For an unlabeled observation X, the predict(X) method returns predicted label y.
- **Evaluate** – This basically means the evaluation of the model i.e classification report, accuracy score, etc.

# Classification Algorithms

* Logistic Regression
* Naive Bayes Classifier
* K-Nearest Neighbor
* Decision Tree
* Random Forest
* Support Vector Machines


# Classification Problem Evaluation Metrics 
1. **Confusion Matrix** :
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

 **Accuracy** :
 <pre>             total number of correct predictions 
Accuracy = ----------------------------------------  
               total number of predictions     </pre>
 **Precision**
 <pre>                 TP 
Precision = --------------
               TP + FP   </pre>
 **Recall (Senstivity)**
 <pre>             TP 
Recall = -----------
           TP + FN   </pre>
 **F1:-score**
 . <pre>                         1                            2 * precision * recall 
F1-score = 2 * -----------------------------  =   -----------------------------
                   1/precision + 1/recall               precision + recall
 **Specificity**
 <pre>                 TN 
Specificity = -----------
               TN + FP   </pre>

**You can contact me from below links provided just click the icon:-**






**Mail** : ragulraj.a2018@gmail.com



#### Thanks For Reading!

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

##### Now that we've got a basic idea of what's Machine Learning and therefore the differing kinds of Machine Learning, allow us to enter the particular topic for discussion here and answer what's Supervised Learning? Why Supervised Learning is important? kinds of Supervised Learning? what are disadvantage?explain applicartion od supervised learning? Supervised Learning Algorithms.

## What is Supervised Learning?:-

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

##### Now that we've got a basic idea of what's Supervised Learning,why SL is very important,disadvantages and application.Let us move in its types and Algorithms.

### What Is Regression? :-

* Regression analysis may be kind of predictive modelling technique which investigates the connection between a dependent and independent variable.
* A regression analysis involves graphing a line over a group of information points that the majority closely fits the general shape of the info or regression showes the changes in variable on y-axis to changes within the variable quantity on the x-axis.
<img src="https://static.javatpoint.com/tutorial/machine-learning/images/linear-regression-vs-logistic-regression.png" alt="Regression" height="70%" width="70%">  

### Types Of Regression :-

1. **Linear Regression** :-
* A Linear Regression is one of the easiest algorithm in ML. is a stastical model that attempts to indicate the link between the 2 variable,input(X) & output(Y) with the equation.The Input variable is called the Independent Variable and the Output variable is called the Dependent Variable.When unseen data is passed to the algorithm, it uses the function, calculates and maps the input to a continuous value for the output.
* The equation has the form Y= B0 + B1X, where Y is the dependent variable (that's the variable that goes on the Y axis), X is the independent variable (i.e. it is plotted on the X axis), B0 is the slope of the line and B1 is the y-intercept.
<img src="https://nextjournal.com/data/QmfPuPp4V74FyvTTojMj6ix9T8Skj1ji4GhX5Pr6zK8w4N?filename=linear-regression.png&content-type=image/png" alt="linear regression">

2. **Logistic Regression** :-
* Logistic Regression could be a method wont to predict a variable,given a collection of independent variables,such that the variable is categorical.It does the prediction by mapping the unseen data to the logit function that has been programmed into it. The algorithm predicts the probability of the new data then it’s output lies between the range of 0 and 1.
* The equation has the shape log(Y/1-Y)=B0+B1X1+B2X2+....,where Y is that the variable (that's the variable that goes on the Y axis), X is that the variable quantity (i.e. it's plotted on the X axis).The output curve is understood as Sigmoid 'S' Curve.
logistic regression
<img src="https://miro.medium.com/max/499/0*ENkZ5v28CDzuaoYU.png" height="35%" width="35%" alt="logistic regression">

**difference between Linear regression and logistic regression:-**

<img src="https://miro.medium.com/max/1450/1*rsNiQDB2HZBzlihOwyi42A.png" height="50%" width="50%" >

> Now,We done with our 1st type of SL,let's take a look at 2nd type, Classification.

### What Is Classification? :-
* Classification is a process of categorizing a given set of knowledge into classes,,it can be performed on both structured or not structured data.The process starts with predicting the class of given data points.The classes are often referred to as target,label or categories.
* The classification predicting modelling is the task of approximating the mapping function from input variables to discrete output variables.The main goal is to identify which class or category the new data will fall into.
<img src="https://developers.google.com/machine-learning/guides/text-classification/images/TextClassificationExample.png" alt="Classification"  height="50%" width="50%">

* so let's try and understand with the straightforward example,Heart disease detection can be identified as a classification problem.There is a binary classification since there can only be two classes(has a heart disease or does not have a heart disease).The classifier in these case needs training data to understand how the given input variables are related to the class & one's the classifier is trained accurately,it can be use to detect whether heart disease or not for a particular patient.

### Classification algorithm :-

* Let me first tell you what are classification algorithms.classification is a supervised learning concept with basically categories are set of data into classes.so most common classification problem are speech recognition,face detection,handwriting recognition,document classification etc.It can be either binary classification problem or multi-lass problem too.so there are bunch of ML lagorithms for classification.Let's take look at those classification algorithms :-

1. Decision tree.
2. Logistic Regression.
3. Artificial Neural Network.
4. Random Forest.
5. Stochastic Gradient Descent.
6. Naive Bayes.
7. Support Vector Machine.
8. K-Nearest Neighbor.

> we already discuss about Logistic Regression,now we discuss another algorithm .
* **Naive Bayes** :- 1. it's a classification algorithm which is predicated on Bayes Theorem.It gives an assumptions of independence among predictors.in simple way we are able to say that,Naive Bayes classifier assumes that the presence of a feature during a class is unrelated to the presence of other feature.Even if the feature rely upon one another all are these properties contribute to the probability independently.So these model is simple to create & use for large dataset.
2. Bayes theorem :- Finding  the probability of event A, when event B is true.<br>
      P(A|B)=  (P(B|A)*P(A))/P(B).<br>
      P(A) = probability of event before event B.<br>
      P(B) = probability of event after event B.
            
> These is all about ML and its types.In next topic we will learn about How it works.

### How Naive Bayes algorithm works?
* Let’s are aware of it using an example.I have a training data set of weather and corresponding target variable ‘Play’ (which showing probability of playing). we want to classify whether players will play or not supported weather. Let’s follow the below steps :-

* Step 1: Convert the dataset into a frequency table

* Step 2: find the probabilities like Overcast probability = 0.29 and probability of playing = 0.64.
<img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/08/Bayes_41-850x310.png" height="70%" width="70%">

* Step 3: Now,We use Naive Bayesian equation to calculate the probability for every class. the category with the best posterior probability is that the ouput.which is comparable to prediction.

* **Problem**: Cricket will play if weather is clear. Is this statement is right?

We can solve this by Naive Bayes Algorithm.

P(Yes | Clear) = P( Clear | Yes) * P(Yes) / P (Clear) ...........{P(A|B)=  (P(B|A)*P(A))/P(B).}

we have P (Clear |Yes) = 3/9 = 0.33, P(Clear) = 5/14 = 0.36, P( Yes)= 9/14 = 0.64

Now, P (Yes | Clear) = 0.33 * 0.64 / 0.36 = 0.60, which has higher probability so weather is clear.

##### Here we end our topic,hope you understand well.

**You can contact me from below links provided just click the icon:-**
* <a href="https://www.facebook.com/yash.naval.92/">
  <img align="left" alt="Yash Naval's Facebook" width="20px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/facebook.svg" />
</a>

* <a href="https://twitter.com/YashNaval2">
  <img align="left" alt="Yash Naval's Twitter" width="20px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg" />
</a>

* <a href="https://www.instagram.com/yash_naval/">
  <img align="left" alt="Yash Naval's Instagram" width="20px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>

* <a href="https://github.com/yashnaval">
  <img align="left" alt="Yash Naval's Github" width="20px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" />
</a>

* <a href="https://www.linkedin.com/in/yash-naval-96104b1b5/">
  <img align="left" alt="Yash Naval's Linkdein" width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>

#### Thanks For Reading!

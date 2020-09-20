# Hello Learner! 

**Its a new day to learn an interesting topic today**🥳📚
I personally believe that asking questions are the perfect and optimal way to learn new things.
When you look around yourself, there are so many unexplained things which one must find to be intriguing. One such topic is ***Natural Language Processing***(aka NLP).

>Have you ever wondered how the mailing system segregates incoming mails and places them under different categories such as primary and spam? Yes,you guessed it right, Natural Language Processing comes into play. The machine is trained to analyze each of the incoming mails and categorize them accordingly.A few decades ago,one can never have imagined that a machine could have an intelligence of its own, but after tons of research, studies and inputs from brilliant minds later,here we are with a machine that literally has a brain of its own.Interesting right!.


![Alt Text](https://miro.medium.com/max/875/1*iJq3Er1yWfKkyTh83gA3Yw.gif)



***Enough of the pep talk,let's jump right into today's lesson!***

-NLP is a sub-class of Artificial Intelligence.

>Putting it into lay-man terms,it is a super-bridge which connects humans and machines and enables the machine to understand,process and draw insights from the human language 👥 🔗 🖥️ .

There are many algorithms related to machine learning,this combined with NLP acts as a resource for creating systems that performs tasks on their own(like the one mentioned above😁☝️).

## One such Algorithm is the *Naive Bayes Classifier*

![image.png](https://miro.medium.com/max/940/1*BX1x7UbkC5JxDK6oDnn-bA.png) 

>It is a probabilistic algorithm which is basically a concoction of **probability theory and bayes theorem**.There a few steps involved in the working:

## Brushing up on the Basics of  Probability:
Let us take a simple example:
**Flipping a coin**

Since there are two possibile outcomes-head and tail

- The probability of getting a head is P(Head)=1/2 and the probability of getting a tail is P(Tail)=1/2

This algorithm primarily predicts the tag of a given word. Tag is nothing but a simple transformation or breaking up of a sentence into a 
    - list of words
    - list of tuples
The sub categories of a tag are noun,verb,adjective,adverb etc.
>Let us take a look at the results of a previosly analyzed set of emails.

|Text                    |Tag     |
|:---------------        |:-------|
|Send pin                |Spam    |
|Update pin              |Not Spam|
|Update account details  |Not Spam|
|Send account details    |Spam|
|Personal details        |Spam|

The probability of Spam and Ham is as follows:

>P(Spam)=3/5
>P(Not Spam)=2/5

List of the probabilities of every word in the Spam or Not Spam:

|Spam|Not Spam|Word     |
|----|--------|---------|
|2/3 |0/2     |Send|
|1/3 |1/2     |Pin|
|0/3 |2/2     |Update|
|1/3 |1/2     |Account|
|2/3 |1/2     |Details|
|1/3 |0/2     |Personal|

* The algorithm classifies and performs tagging on each text in the mail by individually looking at all of its features using    the bayes rule. 

* The probability of each word is calculated for every feature and the product of all the probabilities decides the final      probability and gives the result.

* In our example the result is whether the email is spam or not and the feautures are each of the distinct words in the email

Now let us imagine that a new mail comes in and we need to predict whether it is spam or not
The sentence is ***Send Details***:

>The conditional probability is calculated using the above probabilities which is then applied to the Bayes Theorem:


## Bayes Rule:
![image.png](https://miro.medium.com/max/1468/1*LB-G6WBuswEfpg20FMighA.png)

#### Similarly, the formula for our example will be:
![image.png](https://image.slidesharecdn.com/lecture6-150305162926-conversion-gate01/95/modeling-social-data-lecture-6-classification-with-naive-bayes-11-638.jpg?cb=1425573010)

>Using the above method the algorithm predicts whether a mail is spam or not!
#### The above mail is categorized as Spam.
 
    

## Types of Naive Bayes Classifiers:
There are different types of Naive Bayes Classifiers:
    * Gaussian
    * Multinomial
    * Bernoulli

## Conclusion
- [x] Give yourself a pat on the back!👏

*You are now familiar with the Naive Bayes Classifier and have a profound understanding of how the algorithm actually works under the hood!* 

Go on and get your hands dirty in applyingthe algorithm to a dataset.All the best😀

Author: NIKHITHA S
>Linkedin-[https://www.linkedin.com/in/nikhitha-sivaprakasam-31213418b/]
>Github-[https://github.com/nikhithasiva]
>Gmail-nikhithasiva98@gmail.com


```python

```

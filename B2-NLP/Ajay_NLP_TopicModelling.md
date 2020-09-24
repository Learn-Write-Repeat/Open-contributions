# Topic Modelling

In this world of internet, with each passing day we are producing a massive amount of data. And a large amount of this data is textual and that too without any kind of 
labels attached with it like about which topic this data is talking about.

So, the question is if we want to extract the hidden information (like what are the different topics present) from this textual data, How will we do it ???? 

### " The answer to this question is Topic Modelling "

* Topic Modelling is a method/way which helps you to analyze large volumes of text by clustering documents into certain topics. 

![](https://2.bp.blogspot.com/-UO8E6wws1Go/XGWgbLTPJnI/AAAAAAAABoQ/tGuBrjfJZ1UGmUQ112ZCv3gAu3Tg0O1FACLcBGAs/s1600/image001-min.png)

***Although there are a variety of techniques to do topic modelling but I will be showing you the most famous one i.e., LDA (Latent Dirichlet Allocation)***

## LDA (Latent Dirichlet Allocation)
LDA generates topics based on the frequency of words present in a set of documents.

This technique assumes that :- 
1. Each document is a collection of topics.
2. And further each topic is a collection of certain words.

For Example - I have these 3 documents 
* Document 1 - Coronavirus cases are increasing at a rapid rate.
* Document 2 - We have to take precautions and protect ourselves from this pandemic.
* Document 3 - The increase in unemployment rate and decrease in economy are the issues India is facing amid corona.

So, LDA will now assign these documents to certain topics based on frequency of words.

**Topic 1** - 40% coronavirus, 25% precautions,  15% pandemic....... (We can interpret this topic deals with Coronavirus)

**Topic 2** - 30% Unemployement, 20% Economy, 5% corona....... (We can interpret this topic deals with Economy and Unemployement).

<br>

 ### **Note** :- Two important things to keep in mind before applying LDA
     1. The user must initially decide the no. of topics present in the documents.
     2. And at the end should interpret what are the topics (Just like we interpreted 1st topic is about coronavirus above).
     
***Intersted in Maths behind LDA, read it here ---> https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation***

<br>

Thanks for Reading !!! :blush: 

You can reach me on social media via :

*Linkedin* - https://www.linkedin.com/in/ajay-singh-panwar-134890192/

*Gmail* - a.panwar48656@gmail.com

*Kaggle* - https://www.kaggle.com/ajaysinghpanwar

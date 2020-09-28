# What is Word2Vec ?
Word2Vec is one of the most popular technique to learn word embeddings using shallow neural network. The word2vec algorithm uses a neural network model to learn word associations from a large corpus of text.
Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence. As the name implies, word2vec represents each distinct word with a particular list of numbers called a vector. 
The vectors are chosen carefully such that a simple mathematical function (the cosine similarity between the vectors) indicates the level of semantic similarity between the words represented by those vectors.
It was developed by Tomas Mikolov in 2013 at Google.
# Why do we need them?
The purpose and usefulness of Word2vec is to group the vectors of similar words together in vectorspace. That is, it detects similarities mathematically.
Word2vec creates vectors that are distributed numerical representations of word features, features such as the context of individual words. It does so without human intervention}.
<br>
Given enough data, usage and contexts, Word2vec can make highly accurate guesses about a word’s meaning based on past appearances. Those guesses can be used to establish a word’s association with other words (e.g. “man” is to “boy” what “woman” is to “girl”), or cluster documents and classify them by topic.
Those clusters can form the basis of search, sentiment analysis and recommendations in such diverse fields as scientific research, legal discovery, e-commerce and customer relationship management.
# How does it work ?
Embeddings in Word2Vec can be obtained using two methods (both involving Neural Networks):
Skip Gram and Common Bag Of Words (CBOW)
Skip Gram works well with small amount of data and is found to represent rare words well, While CBOW is faster and has better representations for more frequent words.
## CBOW Model:
This method takes the context of each word as the input and tries to predict the word corresponding to the context. <br>
Consider an example: Have a great day.
Let the input to the Neural Network be the word, great. Notice that here we are trying to predict a target word (day) using a single context input word great. More specifically, we use the one hot encoding of the input word and measure the output error compared to one hot encoding of the target word (day). In the process of predicting the target word, we learn the vector representation of the target word.<br><br>
Let us look deeper into the actual architecture.
<img src="https://i.stack.imgur.com/sAvR9.png">
The input or the context word is a one hot encoded vector of size V. The hidden layer contains N neurons and the output is again a V length vector with the elements being the softmax values.
# Skip-Gram model:
<img src="https://miro.medium.com/max/875/0*Ta3qx5CQsrJloyCA.png" width="600">
We input the target word into the network. The model outputs C probability distributions.
For each context position, we get C probability distributions of V probabilities, one for each word.<br><br>
In both the cases, the network uses back-propagation to learn.

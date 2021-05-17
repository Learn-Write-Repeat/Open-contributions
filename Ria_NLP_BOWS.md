# Bag of Words
A simple model for converting natural languages into machine understandable representation

## What exactly is Bag of Words?
```
Natural Language Processing deals with real, human spoken languages, such as English, Hindi, etc
In order for machines to perform computation on languages and find inferences from them, it is essential for the words to have machine understandable mathematical representation.
One of the models that helps us do so is called the Bag of Words model.
The basic concept behind the model is to accept a set of words, and note the presence or absence of words in different documents and store it in a matrix form.
The machine can then be trained using different training techniques to learn the corresponding output.
So the next time the model sees the same word it can use the previous results to predict the output again.

```

**Example :**

Say that the model is used for a dataset having reviews on a product(say, a phone). The review can be positive or negative. In order to predict the class of a new review, we will first train our dataset with the already available review results. Using bag of words we convert the language into a mathematical form and check which words are present in which reviews and what is the sentiment for the corresponding to it. Then use machine learning any machine learning model to train the machine on the already known reviews so that when a new review is inputted the machine can check words from the vocabulary and make a prediction for the new input.

![Bag of Words representation](https://www.websystemer.no/wp-content/uploads/2020/08/bag-of-words-and-tfidf.jpg)


## Detailed explanation of Bag of Words and why it is used

**Terms used :**

* Document       : A single written account(such as a particular review)
* Corpus         : A collection of documents
* Matrix         : A structure having rows and columns
* Vector         : Matrix with multiple rows and a single column
* Vocabulary     : A collection of words whose meaning is already known
* Feature Matrix : In this case, a matrix accounting for if the word is present or not

Suppose we are given a dataset with one column as Review and the other as its sentiment, with 1 for positive sentiment and 0 for negative sentiment. The entire dataset forms a corpus and individual reviews form a document. Each time a document is picked up and all the distinct words(words discarding the words that are already used) in the review are picked, these words are then added as a column in the feature matrix. Once this process is completed for all the documents in the corpus, what we have is a feature matrix having distinct words from all the documents. Let us call this matrix X. The rows of the matrix represent each of the documents(row of review). After this, each and every document is traversed through to check which words are present in them. If a particular word is present in the document, then for the corresponding document (row) and word (column), the entry 1 is added, signifying that the word was found in the document. This is how the whole feature matrix is filled, thus achieving the goal of representing natural language words in a mathematical format.
All the words in the feature matrix form the vocabulary and a vector Y is made which takes into account the sentiment (0 or 1) for each row. 

Now since the language words have a mathematical representation, we can use any of the machine learning models( such as decision tree, naive bayes, etc) to train on the matrix X and vector Y, and make a prediction for the new review’s sentiment.

**Watchouts :**

1. Since capital letters are different from small letters, the same words may be counted twice if case sensitivity is not checked for. In order to solve this problem, an easy way is to convert all the letters into lowercase before inputting it to bag of words model
2. There are a lot of other symbols used in a language other than the letters, such as punctuations and all of them add no meaning to the words and would occupy unnecessary space in the feature matrix. Thus, all of them should be removed in the beginning.
3. Words like loving, loved convey the same sentiment and counting them twice will again waste memory and space in the matrix, and thus, only the word stem(lov) should be taken.
4. Sometimes abbreviations of words may be present; the abbreviations should be converted into full words before utilizing them in the model for better performance.

**Email** : riagohel@outlook.com

# Word2Vec
Welcome! Before getting to know 'what' the Word2Vec NN algorithm is, we must first understand the 'why' behind it i.e. its purpose. The following description answers just that by introducing to you the concept of word embeddings. So stick around!
## Word Embeddings
In order to use Word2Vec we must first understand what word embeddings are. Word embeddings are vectors assigned to each word in the vocabulary. These vectors lie in an n-dimensional space where n could range from 300 to 1000, and can be understood by  describing features for each word in the vocabulary.</b>
For example words like ‘man’ and ‘woman’ can be converted into vectors where they would have strongly contrasting values on the ‘gender’ axis  (say -1, 1 respectively) since they primarily describe a difference in gender; whereas they would score low on features like ‘food’ or ‘colour’ and would have equal if not similar values w.r.t each other. The following table considers a few more words to understand this better:</b>
Word|Man|Woman|King|Queen|Apple|Orange|Sky
-|-|-|-|-|--|--|-
**Gender**|-1|1|-0.95|0.97|0.00|0.00|0.005
**Colour**|0.01|0.009|0.01|0.009|0.98|0.94|-0.88
**Food**|0.03|0.04|0.04|0.02|0.95|0.956|0.002</b>

As can be seen words like apple and orange score high on the ‘food’ feature and are also very similar to each other on the ‘colour’ feature; whereas the sky which has an almost opposite colour (blue) has a high negative value.
Word embeddings help us find analogies among words by minimizing a distance metric between two vectors as follows:</b>

If;  man:woman ::king: ?</b>

E<sub>man</sub>-E<sub>woman</sub>=E<sub>king</sub>-E<sub>?</sub>+e </b>

![](https://github.com/Nishant11769/Nishant_Word2Vec/blob/master/analogy.png)

The value of E<sub>?</sub> that minimizes the magnitude of e turns out to be the embedding for the required word i.e 'queen':</b>

Hence: E<sub>queen</sub>=argmin(D(E<sub>king</sub>-E<sub>man</sub>+E<sub>woman</sub> , E<sub>?</sub>)); </b>

where the distance function D is usually cosine although root mean squared distance is also used in some cases</b>

Word embeddings can be thought of as a method by which a NLP model understands the meaning of a word and further applies it to other similar words. The embedding matrix can be treated as a parameter and it's values can be learned using the Word2Vec model which will now be discussed.</b>

## Word2Vec Model
Since you have understood the reason to why we use Word2Vec, I shall now explain to you what it exactly is. In simple terms it is shallow
2-layered neural network model that helps us construct the embedding matrix. However it differs from a regular neural network in the sense
that the outputs returned by the softmax layer are used only for the purpose of learning the parameters for the embedding vector *(which turns
out to be the weight matrix for the hidden layer)* and has no purpose in and of itself after the model has been trained.</b>

We will be using the _**Skip-Gram**_ model which works on the principle that similar words occur in similar sentences and hence tend to have a similar
context. Given a specified context window it takes each target-context pair as a new observation. This tends to work better on large datasets as compared
to the Continuous Bag-of-Words (_**CBoW**_) model which treats the entire context as one observation. 
Here is a step-wise guide to help understand a single epoch of the skip-gram algorithm:</b>

1. Obtain a corpus of training data which basically means a bunch of sentences. Larger the corpus is greater the chances that the model picks up a
similarity between words. Hence a more accurate embedding matrix learnt.</b>
2. Create a vocabulary consisting of all words mentioned _(no repetitions)_ in the corpus and label them.</b>
3. Generate context-target pairs chosing a suitable sized context window.</b>
4. Chose number of embedding dimensions  (#emb) and randomly initialize weight matrices for the hidden layer and softmax output layer as follows:
    * hidden layer weight(W1) would have the dimensions- (#emb , vocabulary size)
    * output layer weight(W2) would have the dimensions- (vocabulary size , #emb)</b>
5. The input layer is a single one-hot vector corresponding to the 'context' word in the context-target pair. Hence it would have the dimensions (vocabulary_size,1)
![](https://github.com/Nishant11769/Nishant_Word2Vec/blob/master/Architecture.png)
6. The softmax layer outputs a (vocabulary_size,1) dimensional probability vector.</b>
7. Loss is computed using the softmax loss function w.r.t the target one-hot vector. Calculate the gradients- dW1, dW2 and modify the weights chosing a learning rate. </b>
8. The above steps are done for every context-target pair

**Great! Now that you have an intuitive, theoritical knowledge of the Word2Vec algorithm you are ready to understand
how it actually funtions. So check out the jupyter notebook I have made with the name 'Nishant_NLP_Word2Vec.ipynb' (Link:https://github.com/Nishant11769/Nishant_Word2Vec/blob/master/Nishant_NLP_Word2Vec.ipynb) and play around with the code** _(follow the guidelines given in the notebook if modifying to avoid errors)_</b></b>

### All The Best !! :smiley:


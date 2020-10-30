# SKIP-GRAM MODEL

The Skip-gram model architecture usually tries to achieve the reverse of what the CBOW model does.
It tries to predict the source context words (surrounding words) given a target word (the center word).
Considering our simple sentence from earlier, “the quick brown fox jumps over the lazy dog”. If we
used the CBOW model, we get pairs of (context_window, target_word)where if we consider a context
window of size 2, we have examples like ([quick, fox], brown), ([the, brown], quick), ([the, dog], lazy) and
so on. Now considering that the skip-gram model’s aim is to predict the context from the target word,
the model typically inverts the contexts and targets, and tries to predict each context word from 
its target word. Hence the task becomes to predict the context [quick, fox] given target word ‘brown’ or
[the, brown] given target word ‘quick’ and so on. Thus the model tries to predict the context_window
words based on the target_word.

Just like we discussed in the CBOW model, we need to model this Skip-gram architecture now as a deep learning classification model such that we take in the target word as our input and try to predict the context words.This becomes slightly complex since we have multiple words in our context. We simplify this further by breaking down each (target, context_words) pair into (target, context) pairs such that each context consists of only one word. Hence our dataset from earlier gets transformed into pairs like (brown, quick), (brown, fox), (quick, the), (quick, brown) and so on. But how to supervise or train the model to know what is contextual and what is not?

For this, we feed our skip-gram model pairs of (X, Y) where X is our input and Y is our label. We do this by using [(target, context), 1] pairs as positive input samples where target is our word of interest and context is a context word occurring near the target word and the positive label 1 indicates this is a contextually relevant pair. We also feed in [(target, random), 0] pairs as negative input samples where target is again our word of interest but random is just a randomly selected word from our vocabulary which has no context or association with our target word. Hence the negative label 0indicates this is a contextually irrelevant pair. We do this so that the model can then learn which pairs of words are contextually relevant and which are not and generate similar embeddings for semantically similar words.

## Implementing the Skip-gram Model
 
Let’s now try and implement this model from scratch to gain some perspective on how things work behind the scenes and also so that we can compare it with our implementation of the CBOW model. We will leverage our Bible corpus as usual which is contained in the norm_bible variable for training our model. The implementation will focus on five parts

- Build the corpus vocabulary
- Build a skip-gram [(target, context), relevancy] generator
- Build the skip-gram model architecture
- Train the Model
- Get Word Embeddings

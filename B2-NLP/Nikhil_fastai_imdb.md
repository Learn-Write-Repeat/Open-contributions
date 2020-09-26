
#  IMDB TEXT CLASSIFICATUION

First let's download the dataset we are going to study. The [dataset](http://ai.stanford.edu/~amaas/data/sentiment/) is derived from fastai datasets , which has been originally  curated by Andrew Maas et al. and contains a total of 100,000 reviews on IMDB.
 25,000 of them are labelled as positive and negative for training, another 25,000 are labelled for testing (in both cases they are highly polarized). The remaning 50,000 is an additional unlabelled data (but we will find a use for it nonetheless).

We'll begin with a sample data, so that things run quickly before going over the full dataset.

## data preprocessing

1. **Tokenization**: it takes those words and converts them into a standard form of tokens. Basically each token represents a word.

   But it does things like, see how "didn't" has been turned here into two separate words (`did` and `n't`)? And everything has been lowercased. See how "you're" has been turned into two separate words (`you` and `'re`)? So tokenization is trying to make sure that each "token" (i.e. each thing that we've got with spaces around it) represents a single linguistic concept. Also it finds words that are really rare (e.g. really rare names) and replaces them with a special token called unknown (`xxunk`). Anything's starting with `xx` in fastai is some special token. This is tokenization, so we end up with something where we've got a list of tokenized words. You'll also see that things like punctuation end up with spaces around them to make sure that they're separate tokens.

2. **Numericalization**: The next thing we do is we take a complete unique list of all of the possible tokens﹣ that's called the `vocab` which gets created for us.

   ```python
   data.vocab.itos[:10]
   ```

   ```
   ['xxunk', 'xxpad', 'the', ',', '.', 'and', 'a', 'of', 'to', 'is']
   ```

   So here is every possible token (the first ten of them) that appear in all of the movie reviews. We then replace every movie review with a list of numbers.

   ```python
   data.train_ds[0][0].data[:10]
   ```

   ```
   array([ 43,  44,  40,  34, 171,  62,   6, 352,   3,  47])
   ```

   The list of numbers simply says what numbered thing in the vocab is in this place.

So through tokenization and numericalization, this is the standard way in NLP of turning a document into a list of numbers.

We can do that with the data block API:

```
data = (TextList.from_csv(path, 'texts.csv', cols='text')
                .split_from_df(col=2)
                .label_from_df(cols=0)
                .databunch())
```

 This time, it's not ImageFilesList, it's TextList from a CSV and create a data bunch. At that point, we can start to create a model.

As we learn about it next week, when we do NLP classification, we actually create two models:

1. The first model is something called a **language model** which we train in a kind of a usual way.

   ```python
   learn = language_model_learner(data_lm, pretrained_model=URLs.WT103, drop_mult=0.3)
   ```

   We say we want to create a language model learner, train it, save it, and we unfreeze, train some more.

2. After we've created a language model, we fine-tune it to create the **classifier**. We create the data bunch of the classifier, create a learner, train it and we end up with some accuracy.

```
learn.fit_one_cycle(1, 2e-2, moms=(0.8,0.7))
```

```
Total time: 03:40
epoch	train_loss	valid_loss	accuracy
1	0.310078	0.197204	0.926960
```

```
learn.unfreeze()
learn.fit_one_cycle(2, slice(1e-3/(2.6**4),1e-3), moms=(0.8,0.7))
```

```
Total time: 15:17
epoch	train_loss	valid_loss	accuracy
1	0.240424	0.155204	0.943160
2	0.217462	0.153421	0.943960
```

```
learn.predict("I really loved that movie, it was awesome!")
```

```
(Category pos, tensor(1), tensor([7.5928e-04, 9.9924e-01]))
```
### About me:
#### <a href="https://www.linkedin.com/in/nikilreddybilla/">Nikhil Reddy </a> 
 
 <a href="https://twitter.com/neural_nets_">
  <img align="left" alt="Nikhil's Twitter" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg" />
</a>
<a href="https://www.linkedin.com/in/nikilreddybilla/">
  <img align="left" alt="Nikhil's Linkdein" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://github.com/nikhilreddybilla28">
  <img align="left" alt="Nikhil's Github" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" />
</a>
<a href="https://imultiarmedbandit.blogspot.com/">
  <img align="left" alt="Nikhil's blogspot" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/blogger.svg" />
</a>
<a href="https://medium.com/@icrypto1">
  <img align="left" alt="Nikhil's Medium" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/medium.svg" />
</a>

##### This work i did is inspired from JERMEY HOWARDS fastai MOOC.

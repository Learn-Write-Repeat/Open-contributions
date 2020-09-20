# PYTORCH OVERVIEW
Hey, fellas! Are you going to start a Deep Learning or NLP project with Python?You are looking for more pythonic tools and techniques to work with?
So this is for you.We, Hereby, will be discussing about the most used and fastest deep learning API/Library,Pytorch.
Over the past few years, there has been a huge surge in popularity for Pytorch.I guess some of you have heard of it or some of you may be not. But no need to worry i will start here from the scratch upto the model building and evaluation using just Pytorch and Python.

We will walkthrough Pytorch in three parts:
1.)Why Pytorch?
2.)What is Pytorch?
3.)How it is being implemented?

## Why Pytorch? 

So, let's first discuss the why part.

You might wondering there is already other deep learning options available within the Python ecosystem.Keras is a great choice for starting out and for quickly developing and iterating on models, pure Tensorflow is amazingly fast, and with the recent advent of Tensorflow 2.0, will only become more awesome.Then why on the earth we need another library, pytorch.

There are many reasons one should go for pytorch.Some of them are as follows:

* Pytorch is way more Pythonic than any other libraries.You will see , when we use Pytorch, we go as the python flow. It seems more like      we are just doing programming in python rather than just importing and using the inbuilt models.

* Pytorch is way faster than any of the other deep learning libraries, whether you run small or large neural networks.As we are doing end to end implemantions using Object Oriented Concepts,that makes it faster than Keras API, where it takes some extra time to load the models.

* We get to know our model better here as we build it our own from Forward Propagation, Backward Propagation upto model tunning.

* Writing new neural network modules, or interfacing with PyTorch’s Tensor API was designed to be straight-forward and with minimal abstractions.So,PyTorch is easier to learn and lighter to work with and hence, used widely for passion projects and rapid Protoypes as well. 
You can write new neural network layers in Python using the torch API or your favorite numpy based libraries such as SciPy.

* The memory usage in PyTorch is extremely efficient compared to Torch or some of the alternatives.

So i guess, all these reasons are enough to go with the pytorch.

Now we have our own reasons to use Pytorch , hence it is time to get basic understanding about it.
 
## What is Pytorch?

So, Pytorch is the Deep Learning open source library build by Facebook's AI Research lab(FAIR).PyTorch is based on the Torch library,used for applications such as computer vision and natural language processing.Although the Python interface is more polished and the primary focus of development along with that PyTorch also has a C++ interface.It is free and open-source software released under the Modified BSD license.As it is available as open source(everyone on the earth can use it without paying a penny).
A number of pieces of Deep Learning software are built on top of PyTorch, including Tesla Autopilot, Uber's Pyro, HuggingFace's Transformers,PyTorch Lightning, and Catalyst. 

PyTorch provides two high-level features:

* Tensor computing (like NumPy) with strong acceleration via graphics processing units (GPU).
* Deep neural networks built on a tape-based automatic differentiation system.


For more understanding on Pytorch, visit [here](https://en.wikipedia.org/wiki/PyTorch#cite_note-17)

## How to implement PyTorch

Now we have basic understaning about Pytorch, so it is time to get our hands dirty.Here i would like to introduce some of the main Pytorch concepts, and apply them to a common task in Natural Language Processin:Parts of Speech Tagging. 

I guess, you might familiar with the task.In case, if not, Parts of Speech  is the supervised learning task which attempts to understand the part of speech for each word from the text and classify these words accordingly.In English language we have 8 parts of speech:'Noun',Pronoun','Verb', 'Adjective','Adverb','Prepostions','Conjunctions'and 'Interjections'.But here we will be classifying the words into only some main categories:'Noun','Proper Noun','Pronoun','Adjective','Adverb','Determinates' and 'verb'. As these are the most important part of speech.

So the plan for us is to use this toy task as a means for learning about Pytorch. Let’s do it! 

Please refer to [this](https://github.com/KavishGoyal/Open-contributions/blob/master/B2-NLP/Kavish_NLP_PyTorch.ipynb) for the implementation part:
  

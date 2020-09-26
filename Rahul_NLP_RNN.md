## What is Recurrent neural networks (RNNs)? 

RNNs are a class of neural networks that allow previous outputs to be used as inputs while having hidden states.
Derived from feedforward neural networks, RNNs can use their internal state (memory) to process variable length sequences of inputs. This makes them applicable to tasks such as unsegmented, connected handwriting recognition or speech recognition.

![RNN](https://miro.medium.com/max/313/0*H2Qo1UKOXKfsZO8S.gif)

lets say we have some input say X and internally do cirten operations and get hidden states. Now we take these hidden states and input them to the next step. After repeating the same process we end up with the output state.

![RNN](https://pydeeplearning.weebly.com/uploads/9/8/4/2/98422174/rnn_orig.png)

![RNN](https://miro.medium.com/max/960/1*TqcA9EIUF-DGGTBhIx_qbQ.gif)

In the Gif above the input is represented by the red circle and the hidden state is represented by the blue circle and the output is given bu the black


### What is a sequence?

A sequence is a set of data which has some defined order to it

RNNs are very usefull because they can transform a sequence to a vector 
    
    f : Seq -> Vector
not just this RNNs can perform many such operations


## Why do we need to use Rnn? 

* Firstly RNNs are amazing because they can perform operation on sequence of data. There are many different architectures of RNNs and each used for different purpose.
* Model size does not increase with the size of input
* Weights are shared accross time
* Computation takes into account of previous data

#### RNN architecture: 
* One to One
* One to many
* Many to one 
* Many to Many
* Many to Many (sync)

![RNN_arch](https://miro.medium.com/max/2658/0*sm-7smnbyLioThPQ.png)

### One to One 

one to one is a typical neural networks. Here both i/p and o/p are in fixed length but we can work with sequences with RNNs

### One to Many

This type is generally used in Image captioning. i.e.. We have one image and want to describe what we see in the image 

### Many to One 

This is mainly used in the sentiment classification.... i.e.. If the comment is of positive sentiment or negetive sentiment

**I have implemented Many to One architecture in code using Pytorch with IMBD data set to do sentiment analysis**
and how I made the model is described with Markdown

### Many to Many 

This is generally used in Machine Translation. It has an input sequence and an output sequence 
Say you want to translate what is written in Japanese to English.

## What is Pytorch and Why is it used in NLP?

* PyTorch is an open source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing.
* It is built to be seamlessly integrated with Python and its popular libraries like NumPy. 
* It is comparatively easier to learn than other deep learning frameworks. This is because its syntax and application are similar to many conventional programming languages like Python


```python 
import torch.nn as nn

class RNN(nn.Module):
    def __init__(self, input_dim, embedding_dim, hidden_dim, output_dim):
        
        super().__init__()
        
        self.embedding = nn.Embedding(input_dim, embedding_dim)
        
        self.rnn = nn.RNN(embedding_dim, hidden_dim)
        
        self.fc = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, text):
        
        embedded = self.embedding(text)
        
        output, hidden = self.rnn(embedded)
        
        assert torch.equal(output[-1,:,:], hidden.squeeze(0))
        
        return self.fc(hidden.squeeze(0))
```
As you can see its this easy to implement a RNN model with pytorch

### Author 

Rahul Krishna [Linkedin](https://www.linkedin.com/in/rahul-krishna-75055b1a5/)

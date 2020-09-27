# Long Short-term Memory Network(LSTM)
---

## Introduction
LSTMs are a type of recurrent neural networks that specialise in the learning of dependencies in a sequence of words(sentences) or sequence of numbers. In simpler terms, let's take your brain as an example. You are able to understand the words you are currently reading because you have already encountered them before and know their meanings. In a similar fashion, LSTMs store the relationships between certain words in a sentence. For example, consider the following sentence:-

#### "I grew up in Portugal, and my native tongue is Portuguese"

The above sentence actually consists of 2 smaller sentences "I grew up in Portugal" and "My native tongue is Portuguese". The final word of the second sentence can be directly inferred from 'Portugal' in the previous sentence. That is, *Portuguese* is **dependent** on *Portugal*. There are many examples of such dependencies throughout the English language and such dependencies are learnt by LSTMs.

This reference relationship can be short that is a word can directly refer to the previous word or it can be long meaning it can refer a word that is 10 words down the line. Hence accounting for such a relationship can become very complex for processing patterns that the neural networks need to process

## Architecture
---
Let's take a look at the architectural differences between RNNs and LSTMs. This will help us get an idea of how LSTMs are able to handle long-term dependencies better than regular Recurrent Neural Networks.


##### Repeating Module in RNN

![Repeating module in RNN](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-SimpleRNN.png "Repeating Module in RNN")

##### Repeating Module in LSTM
![Repeating module in RNN](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-chain.png "Repeating Module in RNN")

It is pretty clear from the above figures that LSTM modules have a more complex structure. The RNN module has a single tanh layer. In LSTM module, instead of having a single layer there are four layers in the module interacting in a complex fashion. The key to LSTMs functionality is the cell state – the horizontal line running at the top of the LSTM module. The cell state is a path that carries information from the beginning to the end without causing any change to the information that it carries. The LSTM has the ability to add or remove information from this path with the help of special structures called gates.

### Types of Gates
#### Forget Gate
As the names suggests the gate decides on what information is to be forgotten and what information is retained. It is a function that outputs values between 0 and 1. The values closer to 0 tend to be forgotten whereas values closer to 1 tend to be retained.

![Forget Gate](https://miro.medium.com/max/700/1*GjehOa513_BgpDDP6Vkw2Q.gif)

#### Input Gate
LSTMs primarily work on a current cell state and a hidden state. The input gate is responsible for updating the current cell state of the LSTM. It decides which values need to be updated by assigning them values between 0(remains same) and 1(needs to be updated).
![Input Gate](https://miro.medium.com/max/700/1*TTmYy7Sy8uUXxUXfzmoKbA.gif)

#### Output Gate
Similar to how the input gate decides the current cell state the output gate decides the hidden cell state. The hidden cell state contains information from the previous input data. The output gate determines what portion of the hidden state is propagated to the next step along with the current cell state.
 
 ![Output Gate](https://miro.medium.com/max/700/1*VOXRGhOShoWWks6ouoDN3Q.gif)
 
 ## Code Demo
---
For better understanding of using LSTM in code, I have provided a code snippet illustrating LSTM architecture in PyTorch:

```
class LSTM(nn.Module):
    def __init__(self, input_size=1, hidden_layer_size=100, output_size=1): 
                                                                            
        super().__init__()
        self.hidden_layer_size = hidden_layer_size                          

        self.lstm = nn.LSTM(input_size, hidden_layer_size)

        self.linear = nn.Linear(hidden_layer_size, output_size)

        self.hidden_cell = (torch.zeros(1,1,self.hidden_layer_size),
                            torch.zeros(1,1,self.hidden_layer_size))       

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq) ,1, -1), self.hidden_cell)
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]
```
The LSTM layer is defined under the torch.nn module.
**input_size:** equals the number of features in the input(in the above example,1 ) 
**hidden_layer_size:** defines the number of neurons in the hidden layer of the network
**output_size:** equals the number of features in the output

The ```hidden_cell``` contains the previous hidden and cell state. It is initialized with all zero values. The ```forward() ``` method connects all the layers. It takes the input sequence and passes it to the ```lstm``` layer. The output of the ```lstm``` layer consists of the hidden, current cell state and output. The output  is given to the ```linear``` layer. The predicted values are then passed to the calling function. For the complete example you can visit [here](https://github.com/nrpu88/Open-contributions/blob/master/Nripesh_NLP_LSTM.ipynb). 

## Applications of LSTMs
---
Here are a few interesting applications of the LSTM networks:-
### 1. Machine Translation
![](https://analyticsindiamag.com/wp-content/uploads/2018/01/nural-network-02.jpg)
### 2. Image recognition and characterization
![](https://analyticsindiamag.com/wp-content/uploads/2018/01/RNN-ConNet-image-768x262.png)
### 3. Automatic Machine Translation
![](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/Instant-Visual-Translation.png)
### 4. Automatic Image Caption Generation
![](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/Automatic-Image-Caption-Generation.png)
### 5. Automatic colorization of Images
![](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/Colorization-of-Black-and-White-Photographs.png)
---
---
#### Nripesh Kumar
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/nripesh-kumar/)   [![GitHub](https://i.stack.imgur.com/tskMh.png) GitHub](https://github.com/nrpu88/nrpu88/edit/master/README.md)

# What is Subsampling ?
Language models assign probabilities to sequences of words. They are widely used in many natural language processing applications. 
The probability of a sequence can be modeled as a product of local probabilities as shown in<br><br>
<img src="http://www.sciweavers.org/tex2img.php?eq=P%28w1%2C%20w2%2C%20...%2C%20wl%29%3D%20%5Cprod_i%5El%20%20P%28wi%7Chi%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="P(w1, w2, ..., wl)= \prod_i^l  P(wi|hi)" width="257" height="53" /><br>
<br> 
### Where:
'wi' is the i<sup>th</sup> word, and <br>'hi' is the word history preceding 'wi'.<br>
'i' starts from 0.<br><br>
Therefore the task of language modeling reduces to estimating a set of conditional distributions {P(w|h)}.<br>
For complex models, this poses a computational challenge for learning, because the resulting objective functions are expensive to normalize.<br>
Subsampling is a simple solution to get around
the constraint of computing resources. For the purpose of language modeling, it amounts to taking only part of the text corpus to train the Language Model.
For complex models, it has been shown that subsampling can speed up training greatly, at the cost of some degradation in predictive performance, allowing for trade-off between computational cost and Language Model quality
## In Simple words:
Subsampling is also one of the techniques that we use when we are building word pairs which removes the most frequently used words.<br>
Generally thses words are:
* Prepositions (eg. of, on, for)
* Articles (a, an, the)
## Advantages of Subsampling are:
* Reduces the Training time for Model
* Reduces the bias of the model towards training data.
## Disadvantages of Subsampling are:
* Reduces the overall Model accuracy.

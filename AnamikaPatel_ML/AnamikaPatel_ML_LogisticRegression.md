# Logistic Regression

Logistic regression is named for the function used at the core to the method, the logistic funtion.The logistic function, also called the Sigmoid function was developed by statisticians to describe properties of population growth in ecology, rising quickly and maxing out at the carrying capacity of the environment. It’s an S-shaped curve that can take any real-valued number and map it into a value between 0 and 1, but never exactly at those limits.

1/(1+e^-x)

e is the base of the natural logarithms and x is value that you want to transform via the logistic function.

### Importing required libraries for implmenting Logistic Function
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
%matplotlib inline

print(np.__version__)
print(pd.__version__)
import sys
print(sys.version)
import sklearn
print(sklearn.__version__)
```
### Output: 
1.18.5
1.0.5
3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)]
0.23.1

### Ploting the graph :

```python
x = np.linspace(-6, 6, num = 1000)
plt.figure(figsize = (12,8))
plt.plot(x, 1 / (1 + np.exp(-x))); # Sigmoid Function
plt.title("Sigmoid Function");
```
<table align="center">
    <tr>
        <td><img src="https://github.com/anamikarpp/Open-contributions/blob/master/AnamikaPatel_ML/images/sigmoid.jpeg" width=600 height=200></td>
        
    </tr>
    <tr>
        <td><b>Sigmoid Function</b></td>
        
    </tr>
</table>

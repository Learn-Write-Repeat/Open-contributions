<h2>Introduction :- </h2>
The Machine Learning models can be divided into two groups –
<ol>
<li>Classfication Models - Classification is the task of predicting binary output either 0 or 1, here we have only two outputs.
<li>Regression Models - Regression is the task of predicting a continuous quantity, here we can have any arbitrary number (Eg. 21,33, -1.9)
</ol>
There are various classification models like Logistic Regression , K- Nearest Neighbour(Knn) ,Random Forest , Decision Tree , Support Vector Machine(SVM) etc , where Random Forest and Decision Tree are tree based methods
<h1><u><center>Support Vector Machine</center><u> </h1>
<img src="https://github.com/nilay121/Open-contributions/blob/master/svm4.png">
As shown above fig,the planes passing through the nearest points from the hyper plane are the marginal planes and those nearest points are the marginal points ,we have considered the circles as positive class(+1) and the stars as negative class (-1) , 
our main aim will be to maximise the distance between the two marginal planes as much as possible.<br>
w<sup>T</sup>x + b = -1   --------->(1)<br>
w<sup>T</sup>x + b = +1   --------->(2) <br>
(2) - (1) => w<sup>T</sup> (x<sub>2</sub>-x<sub>1</sub>) = 2	(x<sub>2</sub>,x<sub>1</sub> are marginal points of positive and negative marginal planes)<br>
(w<sup>T</sup> / |w|) (x<sub>2</sub>-x<sub>1</sub>) = 2 / |w|<br>
x<sub>2</sub>-x<sub>1</sub> = 2 / |w| <br>
we need to maximise this marginal distance or min(|w|<sup>2</sup>/2) 
So we can write, minimize (|w|2/2)  given the constraint yi*(w<sup>T</sup>x+b) − 1 >= 0 <br>
The above problem can be solved by langranges’ method of multipliers <br>
f(w,b) =  (|w|<sup>2</sup>/2)<br>
g(w,b) = yi*(w<sup>T</sup>x+b) -1 = 0<br>
L= f – λ*g	(λ is known as the langrange multiplier) -------->(4)<br>
Using equation (4) ,we find the respective values of ‘w’ and ‘b’<br><br>
<i>For prediction we can check the sign of (w<sup>T</sup>x+b)</i> <br>
<ul>
<li>If sign is +ve for a given set of data then we will classify the data point as +1
<li>If sign is -ve for a given set of data then we will classify the data point as -1
</ul>

  
<h3><u><center>What happens when the data is non-linear?</center><u> </h3>
<img src ="https://github.com/nilay121/Open-contributions/blob/master/svm1.png">
When the data is not linearly separable,then the concept of <b>Kernels</b> comes into play.<br>
<i>Kernels transforms the data from a lower dimension to a much higher dimension where we can easily draw a hyperplane separating the two classes.  </i><br><br>
<img src='https://github.com/nilay121/Open-contributions/blob/master/svm2.png'><br>
The various kernels in SVM includes the Gaussian kernel , Polynomial kernel, Radial Basis Function kernel, etc.<br>
<h2><u><center>Benefits of using SVM</center><u> </h2>
<ol>
<li>SVM can handle large feature sets very efficiently , the kernel trick in SVM is very powerful , however the design of kernels for specific problems is an active research field.
<li>SVM is firmly rooted in Statistical learning theory (i.e Statistics and functional analysis) and hence is competitive with efficiency Neural Networks (NNs) and Boosted Decision Trees (BDTs).
<li>SVM model takes less space for storing as they only need to store the marginal points (weight parameter) and the bias (b).
<li>SVM models are less effected by the presence of outliers.
</ol>
 <br><br>
<i>Contributed by Nilay Kushawaha</i>

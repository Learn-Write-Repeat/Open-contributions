# Concrete Compressive Strength Prediction using Machine Learning

Cement is one of the components of concrete. Mxixing of required substances in required amount produces concrete. The strenght of
concrete may be influenced by:
1. Ratio of cement to water
2. Size of aggregate
3. Texture, stifness of particles

In this project, we aim to determine the compressive strength of concrete given some data about cement.The data set
for this project is acquired from the [UCI ML repository](https://archive.ics.uci.edu/ml/datasets/concrete+compressive+strength)

The data set has the following attributes:
1.  Cement 
2.  Blast Furnace Slag 
3.  Fly Ash 
4.  Water 
5.  Superplasticizer 
6.  Coarse Aggregate 
7.  Fine Aggregate 
9.  Age 
10. Concrete compressive strength 

### Prerequisites
You should have the following softwares/libraries installed
```
Python3
Scikit-learn
Jupyter notebook
Scipy
Numpy
Pandas
Matplotlib
Seaborn
```

## Important Machine Learning Algorithms

Good understanding of the following algorithms is required.

### Linear regression

We aim to predict a target variable using some given data variables. What we can do is to pass a line from the data set fitting the data set as shown.
To generalise, you draw a straight line such that it crosses through the maximum points. Once we have done that, we can predict
the target value using that line as the hypothesis function.
![linear regression](https://www.researchgate.net/profile/Hieu_Tran33/publication/333457161/figure/fig3/AS:763959762247682@1559153609649/Linear-Regression-model-sample-illustration.ppm)

The only problem is how to define the parameters of line. Like how to get values of slop and intercept of
the line.
![linear regression intuition](https://miro.medium.com/max/656/1*4nBp-NeOFGBc-nNzP-VG3w.png)\
We can use calculus to get the minimum values of slope and intercept such that the line passes through
maximum number of points.\
[Link](https://en.wikipedia.org/wiki/Linear_regression#:~:text=In%20statistics%2C%20linear%20regression%20is,is%20called%20simple%20linear%20regression.)

We will not go into detailed mathematics because this note just provides intuition for the algorithms.\

###Polynomial Regression
Sometimes the line may not fit the data because of the data might have a polynomial nature. So a line won't be enough. For this we need to increase the degee of attibutes
(which can be using the scikit-learn library)\

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

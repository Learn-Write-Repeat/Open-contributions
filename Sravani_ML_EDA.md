### **What is Exploratory Data Analysis(EDA)?**

* It’s often the first step in data analysis, implemented before any other techniques. It is an approach for summarizing, visualizing, and becoming intimately familiar with the important characteristics of a data set.
* It consists techniques that are used to gain some insights on the dataset before doing any modeling.
* EDA, is essentially a type of storytelling for statisticians. It allows us to uncover patterns and insights, often with visual methods, within data.
* EDA is not a set of rules to follow, it is our state of mind. 

### **Purpose of EDA:**
* It is basically used to filter data from redundancies.
* It helps us to identify the faulty points in data and to understand the relationships between variables.
* Gain maximum insight into the data set and its underlying structure.
* Identify the most influential variables
* EDA is used to gain some statistics and perform visualizations for better understanding of data, and finds some information about the tendencies of the data, its quality and have some assumptions for the hypothesis test.
* EDA is NOT about making fancy visualizations or even aesthetically pleasing ones; the goal is to try and answer questions with data. 
* We should be able to create a figure which should be undersandable to others in a couple of seconds 
* EDA plays an important role in data analysis. We should always check the quality of data even if it provided in platter.
* Data Cleaning is an application of EDA where we can clarify our doubt if our data reaches the expectations or not.

#### Steps involved in EDA:
> Understand the data

> Clean the data

> Analysis of relationship between variables

### **Methods for exploratory data analysis:**
It is good to explore the data through various EDA techniques and compare them. Once the data set is fully understood, it is quite possible that data scientist will have to go back to data and cleansing phases in order to transform the data set according to the desired outcomes. 
###### Methods for EDA are:
*	**Univariate visualization :-** provides summary statistics for each field in the raw data set
*	**Bivariate visualization  :-** is performed to find the relationship between each variable in the dataset and the target variable of interest
*	**Multivariate visualization :-**  is performed to understand interactions between different fields in the dataset
*	**Dimensionality reduction :-**  helps to understand the fields in the data that account for the most variance between observations and allow for the processing of a reduced volume of data. 


Through these methods, the data scientist validates assumptions and identifies patterns that will allow for the understanding of the problem and model selection and validates that the data has been generated in the way it was expected to.


### **Is skipping Exploratory Data Analysis a good idea?**
NO,In a hurry to get to the machine learning stage or simply impress business stakeholders very fast, data scientists tend to either entirely skip the exploratory process or do a very shallow work. It is a very serious and, sadly, common mistake of amateur data science consulting “professionals”.

Such behaviour can lead to skewed data, with outliers and too many missing values and, therefore, some sad outcomes for the project:
* generating inaccurate models;
* generating accurate models on the wrong data;
* choosing the wrong variables for the model;
* inefficient use of the resources, including the rebuilding of the model.

There are a lot of ways to reach these goals as follows:
1.	Import the data
2.	Get a feel of the data ,describe the data,look at a sample of data like first and last rows
3.	Take a deeper look into the data by querying or indexing the data
4.	Identify features of interest
5.	Recognise the challenges posed by data - missing values, outliers
6.	Discover patterns in the data

>One of the important things about EDA is Data profiling.

**Data profiling**  is concerned with summarizing your dataset through descriptive statistics. The goal of data profiling is to have a understanding of the data so that you can start querying and visualizing the data in various ways. Depending on the result of the data profiling, you might decide to correct, discard or handle your data differently.


### **Visualizing data**
* Data visualization is the graphical representation of data.  It contains statistical graphics, plots, information graphics and many more to explore the data easily.
* Your goal should be to be able to create a figure which someone can look at in a couple of seconds and understand what is going on. 
* If not, the visualization is too complicated (or fancy) and something similar should be used.
* EDA is also very iterative since we first make assumptions based on our first exploratory visualizations, then build some models. 
* We then make visualizations of the model results and tune our models.


***Summary Statistics:***
 >•	*Summary statistics are measurements meant to describe data. Examples of summary/ descriptive statistics for a single numerical variable is the mean, median, mode, max, min, range, quartiles/percentiles, variance, standard deviation, coefficient of determination, skewness and kurtosis.* 
>•	*Summary statistics for categorical variables is the number of distinct counts.The most basic summary statistic for text data is term frequency and inverse document frequency.For bivariate data, the summary statistics is the linear correlation, chi-squared, or the p value based z-test, t-test or analysis of variance.*


* In addition to summary statistics, visualizations can be used to explore and describe data. 
* Examples of visualizations for numeric data are line charts with error bars, histograms, box and whisker plots, for categorical data bar charts and waffle charts, and for bivariate data are scatter charts or combination charts.


Some examples of plots used for EDA are:

* Histograms
* Scatter plots
* Pair plots
* Box plots
* Violin plots
* Distribution Plots

### **Histograms:** 
*	It is used in univariate analysis, they give a rough sense of density of underlying distribution of data more precisely probability distribution of data. 
*	The plotting of the histogram depends upon ‘bins’ i.e dividing the entire range into series of interval then based upon the number of values present inside a range of a bin the height of the bar of that bin is determined.
![](https://www.mathworks.com/help/examples/matlab/win64/ChangeNumberOfHistogramBinsExample_03.png)

### **Scatter plot:**
*	A scatter plot is a type of plot which uses X and Y coordinates on a 2d plane to display points. 
*	It is a well known plotting technique to study the interdependence of one variable over other.
![](https://lh3.googleusercontent.com/proxy/z-R0-szEidUIGzSg9y2_rMpn0YlszPtp4e36r2iLKCDOjGsE6YTEWZNXN5j-WRBxdnG26wLccwk9YU2OJdd9cDiCg5pAU8LxZCfI4-YmXHncW05dlDeyBw)

### **PairPlot:**
*	This is a extension to scatter plots and histogram and its PDF representation. 
*	This is primarily used when we want to study the behavior of all variables with every other variables when the data is more than 2-Dimension.
![](https://i.stack.imgur.com/b6JdS.png)

### **Boxplot:**
*	These are fairly complex types of plots ,these are used to represent data according to their quartiles. 
*	They also have lines extending vertically from the boxes indicating the variance outside the upper and lower quartile .
*	The Space between different parts of the box indicate the variance(Spread) of the data. 
*	It also helps in detection of outliers
![](https://miro.medium.com/max/18000/1*2c21SkzJMf3frPXPAR_gZA.png)

### **Voilon Plot:**
*	It is a extension of box plots in this the kernel density plot is also plotted with box plots .
*	A violin plot is better than a plain box plot as a box plot only shows summary statistics such as mean/median and interquartile ranges, the violin plot shows the full distribution of the data.
![](https://images.ctfassets.net/fi0zmnwlsnja/sdfgtcRp16wTNOcRceGQm/5bfcb73d2261d49ff20dd7857e0152b1/Screen_Shot_2019-03-01_at_11.36.10_AM.png)

### **Distribution plots:**
*	These plots are used to know distribution of attributes whether they are normally distributed or skewed distributed. 
*	You can select multiple feature distributions and compare them side by side that is the beauty of plotly very interactive.
![](https://support.minitab.com/en-us/minitab-express/1/distribution_plot_normal_vary_parameters.xml_Graph_cmd1o1.png)






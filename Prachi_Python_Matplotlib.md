# **Matplotlib**

***What is matplotlib?***

Matplotlib is a library in python programming language.
We need to import this library using 'import' , before using it's features.

***Use of matplotlib:***

Matplotlib is a library in python. It helps in embedding plots.
Whenever we want to plot a agraph in python we use this library.

***Some types of graphs we can draw using matplotlib:***

1.Line plot<br>
2.Bar plot<br>
3.Histogram<br>
4.Scatter-plot<br>
5.Pie-chart<br>
6.Contour plot:<br>
7.Box plot<br>
8.Working with images<br>

First we need to install matplotlib using 'pip' command.<br>
Use the following command in the terminal:<br>
pip install matplotlib<br>

**Importing matplotlib:** <br>

import matplotlib.pyplot as plt<br>
This imports the matplotlib library to be used for plotting.<br>

<p>

<img src="https://user-images.githubusercontent.com/49331074/93016552-c3389980-f5df-11ea-9339-c2058cce1192.JPG">
**Parts of a figure.**

*Axes:*<br>
This is what you think of as 'a plot', it is the region of the image with the data space. 
A given figure can contain many Axes, but a given Axes object can only be in one Figure. 
The Axes contains two (or three in the case of 3D) Axis objects (be aware of the difference between Axes and Axis) 
which take care of the data limits (the data limits can also be controlled via the axes.Axes.set_xlim() and axes.Axes.set_ylim() methods). 
Each Axes has a title (set via set_title()), an x-label (set via set_xlabel()), and a y-label set via set_ylabel()).

The Axes class and its member functions are the primary entry point to working with the OO interface.

*Axis:*<br>
These are the number-line-like objects.
They take care of setting the graph limits and generating the ticks (the marks on the axis) and ticklabels (strings labeling the ticks).
The location of the ticks is determined by a Locator object and the ticklabel strings are formatted by a Formatter.
The combination of the correct Locator and Formatter gives very fine control over the tick locations and labels.

*Artist:*<br>
Basically everything you can see on the figure is an artist (even the Figure, Axes, and Axis objects).
This includes Text objects, Line2D objects, collections objects, Patch objects ... (you get the idea). 
When the figure is rendered, all of the artists are drawn to the canvas. Most Artists are tied to an Axes; 
such an Artist cannot be shared by multiple Axes, or moved from one to another.

</p>

<ul>
<li>An empty figure with no Axes</li>
</ul>

fig = plt.figure()
<br>
Output:<Figure size 432x288 with 0 Axes>
<br>

<ul>
<li>A figure with a single Axes</li>
</ul>

fig, ax = plt.subplots() 
<br>
Output:
<img src="https://user-images.githubusercontent.com/49331074/93016734-0e9f7780-f5e1-11ea-8943-86013a7c146c.JPG">
<br>
<p>

1.**Line graph:**

Steps we follow to draw this graph:<br>

1.First, we define the x-axis and the y-axis values as lists.<br>
2.Using .plot() we plot the graph<br>
3.If we want , we can name the x-axis and the y-axis.<br>
4.We can also give a title to our graph.<br>
5.We use .show() to view our graph<br>

Example:<br>

1.<br>
<img src="https://user-images.githubusercontent.com/49331074/93016812-840b4800-f5e1-11ea-9f8e-7402fe761fd1.JPG">
<br>
<img src="https://user-images.githubusercontent.com/49331074/93016857-da788680-f5e1-11ea-857a-620a56479a08.JPG">
<br>
2.
<br><img src="https://user-images.githubusercontent.com/49331074/93016992-13652b00-f5e3-11ea-85a9-4f2ca39a5809.JPG">
<br>
<img src="https://user-images.githubusercontent.com/49331074/93016996-16601b80-f5e3-11ea-83c8-fc79e8652734.JPG">
<br>
**Two or more lines on same graph:**

Example:<br>
3.
<br><img src="https://user-images.githubusercontent.com/49331074/93016936-799d7e00-f5e2-11ea-8264-15f716437089.JPG">
<br>
<img src="https://user-images.githubusercontent.com/49331074/93016954-98037980-f5e2-11ea-9744-a767f5b63902.JPG">
<br>
4.<br><img src="https://user-images.githubusercontent.com/49331074/93016955-99cd3d00-f5e2-11ea-8c43-0557e5dde87b.JPG">
<br>
<img src="https://user-images.githubusercontent.com/49331074/93016957-9cc82d80-f5e2-11ea-8861-e06c23985bc7.JPG">
<br>
Here, we plot two lines on same graph. We differentiate between them by giving them a name(label) which is passed as an argument of .plot() function.
The small rectangular box giving information about type of line and its color is called legend. We can add a legend to our plot using .legend() function.
<br>
5.<br>x = [1,2,3] <br>
y = [2,4,6] <br>
<br>
plt.plot(x, y, label = "line1") <br>
<br>
x1 = [1,2,3] <br>
y1 = [4,8,3] <br>
<br>
plt.plot(x1, y1, label = "line2") <br>
<br>
plt.xlabel('x-axis') <br>
<br>
plt.ylabel('y-axis') <br>
<br>
plt.title('Two lines on one graph') <br>
<br>
plt.legend() <br>
<br>
plt.show() <br>
<br>
Output:<br>
<img src="https://user-images.githubusercontent.com/49331074/93017128-d6e5ff00-f5e3-11ea-83ed-1200afbbc722.JPG">
<br>
<img src="https://user-images.githubusercontent.com/49331074/93017156-14e32300-f5e4-11ea-82d8-1aebed7a20ed.JPG">
</p>

<ul><li><b>Bar Chart</b></li></ul>
To draw bar charts we use, plt.bar() function.<br>
We pass x-coordinates along with the required heights.
We can give names to x-axis coordinates.
<br>
Syntax:<br>
matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
<br>
<br>
<ul>
<li>The bars are at position x.</li>
<li>Height refers to the height of the bars.</li>
<li>We can pass the same height for all the bars , or , pass a list of different heights for each bars.</li>
<li>'align' is the alignment of the bars with the x-axis.</li>
<li>'center': Center the base on the x positions.</li>
<li>'edge': Align the left edges of the bars with the x positions.</li>
<li>We can add colours to the face of the bars as well as to the edges of the bars.</li>
<li>We can give linewidth of the bar.</li>
<li>If we put the linewidth to be 0 , then their won't be any bar edge.</li>
<li>We can provide tick_labels.</li>
<li>The default value of bottom is 0.</li>
</ul>
<br>
6.
<br>
x = [15,82,33,6,95] <br>
 <br>
y = [27,48,69,32,0] <br>
<br>
plt.bar(x,y) <br>
<br>
plt.show() <br>
<br>
Output:
<br>
<img src="https://user-images.githubusercontent.com/49331074/93017435-5ffe3580-f5e6-11ea-8631-56bf9c989323.JPG">
<br>
7.<br>
x = [5,2,3,6,9] <br>
 <br>
y = [27,48,69,32,100]  <br>
 <br>
plt.bar(x,y)  <br>
 <br>
plt.show()  <br>
<br>
Output: <br>
<br>
<img src="https://user-images.githubusercontent.com/49331074/93017495-d733c980-f5e6-11ea-815c-a50a9f5f33bf.JPG">
 <br>
 8.
 <br>
import matplotlib.pyplot as plt 
 <br>

 <br>
x = [1, 2, 3, 4, 5] 
 <br>
 <br>
 
h = [10, 24, 36, 40, 5] 
 <br>
 <br>

tick_label = ['one', 'two', 'three', 'four', 'five'] 
 <br>
 <br>

plt.bar(x, h, tick_label = tick_label, width = 0.6, color = ['blue', 'black']) 
 <br>
 <br>
 
plt.xlabel('x-axis') 
 <br>
 <br>

plt.ylabel('y-axis') 
 <br>
 <br>

plt.title('Bar graph!') 
 <br>
 <br>

plt.show() 
 <br>
 <br>
 Output:
 
 <br>
 <img src="https://user-images.githubusercontent.com/49331074/93017498-dd29aa80-f5e6-11ea-9445-570faf1ec794.JPG">
 
 <br>
 This is how we add colour to our bar graph.
 <br>
 
 <ul><li>Histogram</li></ul>
 
 To draw a histogram we use, matplotlib.pyplot.hist.
 <br>
 Syntax:<br>
 matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwargs)
 <br>
 x: it takes an array or a sequence if array.
 <br>
 bins : bins defines the number of equal width bins in the the given range.
 <br>
 range:The lower and upper range of the bins.
 <br>
 density: It is a boolean value , and its default is False. If it is True,it draws and returns a probability density.
 <br>
 weights: array-like or None, default: None
 <br>
 9.
 <br>y = [27,48,69,32,0] <br>
<br>
plt.hist(y) <br>
<br>

plt.show() <br>
<br>


 
 
 

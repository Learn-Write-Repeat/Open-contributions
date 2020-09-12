<h1>Modules in Python</h1>
<p>Module can be termed as a file containing a set of functions,classesor variables. Grouping related code into a module
makes it easy to keep a track of the code. </p>
<p>In real time scenarios,It is really a tedious task to write the complete code of a project in a single file.
Therefore, the project can be fragmented into various modules, which facilitates the user to keep track of the code
and eases the task to correct the errors if any.</p>

<h2>Built-in Modules</h2>
<p> Modules which are already a part of python programming language and can be readily imported into python files are 
known as Built-in modules.</p>
<h3>Examples:</h3>&nbsp; <i> Platform,OS,SYS,RANDOM,etc.
<ul><li>OS:</li>OS module is a python module that helps us to perform many operating system related tasks. The OS module in Python provides functions
for creating, removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
<h4>Example</h4>
Import OS<br>
os.mkdir(‘C:\\Users\\gayat\\Desktop\\module’)<br>
os.rmdir(‘C:\\Users\\gayat\\Desktop\\module’’)<br><br>
<i>This will create a directory named module on desktop</i><br><br>

<li>Statistics:</li></ul>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The statistics module provides us the functions to handle statistics of numeric data. These functions include:<br>
<ul><li>Mean()</li><li>Median()</li><li>Mode()</li><li>stdev()</li></ul>
<h4>Example</h4>

import statistics as st<br>
List1=[1,2,3,4,5,6,6,3,2,4]<br>
print(st.mean(list1))<br>
print(st.median(list1))<br>
print(st.mode(list1))<br>
print(st.stdev(list1))

<h5>Output:</h5>&nbsp mean<br>
                      median<br>
                      mode<br>
                      stdev

                      
                      


<h2>Creating a Module</h2>
<p>A module can be created by saving the code you want in a file with .py extension. Any name can be given to the module.</p>
<h3>Example</h3>
<table border="1"><tr><th>goodmorning.py</th></tr><tr><td>def goodmorningmsg(name):<br>
&nbsp;&nbsp;print("Good Morning,"+name)</td></tr></table><br>
<p>Use a keyword <i>"import"</i> to import the module into the current workspace.</p>
<table border="1"><tr><th>mainmod.py</th></tr><tr><td>import goodmorning<br>
goodmorning.goodmorningmsg("John")</td></tr></table><br>
<h5>Output:</h5>&nbsp;Good Morning,John<br>
<h2>Alias name or re-naming a module</h2>
<p>It is used to create an alias name for the module.</p>
<h3>Example</h3>
import goodmorning as gm
a=gm.goodmorningmsg("John")
print(a)<br>
<table border="1"><tr><th>goodmorning.py</th></tr><tr><td>def goodmorningmsg(name):<br>
&nbsp;&nbsp;print("Good Morning,"+name)</td></tr></table><br>
<table border="1"><tr><th>mainmod.py</th></tr><tr><td>import goodmorning<br>
goodmorning.goodmorningmsg("John")</td></tr></table><br>

<h5>Output:</h5>&nbsp;Good Morning,John<br>

<h2>from import Statement</h2>
<table><tr><th>Syntax</th></tr><tr><td>from modulename import name1[,name2[,name3..]]</td></tr></table><br>
<h3>Example</h3>
<table border="1"><tr><th>greetings.py</th></tr><tr><td>def greetings(name):<br>
&nbsp;&nbsp;print("Hello How are you?," +name)<br>student1={"name":John,"age":20,"id":33}</td></tr></table><br>
<table border="1"><tr><th>mainmod1.py</th></tr><tr><td>from greetings import student1 <br>
print(student["id"])</td></tr></table><br>
<h5>Output:</h5>&nbsp;Hello How are you?,John<br>
<h2>To display a list of available modules</h2>
<p>Type the following command in the python module.</p><br>
<i>>>>help('modules')</i>
<h5>Output</h5>




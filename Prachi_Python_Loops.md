# **Loops:**

***What are Loops?***

Loops have set of statements which are executed until the condition becomes false.<br> Loops are used for iteration over a sequence of statements.<br>
We can use loops to iterate over lists, tuples, sets, dictionaries.<br>
We can iterate over a string too as it has set of characters.


***Need of Loops?***

Let us consider a very basic example to understand the need of loops.<br>
<br>
Suppose we want to print numbers from 1 to 100,<br> either we can print them by writing a print statement for each of them,<br>or we can use iteration of print statement.<br>
So, we will be using only one print statement and iterate over that to print our values.<br>Thus , loops makes our code efficient and our life easier . 


***Types of loops in python***

Their are two types of loops in python:<br>
1.for loop<br>
2.while loop<br>

***Let's take a look at both types of loops:***

**1.for loop:**

Flowchart of for loop:<br>
<img src="https://user-images.githubusercontent.com/49331074/92987469-3b1f9a80-f4e0-11ea-961c-943aec38f294.jpg">
Till the time the expression has a value and the conditions are satisfied for loop is executed , when the expression has reached it's last value , the control comes out of for loop.</br>
<br>We will see how for loop is used for lists, tuples, dictionaries , sets and numbers.

<ul>
<li><b><i>For loop for lists</i></b></li>
<br>
Let us understand via an example:<br>
<br>
<b><i>Example 1:</i></b><br>
fruits=["dragonfruit","custard apple","mango"] &emsp;#list<br>
for i in fruits:  &emsp;<br>
    &emsp; print(i) &emsp; <br>

<b><i>Output:</i> </b><br>
dragonfruit<br>
custard apple<br>
mango<br>
<br>
Here , we are iterating over the list of name fruits.
First time 'i' takes the value of fruits[0] , next time i=fruits[1] , and finally i becomes fruits[2].
And , inside the loop we are printing 'i'. So, the values of the list is printed one by one.
<br>
<br>
<b><i>Example 2:</i></b><br>
shapes=["triangle","square","rectangle"]<br>
for s in shapes:<br>
&emsp; print(s)<br>
<br>
<b><i>Output:</i> </b><br>
&emsp;triangle<br>
&emsp;square<br>
&emsp;rectangle<br>

This is another similar example. Again , we are taking the values of the list and printing it one by one by iterating over the lists.
<br><br>
<li><b><i>For loop for tuples</i></b></li>
<br>
Let us understand via an example:<br>
<br>
<b><i>Example:</i></b><br>
<br>
colours=("blue","yellow","red")<br>
for c in colours:<br>
&emsp; print(c)<br>
<br>
<b><i>Output:</i> </b><br>
&emsp;blue<br>
&emsp;yellow<br>
&emsp;red<br>
<br>
Here , colours is a tuple. 
We are iterating ober a tuple.
Each time the value of c changes with each iteraton and the new value is printed.
Firstly , c is "blue".
After the first iteration the value of c becomes "red".
After the second iteration the value of c becomes "yellow".
And in each iteration the value of c is printed.
<br>
This , is how we iterate over a tuple.<br>
<br>
<li><b><i>For loop for sets</i></b></li>
<br>
Let us understand via an example:<br>
<br>
<b><i>Example:</i></b><br>
<br>
sets={1,5,11,8}<br>
for c in sets:<br>
&emsp; print(c)<br>
<br>
<b><i>Output:</i> </b><br>
&emsp;1<br>
&emsp;5<br>
&emsp;11<br>
&emsp;8<br>
<br>
Here sets is the set we are iterating over.Each time c takes the value of sets and prints it.This is how we use set in for loop.
<br>
<li><b><i>For loop for dictionaries</i></b></li>
<br>
Let us understand via an example:<br>
<br>
<b><i>Example:</i></b><br>
<br>
dicts={"name":"Prachi","year":"1998","cgpa":"9.23"}<br>
for keys in dicts:<br>
&emsp; print(keys)<br>
<br>
<b><i>Output:</i> </b><br>
&emsp;name<br>
&emsp;year<br>
&emsp;cgpa1<br>
<br>
In each iteration keys takes the values of key in dict and prints the same.

# Functions in Python
<h2>Definition:</h2>
Function is a block of code or set of statements that performs a specific task and executes only when called.
Complex projects can be broken down into smaller tasks.These small tasks can contain multiple lines of code and can be used multiple times in the same program.
<table>
<tr>
<th>Syntax</th>
 <th>Example</th>
</tr>
<tr>
<td>def function-name():</td>
  <td>def palindrome():</td>
</tr>
</table>
<h3>In the above syntax:</h3><br>
<b>def</b> - to declare/define the function<br>
<b>function-name</b>- name of the function<br>
<b>()</b> - required to distinguish between a variable and function and end the definition with a semi-colon<br>
<h3>Example</h3><br>
def greet():<br>            
&nbsp;&nbsp;print("Hello")
&nbsp;&nbsp;print("Im a student")<br><br><br>

greet()-------------> Call the function to print the output<br><br>

<i>Using the above function you can print the greet message multiple times by just calling the function multiple times instead of making the code redundant.</i>



<h3>There are two basic types of Functions:</h3><br>
<ul><li>Built-in Functions</li>
<li>User Defined Functions</li></ul>
<h2>Built-in Functions:</h2><br>
Built-in functions are part of Python language.These are the functions readily available for the use.
<h3>Examples</h3>
<table>
<tr>
<th>Function</th>
  <th>Description</th>
</tr>
<tr>
  <td>max()</td>
<td>Returns the largest item in an iterable</td>
</tr>
  <tr>
  <td>min()</td>
<td>Returns the smallest item in an iterable</td>
</tr>
  <tr>
  <td>input()</td>
<td>To accept the input from the user</td>
</tr>
  </table>
  
  

<h2>User defined Functions:</h2><br>
User defined functions are not in-built and are not a part of Python programming language.Any name can be given to the function.These are the functions are defined according to the need of the user to carry out the tasks.
<h3>Examples</h3>
<table>
<tr>
<th>Function</th>
  <th>Description</th>
</tr>
<tr>
  <td>def sub(x,y):<br>
        &nbsp; diff=x-y<br>
        &nbsp; print(diff)<br><br>
    sub(7,4)</td>
  <td>Prints the difference between two numbers</td>
</tr>
  </table>
  
  
<h2> Functions can return values</h2><br>
When does a function return a value?<br>
Consider the given two scenarios:<br>
<ol><li>Hey Sohal, Please inform boss that I'll be late to the office today.</li>
  <li>Hey Sohal, May i know when does the meeting start?</li></ol><br>
  Clearly in the first scenario,The speaker is just asking his friend Sohal to inform his boss that he will be late todayBut, he's not expecting a reply. He is just informing.
  Whereas in the second case, the speaker is asking his friend about the meeting time. Therefore he's expecting a reply in return. <br>
  In a similar way, the functions will also return the values required after the computation. It can be clearly explained by the below provided example.<br>
  <h3>Example:</h3><br>
  def add(x,y):
  &nbsp;&nbsp;c=x+y
 &nbsp;&nbsp; return c<br><br><br>
 result=add(5,4)
 print(result)<br>
 <b>Output:</b>9<br>
 In the above example, the value returned by the function stores in the variable <i>"result"</i> and the desired output is printed on the console.<br>
 <h3>Function returning two values:</h3>
 A function can return two values in a similar way as the first one, but two variables have to be initialized to store the two values returned by the function after computation.<br>
 <h4>Example</h4>
 def add_sub(x,y):
  &nbsp;&nbsp;c=x+y
  &nbsp;&nbsp;d=x-y;
 &nbsp;&nbsp; return c,d<br><br><br>
 result1,result2=add_sub(5,4)
 print(result1,result2)
 
 <h2>Function Arguments</h2>
 
 
  def add(x,y):
  &nbsp;&nbsp;c=x+y
 &nbsp;&nbsp;print(c)<br><br><br>
 add(5,4)<br><br>

In the above code, the variables <i>x</i> and <i>y</i> are <b>Formal arguments</b> and numbers <i>5</i>,<i>4</i> are <b>Actual Arguments<br>
  <h3>Types of Function Arguments:</h3><br>
  <ul><li>Position Arguments</li><li>Keyword Arguments</li><li>Default Arguments</li><li>Variable Length Arguments</li><li>Keyworded Variable Length Arguments</li></ul><br>
  <h3>Position Arguments</h3><br>
  <h4>Example:</h4><br>
  def student(name,age):
  &nbsp;&nbsp;print(name)
  &nbsp;&nbsp;print(age)<br><br>
  person('paul',28)<br>
  <i>Output:</i>&nbsp;paul<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28<br>
  In the above example <i>'paul'</i> and <i>28</i> were passed as actual arguments

  
  
  
  
  
  
 
    
    
  
 
 
 
 
 
 
 
  


  
 
  
  




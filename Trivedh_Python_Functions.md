# Functions in Python
<h2>Definition:</h2>
Function is a block of code or set of statements that performs a specific task and executes only when called.
Complex projects can be broken down into smaller tasks.These small tasks can contain multiple lines of code and can be used multiple times in the same program.<br>
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
<h3>In the above syntax:</h3>
<b>def</b> - to declare/define the function<br>
<b>function-name</b>- name of the function<br>
<b>()</b> - required to distinguish between a variable and function and end the definition with a semi-colon<br>
<h3>Example</h3>
def greet():<br>            
&nbsp;&nbsp;print("Hello")<br>
&nbsp;&nbsp;print("Im a student")<br><br>

greet()-------------> Call the function to print the output<br><br>

<i>Using the above function you can print the greet message multiple times by just calling the function multiple times instead of making the code redundant.</i>



<h3>There are two basic types of Functions:</h3>
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
  
  
<h2> Functions can return values</h2>
<h4>When does a function return a value?</h4><br>
Consider the given two scenarios:<br>
<ol><li>Hey Sohal, Please inform boss that I'll be late to the office today.</li>
  <li>Hey Sohal, May i know when does the meeting start?</li></ol><br>
 <i><p> Clearly in the first scenario,The speaker is just asking his friend Sohal to inform his boss that he will be late today. But, he's not expecting a reply. He is just informing.
  Whereas in the second case, the speaker is asking his friend about the meeting time. Therefore he's expecting a reply in return. <br>
  In a similar way, the functions will also return the values required after the computation. It can be clearly explained by the below provided example.</i></p><br>
  <h3>Example:</h3>
  def add(x,y):<br>
  &nbsp;&nbsp;c=x+y<br>
 &nbsp;&nbsp; return c<br><br>
 result=add(5,4)
 print(result)<br><br>
 <b>Output:</b>&nbsp;9<br>
 In the above example, the value returned by the function stores in the variable <i>"result"</i> and the desired output is printed on the console.<br>
 <h3>Function returning two values:</h3>
 A function can return two values in a similar way as the first one, but two variables have to be initialized to store the two values returned by the function after computation.<br>
 <h4>Example</h4>
 def add_sub(x,y):<br>
  &nbsp;&nbsp;c=x+y<br>
  &nbsp;&nbsp;d=x-y;<br>
 &nbsp;&nbsp;return c,d<br><br>
 result1,result2=add_sub(5,4)<br>
 print(result1,result2)
 
 <h2>Function Arguments</h2>
 Arguments are used to feed nformation to the functions i.e to pass the information. Any number of arguments can be passed. They are declared inside the parenthesis after the function name.
 <h3>Example:</h3>
  def add(x,y):<br>
  &nbsp;&nbsp;c=x+y<br>
 &nbsp;&nbsp;print(c)<br><br>
 add(5,4)<br><br>

In the above code, the variables <i>x</i> and <i>y</i> are <b>Formal arguments</b> and numbers <i>5</i>,<i>4</i> are <b>Actual Arguments<br>
  <h3>Types of Function Arguments:</h3><br>
  <ul><li>Position Arguments</li><li>Keyword Arguments</li><li>Default Arguments</li><li>Variable Length Arguments</li><li>Keyworded Variable Length Arguments</li></ul><br>
  <h3>Position Arguments</h3><br>
<p> Positional Arguments are the arguments passed in a positional/sequential order. The number of arguments passed should match the function definitions. If the arguments are passed in a non-sequential order, then function computation will throw an error.</p>
  <h4>Example:</h4>
  def student(name,age):<br>
  &nbsp;&nbsp;print(name)<br>
  &nbsp;&nbsp;print(age)<br><br>
  student('paul',28)<br><br>
  <i>Output:</i>&nbsp;paul<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28<br>
  In the above example <i>'paul'</i> and <i>28</i> were passed as actual arguments and they were assigned to the formal arguments in the declared function without an error,as they were passed in a sequential order.
 
 
  <h3>Keyword Arguments</h3><br>
<p> Keyword Arguments are used in the function calls which passes the arguments along with a keyword. This facilitates the user to pass the arguments in a non positional order.If the sequence of the arguments is not known, keyword arguments can be used in a function call.</p>
  <h4>Example:</h4>
  def student(name,age):<br>
  &nbsp;&nbsp;print(name)<br>
  &nbsp;&nbsp;print(age)<br><br>
  student(age=28,name='paul')<br>
  <i>Output:</i>&nbsp;paul<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;28<br>
  
 <h3>Default Arguments</h3><br>
<p> It's a type of argument which assumes a default value if a particular value is not mentioned in the function call.If a user does'nt provide a particular argument the default value in the function definition will be assigned autonomously to the that particular argument.</p>
  <h4>Example:</h4>
  def student(name,age=18):
  &nbsp;&nbsp;print(name)<br>
  &nbsp;&nbsp;print(age)<br><br>
  student('paul')<br>
  <i>Output:</i>&nbsp;paul<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;18<br>
  
   <h3>Variable Length Arguments</h3><br>
<p> Variable Arguments are the arguments used in the function calls when a function has to compute more arguments than the arguments in the function definition or the accuracte value of arguments is not known.They are not named like Default or positional arguments.They are named withan asterisk before the variable-name that holds multiple or nonkeyword arguments.</p>
  <h4>Example:</h4>
  def student(a,*b):
  &nbsp;&nbsp;c=a;<br>
  &nbsp;&nbsp;for i in b:<br>
  &nbsp;&nbsp;&nbsp;c=c+i<br>
  &nbsp;&nbsp;print(c)<br><br>
  sum(5,6,34,78)<br><br>
  
  <i>Output:</i>&nbsp;123<br>
  
 <h2>Recursion</h2>
 <p>Recursion is a process of calling a function from the same function repeatedly. It means a defined function can call itself. It reduces the complexity of a program.</p>
 <h3>Example: Factorial using Recursion</h3><br>
 def fact(n):<br>
 &nbsp;&nbsp;if n==0:<br>
 &nbsp;&nbsp;&nbsp;return 1<br>
 &nbsp;&nbsp;return n*fact(n-1)<br>
 result=fact(5)<br>
 print(result)<br><br>
 <b>Output:</b>&nbsp;120
 
 <h2>Lamba or Anonymous Function</h2>
 <p> As the name suggests, these are the functions without any name.It's a kind of function, which is not defined in an usual manner with <i>def</i>.  Lamba function returns only a single value. It can accept any number of arguments.It has to be assigned to a variable</p>
 <h3>Example 1</h3>
 f = lambda a: a+a<br>
 result=f(5)<br>
 print(result)<br>
 <i>Output:</i>&nbsp;10<br>
 
 <h3>Example 2</h3>
 g = lambda a,b: a-b<br>
 result=f(6,5)<br>
 print(result)<br>
 <i>Output:</i>&nbsp;1<br>
 

 
 
  
  

  
  
  
  
  
  
 
    
    
  
 
 
 
 
 
 
 
  


  
 
  
  




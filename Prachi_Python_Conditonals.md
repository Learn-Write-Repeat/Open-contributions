# **Conditionals:**

***What are Conditional statements?***

Conditional statements have a boolean(True or False) condition . 
If the condition evaluates to True , all the indented statements are executed.
If the condition evaluates to False , then , all the indented statements are ignored and next line is executed.

***Need of Conditional statements:***

We need conditional statements in our program to change the direction of program according to the conditions.

***Types of conditional statements***:
<ul>
<li>if statement</li>
<li>if-else statement</li>
<li>Chained conditional statemets</li>
</ul>


***Let's take a look at all the statements:***

1.<b>If statements</b>

When we have a condition or boolen expression to check , we use if condition.

<p>Syntax:</p>
<p><PRE>
        if boolean condition:<br>
           statement(s)</p>
</PRE>
Example:
<PRE> if a>b:
        print(a)
        </PRE>
      <ul>
      <li>Here, colon(':') is used to seperate the if statement with if body</li>
      <li> 'a>b' is the boolean condition</li>
      <li>If this boolean condition evaluates to True , then the statements inside the if block will be executed</li>
      <li>'print(a)' here , is the statement inside the if block , which will be executed only if the boolean condition evalutes to True</li>
      <li>If the condition evalutes to false the statement(s) inside the if block will be ignored , and rest of the statements will be executed.</li>
      </ul>
        <p>Let's take an example from our daily life:</p>
        <p>Example: If it is rainiing, use an umbrella otherwise don't use an umbrella.</p>
        <p>Explanation: Here , the condition is "if it is raining" , if this condition evaluates to true , then we use an umbrella ,otherwise, it is not raining so we don't need the umbrella.</p>
        <p>Now, let us take a look at the flowchart:</p>
       <p> <img src="https://user-images.githubusercontent.com/49331074/92867276-106d0d80-f41e-11ea-8289-d5e9da1d6b34.JPG" width="300" height="300"></p>
        <p>Thus, this flowchart explain us the flow of the program using 'if' conditional statement.</p>

2.<b>if-else statements</b>
        These if-else statements gives us an opportunity to have a seperate block of code to be executed if the boolean condition return false, i.e, we can write a set of code which we want to be executed when condition is true , in the if block , and other set of codes in the else block.
        <p>Syntax:</p>
<p><PRE>
        if boolean condition:<br>
           statement(s)<br>
        else:
            statements(s)
        </p>
</PRE>
Example:If we want to print the greater number among two numbers:
<PRE>   if a>b:
        print(a)
   else:
        print(b)
        </PRE>
       Here, we first check if a>b , if True ,a is printed . Else , statements under else code is executed and , b is printed.
       <ul>
      <li>Here, colon(':') is used to seperate the if statement with if body and the else statement withe the else body.</li>
      <li> 'a>b' is the boolean condition</li>
      <li>If this boolean condition evaluates to True , then the statements inside the if block will be executed</li>
      <li>'print(a)' here , is the statement inside the if block , which will be executed only if the boolean condition evalutes to True</li>
      <li>If the condition evalutes to false, the statement(s) under else bock will be executed. </li>
        <p>Let's take an example from our daily life:</p>
        <p>Example: Only the students with CGPA greater than 8.5 will be allowed to enter , others , go back home.
        <p>Explanation: Here , the condition is "the CGPA of the student is greater than 8.5" , if this condition evaluates to true , then then student is allowed in , else he is requested to go back home.</p>
        <p>Now, let us take a look at the flowchart:</p>
       <p> <img src="https://user-images.githubusercontent.com/49331074/92884784-ce4cc780-f42f-11ea-837b-0ffc530f42e5.JPG"  width="300" height="300"></p>
        <p>Thus, this flowchart explain us the flow of the program using 'if-else' conditional statement.</p>
      </ul>
      
  3.<b>Chained conditional statements</b>
  
  Sometimes we need more than two branches. When we have codes for more than two possibilites we require chained conditional statements.
  These have an elif statement , where we can mention the second set of possibilties that we have in our mind.
    <p>Syntax:</p>
<p><PRE>
        if boolean condition:<br>
           statement(s)<br>
        elif:<br>
            statements(s)<br>
        else:
            statements(s)
        </p>
</PRE>
Example:If we want to print the greater number among two numbers:
<PRE> if a>b:
        print(a)
 elif b>a:
        print(b)
 else:
        print("equal")
        </PRE>
        Here, we first check if a>b , if True ,a is printed . Else , elif condition is checked, if b>a, if True , b is printed.Else statements under else code is executed and , "equal" is printed.
    <ul>
        <li>It has an if statement at first , if that evaluate to true , then it goes into if block.</li>
        <li>If it evaluates to false, it goes to elif, i.e, it checks the condition of the elif block.</li>
        <li>If the condition in the elif bock evaluates to true , then the elif block is executed.</li>
        <li>If the condition again evaluates to false , then the code in the else block is executed.</li>
    <p>Now, let us take a look at the flowchart:</p>
       <p> <img src="https://user-images.githubusercontent.com/49331074/92886465-47005380-f431-11ea-90dc-74c1c5014a7d.JPG" width="300" height="300"></p>
        <p>Thus, this flowchart explain us the flow of the program using 'Chained conditional'statement.</p>
      <ul>

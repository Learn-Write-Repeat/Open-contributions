# BASIC OPERATORS IN PYTHON

 **Operators are used to perform operations on variables and values.**
 
 
 **Python divides the operators in the following groups:**
 
   - Arithmetic operators
   - Assignment operators
   - Comparison operators
   - Logical operators
   - Identity operators
   - Membership operators
   - Bitwise operators
  
 ***1. Python Arithmetic Operators*** 
 
 <table>
<tr>
<th>Operator</th>
 <th>	Name</th>
   <th>Example</th>
</tr>
<tr>
<td>+	</td>
  <td>Addition</td>
  <td>x + y</td>
</tr>
  
 <tr>
  <td>-	</td>
  <td>Subtraction</td>
  <td>x - y</td>
</tr>
  
  <tr>
  <td>*	</td>
  <td>Multiplication</td>
  <td>x * y</td>
</tr>

  <tr>
  <td>/	</td>
  <td>	Division</td>
  <td>x / y</td>
</tr>


  <tr>
  <td>%	</td>
  <td>	Modulus</td>
  <td>x % y</td>
</tr>

  <tr>
  <td>**	</td>
  <td>Exponentiation</td>
  <td>x ** y</td>
</tr>



</table>


###### Example:
      # Examples of Arithmetic Operator  
         a = 9
         b = 4
  
      # Addition of numbers  
       add = a + b  
  
      # Subtraction of numbers  
      sub = a - b  
  
      # Multiplication of number  
         mul = a * b  
  
      # Division(float) of number  
       div1 = a / b  
         
      # Division(floor) of number  
          div2 = a // b  
  
      # Modulo of both number  
           mod = a % b  
  
       # Power 
           p = a ** b 
       print(add)  
       print(sub)  
       print(mul)  
       print(div1)  
       print(mod) 
       print(div2)
       print(p) 
######  Output:
            
            
          13
          5
          36
          2.25
          2
          1
          6561





   
   
   
   
***2.Python Assignment Operators***

<table>
<tr>
<th>Operator</th>
 <th>Example</th>
   <th>Same as</th>
</tr>
<tr>
<td>=		</td>
  <td>	x = 5</td>
  <td>x = 5</td>
</tr>
  
 <tr>
  <td>+=	</td>
  <td>x=x+5</td>
  <td>x+=5</td>
</tr>
  
  <tr>
  <td>-=		</td>
  <td>x-=5</td>
  <td>x= x-5</td>
</tr>

  <tr>
  <td>/=	</td>
  <td>	x/=5</td>
  <td>x = x/5</td>
</tr>


  <tr>
  <td>%=	</td>
  <td>	x%=5</td>
  <td>x= x%5</td>
</tr>

  <tr>
  <td>//=	</td>
  <td>x// = 5</td>
  <td>x = x//5</td>
</tr>

 <tr>
  <td>//=	</td>
  <td>x// = 5</td>
  <td>x = x//5</td>
</tr>

 <tr>
  <td>**=	</td>
  <td>x** = 5</td>
  <td>x = x**5</td>
</tr>


 <tr>
  <td>&=</td>
  <td>x &= 5</td>
  <td>x = x&5</td>
</tr>

 <tr>
  <td>|=		</td>
  <td>x|=	 5</td>
  <td>x = x|5</td>
</tr>




 <tr>
  <td>//=	</td>
  <td>x// = 5</td>
  <td>x = x//5</td>
</tr>


</table>

***3.Python Comparison Operators***

|Methods|Name|Example|
|-------|-----------|---------|
|== |	Equal|	x == y|
|!=|	Not equal|x != y|
|>|	Greater than| x > y |
|<|		Less than| x < y |
|>=|	Greater than or equal to| x >= y |
|<=	|	Less than or equal to| x <= y |

###### Example:
                  
     # Examples of Comparison Operators 
     a = 13
     b = 33
  
    # a > b is False 
    print(a > b) 
  
    # a < b is True 
    print(a < b) 
  
    # a == b is False 
    print(a == b) 
  
    # a != b is True 
    print(a != b) 
  
    # a >= b is False 
    print(a >= b) 
  
    # a <= b is True 
    print(a <= b)














######  Output:
        

         False
         True
         False
         True
         False
         True
***4.Python Logical Operators***

|Methods|	Description|Example|
|-------|-----------|---------|
|and |	Returns True if both statements are true|	x < 5 and  x < 10|
|or|	Returns True if one of the statements is true|x < 5 or x < 4|
|not|	Reverse the result, returns False if the result is true| 	not(x < 5 and x < 10) |

###### Example:

         # Examples of Logical Operator 
         a = True
         b = False
  
         # Print a and b is False 
         print(a and b) 
  
         # Print a or b is True 
         print(a or b) 
  
         # Print not a is False 
         print(not a) 

######  Output:
         False
         True
         False
         
***5.Python Identity Operators***

|Methods|	Description|Example|
|-------|-----------|---------|
|is  |		Returns True if both variables are the same object|	x is y|
|is not|		Returns True if both variables are not the same object|	x is not y|

###### Example:

     # Examples of Identity operators 
    a1 = 3
    b1 = 3
    a2 = 'hello'
    b2 = 'hello'
    a3 = [1,2,3] 
    b3 = [1,2,3] 
    print(a1 is not b1) 
  
  
    print(a2 is b2) 
  
    # Output is False, since lists are mutable. 
    print(a3 is b3) 

######  Output:
         False
         True
         False
***6.Python Membership Operators***
|Methods|	Description|Example|
|-------|-----------|---------|
|in  |			Returns True if a sequence with the specified value is present in the object|	x in y	|
|not in|				Returns True if a sequence with the specified value is not present in the object|	x  not in  y|

###### Example:

      # Examples of Membership operator 
      x = 'hello guys'
      y = {3:'a',4:'b'} 
  
  
      print('h' in x) 
  
      print('Hello' not in x) 
  
      print('hello' not in x) 
  
      print(3 in y) 
  
     
  

######  Output:
      True
      True
      False
      True
  


***7.Python Bitwise Operators***


|Methods|	Description|Example|
|-------|-----------|---------|
|& ]  |			AND|	Sets each bit to 1 if both bits are 1|
||	|			OR|	Sets each bit to 1 if one of two bits is 1|
| ^	|				XOR|	Sets each bit to 1 if only one of two bits is 1|
|~ 	  | NOT|	Inverts all the bits|
|<<	|			Zero fill left shift|	Shift left by pushing zeros in from the right and let the leftmost bits fall off|
|>>	|		Signed right shift |	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off|





###### Example:
     # Examples of Bitwise operators 
     a = 10
     b = 4
  
     # Print bitwise AND operation   
     print(a & b) 
  
     # Print bitwise OR operation 
     print(a | b) 
  
     # Print bitwise NOT operation  
     print(~a) 
  
     # print bitwise XOR operation  
    print(a ^ b) 
  
    # print bitwise right shift operation  
    print(a >> 2) 
  
    # print bitwise left shift operation  
    print(a << 2) 
    
######  Output:

        0
       14
      -11
       14
       2
       40
***Any All in Python***

Any and All are two built ins provided in python used for successive And/Or.

***Any***

Returns true if any of the items is True. It returns False if empty or all are false. Any can be thought of as a sequence of OR operations on the provided iterables.
It short circuit the execution i.e. stop the execution as soon as the result is known.

##### Syntax : 
     any(list of iterables)
       
###### Example:
     # Since all are false, false is returned 
     print (any([False, False, False, False])) 
  
     # Here the method will short-circuit at the 
     # second item (True) and will return True. 
     print (any([False, True, False, False])) 
  
     # Here the method will short-circuit at the 
     # first (True) and will return True. 
     print (any([True, False, False, False])) 
##### output:  
     False
     True
     True
  

***All***
Returns true if all of the items are True (or if the iterable is empty). All can be thought of as a sequence of AND operations on the provided iterables. It also short circuit the execution i.e. stop the execution as soon as the result is known.

 
##### Syntax : 
    all(list of iterables)
       
###### Example:
    # Here all the iterables are True so all 
    # will return True and the same will be printed 
    print (all([True, True, True, True])) 
  
    # Here the method will short-circuit at the  
    # first item (False) and will return False. 
    print (all([False, True, True, False])) 
  
    # This statement will return False, as no 
    # True is found in the iterables 
    print (all([False, False, False])) 
##### output:  
     True
     False
     False




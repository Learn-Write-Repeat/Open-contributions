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
  
# print results  
            print(add)  
             print(sub)  
             print(mul)  
             print(div1)  
             print(mod) 
             print(div2)
              print(p) 



   
   
   
   
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


***4.Python Logical Operators***

|Methods|	Description|Example|
|-------|-----------|---------|
|and |	Returns True if both statements are true|	x < 5 and  x < 10|
|or|	Returns True if one of the statements is true|x < 5 or x < 4|
|not|	Reverse the result, returns False if the result is true| 	not(x < 5 and x < 10) |

***5.Python Identity Operators***

|Methods|	Description|Example|
|-------|-----------|---------|
|is  |		Returns True if both variables are the same object|	x is y|
|is not|		Returns True if both variables are not the same object|	x is not y|


***6.Python Bitwise Operators***


|Methods|	Description|Example|
|-------|-----------|---------|
|& ]  |			AND|	Sets each bit to 1 if both bits are 1|
||	|			OR|	Sets each bit to 1 if one of two bits is 1|
| ^	|				XOR|	Sets each bit to 1 if only one of two bits is 1|
|~ 	  | NOT|	Inverts all the bits|
|<<	|			Zero fill left shift|	Shift left by pushing zeros in from the right and let the leftmost bits fall off|
|>>	|		Signed right shift |	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off|


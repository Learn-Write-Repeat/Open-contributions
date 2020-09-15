# :thinking: What we will be learning from this documentation :question:

 :point_right: Variables
 
 :point_right: Data types
 
 :point_right: Type Conversions
 
 :point_right: Operators in Python
 
 
 -----------------------------------------------------------------------------------------------

## :clipboard: Variables:


Variables are like boxes or containers which stores any data. We can declare the variables using alphabet or using strings (more than one alphabet).

> In Python, assigning any type of data to the variables is too easy than any other programming languages 

**Ex:** 

X = -4 (Integer type)

Y = 3.8 (Float Type)

comp = 2 + 3j (Complex Type)

char = 'A' (String Type)

name = "Dev-Incept" (String Type) 

- Strings are written inside the quotes, either single quotes or double quotes


## :clipboard: Data Types:

We have seen one of the data type in the above example i.e, Numeric Data type 

- We have 4 data types in python as shown below

| S.No.| Data Type | Types/Operations| Examples|
|-------|-----------|----------|----------------|
|   1.  | Numeric data type  | <ul><li>integer</li><li>float</li><li>complex</li><li>boolean</li>| <ul><li>3</li><li>8.4</li><li>5 + 6j</li><li>True</li></ul>
 |  2. | List data type    | <ul><li>len</li><li>append</li><li>extend</li><li>insert</li><li>pop</li><li>remove</li><li>count</li><li>sorted</li><li>max</li><li>min</li><li>sum</li><li>index</li><li>reverse</li></ul> | <ul><li>[1,2,3,4,5]</li><li>['Dev' , "Incept" , 4.5 ,5]
 |  3. | Tuple data type   | <ul><li>count</li><li>index</li><li>sum</li><li>max</li><li>min</li></ul> | <ul><li>(1,2,3,4,5)</li><li>("Dev", "Incept", 4.5, 24)</li></ul>
  |   4. | Set data type      | <ul><li>remove</li><li>discard</li><li>pop</li><li>update</li><li>union</li><li>intersection</li><li>difference</li><li>isdisjoint</li><li>issubset</li><li>issuperset</li></ul> | <ul><li>{1,2,3,4,5}</li><li>{"Dev", "Incept", 4.5, 24}</li></ul>
 |   5. | String data type   | <ul><li>len()</li><li>capitalize()</li><li>upper()</li><li>lower()</li><li>swapcase()</li><li>count()</li><li>index()</li><li>find()</li><li>strip()</li><li>split()</li><li>join()</li><li>replace()</li><li>sort()</li><li>sorted()</li><li>isdigit()</li><li>isalpha()</li><li>startswith()</li><li>endswith()</li>|<ul><li>"abc"</li><li>"1234"</li></ul>
 |   6. | Dictionary data type | <ul><li>get</li><li>pop</li><li>keys()</li><li>items()</li><li>values()</li><li>update</li></ul> | <ul><li> {"a" : 10 ,"b" : "Dev Incept" , "c" : 19.565 , "d" : "False"} </li></ul>
 
 
***:thought_balloon: List Data Type:***

Lists store any type of data ie., it stores int , float , boolean , string etc.. These are indicated using square brackets []. The operations performed for lists are mentioned above in the tabular form.

Lists are Mutable that means we can change our data in the list.

***:thought_balloon: Tuple Data Type:*** 

Tuples are similar to lists ie., tuples also store int ,  float , boolean , string etc.. but these are indicated with paranthesis or round brackets (). The operations performed for tuples are mentioned above in the tabular form. 

Tuples are Im-mutable that means once we have assigned some data to the variable we can't change the data again.

 **Difference between Lists and Tuple**
 
 <ul><li>Lists are Mutable</li><li>Tuples are Im-mutable</li><li>Tuples take less time to execute than lists</li></ul> 
 
 ***:thought_balloon: Set Data Type:*** 

Sets also store different type of data like int , float , boolean , string etc..These are indicated using curly brackets {}. The operations performed for sets are mentioned above in the tabular form. 

Sets don't return the repeated values in the output and the order in the output is also not as same as the order in the given input.

 ***:thought_balloon:Strings:*** 
 
 Strings are the group of characters or only one charcter inside the singles quotes or double quotes. The characters may be numeric type or alphabets. The operations performed in strings are mentioned above in the tabular form. 
 
***:thought_balloon: Dictionary Data Type:*** 

Dictionary also store different type of data like int , float , boolean , string etc.. followed by key value pairs. These are indicated using curly brackets { "Key" : "Value"} . The keys name should be  **UNIQUE** and the values may be repeated based on our data. The operations performed for sets are mentioned above in the tabular form. 

## :clipboard: Type Conersions:

Converting one data type into another data type is called as type conversion. That means, we can convert an integer to a float value ; boolean value to integer ; float to boolean and vice versa etc..

We observe this type conversion detailly in the "Bommidi_Python_variables,types,type conversions.ipynb" file.


## :clipboard: Operators in python:

Operators are used to perform operations on variables and data 

We have different types of opertors they are: 

<ul><li> Arithmetic Operators </li>
 <li> Comparison Operators </li>
 <li> Logical Operators </li>
 <li> Bitwise Operators </li>
</ul>

> All the examples for this topic will be in "Bommidi_Python_variables,types,type conversions.ipynb" file. 

 ***:thought_balloon:Arithmetic Operators:*** 
 
 Arithemetic operators includes 
 <ol><li>Addition(+)</li><li>Subtraction(-)</li><li>Multiplication(*)</li><li>Division(/)</li><li>Floor division(//)</li><li>Modulus(%)</li><li>Exponential(**)</li></ol>
 
 
  ***:thought_balloon:Comparison Operators:*** 
  
  Comparison Operators  are used to compare two values like 
  <ol><li>Equal to (==) </li>
 <li> Not Equal to (!=) </li>
 <li> Greater than (>) </li>
  <li> Eess than (<) </li>
  <li> Greater than or Equal to (>=) </li>
  <li> Less than or Equal to (<=) </li></ol>
   
   ***:thought_balloon:Logical Operators:*** 
   
   Logical Operators are used to combine conditional statements 
   <ol><li>and</li>
 <li>or</li>
 <li>not</li>
 </ol>
 
 ***:thought_balloon: Bitwise Operators:*** 
 
 Bitwise Operators are used to compare binary numbers 
 
 <ol><li> AND   &</li>
 <li> OR  |</li>
 <li> XOR  ^</li>
 <li> NOT  ~</li>
</ol>

***=====================================================================================***

I hope you have gained some knowledge on these concepts!

**Thanks for reading  :blush:**
 
   
   
   
 
 
  
 









 
 
 

                          

























# Python3 Programming
## Pre-Requisites:
* None
## Before we start with the actual topics lets have a general overview about **Python**
Python is an high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991.It is object oriented and is dynamically typed.Python is meant to be an easily readable language and it often uses English keywords.
* Don't worry about the all the technical terms as we dive deep into the language you will learn all the things.
* For the time being you just have to know that:
  1. Python is a programming language not a snake :snake:.
  2. It is the easiest language which anyone can learn in no time.
  3. And currently it is the most loved and most famous programming language of [2020.](https://www.cleveroad.com/blog/programming-languages-ranking)
  4. And we will be using Python3 over Python2.
## So lets program.
So lets type our first line of code.This is the code which every person in the world types when they start to learn programming.
```python
   print("Hello, World!")
   print("DevIncept")
```
Here ***print*** is a function which is builtin, which takes anything  written in the ***parenthesis*** and the **quotes(''/"")** and prints it out on the screen.
You can try printing anything in the jupyter notebook provided.

## Variables
Variables are the names you give to computer memory locations which are used to store values in a computer program **OR** Variables are containers for storing values.A variable is created the moment you first assign a value to it.
```python
   Name= 'John'
   Age= 19
   Company= 'DevIncept'
   print(Name,Age,Company)
   ```
**Result:**
```python
   John 19 DevIncept
```
As we can see in the above example **Name, Age** and **Company** are three different variables all having different values.And when the variable names are called in the ***print*** function they are printed on the screen.

A variable can store only one value, as we continue through the program  from top to bottom, **if the same variable name is assigned with different value the new value takes over the previous one**,Variables do not need to be declared with any particular type and can even change type after they have been set..As in the below example:
```python
  x=19
  x='DevIncept'
  print(x)
  ```
**Result:** `DevIncept`

```python
  x=19
  x=23
  print(x)
  ```
**Result:** ***23***
> **Unlike other programming languages, Python has no command for declaring a variable.**

### Naming of Variables
  As we now know  what are variables and how are they used now lets see some very important rules to create a valid Variable Name.
  **Note: Rules for Naming of Variables are same in almost all programming languages.**
  * A variable name must start with a letter or the underscore character
  * A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
  * A variable name cannot start with a number 
  * Variable names are case-sensitive (age, Age and AGE are three different variables)
  * There should be no spaces in the words
  
```python
  #Valid Variable names
   myvariable1="DevIncept"
   my_variable="JaneDoe"
   _variable=17
   
  #Invalid Variable names
   invalid-variable='Mahendra'
   8variable=19
   invalid name='Doe'
   ```
When you run the above lines of code when the Pyhton Interpreter reaches Invalid Variable names it raises an Syntax Error.Don't worry check your code correct it and carry on.
![image](https://files.realpython.com/media/Common-Syntax-Problems-Invalid-Syntax-in-Python_Watermarked.f2542f224bb4.jpg)
#### Shorthand for assigning multiple variables in one line
```python
  fruit,color,cost= "Apple","Green",15.75
  print(fruit)
  print(color)
  print(cost)
  ```
 **Result:**`Apple Green 15.75`
So this here finishes the basics of Variables hope you enjoyed the topics.

## Data Types
Remeber all those variables which we created in the above lessons, we saw there were plain **numbers, decimal numbers**, and **simple text**.
These are nothing but different **Data Types**.
!!!Shocker huh :laughing:, all this time you were using data types and you didn't know what they were.:astonished:
* In programming, data type is an important concept.
* Variables can store data of different types, and different types can do different things.
#### Data Types Table
Some basic and most commonly used datatypes.
|Data Type | Abbreviation |     Examples    |
|----------|--------------|-----------------|
|  str     |  text type   |  'Ron', 'Remi'  |
|  int     |  integers    |   10, 5         |
|  float   |  decimal     |   10.5, 5.7     |
|  bool    |  True/False  |   True ,False   |
  
For more advanced and all datatypes you check out the following site ---->> [RealPython](https://realpython.com/python-data-types/)  

Above mentioned Data types are most commonly used. And whenever you are not sure what datatype the object is you can use the `type()` function.
```python
  name="DevIncept"
  print(type(name))
  ```
**Result:** `<class 'str'>`
```python
  age=20
  print(type(age))
  ```
**Result:** `<class 'int'>`

### Python Numbers
  * int: 
      Int, or integer, is a whole number, positive or negative, **without decimals**, of unlimited length.
  * float:
      Float, or "floating point number" is a number, positive or negative, containing **one or more decimals**.

```python
  #int
  x=123
  y=-987
  z=687969176975
  
  #float
  a=23.897
  b=-4.87970879879
  
  print(type(x))
  print(type(y))
  print(type(z))
  print(type(a))
  print(type(b))
  ```
**Result:**
```python
   <class 'int'>
   <class 'int'>
   <class 'int'>
   <class 'float'>
   <class 'float'>
   ```
**In real world what do we do with numbers???**:smirk::smirk:
Calculations right, in python also we can tell the program to do calculations.
```python
   a=30
   b=20
   sum=a+b #does the addition
   diff=a-b #does the subtraction
   div=a/b #does the division
   print(sum)
   print(diff)
   print(div)
   ```
**Result:**
```python
    50
    10
    1.5
   ```
 #### Type Conversion
 You can convert one type to another by using int(),float() methods.
```python
   a=5 #int
   b=7.7 #float
   
   #converting from int to float:
   x=float(a)
   
   #converting from float to int:
   y=int(b)
   
   print(x)
   print(y)
   print(type(x))
   print(type(y))
```
**Result:**
```python 
   5.0
   7
   <class 'float'>
   <class 'int'>
  ```
**Note**: You can also specify the type in the starting only its called Python Casting
```python
   x=int("56") # x will be 56 
   y=int(8.9)  # y will be 8
   z=float(56) # z will be 56.0
   a=str(56)   # a will be '56'
  ```
  
### Python Strings
String literals in python are surrounded by either single quotation marks, or double quotation marks.
`'hello'` is the same as `"hello"`.
```python
   print('hello')
   print("hello")
   
   #Strings assigned in variables
   a= 'DevIncept'
   print(a)
   
   #Multiline Strings
   a = """Lorem ipsum dolor sit amet,
   consectetur adipiscing elit,
   sed do eiusmod tempor incididunt
   ut labore et dolore magna aliqua."""
   print(a)
  ```
**Result:**
```python
   hello
   hello
   DevIncept
   Lorem ipsum dolor sit amet,
   consectetur adipiscing elit,
   sed do eiusmod tempor incididunt
   ut labore et dolore magna aliqua.
  ```
**Strings are very important Data types, There are lots of things you can do with strings**
For example: Square brackets can be used to access elements of the string.
```python
   a='DevIncept'
   print(a[0]) #prints the first letter
   print(a[-1]) #prints the last letter
   print(a[2]) #prints the third letter
  ```
  > You must be wondering i told it will print the first letter but wrote zero(0) in the square bracket.??:smile:
  > Thats a totally valid question.
  > All programing languages are mostly zero-indexed meaning the positioning of the first letter is the considered as zero(0) and not one(1)
**Result:**
```python
   D
   t
   v
  ```
#### String Concatenation  
  Concatenation in general means to combine things.
  As the general meaning, in programming also it means the same you can combine strings using **+** operator
```python
   a="DevIncept "
   b="is a great "
   c="Company"
   print(a+b+c)
 ```
 **Result:**
 ```pyhton
    DevIncept is a great Company
   ``` 
#### String Slicing
 You can return a range of characters by using the string slicing.
 **Specify the start index and the end index(*not included*), separated by a colon, to return a part of the string.**
```python
   a='DevIncept'
   print(a[0:3])
  ```
**Result:**
```python
   Dev
  ``` 
   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   # Attention!! Attention!! Attention!!!                                                                                                                                  
   # You can practice all the above examples in the jupyter notebook                                                                                                       
   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#### String Methods
String Methods are nothing but pyhton built in fuctions to make our life easy...
```python
   a='DevIncept'
   print(a.lower()) # all lowercase
   print(a.upper()) # all uppercase
  ```
**Result:**
```pyhton
   devincept
   DEVINCEPT
  ```
You can find more String methods ------>> [Python-Ds](http://www.python-ds.com/python-3-string-methods)  
### Escape Characters
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
```python
   txt = "We are the so-called \"Vikings\" from the north."
   print(txt)
  ```
**Result:**
```pyhton
   We are the so-called "Vikings" from the north.
  ```
  **Other Escape Characters used in python are:**
  |Code |      Result       |
  |-----|-------------------|
  | \\' |  Single Quote	   |
  |\\\\ |	Backslash	       |
  | \n  |	New Line	       |
  | \r  |	Carriage Return	 |
  | \t  |	Tab              |
  
### Python Boolean
In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False.
```python
   print(10 > 9)
   print(10 == 10)
   print(10 < 9)
   
   a=100
   b=200
   print(a>b)
  ```
 **Result:**
 ```python
    True
    True
    False
    False
   ``` 
 # Finally You have made it to the end of the lessons.Congratulations on doing that,Its not an easy task to learn a programming language from scratch.
 # Take time you have achieved a lot in few hours. Whenever you feel confused review the lessons.
 ## Now you are a part ***Pythonista***:snake: 
   

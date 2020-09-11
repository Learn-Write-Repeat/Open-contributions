# Python
## Pre-Requisites:
* None
## Before we start with the actual topics lets have a general overview about **Python**
Python is an high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991.It is object oriented and is dynamically typed.Python is meant to be an easily readable language and it often uses English keywords.
* Don't worry about the all the technical terms as we dive deep into the language you will learn all the things.
* For the time being you just have to know that:
  1. Python is a programming language not a snake.
  2. It is the easiest language which anyone can learn in no time.
  3. And currently it is the most loved and most famous programming language of [2020.](https://www.cleveroad.com/blog/programming-languages-ranking)
  4. And we will be using Python3 over Python2.
## So lets program.
So lets type our first line of code.This is the code which every person in the world types when they start to learn programming.
* `print("Hello, World!")`
* `print("DevIncept")`

Here ***print*** is a function which is builtin which takes anything  written in the parenthesis and the quotes(''/"") and prints it out on the screen.
You can try printing anything in the jupyter notebook provided.

## Variables
Variables are the names you give to computer memory locations which are used to store values in a computer program **OR** Variables are containers for storing values.A variable is created the moment you first assign a value to it.
```python
   Name= 'John'
   Age= 19
   Company= 'DevIncept'
   print(Name,Age,Company)
   ```
Result:`John 19 DevIncept`

As we can see in the above example Name, Age and Company are three different variables all having different values.And when the variable names are called in the print function they are printed on the screen.
A variable can store only one value as we continue the program flow from top to bottom if the same variable name is assigned with different value the new value takes over the precedence,Variables do not need to be declared with any particular type and can even change type after they have been set..As in the below example:
```python
  x=19
  x='DevIncept'
  print(x)
  ```
Result: `DevIncept`
```python
  x=19
  x=23
  print(x)
  ```
Result: 23
> Unlike other programming languages, Python has no command for declaring a variable.

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
 Result:`Apple Green 15.75`
So this here finishes the basics of Variables hope you enjoyed the topics.

## Data Types
Remeber all those variables which we created in the above lessons we saw there were plain numbers,decimal numbers,and simple text.
These are nothing but different Data Types.
!!!Shocker huh, all this time you were using data types and you didn't know what they were.
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
Result: `<class 'str'>`
```python
  age=20
  print(type(age))
  ```
Result: `<class 'int'>`

### Python Numbers
  * int: 
      Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
  * float:
      Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

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
Result:
```python
   <class 'int'>
   <class 'int'>
   <class 'int'>
   <class 'float'>
   <class 'float'>
   ```
In real type what do we do with numbers???
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
Result:
```python
    50
    10
    1.5
   ```

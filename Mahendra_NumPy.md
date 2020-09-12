![Numpy](https://miro.medium.com/max/765/1*cyXCE-JcBelTyrK-58w6_Q.png)
# NumPy
NumPy **(Numerical Python)** is an open source Python library that’s used  for working with numerical data in Python.
It is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python.

Numpy can also be used as an efficient multi-dimensional container of generic data.

## Pre-Requisites
* Basic working knowledge of Python.

## Basic things to know before we start with the topic:
In the Numpy definition, you read that they basically work with **Arrays** so what are **Arrays**???
### Arrays
* An array is a collection of items stored at continuous memory locations.
* All the stored items should be of same type.

![Array](https://media.geeksforgeeks.org/wp-content/uploads/array-2.png)
Source: GeeksforGeeks

Arrays are of two types:
* One-Dimensional Array
* Multi-Dimensional Array
#### One-Dimensional Array
A one-dimensional array (or single dimension array) is a type of linear array.Accessing its elements involves a single subscript which can either represent a row or column index.
Example:
```
   # A character array in C/C++/Java
   char arr1[] = {'D','e','v','I','n','c','e','p','t'};
   
   # An Integer array in C/C++/Java
   int arr2[] = {10, 20, 30, 40, 50};
  ``` 
  > To access the elements of a **single-dimensional** Array you can use the **indexes** and most of the Arrays are  **zero-indexed.**
 ```
  arr1[0]; # gives us D
  arr1[2]; # gives us v
  arr2[1]; # gives us 20
  arr2[4]; # gives us 50
 ```
 > **Note:** Array of characters is called a string.
 > Yes!! These are the same strings which we use in Pyhton they are also Arrayss hidden in plain sight.
 
#### Multi-Dimensional Arrays
A multi-dimensional array is an array with more than one level or dimension. For example, a 2D array, or two-dimensional array.
**Meaning it is a matrix of rows and columns (think of a table).**

![2-D Array](https://cdn.programiz.com/sites/tutorial2program/files/2d-array-variable-length.jpg)

Example:
```
  int two_d[10][20];
  int x[3][4] = {{0,1,2,3}, {4,5,6,7}, {8,9,10,11}};
  char y[3][4] = {{'a','b','c','d'}, {'D','e','V','I'}, {'n','c','e','p'}};
```  
> To access the elements of a **multi-dimensional** Array you can use the **indexes** and most of the Arrays are  **zero-indexed.**

```
  x[0][1]; # gives us 1
  y[1][2]; # gives us V
```
> You can access elements in a multi-dimensional like in the example showed above..

# Attention!! Python Lists are also kind of Arrays but more easy....
## As *Python* makes everything easy.. :smirk::smirk:
Few simple Examples:
```python
  list=['DevIncept',10,'Sam',100,20]
  print(list[0])
  print(list[2])
  print(list[3])
 ```
 A Python list may contain different types! Indeed, you can store a number, a string, and even another list within a single list.
Result:
```python
   DevIncept
   Sam
   100
 ```
You can tinker with the above example in the provided Jupyter Notebook..

## Why use NumPy over Pyhton Lists???
* ### In Python we have lists that serve the purpose of arrays, but they are slow to process.
* ### NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.
* ### Arrays are very frequently used in data science, where speed and resources are very important.

**Note:**
>  All of the elements in a NumPy array should be homogeneous.


## Installing NumPy
### Attention!!! You must already have Python:snake: installed in order to install Numpy.
If you already have Python, you can install NumPy with:
```python
   pip install numpy
```
**Or**
```python
   conda install numpy
  ```
 If you don’t have Python yet, you might want to consider using [Anaconda](https://www.anaconda.com/). It’s the easiest way to get started.


## How to Import Numpy
Any time you want to use a package or library in your code, you first need to make it accessible.
In order to start using NumPy and all of the functions available in NumPy, you’ll need to import it. This can be easily done with this import statement:
```python
   import numpy as np
 ```
> (You can use any variable instead of **np**) 





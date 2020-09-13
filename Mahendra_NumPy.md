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
*******
*******
# NumPy Basics:
## Creating a basic Array
To create a basic NumPy Array you can use the function ***np.array()***
The array object in NumPy is called **ndarray**
```python
   import numpy as np
   arr1=np.array([1,2,3])
   arr2=np.array(['a','b','c','d','e'])
   arr3= np.array((1, 2, 3, 4, 5)) # You can also pass a tuple to creat an Array
   print(arr1)
   print(arr2)
   print(arr3)
   print(type(arr1))
 ```
**Result:**
```python
   [1 2 3]
   ['a' 'b' 'c' 'd' 'e']
   [1 2 3 4 5]
   <class 'numpy.ndarray'>
  ```
  
  ![arr1](https://numpy.org/devdocs/_images/np_array.png)
  
  
  **Besides the above examples you can create Arrays using builtin function**
  * To create an Array of Zeroes use ***np.zeros()***
  * To create an Array of Ones use ***np.ones()***
  * To create an Array with a range of elements use ***np.arange()***
  ```python
     import numpy as np
     a=np.zeros(3)
     b=np.ones(5)
     c=np.arange(10)
     d=np.arange(2,9)   # To specify start and stop
     e=np.arange(1,10,2) # To specify start and stop with step size
     print(a)
     print(b)
     print(c)
     print(d)
     print(e)
  ``` 
  **Result:**
  ```python
     [ 0.  0.  0.]
     [ 1.  1.  1.  1.  1.]
     [0 1 2 3 4 5 6 7 8 9]
     [2 3 4 5 6 7 8]
     [1 3 5 7 9]
  ```  
  > **You can try the code yourself in the provided Jupyter Notebook**


## NdArray(N-Dimensional Array)
1. An array class in Numpy is called as **ndarray**.
2. Number of dimensions of the array is called rank of the array.

**Lets Create a 2-D(Dimensional) Array**
* They are like a matrix or you can say a table
```python
   import numpy as np
   arr1=np.array([[1,2,3],[4,5,6]])
   arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
   arr3=np.array([['a','b','c'],['d','e','f']])
   
   #creates a 3X3 array with all zeros
   zeros=np.zeros((3,3))
   
   #creates a 2X2 array with all ones
   ones=np.ones((2,2),dtype='int64')  #specify the type with (dtype) parameter 
   
   print(arr1)
   print(arr2)
   print(arr3)
   print(zeros)
   print(ones)
```
**Result:**
```python
   [[1 2 3]
    [4 5 6]]
    
   [[1 2 3]
    [4 5 6]
    [7 8 9]] 
    
   [['a' 'b' 'c']
    ['d' 'e' 'f']]
    
   # 3X3 Matrix
   [[ 0.  0.  0.]
    [ 0.  0.  0.]
    [ 0.  0.  0.]]
    
   # 2X2 Matrix
   [[1 1]
    [1 1]]
```    
> NumPy provides some cool methods you can check the number of dimensions using ***ndim***  
```python
   import numpy as np

   a = np.array(42)
   b = np.array([1, 2, 3, 4, 5])
   c = np.array([[1, 2, 3], [4, 5, 6]])
   d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

   print(a.ndim)
   print(b.ndim)
   print(c.ndim)
   print(d.ndim)
``` 
**Result:**
```python
   0
   1
   2
   3
```
## Basic Operations with Arrays
You can also do basic arthemetic operations with arrays.
```python
   arr1=np.array([5,5,5,5])
   arr2=np.array([3,3,3,3])
   c=arr1+arr2
   d=arr1-arr2
   e=arr1/arr2
   print(arr1)
   print(arr2)
   print(c) # addition
   print(d) # subtraction
   print(e) # division
   print("Adding one to all elements:",c+1)
   print("Subtracting one from all elements:",d-1)
```
**Result:**
```python
   [5 5 5 5]
   [3 3 3 3]
   [8 8 8 8]
   [2 2 2 2]
   [1.66666667  1.66666667  1.66666667  1.66666667]
   Adding one to all elements: [9 9 9 9]
   Subtracting one from all elements: [1 1 1 1]
```
> You can also do other basic operations. Try them yourself in the Jupyter Notebook provided.

## I know just for basics also this is too much.If you have reached till this point and still not sure, DONT WORRY!!!!
## You can practice all the examples in the Jupyter Notebook provided, Don't just see them, change them put new values and see what happens..
## Try new things and slowly but steadily you will definetly get a good grasp on them..:smile::smile:

****************
****************
# Array Indexing and Slicing
## Array Indexing:
* **Array indexing is the same as accessing an array element.**
* **You can access an array element by referring to its index number.**
```python
   import numpy as np
   arr1= np.array([3,2,3,4])
   arr2= np.array([2,1,1,3])
   arr3= np.array(['D','e','V','I','n','c','e','p','t'])
   arr4= np.array([[1,2,3,4,5], [6,7,8,9,10]])
   print(arr1[0]) # prints first element
   print(arr1[-1]) # prints last element
   print(arr2[2]) # prints third element
   print(arr3[0]) # prints first element
   print(arr4[1][3]) #prints 9
   print(arr[1,3]) # Or you can use this type 
```
**Result:**
```python
   3
   4
   1
   D
   9
   9
```
## Array Slicing:
![Slicing](https://wtmatter.com/wp-content/uploads/2020/07/NumPy-Array-Slicing-Python-Tutorial.png)
> Array slicing is same as String Slicing so don't worry...

* Slicing in python means taking elements from one given index to another given index.
* We pass slice instead of index like this: `[start:end]`.
* You can also provide Step size as: `[start:end:step]`.

```python
   import numpy as np
   arr1=np.array(['D','e','V','I','n','c','e','p','t'])
   arr2=np.array([1,2,3,4,5,6,7,8,9])
   
   #2-D Slicing
   arr3=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
   
   print(arr1[:3]) # default is taken as 0
   print(arr1[0:3])
   print(arr1[3:]) # taken till the end
   print(arr1[::2])
   
   print(arr2[-4:-1])
   print(arr2[::2]) # step size as 2
   
   # 2-D Slicing
   print(arr3[1,1:4])
   print(arr3[0:2, 2])
   print(arr3[0:2, 1:4])
```
Result:
```python
   ['D' 'e' 'V']
   ['D' 'e' 'V']
   ['I' 'n' 'c' 'e' 'p' 't']
   ['D' 'V' 'n' 'e' 't']
   
   [6 7 8]
   [1 3 5 7 9]
   
   # Go over these results carefully they are bit tricky..
   [7 8 9]
   [3 8]
   [[2 3 4]
    [7 8 9]]
```
### All in one example
```python
   import numpy as np
   data = np.array([1, 2, 3])
   print(data[1])
   print(data[0:2])
   print(data[1:])
   print(data[-2:])
```
**Result:**
```python
   2
   [1 2]
   [2 3]
   [2 3]
```
![visualization](https://numpy.org/devdocs/_images/np_indexing.png)


****************
******************

# Now to the coolest Part of NumPy. :smile::smile:
# NumPy Functions
## Numpy Array Shape:
`ndarray.shape` will display a tuple of integers that indicate the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3).
```python
   import numpy as np
   arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
   arr1= np.array([1,2,3,4])

   print(arr.shape)
   print(arr1.shape)
 ```
**Result:**
```python
   (2, 4)
   (4,)
 ```
 **All In One Example**
```python
   array_example = np.array([[[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0 ,1 ,2, 3],
                            [4, 5, 6, 7]]])
 
   print('No of dimensions of the array:',array_example.ndim)     # .ndim for dimensions
   print('Total no of elements of the array:',array_example.size) # .size for size
   print('Shape of the array:'array_example.shape)                # .shape for shape
 ```
 **Result:**
 ```python
    No of dimensions of the array: 3
    Total no of elements of the array: 24
    Shape of the array: (3, 2, 4)
 ```
 
   






   
   
   
   
   
   
   
  
  
  



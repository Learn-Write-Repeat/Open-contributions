## What is Tuple?

A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists. The differences between tuples and lists are mutable, the tuples are immutable it means cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.You can access tuple items by referring to the index number, inside square brackets.

###### Syntax 
    tuple1 = ()                             //Empty Tuple
    tuple2 = ('Hello')                      //Tuple Item
    tuple3 = ('Green','Blue','Purple')      //Tuple Items
    
 ### Tuple Advantages over List

- Program execution is faster when manipulating a tuple than it is for the equivalent list.

- Sometimes you don’t want data to be modified. If the values in the collection are meant to remain constant for the life of the program, using a tuple instead of a list guards against accidental modification.

- There is another Python data type that you will encounter shortly called a dictionary, which requires as one of its components a value that is of an immutable type. A tuple can be used for this purpose, whereas a list can’t be.

## Basic Operations of Tuple

|  Python Expression  |    Result    |  Operation  |
|---------------------|--------------|-------------|
|   (1,2,3)+(8,9,9)   |(1,2,3,8,9,9) | Concatination|
|   len((4,5,6))      | 3            | Length |  
|   7 in (1,4,7)      | True         |Membership|
| for n in (1,3,5): print (n) | 1 3 5 |Iteration|

## Built-in Function of Tuple

|   Function   |                Description                      |
|--------------|-------------------------------------------------|
|cmp(tuple1, tuple2)|It compares two tuples and returns true if tuple1 is greater than tuple2 otherwise false.|
|len(tuple)|It calculates the length of the tuple.|
|max(tuple)|It returns the maximum element of the tuple.|
|min(tuple)|It returns the minimum element of the tuple.|
|tuple(seq)|It converts the specified sequence to the tuple.|

## Now You have learnt about Collection Tuple. Next you have to do is to practice from the Tuple practical [click here](https://github.com/akshayadme/Open-contributions/blob/master/Akshay_Python_List%20(1).ipynb)

## Next Topic you have to learn is Set [Click Here]()

## What is Set?

A set is an unordered collection of items. Every set element is unique and must be immutable it means cannot be changed. The sets remove the duplicate items.
There is no index attached to the elements of the set, i.e., we cannot directly access any element of the set by the index. We can print them all together, or we can get the list of elements by looping through the set.

A set is created by placing all the items (elements) inside curly braces {}, separated by comma.

###### Syntax
    set1 = {} #Empty Set
    set2 = {"Python"} #Set with an Element
 
###### Example 
    s1 = set("Hello Welcome to learning of pyhon".split())
    s1 = {'is','and','my','name','honey'}

## Python Set Operations

Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

### Set Union
The union of two sets is calculated by using the pipe (|) operator. The union of the two sets contains all the items that are present in both the sets.

![set union](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQq9OXyKDn48CKz7zZ-NjZsEGDA8yY4aQ64yQ&usqp=CAU)
    
    # Set union method
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    # use | operator
    # Output: {1, 2, 3, 4, 5, 6, 7, 8}
    print(A | B)

### Set Intersection
The intersection of two sets can be performed by the and & operator or the intersection() function. The intersection of the two sets is given as the set of the elements that common in both sets.

![set intersection](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSL9JQeVlCeEYhaK-e1T8CVqpnq2_gk7Wf5kA&usqp=CAU)

    # Intersection of sets
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    # use & operator
    # Output: {4, 5}
    print(A & B)
    
### Set Diffrence
The difference of two sets can be calculated by using the subtraction (-) operator or intersection() method. Suppose there are two sets A and B, and the difference is A-B that denotes the resulting set will be obtained that element of A, which is not present in the set B.

![set diffrence](https://s3.amazonaws.com/hr-challenge-images/9420/1437904659-11e4bef847-A-B.png)

    # Difference of two sets
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    # use - operator on A
    # Output: {1, 2, 3}
    print(A - B)  

### Set Symmetric Difference
The symmetric difference of two sets is calculated by ^ operator or symmetric_difference() method. Symmetric difference of sets, it removes that element which is present in both sets.

![set symmetric diffrrence](https://cdn.programiz.com/sites/tutorial2program/files/set-symmetric-difference.jpg)

    # Symmetric difference of two sets
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    # use ^ operator
    # Output: {1, 2, 3, 6, 7, 8}
    print(A ^ B)
    
## Built-in Set Methods

|   Function   |                Description                      |
|--------------|-------------------------------------------------|
|add(item)|	It adds an item to the set. It has no effect if the item is already present in the set.
|clear()|	It deletes all the items from the set.
|copy()	|It returns a shallow copy of the set.
|difference_update()|	It modifies this set by removing all the items that are also present in the specified sets.
|discard(item)|	It removes the specified item from the set.
|intersection()	|It returns a new set that contains only the common elements of both the sets. 
|intersection_update()	|It removes the items from the original set that are not present in both the sets (all the sets if more than one are specified).
|Isdisjoint()|	Return True if two sets have a null intersection.
|Issubset()	|Report whether another set contains this set.
|Issuperset()	|Report whether this set contains another set.
|pop()	|Remove and return an arbitrary set element that is the last element of the set. Raises KeyError if the set is empty.
|remove(item)|	Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.
|symmetric_difference()	|Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.
|symmetric_difference_update()	|Update a set with the symmetric difference of itself and another.
|union()|	Return the union of sets as a new set.
|update()|	Update a set with the union of itself and others.

## Now You have learnt about Collection Set. Next you have to do is to practice from the Set practical [click here](https://github.com/akshayadme/Open-contributions/blob/master/Akshay_Python_Set.ipynb)

## Next Topic you have to learn is Dictionary [Click Here](https://github.com/akshayadme/Open-contributions/blob/master/Akshay_Python_Dictionary.md)

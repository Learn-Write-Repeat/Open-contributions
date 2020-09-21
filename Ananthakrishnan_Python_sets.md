## SETS
 - In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements.  
 - The order of elements in a set is undefined though it may consist of various elements
##### Example :
    #Create a Set:
    car = {"WagonR", "Swift", "Verna"}
    print(car)

    # Note: the set list is unordered, meaning: the items will appear in a random order.
    # Note: Sets are unordered, so you cannot be sure in which order the items will appear.
##### output :
    {'Swift', 'Verna', 'WagonR'}
***Note: Sets are unordered, so you cannot be sure in which order the items will appear.***

---
***Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by ‘comma’.***<br>
***Note – A set cannot have mutable elements like a list, set or dictionary, as its elements.***
##### Example 2 :
     
    # Python program to demonstrate  
    # Creation of Set in Python 
  
    # Creating a Set 
    set1 = set() 
    print("Intial blank Set: ") 
    print(set1) 
  
    # Creating a Set with  
    # the use of a String 
    set1 = set("MyfavoriatecarisVerna") 
    print("\nSet with the use of String: ") 
    print(set1) 
  
    # Creating a Set with 
    # the use of Constructor 
    # (Using object to Store String) 
    String = 'MyfavoriatecarisVerna'
    set1 = set(String) 
    print("\nSet with the use of an Object: " ) 
    print(set1) 
  
    # Creating a Set with 
    # the use of a List 
    set1 = set(["Swift" , "Verna" ,  "WagonR", "Verna" ]) 
    print("\nSet with the use of List: ") 
    print(set1) 
##### output : 
    Intial blank Set: 
    set()

    Set with the use of String: 
    {'y', 'f', 'i', 'c', 'n', 's', 't', 'o', 'v', 'V', 'M', 'e', 'a', 'r'}

    Set with the use of an Object: 
    {'y', 'f', 'i', 'c', 'n', 's', 't', 'o', 'v', 'V', 'M', 'e', 'a', 'r'}

    Set with the use of List: 
    {'WagonR', 'Verna', 'Swift'}
***NOTE : A set contains only unique elements but at the time of set creation, multiple duplicate values can also be passed. Order of elements in a set is undefined and is unchangeable. Type of elements in a set need not be the same, various mixed up data type values can also be passed to the set.***

## Access Items
 - You cannot access items in a set by referring to an index or a key.
 - But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
 ##### Example :  
    # Python program to demonstrate 
    # Accessing of elements in a set 

    # Creating a set 
    set1 = set(["WagonR", "or", "Swift"]) 
    print("\nInitial set") 
    print(set1) 

    # Accessing element using 
    # for loop 
    print("\nElements of set: ") 
    for i in set1: 
    print(i, end=" ") 

    # Checking the element 
    # using in keyword 
    print("\n")
    print("WagonR" in set1) 
    print("\n")
    print("Verna" in set1
##### output : 
    Initial set
    {'Swift', 'or', 'WagonR'}

    Elements of set: 
    Swift or WagonR 

    True


    False
## Change Items
 - Once a set is created, you cannot change its items, but you can add new items.
## Adding Elements to a Set
 - To add one item to a set use the add() method.
 - To add more than one item to a set use the update() method.
#### Using add() method
##### Example :
    # Python program to demonstrate 
    # Addition of elements in a Set 

    # Creating a Set 
    set1 = set() 
    print("Intial blank Set: ") 
    print(set1) 

    # Adding element and tuple to the Set 
    set1.add(8) 
    set1.add(9) 
    set1.add((6,7)) 
    print("\nSet after Addition of Three elements: ") 
    print(set1) 

    # Adding elements to the Set 
    # using Iterator 
    for i in range(1, 6): 
    set1.add(i) 
    print("\nSet after Addition of elements from 1-5: ") 
    print(set1)
##### output : 
    Intial blank Set: 
    set()

    Set after Addition of Three elements: 
    {8, 9, (6, 7)}

    Set after Addition of elements from 1-5: 
    {1, 2, 3, 4, 5, 8, 9, (6, 7)}
#### Using update() method 
  - Add multiple items to a set, using the update() method:
##### Example :
     # Python program to demonstrate 
    # Addition of elements in a Set 

    # Addition of elements to the Set 
    # using Update function 
    set1 = set([ 4, 5, 6 , 7 , (12 , 14 ) , 'Verna' , 'Swift' ]  ) 
    set1.update([10, 11]) 
    print("\nSet after Addition of elements using Update: ") 
    print(set1) 
##### output : 

    Set after Addition of elements using Update: 
    {4, 5, 6, 7, 10, 11, 'Verna', 'Swift', (12, 14)}
## Remove Item

 - To remove an item in a set, use the remove(), or the discard() method.
 ###### Remove by using the remove() method:
##### Example 1 : 
    carset = {"Verna", "Innova", "EccoSport"}

    carset.remove("Innova")

    print(carset)
##### output : 
    {'EccoSport', 'Verna'}
##### Example 2 : 
    carset = {"Verna", "Innova", "EccoSport"}

    carset.remove("Tavera")

    print(carset)
##### output : 
    KeyError: 'Tavera'   
***Note: If the item to remove does not exist, remove() will raise an error.***
##### Remove by using the discard() method:
##### Example 1 : 
    carset = {"Verna", "Innova", "EccoSport"}

    thisset.discard("Tavera")

    print(carset)
##### output : 
    {'EccoSport', 'Verna', 'Innova'}
***Note: If the item to remove does not exist, discard() will NOT raise an error.***
##### Example : 
    # Python program to demonstrate 
    # Deletion of elements in a Set 

    # Creating a Set 
    set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) 
    print("Intial Set: ") 
    print(set1) 

    # Removing elements from Set 
    # using Remove() method 
    set1.remove(5) 
    set1.remove(6) 
    print("\nSet after Removal of two elements: ") 
    print(set1) 

    # Removing elements from Set 
    # using Discard() method 
    set1.discard(8) 
    set1.discard(9) 
    print("\nSet after Discarding two elements: ") 
    print(set1) 

    # Removing elements from Set 
    # using iterator method 
    for i in range(1, 5): 
            set1.remove(i) 
    print("\nSet after Removing a range of elements: ") 
    print(set1) 
##### output : 
    Intial Set: 
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
***Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.***


    Set after Removal of two elements: 
    {1, 2, 3, 4, 7, 8, 9, 10, 11, 12}

    Set after Discarding two elements: 
    {1, 2, 3, 4, 7, 10, 11, 12}

    Set after Removing a range of elements: 
    {7, 10, 11, 12}
#### using pop() : 
  - You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
 - The return value of the pop() method is the removed item.
##### Example 1  : 
    carset = {"WagonR", "Verna", "Brezza"}

    x = carset.pop()

    print(x) #removed item

    print(carset) #the set after removal
##### output : 
    Brezza
    {'Verna', 'WagonR'}
##### Example 2 : 
    # Python program to demonstrate 
    # Deletion of elements in a Set 

    # Creating a Set 
    set1 = set([1, 2, 3, 4, 5, 6, 
		                	7, 8, 9, 10, 11, 12]) 
    print("Intial Set: ") 
    print(set1) 

    # Removing element from the 
    # Set using the pop() method 
    set1.pop() 
    print("\nSet after popping an element: ") 
    print(set1) 

##### output : 
    Intial Set: 
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    Set after popping an element: 
    {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
#### Using clear() method
 ###### The clear() method empties the set:
##### Example : 
    carset = {"Verna", "Innova", "EccoSport"}

    carset.clear()

    print(carset)
##### output : 
    set()   
 ## Using del() :
 #### The del keyword will delete the set completely:
 ##### Example : 
    carset = {"Verna", "Innova", "EccoSport"}

    del carset

    print(carset)
##### output : 
    NameError: name 'carset' is not defined
 ## Join Two Sets
  - There are several ways to join two or more sets in Python.

  - You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
  ##### Example :   by union()
    set1 = {"Swift", "Brezza" , "Baleno"}
    set2 = {1, 2, 3}

    set3 = set1.union(set2)
    print(set3)
  ##### output : 
    {1, 2, 3, 'Baleno', 'Brezza', 'Swift'}
  ##### Example :   by update()
    set1 = {"Swift", "Brezza" , "Baleno"}
    set2 = {1, 2, 3}

    set1.update(set2)
    print(set1)
  ##### output : 
    {1, 2, 3, 'Baleno', 'Brezza', 'Swift'}
 ##   Set Methods
 - Python has a set of built-in methods that you can use on sets.
 
|Methods |Description|
|-------- |----------- |
|add()   |Adds an element to the set|
|clear() |Removes all the elements from the set|
|copy() |Returns a copy of the set|
|difference() |Returns a set containing the difference between two or more sets|
|difference_update() |Removes the items in this set that are also included in another, specified set|
|discard() |Remove the specified item|
|intersection()| Returns a set, that is the intersection of two other sets|
|intersection_update()|	Removes the items in this set that are not present in other, specified set(s)|
|isdisjoint()|Returns whether two sets have a intersection or not|
|issubset()|Returns whether another set contains this set or not|
|issuperset()|Returns whether this set contains another set or not|
|pop()|	Removes an element from the set|
|remove()|	Removes the specified element|
|symmetric_difference()|	Returns a set with the symmetric differences of two sets|
|symmetric_difference_update()|		inserts the symmetric differences from this set and another|
|union()|	Return a set containing the union of sets|
|update()|		Update the set with the union of this set and others|

  
  

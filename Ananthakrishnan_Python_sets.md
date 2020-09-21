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

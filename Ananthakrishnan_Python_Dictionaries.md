## Python Dictionaries

 - A dictionary is a collection which is unordered, changeable and indexed. In Python ,  dictionaries are written with curly brackets  ***{}*** , and they have keys and values.
 - Dictionaries are ***mutable.*** i.e. it is possible to add, modify, delete key-value pairs.
-  The key should be ***unique*** and can be of any data type.

###### example:
    thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
    print(thisdict)

###### output:
    {'Company': 'Maruti', 'model': 'Swift', 'year': 2020}

## Properties of Dictionary

-  In  dictionary, we cannot store multiple values for the same keys. If we pass more than one value for a single key, then the value which is last assigned is considered as the value of the key.

- In python, the key cannot be any mutable object. We can use numbers, strings, or tuples as the key, but we cannot use any mutable object like the list as the key in the dictionary.


##### example:
    thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020,
     "model": "WagonR"   #then the value which is last assigned is considered as the value of the key.
    }
    print(thisdict)
    
###### output:
    {'Company': 'Maruti', 'model': 'WagonR', 'year': 2020}



## Accessing Items 
 - You can access the items of a dictionary by referring to its key name, inside square brackets:

###### example:
Get the value of the "model" key:
    
    
    thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
    x = thisdict["model"]
    print(thisdict)
##### output:
    Swiftt


There is also a method called get() that will give you the same result:

###### example:
    thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
    x = thisdict.get("model")
    print(x)

##### output:
    Swiftt
     
## Change Values
- You can change the value of a specific item by referring to its key name:


###### example:
    thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
    thisdict["year"] = 2018
    print(thisdict)

##### output:
    {'Company': 'Maruti', 'model': 'Swift', 'year': 2018}
    
## Loop Through a Dictionary
- You can loop through a dictionary by using a for loop.
- When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.


###### example:
###### Print all key names in the dictionary, one by one:
    thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
    
    for x in thisdict:
         print(x)

##### output:
    Company
    model
    year
    
    
 
###### Example
###### Print all values in the dictionary, one by one:   

    thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
    
    for x in thisdict:
        print(thisdict[x])

###### output:
        Maruti
        Swift
        2020
        
###### Example
###### You can also use the values() method to return values of a dictionary:
    thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
    for x in thisdict.values():
        print(x)
 ###### output:
        Maruti
        Swift
        2020 
        
        
###### Example
###### Loop through both keys and values, by using the items() method:
     thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
    for x in thisdict.values():
    print(x)
 ###### output:
        Maruti
        Swift
        2020    
 
 
 ###### Example
###### Loop through both keys and values, by using the items() method:
     thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
     for x, y in thisdict.items():
      print(x, y)
 ###### output:
      Company Maruti
      year 2020
      model Swift
      
## Dictionary Length
- To determine how many items (key-value pairs) a dictionary has, use the len() function.

 ###### Example
###### Loop through both keys and values, by using the items() method:
     thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
     print(len(thisdict))
 ###### output:
     3
 ## Adding Items
 - Adding an item to the dictionary is done by using a new index key and assigning a value to it:

 ###### Example 
     thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
     thisdict["color"] = "blue"
     print(thisdict)
 ###### output:
    {'Company': 'Maruti', 'model': 'Swift', 'year': 2020, 'color': 'blue'}


## Removing Items
 - There are several methods to remove items from a dictionary:
 
###### Example
###### The pop() method removes the item with the specified key name:
     thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
    thisdict.pop("model")
     print(thisdict)
###### output:
        {'Company': 'Maruti', 'year': 2020}
              

 
###### Example
###### The popitem() method removes the last inserted item
     thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
    thisdict.popitem()
     print(thisdict)
###### output:
    {'Company': 'Maruti', 'model': 'Swift'}
 
 
  
  
  
###### Example
###### The del keyword removes the item with the specified key name:
     thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
     del thisdict["model"]
     print(thisdict)
###### output:
    {'Company': 'Maruti', 'year':  2020}
        
        
###### Example
###### The del keyword can also delete the dictionary completely:
     thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
     del thisdict
     print(thisdict)  #this will cause an error because "thisdict" no longer exists.
###### output:
     ---------------------------------------------------------------------------
     NameError                                 Traceback (most recent call last)
     NameError: name 'thisdict' is not defined
   
 ###### Example  
 ###### The clear() method empties the dictionary:
     thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
     thisdict.clear()
     print(thisdict)  
###### output:
    {} 
 
 
 ## Copy a Dictionary
 
 
 ###### Example  
 ###### The clear() method empties the dictionary:
     thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020
    }
     mydict = thisdict.copy()
     print(mydict) 
###### output:
    {'Company': 'Maruti', 'model': 'Swift', 'year': 2020}   
   
   
 ## Built-in Methods of Dictionary

|Methods|Description|
|-------|-----------|
|clear()|	Removes all items from the dictionary.|
|copy()|	Returns a shallow copy of the dictionary.|
|fromkeys(seq[, v])|	Returns a new dictionary with keys from seq and value equal to v (defaults to None).|
|get(key[,d])|	Returns the value of the key. If the key does not exist, returns d (defaults to None).|
|items()|	Return a new object of the dictionary's items in (key, value) format.|
|keys()|	Returns a new object of the dictionary's keys.|
|pop(key[,d])|	Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.|
|popitem()|	Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.|
|setdefault(key[,d])|	Returns the corresponding value if the key is in the dictionary. If not, inserts the key with a value of d and returns d (defaults to None).|
|update([other])|	Updates the dictionary with the key/value pairs from other, overwriting existing keys.|
|values()|	Returns a new object of the dictionary's values|
  
    

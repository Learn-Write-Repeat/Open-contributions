## What is Dictionary

- A dictionaries can be defined as an unordered collection of key-value pairs separated by (:) and enclosed in ({}) braces.

- The key should be unique and can be of any data type.

- Keys are used to access elements in dictionary just like index in List.

- Dictionaries are mutable. i.e. it is possible to add, modify, delete key-value pairs.

###### Syntax:
    phonebook = {} #Empty Dictionary
    phonebook = {"Jhon":9524852155} #Dictionary with one key-value pair
    phonebook = {"Jhon":5449515965,"Ryan":7894568945} #2 key-value pairs

## Properties of Dictionary

-  In the dictionary, we cannot store multiple values for the same keys. If we pass more than one value for a single key, then the value which is last assigned is considered as the value of the key.

- In python, the key cannot be any mutable object. We can use numbers, strings, or tuples as the key, but we cannot use any mutable object like the list as the key in the dictionary.

## Accessing Items 
    crew =
        { "Pilot":"Kumar",
          "Co-pilot":"Raghav",
          "Head-Strewardess":"Malini",
          "Stewardess":"Mala" }
          
    crew["Pilot"]
    crew.get("Co-pilot") //get() method will also give same result for accessing 

## Iterating through the Dictionary
    
    //items function gives both key and value, which can be used in a for loop.
    
    for key,value in crew.items():    
        print(key,":",value)
        
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

## Now You have learnt about Collection List. Next you have to do is to practice from the List practical [click here]()


# Congratulation! You have Successfully Learned Python Data Structure. :smiley:

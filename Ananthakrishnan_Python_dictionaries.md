## Python Dictionaries

 - A dictionary is a collection which is unordered, changeable and indexed. In Python ,  dictionaries are written with curly brackets  ***{}*** , and they have keys and values.
 - Dictionaries are ***mutable.*** i.e. it is possible to add, modify, delete key-value pairs.
-  The key should be ***unique*** and can be of any data type.

##### syntax:
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


##### syntax:
    thisdict = {
    "Company": "Maruti",
    "model": "Swift",
    "year": 2020,
     "model": "WagonR"   #then the value which is last assigned is considered as the value of the key.
    }
    print(thisdict)
    
###### output:
        {'model': 'WagonR', 'Company': 'Maruti', 'year': 2020}



## Accessing Items 

- You can access the items of a dictionary by referring to its key name, inside square brackets:

***Example***
  Get the value of the **"model**" key:
          

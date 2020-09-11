## Data Structures

### Data Structure is a core concept of computer science by which we can do programming in any other progrmming languages. Data structure are used to store the data elements in a sequential manner.

#### In Python we can call Data Structure as Collections. Collections are containers that are used to store collections of data.
#### There are 4 Built-in collections or data structure namely:-
- List
- Dictionary
- Tuple
- Set

## What is a List?

A List is used to store the sequence of various types of data. Data are inclosed inside [ ] brackets seprated by commas(,). Lists are mutable in nature it means data which can be changed when required. Duplicate entries are allowed in list.  A list can also have another list as an item. This is called a nested list.

###### Syntax:-
    list1 = [ ] #Empty List
    list2 = [ sequence1 ]
    list3 = [ sequence1, sequence2, sequence3 ]
    
###### Example:-
    language = ['C','C++','Java','Python']       //List of Strings
    number = [3,5,4,9]                           //List of Numbers
    mixed = ['Mango','Apple',1,'Banana',8]       //List of Mixed Data Type 
    nested = [['Raman', 'Nikhil'],[2,5,7]]       //List of Nested List
    deep_nested = ['Honey','Deepak',[1,5,8,['Akshay','Shubham',['India','Australia]]]]              //Deeply Nested
    
- Each element in the list has a position in the list known as an index. The list index starts from zero.

| Element |Index|
|-------- |-----|
|  23461  |  0  |
|  77194  |  1  |
|  10295  |  2  |
|  14920  |  3  |

- Index positions actually help us to directly access a value from the list. list_name[index] can be used to directly access the list element at the mentioned index position.
- If we want to access an element directly, we can also use it to directly modify an element in the list.  element[1] = 23413




 # :mortar_board: Python OOPs Concepts

:sparkles: learning OOPs is Smart ~~difficult~~

Like the other general programming languages,Python is also an ***Object-Oriented Programming*** language.
It allows us to develop applictions using an object oriented approach.In Python,we can easily create and use classes and objects

**Major Topics in OOPS are:**

- Class
- Objects
- Methods
- Inheritance
- Polymorphism
- Encapsulation
- Data Abstraction


> This main objective of this documentation is to make understand these concepts in a "Simple way".

**:mag_right: Class:**

 It's the blueprint or design of any object where we intiliaze the necessary parameters to construct our object
 
+ Functions inside class is called as ***Methods***
+ It's good to start a class name with an upper case alphabet (not a necessary condition) and followed by some mthods.


***Syntax***
```
class Classname:
   methods():
      <statements>
```

**:mag_right: Objects:**


The object is an entity that has state and behaviour.

In simple way, it's the output derived from our blue print (i.e, class)

Everything in python is an object and almost everything has attributes and methods.All functions have a built-in attribute **doc**,which returns the doc string defined in the function source code 

we create object by specifying a variable to the class

 ![Class-Objects](https://github.com/bgayathri0606/Open-contributions/blob/master/Github%20images/oop_car.jpg)

***Syntax***
```
class Classname:
  methods():
    <statements>
   
c1 = Classname()
c2 = Classname()     # c1 and c2 are the objects of the "Classname"
```
**:mag_right: Methods:**

The method is a function that is associated with an object. In python, a method is not a unique to class instances. Any object type can have methods

In simple way,Functions inside the class are called as Methods.

**:mag_right: Inheritance:**

Inheritance is the most important aspect of object-oriented programming which simulates the real world concept of inheritance.It specifies that the child object acquires all the properties and behavioursof the parent object

By using inheritance,we can create a class which uses all the properties and behaviour of another class. The new class is also known as *<ins>derived class</ins>* or *<ins>child class</ins>*, and the one whose properties are acquired is known as *<ins>base class</ins>* or  *<ins>parent class</ins>* :dna:

We have 5 types of inheritance 
- Single Inheritance
- Multiple Inheritance
- Multi-level Inheritance
- Hierarical Inheritance
- Hybrid Inheritance

> It provides re-usability of the code

![Inheritance pictorial details](https://github.com/bgayathri0606/Open-contributions/blob/master/Github%20images/inheritance.jpg)

**:mag_right: Polymorphism:**

The name polymorphism itself contains two words "Ploy" and "morphs". poly means "many" and morphs means "form,shape". By this,we can undersatand that one task can be performed in different ways.

***For Example***

You have a class animal, and all animals have voice. But they speak diiferently. Here the 'Speak' behaviour is polymorphic, in the sense and depends on the animal.So, the abstract "animal" concept does not actually "speak" , but specific animals (like dogs and cats) have a concrete implementation of the action "speak".

**:mag_right: Encapsulation:**

Encapsulation is also an important aspect of the object-oriented programming. It is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by an accident.

   - In simple way, we can create a data which cannot be modified i.e, we can create our private data(starts with "__name").If we want to change our private data, we have to create a method inside that class and modify it!
   
   > we can understand this concept in detail, by looking at an example which is in "Bommidi_Python_OOPS.ipynb" file.

**:mag_right: Data Abstraction:**

Data abstraction is achieved through encapsulation. So that's why, Data abstraction and encapsulation both are often used as synonyms. 

Abstraction is used to hide internal details and show only functionalities. Abstracting something means to give names to things so that the name captures the core of what a function or a whole program does.










		




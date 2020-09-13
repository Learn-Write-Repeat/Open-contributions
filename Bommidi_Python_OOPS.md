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

**:point_right: Class:**

 It's the blueprint of any object where we intiliaze the necessary parameters to construct our object
 
+ Functions inside class is called as ***Methods***
+ Class name should start with an upper case alphabet and followed by some methods

***Syntax***
```
class Classname:
   methods():
      <statements>
```

**<ins>2. Objects:</ins>**


The object is an entity that has state and behaviour.Simply, It's the output from our class.
Everything in python is an object and almost everything has attributes and methods.All functions have a built-in attribute **doc**,which returns the doc string defined in the function source code 

we create object by specifying a variable to the class

***Syntax***
```
class Classname:
  methods():
    <statements>
   
c1 = Classname()
c2 = Classname()     # c1 and c2 are the objects of the "Classname"
```
**<ins>3. Methods:</ins>**

The method is a function that is associated with an object. In python, a method is not a unique to class instances. Any object type can have methods

**<ins>Inheritance:</ins>**

Inheritance is the most important aspect of object-oriented programming which simulates the real world concept of inheritance.It specifies that the child object acquires all the properties and behavioursof the parent object

By using inheritance,we can create a class which uses all the properties and behaviour of another class. The new class is also known as *<ins>derived class</ins>* or *<ins>child class</ins>*, and the one whose properties are acquired is known as *<ins>base class</ins>* or  *<ins>parent class</ins>*

> It provides re-usability of the code

**<ins>4. Polymorphism:</ins>**

The name polymorphism itself contains two words "Ploy" and "morphs". poly means "many" and morphs means "form,shape". By this,we can undersatand that one task can be performed in different ways.

***For Example***

You have a class animal, and all animals have voice. But they speak diiferently. Here the 'Speak' behaviour is polymorphic, in the sense and depends on the animal.So, the abstract "animal" concept does not actually "speak" , but specific animals (like dogs and cats) have a concrete implementation of the action "speak".

**<ins>5. Encapsulation:</ins>**

Encapsulation is also an important aspect of the object-oriented programming. It is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by an accident.

**<ins>6. Data Abstraction:</ins>**

Data abstraction is achieved through encapsulation. So that's why, Data abstraction and encapsulation both are often used as synonyms. 

Abstraction is used to hide internal details and show only functionalities. Abstracting something means to give names to things so that the name captures the core of what a function or a whole program does.










		




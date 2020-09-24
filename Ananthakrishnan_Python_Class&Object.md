## PYTHON CLASSES AND OBJECTS
 - Python is an object oriented programming language.
 - A class is a user-defined prototype from which objects are created. 
 - Classes provide a means of  functionality together.
 - Creating a new class creates a new type of object, allowing new instances of that type to be made.
 - Each class instance can have  its own attributes.
 - Class instances can also have methods (defined by its class) for modifying its state.
### POINTS TO REMEMBER ON PYTHON CLASS:
 - Classes are created by keyword class.
 - Attributes are the variables that belong to class.
 - Attributes are always public and can be accessed using dot (.) operator. 


###### Create a **Class**
    To create a class, use the keyword class:
       
     class car:
      x = 5
     print(car)
 
 ###### output:
    <class '__main__.car'>
    
#### Class Objects
 - An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values.
 * An object consists of :
 
         1. State : It is represented by attributes of an object. It also reflects the properties of an object.
         2. Behavior : It is represented by methods of an object. It also reflects the response of an object with other objects.
         3. Identity : It gives a unique name to an object and enables one object to interact with other objects
         
###### Create Object ( Example 1 )
      Now we can use the class named car to create objects:
   
      class car:
          x = 5

     p1 = car()
     print(p1.x)
###### output:
     5
     Maruti

     
###### Example 2     
    class Jeep:  
      
               # A simple class 
               # attribute 
          company = "Maruti"
          location = "India"
  
              # A sample method   
          def test(self):  
               print("I'm from", self.company) 
               print("I'm made in ", self.location) 
  

    # Object instantiation 
    jimny = Jeep() 
  
    # Accessing class attributes 
    # and method through objects 
    print(jimny.company) 
    jimny.test() 

###### output:
    Maruti
    I'm from Maruti
    I'm made in  India
    
In the above example, an object is created which is basically a ***Jeep*** named ***jimny***. This class only has two class attributes that tell us that ***jimny*** is from ***Maruti*** and made from ***India***.<br>
**NOTE**: The  ***self***  parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


***The self Parameter***
 - Class methods must have an extra first parameter in method definition. We do not give a value for this parameter when we call the method, Python provides it.
 - If we have a method which takes no arguments, then we still have to have one argument.
 - This is similar to this pointer in C++ and this reference in Java.
 - The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
 - It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
 ##### Example:
    class Car:
        def __init__(sampleobject, name, price):
            sampleobject.name = name
            sampleobject.age = price

       def myfunc(abc):
           print("Hello ,  my car is " + abc.name)

    p1 = Car("BMW", 1)
    p1.myfunc()
###### output:
    Hello ,  my car is BMW
    
    
 **The __init__() Function**
  - The __init__ method is similar to constructors in C++ and Java.
  - Constructors are used to initialize the object. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. 
  - It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
  - All classes have a function called __init__(), which is always executed when the class is being initiated.
  - Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:


###### Example:
         class Car:
                def __init__(self, company):
                         self.company =  company 
                         

          p1 = Car("Maruti" )

          print(p1.company)
####### output:
              Maruti
**Modify Object Properties**
 - You can modify properties on objects like this:
 ###### Example:
        class Car:
              def __init__(self, model, rate):
                           self.model = model
                           self.rate = rate

              def  myfunc(self):
                           print("Hello my name is " + self.model)

         p1 = Car("Swift", 500000)
         p1.myfunc()
         print(p1.model)
         print("Previous rate of my model was " , p1.rate) 
         p1.rate = 400000
         print("New rate is" , p1.rate)

###### output:
          Hello my name is Swift
          Swift
          Previous rate of my model was  500000
          New rate is 400000
        
        
 **Delete Object Properties**
  - You can delete properties on objects by using the del keyword:

###### Example:
    class Car:
            def __init__(self, model, rate):
                   self.model = model
                   self.rate = rate

            def myfunc(self):
                    print("Hello my name is " + self.model)

     p1 = Car("Swift",500000 )


     del p1.rate
     print(p1.rate)
###### output:
      AttributeError: 'Car' object has no attribute 'rate'
**Delete Objects**
 - You can delete objects by using the del keyword:
 ###### Example :
    class Car:
            def __init__(self, model, rate):
                   self.model = model
                   self.rate = rate

            def myfunc(self):
                    print("Hello my name is " + self.model)

    p1 = Car("Swift",500000 )


    del p1
    print(p1.rate)
##### Outpput :
    NameError: name 'p1' is not defined
***The pass Statement***
 - ***class*** definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
##### Example :
     class Person:
     pass
     # having an empty class definition like this, would raise an error without the pass statement

##### Complete Example
    class Car:  
    
              # Class Variable  
              fav_car = 'Verna'             
    
              # The init method or constructor  
              def __init__(self, model, color):  
      
               # Instance Variable      
               self.model = model 
               self.color = color         
     
    # Objects of Dog class  
    Moderna = Car("swift", "brown")  
    Buziga = Car("wagonR", "black")  
  
    print('Moderna details:')    
    print('Moderna is a', Moderna.fav_car)  
    print('Model: ', Moderna.model) 
    print('Color: ', Moderna.color) 
  
    print('\nBuziga details:')    
    print('Buziga is a', Buziga.fav_car)  
    print('Model: ', Buziga.model) 
    print('Color: ', Buziga.color) 
  
    # Class variables can be accessed using class  
    # name also  
    print("\nAccessing class variable using class name") 
    print(Car.fav_car)
##### output : 
    Moderna is a Verna
    Model:  swift
    Color:  brown

    Buziga details:
    Buziga is a Verna
    Model:  wagonR
    Color:  black

    Accessing class variable using class name 
    Verna

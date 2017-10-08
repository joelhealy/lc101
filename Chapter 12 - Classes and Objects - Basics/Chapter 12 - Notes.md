
# Chapter 12 of LC101 version of Think Python:  Classes and Objects - Basics


## 1. Object-oriented programming

Python is an **object-oriented programming language**.  That means it provides features that support object-oriented programming (**OOP**).

Object-oriented programming has its roots in the 1960s, but it wasn't until the mid 1980s that it became the main programming paradigm used in the creation of new software.

Up to now, some of the programs we have been writing use a procedural programming paradigm.  In procedural programming the focus is on writing functions or *procedures* which operate on data.  In object-oriented programming the focus is on the creation of **objects** which contain both data and functionality together.  Usually, each object definition corresponds to some object or concept in the real world and the functions that operate on that object correspond to the ways we interact with real-world objects.


## 2. A Change of Perspective

In object-oriented programming, the objects are considered the active agents.

Often times *shifting responsibility from the functions onto the objects* makes it possible to write more versatile functions and makes it easier to maintain and reuse code.

The most important advantage of the object-oriented style is that it fits our mental chunking and real-life experience more accurately.


## 3. Objects Revisited

In Python, every value is actually an object.  Programs manipulate those objects, either by performing computation with them or by asking them to perform methods.

You can think of an object as consisting of two things: an internal **state**, and a collection of **methods** that it can perform.

The **state** of an object represents those things that the object knows about itself.

The **methods** of an object are functions that allow you to change its state or ask questions about its state.  Methods are like the actions that an object is able to do, or the questions that an object is able to answer about itself.


## 4. User Defined Classes

We've already seen classes like `str`, `int`, `float` and `Turtle`.  These were defined by Python and made available for us to use.

However, it can be helpful to have data objects that are uniquely tailored to represent concepts related to the specific problem we are trying to solve.  For these situations, Python gives us the ability to **create our own custom classes**.

A custom class (or, *user defined class*) usually comes about when you want to cluster together a few disparate pieces of information into one larger coherent concept.

### Syntax for Defining and Using a Class

To start off, we will define the simplest possible point class, just a "data cluster" composed of an x and a y.  the code for defining our `Point` class looks like this:

```python
# Let's define a Point class!
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0
```

The syntax rules for a class definition are the same as for other compound statements.  There is a header which begins with the keyword, `class`, followed by the name of the class (in this case, `Point`), and ending with a colon.  Notice also that we use a capital "P": the standard convention is that the name of a class should be "CapWords" and start with a capital letter.

Underneath the header, you define the class's methods.  Our `Point` class has only one method so far, `__init__`.  Any time you create a new class, you should include a method with the special name `__init__`.  This **initializer method** is automatically called whenever a new instance of `Point` is created.  It give the programmer the opportunity to set up the attributes required within the new instance by giving them their initial values.  The `self` parameter (you could choose any other name, but nobody ever does!) is automatically set to reference the newly-created object that needs to be initialized.


### Classes vs Objects (or Instances)

It is important to understand the difference between a class, and an individual "instance" of that class.


### More on Constructors

A function invocation like `Turtle()` or `Point()`, which creates a new object instance, is called a **constructor**.  Every class automatically uses the name of the class as the name of the constructor function.  When the constructor function is invoked, a new instance of `Point` or `Turtle` is created, and then inside the `__init__` function you have the opportunity to configure the new instance into some kind of reasonable "default starting state".

It may be helpful to think of a class as *a factory for making objects*.  The class itself isn't an instance of a point, but it contains the machinery to make point instances.  Every time you call the constructor, you're asking the factory to make you a new object.  As the object goes through the production line, its initialization method is executed in order to get the object properly set up with its factory default settings.

The combined process of "make me a new object" and "get its settings initialized to the factory default settings" is called **instantiation**.


## 5. Improving our Constructor

How to add parameters to the constructor.


## 6. Adding Other Methods to our Class

The key advantage or using a class like `Point` rather than something like a simple tuple `(7, 6)` now becomes apparent.  We can add methods to the `Point` class that are sensible operations for points.  Had we chosen to use a simple tuple to represent the point, we would not have this capability.  Creating a class like `Point` brings an exceptional amount of "organizational power" to our programs, and to our thinking.  We can group together the sensible operations and the kinds of data they apply to, and each instance of the class can have its own state.

A **method** behaves like a function but it is invoked on a specific instance.  Methods are access using dot notation.

All methods defined in a class that operate on objects of that class will have `self` as their first parameter.  Again, this serves as reference to the object itself which in turn gives access to the state data inside the object.  The definition will always have one additional parameter as compared to the invocation.


## 7. Objects as Arguments and Parameters

You can pass an object as an argument in the usual way.


## 8. Converting an Object to a String

The naming convention used for special methods consisting of inserting two underscores both before and after the name is common in Python and is called a **dunder**, a shortening of "double underscore".

The `__repr__` method is responsible for returning a string representation as defined by the class creator.  This special method is invoked when an object appears as an argument of the `print` function.  It is required that the `__repr__` method create and *return* a string.

It is also possible to define a `__str__` method for the object which does essentially the same thing as the `__repr__` method.  If we were to do this, then the `print` function would invoke the `__str__` method.  Technically, this is the first thing it tries to do, and then it falls back on invoking the `__repr__` method.

When a programmer changes the meaning of a special method we say that we **override** the method.


## 9. Instances as Return Values

Functions and methods can return objects.  This is actually nothing new since everything in Python is an object an we have been returning values for quite some time.  The difference here is that we want to have the method *create an object* using the constructor and then return it as the value of the method.


## 10. Glossary


**class**  
A class can also be thought of as a template, or blueprint, for the objects that are instances of it. It contains both the attributes and the methods that each instance of it will have.

**constructor**  
The constructor is a “factory” for making new instances of the class. It is called by the same name as the class (e.g., for the Turtle class you call Turtle() to create a new instance). You can customize the constructor by using an initializer method to set up the attributes (i.e. the state) of the new object.

**initializer method**  
A special method in Python (__init__) that is invoked automatically to set a newly-created object’s attributes to its initial (factory-default) state.

**instance**  
An object that belongs to a class. The terms instance and object are used interchangeably.

**instantiate**  
To create an instance of a class, and to run its initializer.

**method**  
A function that is defined inside a class definition and is invoked on instances of that class.

**object**  
A compound data type that is often used to model a thing or concept in the real world. It bundles together data (attributes) and operations on that data (methods).

**object-oriented programming**  
A powerful style of programming in which data and the operations that manipulate it are organized into classes with attributes and methods.

**object-oriented language**  
A language that provides features, such as user-defined classes and inheritance, that facilitate object-oriented programming.

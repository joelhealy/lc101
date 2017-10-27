# Chapter 13 of LC101 version of Think Python:  Classes and Objects - Digging Deeper


## 1. Fractions

The *state* of a fraction object can be completely described by representing
two integers.

```python
class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def get_numerator(self):
        return self.num

    def get_denominator(self):
        return self.den
```


## 2. Object Mutability

We can change the state of a mutable object by making an assignment to one of its instance variables.


## 3. Sameness

**Shallow equality** compares only the references, not the contents of the objects.  Using the `==` operator to check equality between two user defined objects will return the shallow equality result.  In other words, the objects are equal (==) if they are the same object.

**Deep equality** compares the values "deep" in the object, not just the reference to the object.

For lists (or tuples), the `==` operator tests for deep equality.


## 4. Arithmetic Methods

Several of the numeric operators have an associated special method, e.g., `+` and `__add__`, which can be overridden for user defined classes.


## 5. Inheritance

Inheritance is a syntax for defining a custom class that *inherits* much of its structure and behavior from some other class.

In general, the syntax for any subclass that inherits from some **superclass** is:

```python
class Subclass(Superclass):

    # method definitions for Subclass
```

A subclass inherits all the functionality of its superclass, but can additionally define its own new attributes and methods and can override the implementation of preexisting methods.


## 6. Glossary


**deep equality**  
Equality of values, i.e., two references that point to objects that have the same value.

**inheritance**  
Allows us to define a class that “inherits” the functionality of its parent class, or superclass, and enables us to modify or extend that functionality in our new subclass.

**shallow equality**  
Equality of references, or two references that point to the same object.

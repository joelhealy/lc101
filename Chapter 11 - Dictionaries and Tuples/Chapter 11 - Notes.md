# Chapter 11 of LC101 version of Think Python:  Dictionaries and Tuples


## 1. Dictionaries

Sequential collections have items that are ordered from left to right and they use integers as indices to access the values they contain.

**Dictionaries** are a different kind of collection.  They are Python's built-in **mapping type**.  A map is an unordered, associative collection.  The association, or mapping, is from a **key**, which can be any immutable type, to a **value**, which can be any Python data object.

One way to create a dictionary is to start with the empty dictionary and add **key-value pairs**.  The empty dictionary is denoted `{}`.

We can print the current value of a dictionary in the usual way.  The key-value pairs of the dictionary are separated by commas.  Each pair contains a key and a value separated by a colon.


## 2. Dictionary Operations

**Dictionaries are mutable**.

The `del` statement removes a key-value pair from a dictionary.

The `len` function works on dictionaries.  It returns the number of key-value pairs.


## 3. Dictionary Methods

Dictionaries have a number of useful built-in methods.  The following table provides a summary:

Method   | Parameters  | Description
---------|-------------|-------------------------------------------------------
keys     | none        | Returns a view of the keys in the dictionary
values   | none        | Returns a view of the values in the dictionary
items    | none        | Returns a view of the key-value pairs in the dictionary
get      | key         | Returns the value associated with key; None otherwise
get      | key, alt    | Returns the value associated with key; alt otherwise

The `keys` method returns what Python 3 calls a **view** of its underlying keys.  We can iterate over the view or turn the view into a list by using the `list` conversion function.

It is so common to iterate over the keys in a dictionary that you can omit the `keys` method call in the `for` loop -- iterating over a dictionary implicitly iterates over its keys.

```python
inventory = {'a': 1, 'b': 2, 'c': 3}

for k in inventory:
    print("Got key", k)
```

The `values` and `items` methods are similar to `keys`.  They return view objects which can be turned into lists or iterated over directly.  Note that the items are shown as tuples containing the key and the associated value.

```python
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got", k, "that maps to", inventory[k])
```
Note that tuples are often useful for getting both the key and the value at the same time while you are looping.

The `in` and `not in` operators can test if a key is in the dictionary.  Looking up a non-existent key in a dictionary causes a *runtime error*.

The `get` method allows us to access the value associated with a key, similar to the `[]` operator.  The important difference is that `get` will not cause a runtime error if the key is not present.  It will instead return None.

There exists a variation of `get` that allows a second parameter that serves as an alternative return value in the case where the key is not present.


## 4. Aliasing and Copying

Because dictionaries are mutable, like lists, you need to be aware that aliasing can also occur with dictionaries.  Whenever two variables refer to the same dictionary object, changes to one affect the other.

If you want to modify a dictionary and keep a copy of the original, use the dictionary `copy` method.  This is the dictionary equivalent to list cloning.


## 5. Tuples and Mutability

A **tuple**, like a list, is a sequence of items of any type.  Unlike lists, however, *tuples are immutable*.  Syntactically, a tuple is a comma-separated sequence of values.  Although it is not necessary, it is conventional to enclose tuples in parentheses.

Tuples are useful for representing what other languages often call **records** -- some related information that belongs together.  There is no description of what each of these *fields* means.  A tuple lets us "chunk" together related information and use it as a single thing.

Tuples support the same sequence operations as strings and lists.

Functions can return tuples as return values.


## 6. Tuple Assignment

Python has a very powerful **tuple assignment** feature that allows a tuple of variables on the left of an assignment to be assigned values from a tuple on the right of the assignment.

Tuple assignment can be used to swap the values referred to by variables:

```python
(a, b) = (b, a)
```

The left side is a tuple of variables; the right side is a tuple of values.  All the expressions on the right side are evaluated before any of the assignments occur.  This feature makes tuple assignment quite versatile.  Naturally, the number of variables on the left and the number of values on the right have to be the same.


## 7. Sparse Matrices

A matrix is a two dimensional collection, typically thought of as having rows and columns of data.  One of the easiest ways to create a matrix is to use a list of lists.

A sparse matrix can also be represented as a dictionary with keys consisting of tuples representing positions within the matrix that are populated.


## 8. The enumerate Function

Python has a very useful function, `enumerate`, that can be used when iterating through data collections.  This function allows us to easily print (or otherwise use) both the *index* (or *count*) of the item in the collection and the *item* itself.


## 9. Glossary


**dictionary**  
A collection of key-value pairs that maps from keys to values. The keys can be any immutable type, and the values can be any type.

**enumerate**  
A built-in Python function that enables us to iterate over a collection and generate an auto-incremented index to associate with each item.

**key**  
A data item that is mapped to a value in a dictionary. Keys are used to look up values in a dictionary.

**key-value pair**  
One of the pairs of items in a dictionary. Values are looked up in a dictionary by key.

**mapping type**  
A mapping type is a data type comprised of a collection of keys and associated values. Python’s only built-in mapping type is the dictionary. Dictionaries implement the associative array abstract data type.

**tuple**  
A sequential collection of items, similar to a list. Any python object can be an element of a tuple. However, unlike a list, tuples are immutable. 

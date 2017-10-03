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


# Chapter 10 of LC101 version of Think Python:  Lists


## 1. Lists

A **list** is a sequential collection of Python data values, where each value is identified by an index.  The values that make up a list are called its **elements**.  Lists are similar to strings, which are ordered collections of characters, except that the elements of a list can have *any type* and for any one list, the items can be of different types.

There are several ways to create a new list.  The simplest is to enclose the elements in square brackets.

A list within another list is said to be **nested** and the inner list is often called a **sublist**.  There is a special list that contains no elements.  It is call the empty list and is denoted `[]`.

As you would expect, we can assign list values to variables and pass lists to functions.

The syntax for accessing the elements of a list is the same as the syntax for accessing the characters of a string.  We use the index operator (`[]` - not to be confused with an empty list).  The expression inside the brackets specifies the index.  Remember that the indices start at 0.  Any integer expression can be used as an index and negative index values will locate items from the right instead of from the left.

A nested list is a list that appears as an element in another list.  Bracket operators evaluate from left to right.


## 2. Lists and Strings are Similar

Lists, like strings, are collection data types.  Many of the operations you learned to do on strings in the last chapter you can do on lists.  In this lesson we'll review a few of these similarities.

### List Length

As with strings, the function `len` returns the length of a list (the number of items in the list).  However, since lists can have items which are themselves lists, it is important to note that `len` only returns the length of the top-most list.  In other words, sublists are considered to be a single item when counting the length of the list.

### List Membership

`in` and `not in` are boolean operators that test membership in a sequence.

### List Slices

The slice operation we saw with strings also work on lists.

### List Deletion

Although there are many similarities between lists and string, there are some important differences.  Perhaps the most profound is that lists are mutable (can be changed), where as strings are immutable.  An example of this can be seen in list deletion -- an operation that wouldn't be possible on a string, since its collection of characters can't be changed.

The `del` statement removes an element from a list by using its position.

```python
a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)
```

**OUTPUT**
```
['one', 'three']
['a', 'f']
```

As you might expect, `del` handles negative indices and causes a runtime error if the index is out of range.  In addition, you can use a slice as an index for `del`.


## 3. Lists Are Mutable

Unlike strings, lists are **mutable**.  This means we can change an item in a list by accessing it directly as part of the assignment statement.  Using the indexing operators (square brackets) on the left side of an assignment, we can update on of the list items.

An assignment to an element of a list is called **item assignment**.  Item assignment does not work for strings.  Recall that strings are immutable.

By combining assignment with the slice operator we can update several elements at once.  We can also remove elements from a list by assigning the empty list to them.  We can even insert elements into a list by squeezing them into an empty slice at the desired location.


## 4. List Methods

The dot operator can also be used to access built-in methods of list objects.  `append` is a list method which adds the argument passed to it to the end of the list.

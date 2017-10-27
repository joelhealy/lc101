
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

Unlike strings, lists are **mutable**.  This means we can change an item in a list by accessing it directly as part of the assignment statement.  Using the indexing operators (square brackets) on the left side of an assignment, we can update one of the list items.

An assignment to an element of a list is called **item assignment**.  Item assignment does not work for strings.  Recall that strings are immutable.

By combining assignment with the slice operator we can update several elements at once.  We can also remove elements from a list by assigning the empty list to them.  We can even insert elements into a list by squeezing them into an empty slice at the desired location.


## 4. List Methods

The dot operator can also be used to access built-in methods of list objects.  `append` is a list method which adds the argument passed to it to the end of the list.

There are two ways to use the `pop` method.  The first, with no parameter, will remove and return the last item of the list.  If you provide a parameter for the position, `pop` will remove and return the item at that position.  Either way the list is changed.

The following table provides a summary of the list methods.  In the column labeled "result", the word **mutator** means that the list is changed by calling the method on it but nothing is returned (actually `None` is returned).  A **hybrid** method is one that not only changes the list *but also returns a value* as its result.  Finally, if the result is simply a return, then the list is unchanged by the method.

Method  | Parameters     | Result     | Description
--------|----------------|------------|-------------------------------------------
append  | item           | mutator    | Adds a new item to the end of a list
insert  | position, item | mutator    | Inserts a new item at the position given
pop     | none           | hybrid     | Removes and returns the last item
pop     | position       | hybrid     | Remove and returns the item at position
sort    | none           | mutator    | Modifies a list to be sorted
reverse | none           | mutator    | Modifies a list to be in reverse order
index   | item           | return idx | Returns the position of first occurrence of item
count   | item           | return ct  | Returns the number of occurrences of item
remove  | item           | mutator    | Removes the first occurrence of item

It is important to remember that methods like `append`, `sort`, and `reverse` all return `None`.  This means that re-assigning `mylist` to the result of sorting `mylist` will result in losing the entire list.


## 5. Lists and for loops

Returning to the theme of how lists are similar to strings, it is also possible to perform **list traversal** using iteration by item as well as iteration by index, just as we did with strings.

Since lists are mutable, it is often desirable to traverse a list, modifying each of its elements as you go.


## 6. Concatenation and Repetition

As with strings, the `+` operator concatenates lists.  Similarly, the `*` operator repeats the items in a list a given number of times.  It is important to see that these operators **create new lists** from the elements of the operand lists.  Note that concatenation is similar to the append method, but with the important difference that `append` only *modifies* the original list.  It does not *create a new list* as concatenation does.

Also be aware that you can only concatenate *lists* together.  If you want to add an item to a list using concatenation, you must convert the item to a singleton list first.


## 7. Objects and References

An object is something a variable can refer to.

We can test whether two names refer to the same object using the *is* operator.  The *is* operator will return true if the two references are to the same object.  In other words, the references are the same.

Since strings are *immutable*, Python optimizes resources by making two names that refer to the same string value refer to the same object.  **This is not the case with lists.**

A list is **a collection of references to objects**.

Like strings, integers are also immutable, so Python optimizes and lets everyone share the same object.


## 8. Aliasing and Cloning Lists

Since variables refer to objects, if we assign one variable to another, both variables refer to the same object.

When the same list has two different names, we say that it is **aliased**.  *Changes made with one alias affect the other*.

In general, it is safer to avoid aliasing when you are working with mutable objects.  Of course, for immutable objects, there's no problem; they can't be updated or changed.  That's why Python is free to alias strings and integers when it sees an opportunity to economize.

If we want to modify a list and also keep the original list intact and unchanged, we need to be able to make a copy of the list itself, not just the reference.  This process is sometimes called **cloning**, to avoid the ambiguity of the word copy.

The easiest way to clone a list is to use the slice operator.  Taking any slice of a list creates a new list.


## 9. Repetition and References

With a list, the repetition operator creates copies of the references.


## 10. Using Lists as Parameters

There are two types of functions that take lists as parameters, modifiers and pure functions.

### Modifiers

Functions which take lists as arguments and change them during execution are called **modifiers** and the changes they make are called **side effects**.  Passing a list as an argument actually *passes a reference to the list, not a copy of the list*.  Since lists are mutable, changes made to the elements referenced by the parameter change the same list that the argument is referencing.

### Pure Functions

On the contrary, a **pure function** does not produce side effects.  It communicates with the calling program only through parameters (which it does not modify) and a return value.

### Which is Better ###

In general, we recommend that you write pure functions whenever it is reasonable to do so and resort to modifiers only if there is a compelling advantage.


## 11. List Comprehensions

**List comprehensions** are concise ways to create lists.  The general syntax is:

```
[<expression> for <item> in <sequence> if <condition>]
```
where the if clause is optional.

The expression describes each element of the list that is being built.  The `for` clause iterates through each item in a sequence.  The items are filtered by the `if` clause if there is one.


## 12. split and join

The `split` method is used on a string and breaks the string into a list of words.  By default, any number of whitespace characters is considered a word boundary.  An optional argument called a **delimiter** can be used to specify which characters to use as word boundaries.  The delimiter doesn't appear in the result.

The inverse of the `split` method is `join`, which is used on a list.  You choose a desired **separator** string, (often called the *glue*) and join the list with the glue between each of the elements to form a new string.  The list whose elements you glued together is not itself modified.  Also, you can use empty glue or multi-character strings as glue.

### List Type Conversion Function

Python has a built-in type conversion function called `list` that tries to turn whatever you give it into a list.  In general, any sequence can be turned into a list using this function.  The result will be a list containing the elements in the original sequence.  It is not legal to use the `list` conversion function on any argument that is not a sequence.

It is also important to point out that the `list` conversion function will place each element of the original sequence in the new list.  When working with strings, this is very different that the result of the `split` method.  Whereas `split` will break a string into *a list of words*, `list` will always break it into *a list of characters*.


## 13. Glossary


**aliases**  
Multiple variables that contain references to the same object.

**clone**  
To create a new object that has the same value as an existing object. Copying a reference to an object creates an alias but does not clone the object.

**delimiter**  
A character or string used to indicate where a string should be split.

**element**  
One of the values in a list (or other sequence). The bracket operator selects elements of a list.

**list**  
A collection of objects, where each object is identified by a sequential index. Like other types str, int, float, etc. there is also a list type-converter function that tries to turn its argument into a list.

**list traversal**  
The sequential accessing of each element in a list.

**modifier**  
A function which changes its arguments inside the function body. Only mutable types can be changed by modifiers.

**mutable data type**  
A data type in which the elements can be modified. All mutable types are compound types. Lists are mutable data types; strings are not.

**nested list**  
A list that is an element of another list.

**pattern**  
A sequence of statements, or a style of coding something that has general applicability in a number of different situations. Part of becoming a mature Computer Scientist is to learn existing and establish new patterns and algorithms that will form your toolkit. Patterns often correspond to your “mental chunking”.

**pure function**  
A function which has no side effects. Pure functions only make changes to the calling program through their return values.

**sequence**  
Any of the data types that consist of an ordered collection of elements, with each element identified by an index.

**side effect**  
A change in the state of a program made by calling a function that is not a result of reading the return value from the function. Side effects can only be produced by modifiers.

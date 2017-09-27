
# Chapter 9 of LC101 version of Think Python:  Strings


## 1. Strings: A Collection Data Type

Strings are objects with methods that can be performed on them.  They are also what is called a **collection data type**.

Strings are made up of smaller strings each containing one **character**.

Strings can be defined as sequential collections of characters.  This means that the individual characters that make up the string are assumed to be in a particular order from left to right.

A string that contains no characters, often referred to as the **empty string**, is still considered to be a string.  It is simply a sequence of zero characters and is represented by '' or "" (two single or two double quotes with nothing in between).

Types -- like strings and lists -- that are comprised of smaller pieces are called *collection data types*.  Depending on what we are doing, we may want to treat a collection data type as a single entity (the whole), or we may want to access its parts.  This duality is useful.


## 2. Operations on Strings

In general, you cannot perform mathematical operations on strings, even if the strings look like numbers.

Interestingly, the `+` operator does work with strings, but for strings, the `+` operator represents **concatenation**, not addition.  Concatenation means joining the two operands by linking them end-to-end.

The `*` operator also works on strings.  It performs repetition.  For example, `'Fun'*3` is `'FunFunFun'`.  One of the operands has to be a string and the other has to be an integer.

The comparison operators also work on strings.  To see if two strings are equal you simply write a boolean expression using the equality operator.  Other comparison operations are useful for putting words in lexicographical order (all uppercase letters come before all the lowercase letters).

Each character is assigned a unique integer value. "A" is 65, "B" is 66, and "5" is 53.  The way you can find out the so-called **ordinal value** for a given character is to use a string method called `ord`.

There is also a similar, but reverse, method called `chr` that converts integers into their character equivalent.


## 3. Index Operator: Working with the Characters of a String

The **indexing operator**, `[ ]`, selects a single character from a string.  The characters are accessed by their position or index value, indexed from left to right beginning with 0.  It is also the case that the positions are named from right to left using negative numbers where -1 is the rightmost index and so on.

The expression `school[3]` selects the character at index 3 from `school`, and creates a new string containing just this one character.

Python has no special type for a single character.  It is just a string of length 1.

When you are going to be indexing into a string, it is useful to know the length of the string.  The `len` function, when applied to a string, returns the number of characters in a string.


## 4. The Slice Operator

A substring of a string is called a **slice**.

The **slice** operator `[n:m]` returns the part of the string from the n'th characters to the m'th character, including the first but excluding the last.  In other words, start with the character at index n and go up to the character at index m-1.

If you omit the first index (before the colon), the slice starts at the beginning of the string.  If you omit the second index, the slice goes to the end of the string.


## 5. String methods

The *dot notation* is the way we connect the name of an object to the name of a method it can perform.

Strings are also objects.  Each string has its own methods.

Method     | Parameter | Description
-----------|-----------|--------------------------------------------------
upper      | none      | Returns a string in all uppercase
lower      | none      | Returns a string in all lowercase
capitalize | none      | Returns a string with first character capitalized, the rest lower
strip      | none      | Returns a string with the leading and trailing whitespace removed
lstrip     | none      | Returns a string with the leading whitespace removed
rstrip     | none      | Returns a string with the trailing whitespace removed
count      | item      | Returns the number of occurrences of item
replace    | old, new  | Replaces all occurrences of old substring with new
center     | width     | Returns a string centered in a field of width spaces
ljust      | width     | Returns a string left justified in a field of width spaces
rjust      | width     | Returns a string right justified in a field of width spaces
find       | item      | Returns the leftmost index where the substring item is found
rfind      | item      | Returns the rightmost index where the substring item is found
index      | item      | Like find except causes a runtime error if item is not found
rindex     | item      | like rfind except causes a runtime error if item is not found

Note that the methods that return strings *do not change the original*.  Strings are immutable.

The `str.format()` method can be called on a string in order to replace fields delimited by braces `{ }`.  Inside the braces is where you will put either the index of a positional argument, or the name of a keyword argument.  Inside the format() call you put the variable or expression you want to add to the string.

As we stated above, strings are **immutable**, which means you cannot change an existing string.  The best you can do is create a new string that is a variation on the original.


## 6. String Traversal

A lot of computations involve processing a collection one item at a time.  For strings this means that we would like to process one character at a time.  Often we start at the beginning, select each character in turn, do something to it, and continue until the end.  This pattern of processing is called a **traversal**.

The `for` statement can iterate over the items of a sequence (e.g., a list or the sequence of integers created by the `range` function.)

Since a string is simply a sequence of characters, the `for` loop iterates over each character automatically.

We will refer to this type of sequence iteration as **iteration by item**.  Note that it is only possible to process the characters one at a time from left to right.

### The for Loop: By Index

It is also possible to use the `range` runction to systematically generate the indices of the characters.  The `for` loop can then be used to iterate over these positions.  These positions can be used together with the indexing operator to access the individual characters in the string.

Iteration by position allows the programmer to control the direction of the traversal by changing the sequence of index values.

### The while Loop: By Index

The `while` loop can also control the generation of the index values.  Remember that the programmer is responsible for setting up the initial condition, making sure that the condition is correct, and making sure that something changes inside the body to guarantee that the condition will eventually fail and we avoid an infinite loop.

## 7. Looping and Counting

If you want to find out if a particular character is in a string, you could iterate through the string and compare each character to the desired character and then return a boolean value indicating if it was found or not.  But you could also just use the convenient `in` operator (or its opposite, `not in`) and it will return the same information.  The `in` operator tests if one string is a substring of another.

Note that a string is a substring of itself, and the empty string is a substring of any other string.


## 8.  Character Classification

The `string` module provides several constants that are useful.  One of these, `string.digits` is equivalent to "0123456789".  It can be used to check if a character is a digit using the `in` operator.

The string `string.ascii_lowercase` contains all of the ascii letters that the system considers to be lowercase.  Similarly, `string.ascii_uppercase` contains all of the uppercase letters.  `string.punctuation` comprises all the characters considered to be puctuation.


## 9. Summary

**indexing(`[ ]`)**  
Access a single character in a string using its postion (starting from 0).

**length function(`len`)**  
Returns the number of characters in a string.

**for loop traversal(`for`)**  
*Traversing* a string means accessing each character in the string, one at a time.

**slicing(`[:]`)**  
A *slice* is a substring of a string.

**string comparison(`>, <, >=, <=, ==, !=`)**  
The six common comparison operators work with strings, evaluating according to lexicographical order.  All upper case letters precede lower case letters.

**in and not in operator(`in`, `not in`)**  
The `in` operator tests whether one string is contained inside another string.


## 10. Glossary

**collection data type**  
A data type in which the values are made up of components, or elements, that are themselves values.

**dot notation**  
Use of the **dot operator**, `.`, to access functions inside a module, or to access methods and attributes of an object.

**immutable**  
Data types whose content cannot be changed after creation (e.g., strings, ints, floats, tuples).

**index**  
A variable or value used to select a memeber of an ordered collection, such as a character from a string, or an element from a list.

**slice**  
A part of a string (substring) specified by a range of indices.  More generally, a subsequence of any sequence type in Python can be created using the slice operator (`sequence[start:stop]`).

**traverse**  
To iterate through the elements of a collection, performing a similar operation on each.

**whitespace**  
Any of the charactrers that move the cursor without printing visible characters.  The constant `string.whitespace` contains all the white-space characters.

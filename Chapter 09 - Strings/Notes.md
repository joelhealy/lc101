
# Chapter 9 of LC101 version of Think Python:  Strings


## 1. Strings: A Collection Data Type

Strings are objects with methods that can be performed on them.  They are also what is called a **collection data type**.

Strings are made up of smaller strings each containing one **character**.

Strings can be defined as sequential collections of characters.  This means that the individual characters that make up the string are assumed to be in a particular order from left to right.

A string that contains no characters, often referred to as the **empty string**, is still considered to be a string.  It is simply a sequence of zero characters and is represented by '' or "" (two single or two double quotes with nothing in between).

Types -- like strings and lists -- that are comprised of smaller ieces are called *collection data types*.  Depending on what we are doing, we may want to treat a collection data type as a single entity (the whole), or we may want to access its parts.  This duality is useful.


## 2. Operations on Strings

In general, you cannot perform mathematical operations on strings, even if the strings look like numbers.

Interesting, the `+` operator does work with strings, but for strings, the `+` operator represents **concatenation**, not addition.  Concatenation means joining the two operands by linking them end-to-end.

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

Strings are also object.  Each string has its own methods.

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

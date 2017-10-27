# Optional Chapter of LC101 version of Think Python:  Recursion


## 1. What Is Recursion?

**Recursion** is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially.  Usually recursion involves a function calling itself.


## 2. Calculating the Sum of a List of Numbers

A recursive function is a function that calls itself.


## 3. The Three Laws of Recursion

1.  A recursive algorithm must have a **base case**.
1.  A recursive algorithm must change its state and move toward the base case.
1.  A recursive algorithm must call itself, recursively.

A base case is the condition that allows the algorithm to stop recursing.  A base case is typically a problem that is small enough to solve directly.

We must arrange for a change of state that moves the algorithm toward the base case.  Usually the data that represents our problem gets smaller in some way.


## 4. Converting an Integer to a String in Any Base


## 5. Visualizing Recursion

The definition of a fractal is that when you look at it the fractal has the same basic shape no matter how much you magnify it.


## 6. Sierpinski Triangle


## 7. Glossary


**base case**  
A branch of the conditional statement in a recursive function that does not give rise to further recursive calls.

**data structure**  
An organization of data for the purpose of making it easier to use.

**exception**  
An error that occurs at runtime.

**handle an exception**  
To prevent an exception from terminating a program by wrapping the block of code in a try / except construct.

**immutable data type**  
A data type which cannot be modified. Assignments to elements or slices of immutable types cause a runtime error.

**infinite recursion**  
A function that calls itself recursively without ever reaching the base case. Eventually, an infinite recursion causes a runtime error.

**mutable data type**  
A data type which can be modified. All mutable types are compound types. Lists and dictionaries (see next chapter) are mutable data types; strings and tuples are not.

**raise**  
To cause an exception by using the raise statement.

**recursion**  
The process of calling the function that is already executing.

**recursive call**  
The statement that calls an already executing function. Recursion can even be indirect — function f can call g which calls h, and h could make a call back to f.

**recursive definition**  
A definition which defines something in terms of itself. To be useful it must include base cases which are not recursive. In this way it differs from a circular definition. Recursive definitions often provide an elegant way to express complex data structures.

**tuple**  
A data type that contains a sequence of elements of any type, like a list, but is immutable. Tuples can be used wherever an immutable type is required, such as a key in a dictionary (see next chapter).

**tuple assignment**  
An assignment to all of the elements in a tuple using a single assignment statement. Tuple assignment occurs in parallel rather than in sequence, making it useful for swapping values.

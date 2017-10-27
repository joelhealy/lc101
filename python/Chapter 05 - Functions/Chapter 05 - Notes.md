# Chapter 5 of LC101 version of Think Python:  Functions


## Functions

In Python, a **function** is a named sequence of statements that belong together.  Their primary purpose is to help us organize programs into chunks that match how we think about the solution to the problem.

The syntax for a **function definition** is:

```python
def name( parameters ):
    statements
```

The parameters specify what information, if any, you have to provide in order to use the function.

There can be any number of statements inside the function, but they have to be indented from the `def` line.  Use the standard indentation of four spaces.

Function definitions are the second of several **compound statements** we will see, all of which have the same pattern:

1.  A **header** line which begins with a keyword and ends with a colon.
1.  A **body** line consisting of one or more Python statements, each indented the same amount - *4 spaces is the Python standard* - from the header line.

We've already seen the `for` loop which is also a compound statement and therefore follows this pattern.

In a function definition, the keyword in the header is `def`, which is followed by the name of the function and some *parameters* enclosed in parentheses.  The parameter list may be empty, or it may contain any number of parameters separated from one another by commas.  In either case, the parentheses are required.

In the definition, the parameter list is more specifically known as the **formal parameters**.  When you call a function, you provide values to the formal parameters.  These values, often called **arguments** or **actual parameters**, are passed to the function by the user.

If the first thing after the function header is a string (some tools insist that it must be a triple-quoted string), it is called a **docstring** and gets special treatment in Python and in some of the programming tools.

One way to retrieve the information in this string is to use the interactive interpreter, and enter the expression `<function_name>.__doc__` which will retrieve the docstring for the function.  So the string you write as documentation at the start of a function is retrievable by Python tools *at runtime*.  This is different from comments in your code, which are completely eliminated when the program is parsed.

By convention, Python programmers use docstrings for the key documentation of their functions.

Defining a new function does not make the function run.  To do that we need a **function call**.  This is also known as a **function invocation**.  Function calls contain the name of the function to be executed followed by a list of values, called *arguments*, which are assigned to the parameters in the function definition.


## Functions That Return Values

Most functions require arguments -- values that control how the function does its job.

Python has a built-in function `abs` for computing the absolute value.

The math module contains a function called `pow` which takes two arguments, the base and the exponent.  Of course, we have already seen that raising a base to an exponent can be done with the ** operator.

Another built-in function that takes more than one argument is `max` which can be sent any number of arguments, separated by commas, and will return the maximum value sent.  The arguments can be either simple values or expressions.  Note that `max` also works on lists of values.

Functions that return values are sometimes called **fruitful functions**.  In may other languages, a chunk that *doesn't* return a value is called a **procedure**, but we will stick here with the Python way of simply calling it a function, or if we want to stress its lack of a return value, a *non-fruitful* function.

The **return** statement is followed by an expression which is evaluated.  Its result is returned to the caller as the "fruit" of calling the function.

All Python functions return the value `None` unless there is an explicit return statement with a value other than `None`.


## Parameters and Local Variables

An assignment statement in a function creates a **local variable** for the variable on the left hand side of the assignment operator.  It is called local because this variable only exists inside the function and you cannot use it outside of it.

When the execution of the function terminates (returns), the local variables are destroyed.

Formal parameters are also local and act like local variables.

It is not possible for a function to set some local variable to a value, complete its execution, and then when it is called again next time, recover the local variable.  Each call of the function creates new local variable, and their lifetimes expire when the function returns to the caller.

It is legal for a function to access a global variable.  However, this is considered **bad form** by nearly all programmers and should be avoided.

Python first looks at the variables that are defined as local variables in the function.  We call this the **local scope**.  If the variable name is not found in the local scope, then Python looks at the global variables, or **global scope**.

There is another important aspect of local versus global variables: *assignment statements in the local function cannot change variables defined outside the function*.

When a local variable has the same name as a global variable we say that the local shadows the global.  A **shadow** means that the global variable cannot be accessed by Python because the local variable will be found first.


## The Accumulator Pattern

The pattern of iterating the updating of a variable is commonly referred to as the **accumulator pattern**.  We refer to the variable as the **accumulator**.  The key to making it work successfully is to be sure to initialize the variable before you start the iteration.  Once inside the iteration, it is required that you update the accumulator.


## Functions Can Call Other Functions

It is important to understand that each of the functions we write can be used and called from other functions we write.  This is one of the most important ways that computer scientists take a large problem and break it down into a group of smaller problems.  This process of breaking a problem into smaller subproblems is called **functional decomposition**.

* Creating a new function gives you an opportunity to name a group of statements.  Functions can simplify a program by hiding a complex computation behind a single command.  The function (including its name) can capture your mental chunking, or **abstraction**, of the problem.
* Creating a new function can make a program smaller by eliminating repetitive code.
* Sometimes you can write functions that allow you to solve a specific problem using a more general solution.


## Flow of Execution Summary

When you are working with functions it is really important to know the order in which statements are executed.  This is called the **flow of execution** or **control flow**.

Execution always begins at the first statement of the program.  Statements are executed one at a time, in order, from top to bottom.  Function *definitions* do not alter the flow of execution of the program, but remember that statements inside the function are not executed until the function is called.  Function calls are like a detour in the flow of execution.  Instead of going to the next statement, the flow jumps to the first line of the called function, executes all the statements there, and the comes back to pick up where it left off.


## Using a main Function

Our program structure is as follows:

1.  Import any modules that will be required.
1.  Define any functions that will be needed.
1.  Define a `main` function that will do the necessary setup to get the program started.
1.  Invoke the `main` function (which will in turn call the other functions as needed).

In Python there is nothing special about the name `main`.  We could have called this function anything we wanted.  We chose `main` by convention and to be consistent with other major languages.

Before the Python interpreter executes your program, it defines a few special variables.  One of those variables is called `__name__` and it is automatically set to the string value `"__main__"` when the program is being executed by itself in a standalone fashion.  On the other hand, if the program is being imported by another program, then the `__name__` variable is set to the name of that module.  This means that we can know whether the program is being run by itself or whether it is being used by another program and based on that observation, we may or may not choose to execute some of the code that we have written.


## Program Development

The goal of **incremental development** is to avoid long debugging sessions by adding and testing only a small amount of code at a time.

The key aspects of the process are:

1.  Start with a working skeleton program and make small incremental changes.  At any point, if there is an error, you will know exactly where it is.
1.  Use temporary variables to hold intermediate values so that you can easily inspect and check them.
1.  Once the program is working, you might want to consolidate multiple statements into compound expressions, but only do this if it does not make the program more difficult to read.


## Composition

The ability to build functions by using other functions is called **composition**.


## A Turtle Bar Chart

* We can get a turtle to display text on the canvas at the turtle's current position.  This method is called `write`.
* We can fill a shape (circle, semicircle, triangle, etc.) with a fill color.  It is a two-step process.  First you call the method `begin_fill`, then you draw the shape.  Finally, you call `end_fill`.
* We've previously set the color of our turtle -- we can now also set it's fill color, which need not be the same as the turtle and the pen color.  To do this, we use a method called `fillcolor`.

We can use the `setworldcoordinates` method the the `Screen` class to rescale the window.


## Programming With Style

Readability is very important to programmers, since programs are read and modified far more often than they are written.

*  use 4 spaces for indentation
*  imports should go at the top of the file
*  keep function definitions together in the file (not littered throughout your code)
*  keep top level statements, including function calls, together at the bottom of the program, preferably in a `main` function.


## Glossary

**composition (of functions)**

**fruitful function**

**incremental development**

**None**

**return value**

**temporary variable**

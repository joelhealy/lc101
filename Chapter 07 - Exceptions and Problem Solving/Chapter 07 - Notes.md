# Chapter 7 of LC101 version of Think Python:  Exceptions and Problem Solving


## Intro to Exceptions

An **exception** is a signal that a condition has occurred that can't easily be handled using the normal flow of control of a Python program.

*Exceptions* are often defined as being "errors" but that is not always the case.  Programmers can create exceptions in response to any special situation -- not just an error -- that they think it would be useful to change the flow of control to handle.  In other words, all errors in Python are dealt with using exceptions, but not all exceptions are errors.

The normal flow of execution is for Python to execute statements sequentially, one after the other.  For three constructs, `if` statements, loops, and function invocations, this sequential executions is interrupted.

*  For `if` statements, *only one* of several statement blocks is executed, then flow of control jumps to the first statement after the `if` statement.
*  For loops, when the end of the loop is reached, flow of control jumps back to the start of the loop and a conditions is used to determine if the loop needs to execute again.  If the loop is finished, flow of control jumps to the first statement after the loop.
*  For function invocations, flow of control jumps to the first statement in the called function, the function is executed, and the flow of control jumps back to the next statement after the function call.

Even when the flow of control is not *purely* sequential, it always executes the first statement *immediately following* the altered flow of control.

An exception is a message to any function currently on the executing program's **run-time stack**.  (The run-time stack is what keeps track of the active function calls while a program is executing.  It is also known as a call stack.)

In Python, you create an exception message using the `raise` command.  The simples format for a `raise` command is the keyword `raise` followed by the name of an exception.  Notice that the Pythonic naming convention for exceptions is the use the *CapWords* case.  It is also conventional for the last word of the exception name to be "Error", if the exception is indeed an error.

```python
raise ExceptionName
```

So what happens to an exception message after it is created?  The normal flow of  control of a Python program is interrupted and Python starts looking for any code in its run-time stack that is interested in dealing with the message.  It always searches from its current location at the bottom of the run-time stack, up the stack, in the order the functions were originally called.  The first `try: except:` block that Python finds on its search back up the run-time stack will be executed.  If there is no `try: except:` block found, the program "crashes" and prints its run-time stack to the console.

An *exception* is a message that something "out-of-the-ordinary" has happened and the normal flow of control needs to be circumvented.  When an exception is raised, Python searches its run-time stack for a `try: except:` block that can appropriately deal with the situation.  The first `try: except:` block that knows how to deal with the issue is executed, and then flow of control is returned to its normal sequential execution.  If no appropriate `try: except` block is found, the program "crashes" and prints its run-time stack to the console.


## Standard Exceptions

Good exceptions handling involves **both** creating exceptions for special cases unique to your program and then catching and handling these with `try: except` blocks **and** catching and handling **standard exception** that you think may be triggerred by your program.

Standard exceptions are exceptions that are built into Python; most of them are listed below.  They are organized into related groups based on the types of issues they deal with.


Language Exceptions  |  Description
---------------------|---------------------------------------------------------
StandardError        |  Base class for all built-in exceptions except StopIteration and SystemExit.
ImportError          |  Raised when an import statement fails.
SyntaxError          |  Raised when there is an error in Python syntax.
Indentation Error    |  Raised when indentation is not specified properly.
NameError            |  Raised when an identifier is not found in the local or global namespace.
UnboundLocalError    |  Raised when trying to access a local variable in a function or method but no value has been assigned to it.
TypeError            |  Raised when an operation or function is attempted that is invalid for the specified type.
LookupError          |  Base class for all lookup errors.
IndexError           |  Raised when an index is not found in a sequence.
KeyError             |  Raised when the specified key is not found in the dictionary.
ValueError           |  Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.
RuntimeError         |  Raised when a generated error does not fall into any category.
MemoryError          |  Raised when a operation runs out of memory.
RecursionError       |  Raised when the maximum recursion depth has been exceeded.
SystemError          |  Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.


Math Exceptions      |  Description
---------------------|---------------------------------------------------------
ArithmeticError      |  Base class for all errors that occur for numeric calculation.  You know a math error occurred, but you don't know the specific error.
OverflowError        |  Raised when a calculation exceeds maximum limit for a numeric type.
FloatingPointError   |  Raised when a floating point calculation fails.
ZeroDivisionError    |  Raised when division or modulo by zero takes place for all numeric types.


I/O Exceptions       |  Description
---------------------|---------------------------------------------------------
FileNotFoundError    |  Raised when a file or directory is requested but doesn't exist.
IOError              |  Raised when an input/output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.  Also raised for operating system-related errors.
PermissionError      |  Raised when trying to run an operation without the adequate access rights.
EOFError             |  Raised when there is no input from either the raw_input() or input() function and the end of file is reached.
KeyboardInterrupt    |  Raised when the user interrupts program execution, usually by pressing Ctrl+c.


Other Exceptions     |  Description
---------------------|---------------------------------------------------------
Exception            |  Base class for all exceptions.  This catches most exception messages.
StopIteration        |  Raised when the next() method of an iterator does not point to any object.
AssertionError       |  Raised in case of failure of the Assert statement.
SystemExit           |  Raised when Python interpreter is quit by using the sys.exit() function.  If not handled in the code, it causes the interpreter to exit.
OSError              |  Raises for operating system related errors.
EnvironmentError     |  Base class for all exceptions that occur outside the Python environment.
AttributeError       |  Raised in case of failure of an attribute reference or assignment.
NotImplementedError  |  Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.

All exceptions are objects.  The classes that define the objects are organized ina hierarchy, which is shown below.  This is important because the parent class of a set of related exceptions will catch all exception messages for itself and its child exceptions.

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```


## Principles for Using Exceptions

The purpose of an exception is to modify the flow of control, not to catch simple errors.  If your `try: except:` block is in the same function that `raises` the exceptions, you are probably misusing exceptions.

```
Principle 1:

If a condition can be handled using the normal flow of control, don't use an exception!
```

```
Principle 2:

If you call a function that potentially raises exceptions, and you can do something appropriate to deal with the exception, then surround the code that contains the *function call* with a `try: except:` block.
```

```
Principle 3:

If you call a function that potentially raises exceptions, and you can't do anything meaningful about the conditions that are raised, then don't catch the exception message(s).
```


## Exception Syntax

### Catch All Exceptions

Catch all exceptions, regardless of their type.  This will prevent your program from crashing, but this type of exception handling is rarely useful because you can't do anything meaningful to recover from the abnormal condition.  In fact, you don't even know what the abnormal condition is since it could be *any* exception.

```python
try:
    # Your normal code goes here.
    # Your code should include function calls which might raise exceptions.
except:
    # If ANY exception was raised, then execute this code block
```

### Catch A Specific Exception

This is perhaps the most often used syntax.  It catches one specific condition and tries to recover from the condition.

```python
try:
    # Your normal code goes here.
    # Your code should include function calls which might raise exceptions.
except ExceptionName:
    # If ExceptionName was raised, then execute this block
```

### Catch Multiple Specific Exceptions

If you are writing a code block that contains calls to fucntions that may raise multiple different exceptions, then you can write separate `except` clauses to handle each.  You may also include an `else` clause after your `except` clauses to contain any code that you want to run in case the `try` clause does *not* raise an exception.

```python
try:
    # Your normal code goes here.
    # Your code should include function calls which might raise exceptions.
except ExceptionOne:
    # If ExceptionOne was raised, then execute this block.
except ExceptionTwo:
    # If ExceptionTwo was raised, then execute this block.
else:
    # If there was no exception then execute this block.
```

Be aware that when you have more than one `except` clause in a `try: except:` block, it is only *the first* matching exception that will be triggered and have its code block executed.  Therefore, you want to list the exceptions in the order of more specific to less specific.

### Clean-up After Exceptions

If you have code that you want to be executed even if exceptions occur, you can include a `finally` code block:

```python
try:
    # Your normal code goes here.
    # Your code might include function calls which might raise exceptions.
    # If an exception is raised, some of these statements might not be executed.
finally:
    # This block of code will always execute, even if there are exceptions raised
```

There are even more syntactical variations for exceptions handling than those covered above.  Reference the Python Tutorial.

One place where you will always want to include exception handling is when you read or write to a file.


## Principles of Problem Solving

### Don't Panic!

You will sometimes feel anxiety creep in when starting a new problem.  This is natural.  When this happens, just acknowledge it and put it aside.

If you want to be an outstanding programmer, then bugs and difficult problems are your teachers and your best friends.

### Restate the Problem

When a problem is presented to you, in writing or verbally, restating the problem ensures that you understand precisely what you're being asked to do.

### Outline the Problem

Here are two strategies for outlining:

*  Write down what you know.
*  Subdivide the problem.

### Reduce the Problem

When it's not clear how to approach a problem, make the problem smaller.  This will give you a stepping stone on the path to the ultimate solution.  Solving a smaller version of the problem can often reveal an approach that can be generalized to the larger problem

### Look for Similarities

Have you solved a problem that has some similarities to the one at hand?  If so, go back and review that solution.  Think about how the problems are similar, and how they are different.  Are any of the techniques you used then applicable now?  What new techniques will you need to learn or utilize to solve this new problem?

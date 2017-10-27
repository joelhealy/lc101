# Chapter 2 of LC101 version of Think Python:  Simple Python Data


## Values and Data Types

A **value** is one of the fundamental things -- like a word or a number -- that a program manipulates.

We often refer to values as **objects** and we will use the words value and object interchangeably.

These objects are classified into different **classes**, or **data types**.

If you are not sure what class a value falls into, Python has a function called `type()` which can tell you.

Numbers with a decimal point belong to a class called **float**.

At this stage, you can treat the words *class* and *type* interchangeable.  (We'll come back to a deeper understanding of what a class is in later chapters.)

Strings in Python can be enclosed in either single quotes (`'`) or double quotes (`"`), or three of each (`'''` or `"""`).

Triple quoted strings can span multiple lines.

The `print()` function can print any number of values as long as you separate them by commas.  Notice that the values are separated by spaces when they are displayed.

Formal languages are strict, the notation is concise, and even the smallest change might mean something quite different from what you intended.


## Type conversion functions

The functions `int()`, `float()` and `str()` will attempt to convert their arguments into types `int`, `float` and `str` respectively.  We call these **type conversion** functions.

The `int()` function can take a floating point number or string, and turn it into an integer.  For floating point numbers, it *discards* the decimal part of the number - a process we call *truncation towards zero* on the number line.

The type converter `float()` can turn an integer, a float, or a syntactically legal string into a float.

The type converter `str()` turns its argument into a string.  Remember that when we print a string, the quotes are removed.


## Variables

A **variable** is a name that refers to a value.

**Assignment statements** create new variables and also give them values to refer to.

The **assignment token**, `=`, should not be confused with *equality* (we will see later that equality uses the `==` token).  The assignment statement links a *name*, on the left hand side of the operator, with a *value*, on the right hand side.

When reading or writing code, say to yourself "n is assigned 17" or "n gets the value 17" or "n is a reference to the object 17" or "n refers to the object 17".  Don't say "n equals 17".

A common way to represent variables on paper is to write the name with an arrow pointing to the variable's value.  This kind of figure, known as a **reference diagram**, is often called a **state snapshot**.

If you ask Python to evaluate a variable, it will produce the value that is currently linked to the variable.

The type of a variable is the type of the object it currently refers to.

Variables are *variable*.  This means they can change over time.  You can assign a value to a variable, and later assign a different value to the same variable.


## Variable Names and Keywords

**Variable names** can be arbitrarily long.  They can contain both letters and digits, but they have to begin with a letter or an underscore.  Although it is legal to use uppercase letters, by convention we don't.  Case matters!

Variable names can never contain spaces.

The underscore character (`_`) can also appear in a name.  It is often used in names with multiple words.  There are some situations in which names beginning with an underscore have special meaning, so a safe rule for beginners is to start all names with a letter.

**Keywords** are reserved words and cannot be used as variable names.  They define the language's syntax rules and structure.

Python has thirty-something keywords including:
```
and      as        assert    break     class     continue
def      del       elif      else      except    import
finally  for       from      global    if        or
in       is        lambda    nonlocal  not       with
pass     raise     return    try       while     yield
None     True      False```

Programmers generally choose names for their variables that are meaningful to the human readers of the program -- they help the programmer document, or remember, what the variable is used for.


## Statements and Expressions

A **statement** is an instruction that the Python interpreter can execute.

An **expression** is a combination of values, variables, operators, and calls to functions.  Expressions need to be evaluated.  If you ask Python to *print* an expression, the interpreter **evaluates** the expression and displays the result.

`len()` is a built-in Python function that returns the number of characters in a string.

The *evaluation of an expression* produces a value, which is why expressions can appear on the right hand side of assignment statements.  A value all by itself is a simple expression, and so is a variable.  Evaluating a variable gives the value that the variable refers to.

Statements, such as the assignment statement, do not return a value.  They are simply executed.


## Operators and Operands

**Operators** are special tokens that represent computations like addition, multiplication and division.  The values the operator works on are called **operands**.

The tokens `+` and `-`, and the use of parenthesis for grouping, mean in Python what they mean in mathematics.  The asterisk (`*`) is the token for multiplication, and `**` is the token for exponentiation.

When a variable name appears in the place of an operand, it is replaced with the value that it refers to before the operation is performed.

In Python 3, division is denoted by the operator token `/` which always evaluates to a floating point result.

**Integer division**, uses the token `//`.  it always *truncates* its result down to the next smallest integer (to the left on the number line).

The **modulo operator**, sometimes also called **modulus**, the **remainder operator**, or **integer remainder operator** works on integers (and integer expressions) and yields the remainder when the first operand is divided by the second.  In Python, the modulus operator is a percent sign (`%`).


## Input

In Python, there is a built-in function to get input from the user called unsurprisingly `input()`.

The `input` function allows the coder to provide a **prompt string**.  When the function is evaluated, the prompt is shown.  The `input` function returns a string value.


## Order of Operations

When more than one operator appears in an expression, the order of evaluation depends on the **rules of precedence**.  Python follows the same precedence rules for its mathematical operators that mathematics does.

1. Parentheses have the highest precedence and can be used to force an expression to evaluate in the order you want.
1. Exponentiation has the next highest precedence.
1. Multiplication and both division operators have the same precedence, which is higher than addition and subtraction, which also have the same precedence.
1. Operators with the *same* precedence are evaluated from left-to-right.  In algebra we say they are *left-associative*.  An exception to the left-to-right associative rules is the exponentiation operator `**` which associates right-to-left.


## Reassignment

It is legal to make more than one assignment to the same variable.  A new assignment makes an existing variable refer to a new value (and stop referring to the old value).


## Updating Variables

One of the most common forms of reassignment is an **update** where the new value of the variable depends on the old.  For example,
```
x = x + 1
```
Remember that executing assignment is a two-step process:

1. Evaluate the right-hand expression.
1. Set the variable name on the left-hand side refer to this new resulting object.

Before you can update a variable, you have to **initialize** it, usually with a simple assignment.  Updating a variable by adding 1 is called an **increment**; subtracting 1 is called a **decrement**.

For incrementing, instead of `x = x + 1` you can use: `x += 1`.  For decrementing, instead of `x = x - 1` you can use: `x -= 1`.


## Glossary

**assignment statement**

**assignment token**

**class**

**comment**

**data type**

**decrement**

**evaluate**

**expression**

**float**

**increment**

**initialization (of a variable)**

**int**

**integer division**

**keyword**

**modulus operator**

**object**

**operand**

**operator**

**prompt string**

**reference diagram**

**rules of precedence**

**state snapshot**

**statement**

**str**

**type conversion function**

**value**

**variable**

**variable name**

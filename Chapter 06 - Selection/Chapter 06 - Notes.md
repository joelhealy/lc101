# Chapter 6 of LC101 version of Think Python:  Selection


## Boolean Values and Boolean Expressions

The Python type for storing true and false values is called `bool`, named after the British mathematician, George Boole.  George Boole created Boolean Algebra which is the basis of all modern computer arithmetic.

There are only two **boolean values**.  They are `True` and `False`.  Capitalization is important, since "true" and "false" are not boolean values in Python (remember Python is case sensitive).

Boolean values are not strings!  It is extremely important to realize that `True` and `False` are not strings.  They are not surrounded by quotes.  They are the only two values in the data type `bool`.

A **boolean expression** is an expression that evaluates to a boolean value.  The equality operator, `==`, compares two values and produces a boolean value related to whether the two values are equal to one another.

The `==` operator is one of six common **comparison operators**; the others are:

```python
x != y        # x is not equal to y
x > y         # x is greater than y
x < y         # x is less than y
x >= y        # x is greater than or equal to y
x <= y        # x is less than or equal to y
```

Remember that `=` is an *assignment* operator and `==` is a *comparison* operator.

Note too that an equality test is symmetric, but assignment is not.


## Logical Operators

There are three **logical operators**: `and`, `or`, and `not`.  The semantics (meaning) of these operators is similar to their meaning in English.

In Python it is permissible to write `x < y < z` which means the same as its mathematical expression and is functionally equivalent to the Python expression `x < y and y < z`.

p      | q      | p and q
-------|--------|--------
True   | True   | True
True   | False  | False
False  | True   | False
False  | False  | False

p      | q      | p or q
-------|--------|--------
True   | True   | True
True   | False  | True
False  | True   | True
False  | False  | False

p      | not p
-------|------
True   | False
False  | True


## Precedence of Operators

Python will always evaluate the arithmetic operators first.  Next comes the relational (or *comparison*) operators.  Finally, the logical operators are done last.

Level    | Category        | Operators
---------|-----------------|---------------------
7(high)  | exponent        | **
6        | multiplication  | *, /, //, %
5        | addition        | +, -
4        | relational      | ==, !=, <=, >=, >, <
3        | logical         | not
2        | logical         | and
1(low)   | logical         | or


## Conditional Execution: Binary Selection

**Selection statements**, sometimes also referred to as **conditional statements**, give us the ability to check conditions and change the behavior of the program accordingly.  The simplest form of slection is the `if` **statement**.  This is sometimes referred to as **binary selection** since there are two possible paths of execution.

The syntax for an `if` statment looks like this:

```python
if BOOLEAN EXPRESSION:
    STATEMENTS_1         # executed if condition evaluates to True
else:
    STATEMENTS_2         # executed if condition evaluates to False
```

The boolean expression after the `if` statement is called the **condition**.  If it is true, then the indented statements get executed.  If not, then the statements indented under the `else` clause get executed.  The indented statments are called a **block**.  The first unindented statment marks the end of the block.

There is no limit on the number of statments that can appear under the two clauses of an `if` statement, but there has to be at least one statement in each block.  Also, not that each `if` statement can have only *one* `else` clause.


## Omitting the else Clause: Unary Selection

Another form of the `if` statement is one in which the `else` clause is omitted entirely.  This creates what is sometimes called **unary selection**.  In this case, when the condition evaluates to `True`, the statements are executed.  Otherwise the flow of execution continues to the statement after the body of the `if`.


## Nested Conditionals

One conditional can also be **nested** within another.

In some programming languages, matching the `if` and the `else` can be confusing.  However, in Python this is not the case.  The indentation pattern tells us exactly which `else` belongs to which `if`.


## Chained Conditionals

Python provides an alternative way to write nested selection.  This is sometimes referred to as a **chained conditional**.

```python
if BOOLEAN EXPRESSION_1:
    STATEMENTS_1
elif BOOLEAN EXPRESSION_2:
    STATEMENTS_2
else:
    STATEMENTS_3
```

`elif` is an abbreviation of "else if".  Again, exactly one branch will be executed.  There is no limit to the number of `elif` statements but only a single (and optional) final `else` statement is allowed and it must be the last branch in the statement.


## Boolean Functions

Functions can return boolean values.  This turns out to be a very convenient way to hide the details of complicated tests.  It is common to give **boolean functions** names that sound like yes/no questions.


## Glossary

**block**

**body**

**boolean expression**

**boolean function**

**boolean value**

**branch**

**chained condtional**

**comparison operator**

**condition**

**conditional statement**

**logical operator**

**nesting**

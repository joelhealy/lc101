# Chapter 4 of LC101 version of Think Python:  Modules (and Turtles!)


## Hello Little Turtles!

Turtles are fun, but the real purpose of this chapter is to teach ourselves a little more Python and to develop our theme of *computational thinking*, or *thinking like a computer scientist*.

## Our First Turtle Program

```python
import turtle                # allows us to use the turtles library
wn = turtle.Screen()         # creates a graphics window
alex = turtle.Turtle()       # create a turtle named alex
alex.forward(150)            # tell alex to move forward by 150 units
alex.left(90)                # turn by 90 degrees
alex.forward(75)             # complete the second side of a rectangle
```

The first line tells Python to load a **module** named `turtle`.  That module brings us two new types that we can use: the `Turtle` type, and the `Screen` type.

We then create and open what the turtle module calls a screen (we sometimes refer to it as a window), which we assign to the variable `wn`.  Every window contains a **canvas**, which is the area inside the window on which we can draw.

In line 3 we create a turtle.  The variable `alex` is made to refer to this turtle.

An object can have various **methods** — things it can do — and it can also have **attributes** — (sometimes called **properties**).


## Instances - A Herd of Turtles

Just like we can have many different integers in a program, we can have many turtles.  Each of them is an independent object and we call each one an **instance** of the Turtle type (class).  Each instance has its own state represented by its attributes and set via its methods.


## The for Loop

A basic building block of all programs is to be able to repeat some code over and over again.  In computer science, we refer to this repetition as **iteration**.

In Python, the **for** statement allows us to write programs that implement iteration.

```python
for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")
```

* **name** in this `for` statement is called the **loop variable**.
* The list of names in the square brackets is called a Python `list`.
* Line 2 is the **loop body**.  The loop body is always indented.  The loop body is performed one time for each name in the list.
* On each *iteration* or *pass* of the loop, first a check is done to see if there are still more items to be process (this is called the **terminating condition** of the loop).  If there are none left, the loop has finished.  Program execution continues at the next statement after the loop body.
* If there are items still to be processed, the loop variable is updated to refer to the next item in the list.
* At the end of each execution of the body of the loop, Python returns to the `for` statement, to see if there are more items to be handled.


## Flow of Execution of the for Loop

As a program executes, the interpreter always keeps track of which statement is about to be executed.  We call this the **control flow**, or the **flow of execution** of the program.

Control flow unitl now has been strictly top to bottom, one statement at a time.  We call this type of control **sequential**.  Sequential flow of control is always assumed to be the default behavior for a computer program.  The `for` statement changes this.


## Iteration Simplifies Our Turtle Program

```python
import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0, 1, 2, 3]:      # repeat four times
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
```

Finding the chunks and somehow getting our programs arranged around those chunks is a vital skill when learning *How to think like a computer scientist*.


## The range Type

Python gives us a special built-in `range` type that can provide a sequence of values.  The sequence provided by `range` always starts with 0.  This way of starting a count at 0, instead of 1, is called **zero-based indexing** and is very common in computer programming.

The range constructor (a *constructor* is a special class method that creates an object) can take one, two or three parameters.

range(start, stop, step)
range(4) produces the sequence [0, 1, 2, 3]
range(1, 6) produces the sequence [1, 2, 3, 4, 5]
range(1, 6, 2) produces the sequence [1, 3, 5]

You can also create a sequence of numbers that starts big and gets smaller by using a negative value for the step parameter.


## A Few More turtle Methods and Observations

* Turtle methods can use negative angles or distances.
* A turtle's pen can be picked up or put down with the `up` and `down` methods.
* Every turle can have its own shape.  The one's available "out of the box" are `arrow`, `blank`, `circle`, `classic`, `square`, `triangle`, `turtle`.
* You can speed up or slow down the turtle's animation speed using the `speed` method.  Speed setting can be set between 1 (slowest) to 10 (fastest) as well as 0 to turn animation delays off and go as fast as possible.
* A turtle can "stamp" its footprint onto the canvas, and this will remain after the turtle has moved somewhere else.  Stamping works even when the pen is up.


## Summary of Turtle Methods

Method     | Parameters | Description
-----------|------------|-------------
Turtle     | None       | Creates and returns a new turtle object
forward    | distance   | Moves the turtle forward
backward   | distance   | Moves the turtle backward
right      | angle      | Turns the turtle clockwise
left       | angle      | Turns the turtle counter clockwise
up         | None       | Picks up the turtles tail
down       | None       | Puts down the turtles tail
color      | color name | Changes the color of the turtle's tail
fillcolor  | color name | Changes the color the turtle will use to fill a polygon
heading    | None       | Returns the current heading
position   | None       | Returns the current position
goto       | x,y        | Move the turtle to position x,y
begin_fill | None       | Remember the starting point for a filled polygon
end_fill   | None       | Close the polygon and fill with the current fill color
dot        | None       | Leave a dot at the current position
stamp      | None       | Leaves an impression of the turtle's shape at the current location
shape      | shapename  | Should be 'arrow', 'classic', 'turtle', or 'circle'


## Modules and Getting Help

A **module** is a file containing Python definitions and statements intended for us in other Python programs.  There are many Python modules that come with Python as part of the **standard library**.  Recall that one we import the module, we can use things that are defined inside.

The [Python Documentation](http://docs.python.org/py3k/) site for Python version 3 is an extrememly useful reference for all aspects of Python.  The site contains a listing of all the standard modules that are available with Python (see [Global Module Index](http://docs.python.org/py3k/py-modindex.html)).  You will also see that there is a [Language Reference](http://docs.python.org/py3k/reference/index.html) and a [Tutorial](http://docs.python.org/py3k/tutorial/index.html) as well as installation instructions, how-to guides, and frequently asked questions.


## More About Using Modules

One of the most important things to realize about modules is the fact that they are data objects, just like any other data in Python.  Module objects simply contain other Python elements.

The first think we need to do when we wish to use a module is perform an `import`.  The statement `import turtle` creates a new name, `turtle`, and makes it refer to a module object.

In order to use something contained in a module, we use the **dot notation**, providing the module nume and the specific item joined together with a "dot".


## The math module

The `math` module contains the kinds of mathematical functions you would typically find on your calculator and also some mathematical constants like pi and e.

If you want more information, you can check out the [Math Module](http://docs.python.org/py3k/library/math.html#module-math) Python Documentation.

When we say `alex = turtle.Turtle()`, we are calling the constructor for the Turtle class which returns a single turtle object.  We need to create (or, **instantiate**) one in order to use it.

However, mathematical functions do *not* need to be constructed.  They simply perform a task.  They are all housed together in a module called `math`.


## The random module

Python provides a module `random`.  You can take a look at it in [the documentation](https://docs.python.org/3/library/random.html#module-random)

The `randrange` function generates an integer between its lower and upper argument, using the same semantics as `range` -- so the lower bound is included, but the upper bound is excluded.

The `random()` function returns a floating point number in the range [0.0, 1.0).


## Glossary

**attribute**

**canvas**

**deterministic**

**documentation**

**for loop**

**import**

**instance**

**invoke**

**iteration**

**loop**

**loop body**

**loop variable**

**method**

**module**

**object**

**pseudo-random number**

**random number**

**random number generator**

**range**

**sequential**

**standard library**

**state**

**terminating condition**

**turtle**

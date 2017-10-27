# Chapter 8 of LC101 version of Think Python:  More About Iteration


## Iteration Revisited

Repeated execution of a sequence of statements is called **iteration**.

In this chapter we are going to review the `for` loop and then introduce the `while` loop -- another way to have your program do iteration.


## The for Loop Revisited

Recall that the `for` loop processes each item in a list.  Each item in turn is assigned to the loop variable -- also called the iterator variable -- and the body of the loop is executed.

We have also seen iteration and variable updating in the form of the accumulator pattern.


## The while Statement

There is another Python statement that can also be used for iteration.  It is called the `while` statement or a `while` loop.  The `while` statement provides a much more general mechanism for iterating.  Similar to the `if` statement, it uses a boolean expression to control the flow of execution.  The body of the `while` loop will be repeated as long as the controlling boolean expression evaluates to  True.

We can use the `while` loop to create any type of iteration we wish, including anything that we have previously done with a `for` loop.

In order to control the iteration, we must create a boolean expression that evaluates to `True` as long as we want to keep adding values to our running total.

Here is the flow of execution for a `while` statement:

1.  Evaluate the condition, which yields a value of `False` or `True`.
1.  If the condition is `False`, exit the while statement and continue execution at the next statement after the loop body.
1.  If the condition is `True`, execute the statements in the body and then go back to step 1.

The body consists of all of the statements below the header and indented at least 4 spaces in from the header of the `while` loop.

This type of flow is called a **loop** because the third step loops back around to the top.  Notice that if the condition is `False` the first time through the loop, the statements inside the loop are never executed.

The body of the loop should change the value of one or more variables so that eventually the condition becomes `False` and the loop terminates.  Otherwise the loop will repeat forever.  When this happens, the loop is called an **infinite loop**.

The `for` statement will always iterate through a sequence of values like a list of names or a list of numbers created by `range`.  since we know that it will iterate once for each value in the collection, it is often said that a `for` loop creates a **definite iteration** because we definitely know how many times we are going to iterate.

On the other hand, the `while` statement is *dependent on a condition* that needs to evaluate to `False` in order for the loop to terminate.  Since we do not necessarily know when (or even if) this will happen, it creates what we call **indefinite iteration**.  Indefinite iteration simply means that we don't know how many times we will repeat.


## break and continue Statements

There are times when you will want to change the typical flow of control of the loop body itself.  For these instances, Python has `break` and `continue` statements that allow you to precisely tweak the flow of control in both you `for` and `while` loops.

For example, there are times when you may want to terminate your loop if a given condition -- besides the controlling condition -- is met.  This is where the `break` statement is useful.  Unlike the `continue` statement, which we will examine next, the `break` statement **does not** cause the flow of control to return again to the loop header to check the controlling condition.

The flow of control for the `continue` statement is, like the `break` statement, to halt execution of the loop body when a given condition is met.  But unlike the `break` statement, the flow of execution does not move outside the loop entirely and onto the next statement after it.  Instead, the flow of execution "continues" by returning to the loop header and checking the controlling condition again.


## Randomly Walking Turtles



## Choosing Which Loop to Use

In this lesson we'll explore two more examples of indefinite iteration: the 3n + 1 sequence and user input.  Then we'll review how you can choose whether a `for` loop or a `while` loop will best suit your needs in various circumstances.

Use a `for` loop if you know the maximum number of times that you'll need to execute the body.

By contrast, if you are required to repeat some computation until some condition is met, as we did in the two problems above, you'll need a `while` loop.

As we noted before, the former case is called a **definite iteration** -- we have definite bounds for what is needed.  The latter case is called an **indefinite iteration** -- we are not sure how many iterations we'll need.  For an indefinite iteration, it is generally impossible to determine the maximum number of times the loop might run.


## Simple Tables

One of the things loops are good for is generating tabular data.

the string `'\t'` represents a **tab character**.  The backslash character in `'\t'` indicates the beginning of an **escape sequence**.  Escape sequences are used to represent invisible characters like tabs and newlines.  The sequence `\n` represents a newline character.

As characters and strings are displayed on the screen, an invisible marker called the **cursor** keeps track of where the next character will go.  After a `print` function is executed, the cursor normally goes to the beginning of the next line.

The tab character shifts the cursor to the right until it reaches one of the tab stops.  Tabs are useful for making columns of text line up.


## 2-Dimensional Iteration: Image Processing

Two-dimensional tables have both rows and columns.

A **digital image** is a finite collection of small, discrete picture elements called **pixels**.  These pixels are organized in a two-dimensional grid.  Each pixel represents the smallest amount of picture information that is available.  Sometimes these pixels appear as small "dots".

The width is the number of columns and the height is the number of rows.

Each pixel of the image will represent a single color.  The specific color depends on a formula that mixes various amounts of three basic colors: red, green, and blue.  This technique for creating color is known as the **RGB Color Model**.  The amount of each of the three colors, sometimes called the **intensity** of the color, allows us to have a very fine control over the resulting color.

The minimum intensity value for a basic color (red, green, and blue) is 0.  The maximum intensity is 255.  This means that there are actually 256 different amounts of intensity for each basic color.  Since there are three basic colors, that means that you can create 256\**3 distinct colors using the RGB Color Model.

In order to manipulate an image, we need to be able to access individual pixels.  This capability is provided by a module called **image**.  The image module we will use -- which is *not* a standard Python module -- defines two classes: `Image` and `Pixel`.

Each Pixel object has three attributes: the red intensity, the green intensity, and the blue intensity.  A pixel provides three methods that allow us to ask for the intensity values.  They are called `getRed`, `getGreen`, and `getBlue`.  In addition, we can ask a pixel to change an intensity value using its `setRed`, `setGreen`, and `setBlue` methods.

To access the pixels in areal image, we need to first create an `Image` object.  `Image` objects can be created in two ways.  First, an `Image` object can be made from the files that store digital images.  This object will have attributes corresponding to the width, the height, and the collection of pixels in the image.

It is also possible to create an `Image` object that is "empty".  The method `EmptyImage()` can be used to return an `Image` object that has a width and a height.  However, the pixel collection consists of only "white" pixels.

We can ask an `Image` object to return its size using the `getWidth` and `getHeight` methods.  We can also get a pixel from a particular location in the image using `getPixel` and change the pixel at a particular location using `setPixel`.

**Image Processing** refers to the ability to manipulate the individual pixels in a digital image.  In order to process all of the pixels, we need to be able to systematically visit all of the rows and columns in the image.  The best way to do this is to use **nested iteration** or **nested loops**.

Nested iteration simply means that we will place one iteration construct inside of another.  We will call these two iterations the **outer iteration** (or outer loop) and the **inner iteration** (or inner loop).


## Glossary

**counter**  
A variable used to count something, usually initialized to zero and incremented in the body of the loop.

**cursor**  
An invisible marker that keeps track of where the next character will be printed.

**definite iteration**  
A loop where we have an upper bound on the number of times the body will be executed.  Definite iteration is usually best coded as a `for` loop.

**escape sequence**  
An escape character, `\`, followed by one or more printable characters used to designate a non-printable character.

**infinite loop**  
A loop in which the terminating condition is never satisfied.

**indefinite iteration**  
A loop we need to keep repeating until some condition is met.  A `while` statement is used for this case.

**nested loop**  
A loop inside the body of another loop.

**newline**  
A special character that causes the cursor to move to the beginning of the next line.

**tab**  
A special character that causes the cursor to move to the next tab stop on the current line.


# Optional Chapter of LC101 version of Think Python:  Files


## 1. Working with Data Files

In real life data reside in files.  In this chapter we will introduce the Python concepts necessary to use data files in our programs.

We will assume that our data files are text files -- that is, files filled with characters.

In Python, we must **open** files before we can use them and **close** them when we are done with them.  Once a file is opened it becomes a Python object just like all other data.

Method | Use                      | Explanation
-------|--------------------------|--------------------------------------------
open   | open(filename, 'r')      | Open a file called filename and use it for reading.  This will return a reference to a file object.
open   | open(filename, 'w')      | Open a file called filename and use it for writing.  This will also return a reference to a file object.
close  | filevariable.close()     | File use is complete.


## 2. Finding a File on your Disk

Opening a file requires that you, as a programmer, and Python agree about the location of the file on your disk.  The way that files are located on disk is by their **path**.  You can think of the filename as the short name for a file, and the path as the full name.


## 3. Reading a File

To open a file, we call the `open` function.  This function will return a reference to a file object.  When we are finished with the file, we can close it by using the `close` method.  After a file is closed any further attempts to use a reference to the file object will result in an error.


## 4. Iterating over lines in a file.

Because text files are sequences of lines of text, we can use the *for* loop to iterate through each line of the file.  A **line** of a file is defined to be a sequence of characters up to and including a special character call the **newline** character.  This special character is represented as `\n`.

As the *for* loop iterates through each line of the file the loop variable will contain the current line of the file as a string of characters.  The general pattern for processing each line of a text file is as follows:

```python
for line in myFile:
    statement1
    statement2
    ...
```


## 5. Alternative File Reading Methods

In addition to the `for` loop, Python provides three methods to read data from the input file.  The `readline` method reads one line from the file and returns it as a string.  The string returned by `readline` will contain the newline character at the end.  This method returns the empty string when it reaches the end of the file.

The `readlines` method returns the contents of the entire file as a list of strings, where each item in the list represents one line of the file.

It is also possible to read the entire file into a single string with `read`.

Each file has a marker that denotes the current read position in the file.  Any time one of the read methods is called the marker is moved to the character immediately following the last character returned.


Method Name  | Use                    | Explanation
-------------|------------------------|----------------------------------------
write        | filevar.write(astring) | Add astring to the end of the file.  filevar must refer to a file that has been opened for writing.
read(n)      | filevar.read()         | Reads and returns a string of n characters, or the entire file as a single string if n is not provided.
readline(n)  | filevar. readline()    | Returns the next line of the file with all text up to and including the newline character.  If n is provided as a parameter then only n characters will be returned if the line is longer than n.
readlines(n) | filevar.readlines()    | Returns a list of strings, each representing a single line of the file.  If n is not provided then all lines of the file are returned.  If n is provided then n characters are read but n is rounded up so that an entire line is returned.


Now let's look at another method of reading our file using a `while` loop.  This is important because many other programming languages do not support the `for` loop style for reading files but they do support the pattern we'll show you here.

```python
infile = open("qbdata.txt", "r")
line = infile.readline()
while line:
    values = line.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )
    line = infile.readline()

infile.close()
```

The initial read (on line 2 above) is called the **priming read**.  The `readline` method will return the empty string if there is no more data in the file.  The condition `while line:` means while the content of line is not the empty string.  Remember that a blank line in the file actually has a single character, the `\n` character (newline).  So, the only way that a line of data from the file can be empty is if you are reading at the end of the file.


## 6. Writing Text Files

When we open a file for writing, a new, empty file with that name is created and made ready to accept our data.  The `open` function returns a reference to the new file object.

The `write` method takes one parameter, a string.  When invoked, the characters of the string will be added to the end of the file.  This means that it is the programmers job to include the newline characters as part of the string if desired.

## 7. Glossary


**open**  
You must open a file before you can read its contents.

**close**  
When you are done with a file, you should close it.

**read**  
Will read the entire contents of a file as a string. This is often used in an assignment statement so that a variable can reference the contents of the file.

**readline**  
Will read a single line from the file, up to and including the first instance of the newline character.

**readlines**  
Will read the entire contents of a file into a list where each line of the file is a string and is an element in the list.

**write**  
Will add characters to the end of a file that has been opened for writing.

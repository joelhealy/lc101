/**********************************************************************
**
**  Eloquent JavaScript - Chapter 2: Program Structure
**
**  Exercise 3:  Chess board
**
**  Write a program that creates a string that represents an 8 x 8 grid,
**  using newline characters to separate lines. At each position of the
**  grid there is either a space or a "#" character. The characters
**  should form a chess board.
**  
**  Passing this string to console.log should show something like this:
**  
**    # # # #
**   # # # #
**    # # # #
**   # # # #
**    # # # #
**   # # # #
**    # # # #
**   # # # #
**  
**  When you have a program that generates this pattern, define a
**  variable size = 8 and change the program so that it works for any
**  size, outputting a grid of the given width and height.
**  
**********************************************************************/

var size = 8;
var row;
var offset;

for (var rownum = 0; rownum < size; rownum++) {
  if (rownum % 2 == 0) {
    row = ' ';
    offset = 1;
  } else {
    row = "";
    offset = 0;
  }
  for (var colnum = 0; colnum < size - offset; colnum++) {
    if (colnum % 2 == 0) {
      row += '*';
    } else {
      row += ' ';
    }
  }
  console.log(row);
}



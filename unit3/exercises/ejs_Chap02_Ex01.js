/**********************************************************************
**
**  Eloquent JavaScript - Chapter 2: Program Structure
**
**  Exercise 1: Looping a triangle
**  
**  Write a loop that makes seven calls to console.log to output the following triangle:
**  
**  #
**  ##
**  ###
**  ####
**  #####
**  ######
**  #######
**  
**  It may be useful to know that you can find the length of a string by writing .length after it.
**  
**  var abc = "abc";
**  console.log(abc.length);
**  //  3
**  
**********************************************************************/

var str = ""
while (str.length < 7) {
  str += '*';
  console.log(str);
}


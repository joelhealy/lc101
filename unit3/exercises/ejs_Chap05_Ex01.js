/**********************************************************************
**
**  Eloquent JavaScript - Chapter 5:  Higher-Order Functions
**
**  Exercise 1:  Flattening
**  
**  Use the reduce method in combination with the concat method to
**  “flatten” an array of arrays into a single array that has all the
**  elements of the input arrays.
**  
**    var arrays = [[1, 2, 3], [4, 5], [6]];
**    // Your code here.
**    // → [1, 2, 3, 4, 5, 6]
**  
**********************************************************************/

var arrays = [[1, 2, 3], [4, 5], [6]];

console.log(arrays.reduce(function(accumulator, current) {
  return accumulator.concat(current);
}))
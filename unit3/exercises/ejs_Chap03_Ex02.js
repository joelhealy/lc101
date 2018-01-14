/**********************************************************************
**
**  Eloquent JavaScript - Chapter 3:  Functions
**
**  Exercise 2: Recursion
**  
**  Weve seen that % (the remainder operator) can be used to test
**  whether a number is even or odd by using % 2 to check whether its
**  divisible by two. Heres another way to define whether a positive
**  whole number is even or odd:
**  
**    -  Zero is even.
**  
**    -  One is odd.
**  
**    -  For any other number N, its evenness is the same as N - 2.
**  
**  Define a recursive function isEven corresponding to this
**  description. The function should accept a number parameter and
**  return a Boolean.
**  
**  Test it on 50 and 75. See how it behaves on -1. Why? Can you
**  think of a way to fix this?
**  
**  // Your code here.
**  
**  console.log(isEven(50));
**  //  true
**  console.log(isEven(75));
**  //  false
**  console.log(isEven(-1));
**  //  ??
**  
**              
**  
**********************************************************************/

function isEven(n) {
  if (n < 0) {
    return isEven(-n);
  } else if (n == 0) {
    return true;
  } else if (n == 1) {
    return false;
  } else {
    return isEven(n - 2);
  }
}

console.log(isEven(50));
console.log(isEven(75));
console.log(isEven(-1));


/**********************************************************************
**
**  Eloquent JavaScript - Chapter 4:  Data Structures: Objects and Arrays
**
**  Exercise 2: Reversing an Array
**
**  Arrays have a method reverse, which changes the array by inverting
**  the order in which its elements appear. For this exercise, write
**  two functions, reverseArray and reverseArrayInPlace. The first,
**  reverseArray, takes an array as argument and produces a new array
**  that has the same elements in the inverse order. The second,
**  reverseArrayInPlace, does what the reverse method does: it modifies
**  the array given as argument in order to reverse its elements.
**  Neither may use the standard reverse method.
**  
**  Thinking back to the notes about side effects and pure functions
**  in the previous chapter, which variant do you expect to be useful
**  in more situations? Which one is more efficient?
**    
**    // Your code here.
**    
**    console.log(reverseArray(["A", "B", "C"]));
**    // → ["C", "B", "A"];
**    var arrayValue = [1, 2, 3, 4, 5];
**    reverseArrayInPlace(arrayValue);
**    console.log(arrayValue);
**    // → [5, 4, 3, 2, 1]
**  
**********************************************************************/

function reverseArray(arr) {
    var newArr = [];
    for (var i = arr.length - 1; i >= 0; i--) {
        newArr.push(arr[i]);
    }
    return newArr;
}

function reverseArrayInPlace(arr) {
    var tmp;
    var len = arr.length;
    for (var i = 0; i < len / 2; i++) {
        tmp = arr[i];
        arr[i] = arr[len - i - 1];
        arr[len - i - 1] = tmp;
    }
    return arr;
}

console.log(reverseArray(["A", "B", "C"]));

var arrayValue = [1, 2, 3, 4, 5];
reverseArrayInPlace(arrayValue);
console.log(arrayValue);

var arrayValue = [1, 2, 3, 4, 5, 6];
reverseArrayInPlace(arrayValue);
console.log(arrayValue);
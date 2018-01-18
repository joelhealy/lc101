/**********************************************************************
**
**  Eloquent JavaScript - Chapter 4:  Data Structures: Objects and Arrays
**
**  Exercise 4:  Deep comparison
**  
**  The == operator compares objects by identity. But sometimes, you
**  would prefer to compare the values of their actual properties.
**  
**  Write a function, deepEqual, that takes two values and returns true
**  only if they are the same value or are objects with the same
**  properties whose values are also equal when compared with a
**  recursive call to deepEqual.
**  
**  To find out whether to compare two things by identity (use the
**  === operator for that) or by looking at their properties, you can
**  use the typeof operator. If it produces "object" for both values,
**  you should do a deep comparison. But you have to take one silly
**  exception into account: by a historical accident, typeof null
**  also produces "object".
**  
**    // Your code here.
**  
**    var obj = {here: {is: "an"}, object: 2};
**    console.log(deepEqual(obj, obj));
**    // → true
**    console.log(deepEqual(obj, {here: 1, object: 2}));
**    // → false
**    console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
**    // → true
**  
**********************************************************************/

function deepEqual(val1, val2) {
    if (typeof val1 != 'object' || typeof val2 != 'object' ||
        val1 === null || val2 === null) {
            return (val1 === val2);
    } else if (Object.keys(val1).length != Object.keys(val2).length) {
        return false;
    } else {
        var retVal = true;
        for (key in val1) {
            retVal = retVal && deepEqual(val1[key], val2[key]);
            if (!retVal) break;
        }
        return retVal;
    } 

}

var obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));
// → true
console.log(deepEqual(obj, {here: 1, object: 2}));
// → false
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
// → true

/**********************************************************************
**
**  Eloquent JavaScript - Chapter 5:  Higher-Order Functions
**
**  Exercise 2:  Mother-child age difference
**  
**  Using the example data set from this chapter, compute the average
**  age difference between mothers and children (the age of the mother
**  when the child is born). You can use the average function defined
**  earlier in this chapter.
**  
**  Note that not all the mothers mentioned in the data are themselves
**  present in the array. The byName object, which makes it easy to
**  find a person’s object from their name, might be useful here.
**  
**  function average(array) {
**    function plus(a, b) { return a + b; }
**    return array.reduce(plus) / array.length;
**  }
**  
**  var byName = {};
**  ancestry.forEach(function(person) {
**    byName[person.name] = person;
**  });
**  
**  // Your code here.
**  
**  // → 31.2
**  
**********************************************************************/

var fs = require("fs");

var contents = fs.readFileSync("ancestry.json");
var ancestry = JSON.parse(contents);

function average(array) {
  function plus(a, b) { return a + b; }
  return array.reduce(plus) / array.length;
}

var byName = {};
ancestry.forEach(function(person) {
  byName[person.name] = person;
});

var motherInAncestry = function(person) {
  return ancestry.indexOf(byName[person.mother]) != -1;
}

var calcMomsAge = function(person) {
  return person.born - byName[person.mother].born;
}

console.log(average(ancestry.filter(motherInAncestry).map(calcMomsAge)));
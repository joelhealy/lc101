/**********************************************************************
**
**  Eloquent JavaScript - Chapter 5:  Higher-Order Functions
**
**  Exercise 3:  Historical life expectancy
**  
**  When we looked up all the people in our data set that lived more
**  than 90 years, only the latest generation in the data came out.
**  Let’s take a closer look at that phenomenon.
**  
**  Compute and output the average age of the people in the ancestry
**  data set per century. A person is assigned to a century by taking
**  their year of death, dividing it by 100, and rounding it up, as in
**  Math.ceil(person.died / 100).
**  
**    function average(array) {
**      function plus(a, b) { return a + b; }
**      return array.reduce(plus) / array.length;
**    }
**  
**    // Your code here.
**  
**    // → 16: 43.5
**    //   17: 51.2
**    //   18: 52.8
**    //   19: 54.8
**    //   20: 84.7
**    //   21: 94
**  
**  
**  
**********************************************************************/

var fs = require("fs");

var contents = fs.readFileSync("ancestry.json");
var ancestry = JSON.parse(contents);

function average(array) {
  function plus(a, b) { return a + b; }
  return array.reduce(plus) / array.length;
}

function century(person) {
  return Math.ceil(person.died / 100);
}

function age(person) {
  return person.died - person.born;
}

var agesByCentury = {};
ancestry.forEach(person => {
  if (!agesByCentury[century(person)]) {
    agesByCentury[century(person)] = [];
  }
  agesByCentury[century(person)].push(age(person));
});

for (cent in agesByCentury) {
  console.log("" + cent + ':', average(agesByCentury[cent]).toFixed(1));
}
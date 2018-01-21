
/**
 * determineHeightAndThenDrawPyramid
 *
 * Determines the current value that the user has typed in the 'How high?' text-box,
 * and then draws a pyramid with that height.
 */
function determineHeightAndThenDrawPyramid() {

    // just so we know we're here
    console.log("someone invoked the determineHeightAndThenDrawPyramid function!");

    // figure out the height the user typed (replace the "5" below)
    heightStr = document.getElementById("height").value;

    // here we convert the string to an int
    height = parseInt(heightStr);

    // draw the pyramid with the given height
    drawPyramid(height);

}


var drawButton = document.getElementById("drawButton");
drawButton.addEventListener("click", determineHeightAndThenDrawPyramid);


/**
 * drawPyramid
 *
 * Renders, in the HTML document, a Mario pyramid of the specified height
 */
 function drawPyramid(height) {

     // before drawing, clear the old content
     pyramid = document.getElementById("pyramid");
     // someone suggested that looping through the children is more
     // efficient than setting innerHTML = '' and that the latter method
     // would fail if one of the children was not HTML, e.g., SVG
     while (pyramid.lastChild) {
         pyramid.removeChild(pyramid.lastChild);
     }


     // for each row....
     for (var row = 0; row < height; row++) {

         // figure out number of bricks and spaces
         var numBricks = row + 2;
         var numSpaces = height - row - 1;

         // build up a string for this row
         var rowStr = "";
         for (var i = 0; i < numSpaces; i++) {
             rowStr += ".";
         }
         for (var i = 0; i < numBricks; i++) {
             rowStr += "#";
         }

        // create a text element with the string of characters
        textElem = document.createTextNode(rowStr);

        // create a <p> element with the text inside
        rowElem = document.createElement("p");
        rowElem.appendChild(textElem);

        // insert the paragraph as a child of the container <div>
        document.getElementById("pyramid").appendChild(rowElem);
    }
}

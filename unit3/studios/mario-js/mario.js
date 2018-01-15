
printPyramid(6);


/*
 * printPyramid
 *
 * Prints to the console a pyramid of '#' characters of the specified height
 * For example, if height is 5, the console will look like this:
 *          ##
 *         ###
 *        ####
 *       #####
 *      ######
 */
function printPyramid(height) {
    var row; 

    for (var rownum = 0; rownum < height; rownum++) {
        row = "";
        for (var colnum = 0; colnum <= height; colnum++) {
            if (colnum < height - rownum - 1) {
                row += ' ';
            } else {
                row += '#';
            }
        }
        console.log(row);
    }
}

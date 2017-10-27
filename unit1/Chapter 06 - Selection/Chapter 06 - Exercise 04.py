# =============================================================================
# In the Turtle bar chart program, what do you expect to happend if one or more
# of the data values in the list is negative?  Go back and try it out.  Then
# change the program so that when it prints the text value for the negative
# bars, it puts the text above the base of the bar (on the 0 axis).
# =============================================================================
import turtle


def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """

    t.begin_fill()               # start filling this shape
    if height < 0:               # if bar is negative, print text value above
        t.write(str(height))     # the base of the bar (on the 0 axis)
    t.left(90)
    t.forward(height)
    if height >= 0:              # if bar is nonnegative, print text value
        t.write(str(height))     # above the bar
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape


def main():

    data = [48, -117, 200, 240, -160, 260, 220]
    max_height = max(data)
    max_neg_height = min(0, min(data))  # longest bar below axis
    num_bars = len(data)
    border = 10

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0 - border, 0 - border + max_neg_height,
                           40 * num_bars + border, max_height + border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)

    for x in data:
        draw_bar(tess, x)

    wn.exitonclick()


if __name__ == "__main__":
    main()

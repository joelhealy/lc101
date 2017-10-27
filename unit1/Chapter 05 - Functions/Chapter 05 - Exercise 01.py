import turtle


def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)


def main():
    num_squares = 5          # number of squares to draw
    sq_side_length = 20      # length of each side of square
    sq_spacing = 20          # horizontal spacing between squares

    wn = turtle.Screen()
    wn.setup(300, 115, 0, 0)   # adjust the size of the screen
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color('#FF67AF')    # used ColorPic to grab the color from the picture
    alex.pensize(3)

    # reposition the starting position of the turtle
    alex.penup()
    alex.left(180)
    alex.forward(100)
    alex.left(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

    for _ in range(num_squares):
        draw_square(alex, sq_side_length)
        alex.penup()
        alex.forward(sq_side_length)
        alex.forward(sq_spacing)
        alex.pendown()

    wn.exitonclick()


if __name__ == "__main__":
    main()

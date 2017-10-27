import turtle


def draw_centered_square(t, sz, x, y):
    """
    Get turtle t to draw a square with sz side centered on the point (x,y)
    """

    init_position = t.pos()
    t.penup()
    t.goto(x - sz / 2, y - sz / 2)
    t.pendown()
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.goto(init_position)


def main():
    num_squares = 5                # number of squares to draw
    sq_side_length = 20            # length of each side of square
    sq_side_length_increase = 20   # increase in side length between squares

    wn = turtle.Screen()
    wn.setup(175, 150, 0, 0)   # adjust the size of the screen
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color('#FF67AF')    # used ColorPic to grab the color from the picture
    alex.pensize(3)

    side = sq_side_length
    for _ in range(num_squares):
        draw_centered_square(alex, side, 0, 0)
        side += sq_side_length_increase

    # reposition the turtle below and to the left of the final square
    alex.penup()
    alex.goto(-side / 2, -side / 2)

    wn.exitonclick()


if __name__ == "__main__":
    main()

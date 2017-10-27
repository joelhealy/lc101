import turtle


def draw_square(t, sz):
    """Use turtle t to draw a square with side of length sz"""

    for _ in range(4):
        t.forward(sz)
        t.left(90)


def draw_four_square(t, sz):
    """Use turtle t to draw a four-square pattern"""

    for _ in range(4):
        draw_square(t, sz)
        t.left(90)


def draw_rotating_four_square(t, n, sz):
    """
    Use turtle t to draw an n-part rotating four-square pattern
    of radius sz
    """

    for _ in range(n):
        draw_four_square(t, sz)
        t.right(90 / n)


def main():
    """    Draw a pretty pattern similiar to a rotating four-square"""

    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    studio_turtle = turtle.Turtle()
    studio_turtle.pensize(2)
    studio_turtle.color('blue')
    studio_turtle.speed(10)

    draw_rotating_four_square(studio_turtle, 5, 100)

    wn.exitonclick()


if __name__ == '__main__':
    main()

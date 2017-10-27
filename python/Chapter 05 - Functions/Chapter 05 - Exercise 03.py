import turtle


def draw_poly(t, sides, side_length):
    '''
    Use turtle <t> to draw a regular polygon with <sides> sides.
    Each side should have a length of <side_length>
    '''

    turn_angle = 360 / sides
    for _ in range(sides):
        t.forward(side_length)
        t.left(turn_angle)


def main():
    wn = turtle.Screen()
    wn.setup(175, 175, 0, 0)
    wn.bgcolor('lightgreen')

    bob = turtle.Turtle()
    bob.color('hotpink')
    bob.pensize(3)

    bob.penup()
    bob.goto(-25, -60)
    bob.pendown()

    draw_poly(bob, 8, 50)

    wn.exitonclick()


if __name__ == '__main__':
    main()

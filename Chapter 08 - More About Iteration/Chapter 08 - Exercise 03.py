#  Modify the turtle walk program so that you have two turtles each with a
#  random starting location. Keep the turtles moving until one of them leaves
#  the screen.


import random
import turtle


def is_in_screen(screen, t):
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False

    return still_in


def random_x_on_screen(screen):
    """Return a random x-coordinate on <screen>"""

    w = screen.window_width()
    randx = random.randrange(w) - w // 2
    return randx


def random_y_on_screen(screen):
    """Return a random y-coordinate on <screen>"""

    h = screen.window_height()
    randy = random.randrange(0, h) - h // 2
    return randy


def main():
    screen = turtle.Screen()

    julia = turtle.Turtle()
    julia.shape('turtle')
    julia.color('green')
    julia.penup()
    julia.goto(random_x_on_screen(screen), random_y_on_screen(screen))
    julia.pendown()
    julia.stamp()

    george = turtle.Turtle()
    george.shape('turtle')
    george.color('purple')
    george.penup()
    george.goto(random_x_on_screen(screen), random_y_on_screen(screen))
    george.pendown()
    george.stamp()

    while is_in_screen(screen, julia) and is_in_screen(screen, george):
        for t in [julia, george]:
            coin = random.randrange(0, 2)
            if coin == 0:
                t.left(90)
            else:
                t.right(90)
            t.forward(50)

    screen.exitonclick()


if __name__ == "__main__":
    main()

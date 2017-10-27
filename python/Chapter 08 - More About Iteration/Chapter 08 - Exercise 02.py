#  Modify the walking turtle program so that rather than a 90 degree left or
#  right turn the angle of the turn is determined randomly at each step.


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


def main():
    julia = turtle.Turtle()
    screen = turtle.Screen()

    julia.shape('turtle')
    while is_in_screen(screen, julia):
        #  The following is my interpretation of a "random" angle.  If the
        #  desired interpretation is that the angle should be between -90 and
        #  +90, then use the commented subsequent line instead
        turn_angle = random.random() * 360
        # turn_angle = random.random() * 180 - 90
        julia.left(turn_angle)
        julia.forward(50)

    screen.exitonclick()


if __name__ == "__main__":
    main()

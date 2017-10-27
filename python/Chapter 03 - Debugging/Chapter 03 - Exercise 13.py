import turtle

num_legs = int(input("Enter number of legs: "))

turn_angle = 360 / num_legs
leg_length = 50

wn = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()

for step in range(num_legs):
    t.forward(leg_length)
    t.backward(leg_length)
    t.left(turn_angle)

wn.exitonclick()

import turtle              # 1. import the modules
import random


wn = turtle.Screen()       # 2. Create a screen
wn.setup(750, 250, 0, 0)
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3. Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4. Move the turtles to their starting point
lance.up()
andy.goto(-300, 20)
lance.goto(-300, -20)

andy_max_step = 75
lance_max_step = 85

num_steps = random.randrange(5, 16)
print("Today's race will be", num_steps, "lengths")
for n in range(num_steps):
    andy.forward(random.randrange(0, andy_max_step))
    andy.write(str(n + 1))
    print('after', n + 1, 'steps andy is at ', andy.xcor())
    # andy.dot()
    lance.forward(random.randrange(0, lance_max_step))
    lance.write(str(n + 1))
    print('after', n + 1, 'steps lance is at ', lance.xcor())
    # lance.dot()
andy.hideturtle()
lance.hideturtle()


wn.exitonclick()

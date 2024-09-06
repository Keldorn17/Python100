from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)  # important not to get error if you want to have custom RBG colors
# tim.shape("turtle")
# tim.color("green")

# # Square
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# # Dashed Line
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# # Multiple Shapes
# for sides in range(3, 11):
#     random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     tim.color(random_color)
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360 / sides)

# # Random Walk
# tim.width(10)
# tim.speed(0)
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     tim.color(random_color)
#     tim.setheading(random.choice(directions))
#     tim.forward(30)

# Spirograph
tim.speed(0)
for angle in range(90):
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.color(random_color)
    tim.setheading(angle * 4)
    tim.circle(100)


screen.exitonclick()

import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x: int = random.randint(-280, 280)
        random_y: int = random.randint(-280, 260)
        self.goto(random_x, random_y)


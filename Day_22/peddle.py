import turtle

MOVEMENT_SPEED = 20


class Peddle(turtle.Turtle):

    def __init__(self, starting_cord: tuple[float, float]):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(starting_cord)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self) -> None:
        self.goto(self.xcor(), self.ycor() + MOVEMENT_SPEED)

    def move_down(self) -> None:
        self.goto(self.xcor(), self.ycor() - MOVEMENT_SPEED)

from turtle import Turtle

STARTING_POSITION: tuple[int, int] = (0, -280)
MOVE_DISTANCE: int = 10
FINISH_LINE_Y: int = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.__spawn()
        self.setheading(90)

    def move(self) -> None:
        self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)

    def __spawn(self) -> None:
        self.goto(STARTING_POSITION)

    def check_finish_line(self) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            self.__spawn()
            return True
        return False

import turtle
import time


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.__move_speed = .1
        self.__x_move: int = 10
        self.__y_move: int = 10

    def move(self) -> None:
        new_x: float = self.xcor() + self.__x_move
        new_y: float = self.ycor() + self.__y_move
        self.goto(new_x, new_y)
        time.sleep(self.__move_speed)

    def bounce_y(self) -> None:
        self.__y_move *= -1

    def bounce_x(self) -> None:
        self.__x_move *= -1
        self.__move_speed *= .9

    def reset_position(self) -> None:
        self.home()
        self.bounce_x()
        self.__move_speed = .1

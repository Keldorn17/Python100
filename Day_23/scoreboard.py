from turtle import Turtle

FONT: tuple[str, int, str] = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.__level: int = 1
        self.__write_scoreboard()

    def __write_scoreboard(self) -> None:
        self.clear()
        self.goto(x=-280, y=260)
        self.write(f"Level: {self.__level}", align="left", font=FONT)

    def increase_level(self) -> None:
        self.__level += 1
        self.__write_scoreboard()

    def game_over(self) -> None:
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
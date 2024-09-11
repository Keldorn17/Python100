import turtle

FONT: tuple[str, int, str] = ("Courier", 70, "bold")
ALIGN: str = "center"


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.__l_score = 0
        self.__r_score = 0
        self.__write_score()

    def __write_score(self) -> None:
        self.clear()
        self.goto(-100, 200)
        self.write(self.__l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.__r_score, align=ALIGN, font=FONT)

    def l_point(self) -> None:
        self.__l_score += 1
        self.__write_score()

    def r_point(self) -> None:
        self.__r_score += 1
        self.__write_score()

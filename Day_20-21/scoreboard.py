import turtle

FONT = ("Courier", 16, "bold")
ALIGNMENT = "center"


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.__score: int = 0
        self.__high_score: int = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.__read_high_score()
        self.__draw_scoreboard()

    def increase_score(self):
        self.__score += 1
        self.__draw_scoreboard()

    def __draw_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.__score} High Score: {self.__high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.clear()
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.goto(0, -20)
    #     self.write(f"Final score: {self.__score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.__score > self.__high_score:
            self.__high_score = self.__score
            self.__update_high_score()
        self.__score = 0
        self.__draw_scoreboard()

    def __read_high_score(self) -> None:
        try:
            with open("data.txt") as file:
                self.__high_score = int(file.read())
        except FileNotFoundError:
            with open("data.txt", "w") as file:
                file.write("0")

    def __update_high_score(self) -> None:
        with open("data.txt", "w") as file:
            file.write(f"{self.__high_score}")

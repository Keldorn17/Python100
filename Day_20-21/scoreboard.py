import turtle

FONT = ("Courier", 16, "bold")
ALIGNMENT = "center"


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.__score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.__draw_scoreboard()

    def increase_score(self):
        self.__score += 1
        self.__draw_scoreboard()

    def __draw_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.__score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write(f"Final score: {self.__score}", align=ALIGNMENT, font=FONT)



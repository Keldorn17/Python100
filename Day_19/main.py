import turtle
import random


def main() -> None:
    screen: turtle.Screen = turtle.Screen()
    screen.setup(width=500, height=400)
    user_bet: str = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]

    turtles: list[turtle.Turtle] = [turtle.Turtle(shape="turtle") for _ in range(len(colors))]
    y_cord: int = -75
    for index, single_turtle in enumerate(turtles):
        single_turtle.color(colors[index])
        single_turtle.penup()
        single_turtle.goto(x=-230, y=y_cord)
        y_cord += 30

    is_race: bool = True
    while is_race:
        for single_turtle in turtles:
            if single_turtle.xcor() > 230:
                is_race: bool = False
                winning_color = single_turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner.")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner.")
                break
            random_distance: int = random.randint(0, 10)
            single_turtle.forward(random_distance)

    screen.exitonclick()


if __name__ == '__main__':
    main()

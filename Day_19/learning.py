import turtle


def move_forward() -> None:
    tim.forward(10)


def move_backward() -> None:
    tim.back(10)


def turn_right() -> None:
    tim.right(10)


def turn_left() -> None:
    tim.left(10)


def reset() -> None:
    tim.home()
    tim.clear()


tim = turtle.Turtle()
screen = turtle.Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)

screen.exitonclick()

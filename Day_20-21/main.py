import turtle
import time
import snake


def main() -> None:
    screen: turtle.Screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake_obj: snake.Snake = snake.Snake()

    screen.listen()
    screen.onkey(snake_obj.up, "w")
    screen.onkey(snake_obj.down, "s")
    screen.onkey(snake_obj.left, "a")
    screen.onkey(snake_obj.right, "d")

    game_is_on: bool = True
    while game_is_on:
        screen.update()
        time.sleep(.1)
        snake_obj.move()

    screen.exitonclick()


if __name__ == '__main__':
    main()

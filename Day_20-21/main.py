import turtle
import time
import snake
import food
import scoreboard


def main() -> None:
    screen: turtle.Screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake_obj: snake.Snake = snake.Snake()
    food_obj: food.Food = food.Food()
    scoreboard_obj: scoreboard.Scoreboard = scoreboard.Scoreboard()

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

        # Detect collision with food
        if snake_obj.get_head().distance(food_obj) < 15:
            food_obj.refresh()
            scoreboard_obj.increase_score()
            snake_obj.extend()

        # Detect collision with wall
        if snake_obj.get_head().xcor() > 280 or snake_obj.get_head().xcor() < -280 or snake_obj.get_head().ycor() > 280 or snake_obj.get_head().ycor() < -280:
            game_is_on = False
            scoreboard_obj.game_over()

        # Detect collision with tail
        for segment in snake_obj.get_segments():
            if snake_obj.get_head().distance(segment) < 10:
                game_is_on = False
                scoreboard_obj.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main()

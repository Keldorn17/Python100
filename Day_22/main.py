import turtle
import peddle
import ball
import scoreboard


def main() -> None:
    screen: turtle.Screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    peddle_obj_r: peddle.Peddle = peddle.Peddle((350, 0))
    peddle_obj_l: peddle.Peddle = peddle.Peddle((-350, 0))
    ball_obj: ball.Ball = ball.Ball()
    scoreboard_obj: scoreboard.Scoreboard = scoreboard.Scoreboard()

    screen.listen()
    screen.onkey(peddle_obj_r.move_up, "Up")
    screen.onkey(peddle_obj_r.move_down, "Down")
    screen.onkey(peddle_obj_l.move_up, "w")
    screen.onkey(peddle_obj_l.move_down, "s")

    game_is_on: bool = True
    while game_is_on:
        screen.update()
        ball_obj.move()

        # Detect collision with wall
        if ball_obj.ycor() > 280 or ball_obj.ycor() < -280:
            ball_obj.bounce_y()

        # Detect collision with peddle
        if not (-330 < ball_obj.xcor() < 330):
            if ball_obj.distance(peddle_obj_l) < 60 or ball_obj.distance(peddle_obj_r) < 60:
                ball_obj.bounce_x()

            # Detect right peddle misses
            if ball_obj.xcor() > 390:
                ball_obj.reset_position()
                scoreboard_obj.l_point()

            # Detect right peddle misses
            if ball_obj.xcor() < -390:
                ball_obj.reset_position()
                scoreboard_obj.r_point()

    screen.exitonclick()


if __name__ == '__main__':
    main()

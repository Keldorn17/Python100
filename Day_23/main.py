import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main() -> None:
    screen: Screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    scoreboard_obj: Scoreboard = Scoreboard()
    car_manager_obj: CarManager = CarManager(30)
    player_obj: Player = Player()

    screen.listen()
    screen.onkey(player_obj.move, "w")

    game_is_on: bool = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager_obj.move()

        for car in car_manager_obj.get_cars():
            if car.distance(player_obj) < 25:
                scoreboard_obj.game_over()
                game_is_on: bool = False

        if player_obj.check_finish_line():
            scoreboard_obj.increase_level()
            car_manager_obj.increase_speed()

    screen.exitonclick()


if __name__ == '__main__':
    main()

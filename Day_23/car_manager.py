from turtle import Turtle
import random

COLORS: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE: int = 5
MOVE_INCREMENT: int = 5


class CarManager:

    def __init__(self, amount_of_cars: int = 1):
        self.__car_list: list[Turtle] = [Turtle("square") for _ in range(amount_of_cars)]
        self.__define_car()
        self.__movement_speed: int = STARTING_MOVE_DISTANCE

    def __define_car(self) -> None:
        for car in self.__car_list:
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.__spawn(car)

    def move(self) -> None:
        for car in self.__car_list:
            car.goto(x=car.xcor() - self.__movement_speed, y=car.ycor())
            self.__check_respawn(car)

    def increase_speed(self) -> None:
        self.__movement_speed += MOVE_INCREMENT

    def __spawn(self, car_instance: Turtle) -> None:
        x_cord: float = random.randint(300, 1500)
        y_cord: float = random.randint(-220, 250)
        car_instance.goto(x_cord, y_cord)
        car_instance.color(random.choice(COLORS))

    def __check_respawn(self, car_instance: Turtle) -> None:
        if car_instance.xcor() < -320:
            self.__spawn(car_instance)

    def get_cars(self) -> list[Turtle]:
        return self.__car_list

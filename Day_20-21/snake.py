import turtle

MOVE_DISTANCE = 20
HEADINGS = {
    "up": 90,
    "down": 270,
    "left": 180,
    "right": 0
}


class Snake:

    def __init__(self, base_snake_length: int = 3) -> None:
        self.__base_snake_length = base_snake_length
        self.__segments: list[turtle.Turtle] = []
        self.__initialize_snake()
        self.__head = self.__segments[0]

    def __initialize_snake(self) -> None:  # Private function
        x_cord: int = 0
        for _ in range(self.__base_snake_length):
            self.__add_segment((x_cord, 0))
            x_cord -= MOVE_DISTANCE

    def __add_segment(self, position) -> None:
        segment = turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.__segments.append(segment)

    def extend(self):
        self.__add_segment(self.__segments[-1].position())

    def move(self) -> None:
        for seg_num in range(len(self.__segments) - 1, 0, -1):  # Start/Stop/Step
            new_x: float = self.__segments[seg_num - 1].xcor()
            new_y: float = self.__segments[seg_num - 1].ycor()
            self.__segments[seg_num].goto(new_x, new_y)
        self.__head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.__head.heading() != HEADINGS["down"]:
            self.__head.setheading(HEADINGS["up"])

    def down(self) -> None:
        if self.__head.heading() != HEADINGS["up"]:
            self.__head.setheading(HEADINGS["down"])

    def left(self) -> None:
        if self.__head.heading() != HEADINGS["right"]:
            self.__head.setheading(HEADINGS["left"])

    def right(self) -> None:
        if self.__head.heading() != HEADINGS["left"]:
            self.__head.setheading(HEADINGS["right"])

    def get_head(self) -> turtle.Turtle:
        return self.__head

    def get_segments(self) -> list[turtle.Turtle]:
        return self.__segments[1:]

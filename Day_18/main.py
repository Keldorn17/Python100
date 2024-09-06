import colorgram
import turtle
import random


def main() -> None:
    colors = colorgram.extract('image.jpg', 10)
    draw = turtle.Turtle()
    draw.speed(0)
    draw.hideturtle()
    screen = turtle.Screen()
    screen.colormode(255)
    turtle.bgcolor(colors[0].rgb)
    colors.remove(colors[0])

    draw.penup()
    draw.goto(-200, -200)
    draw.pendown()
    for _ in range(25):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.pencolor(random_color)
        draw.dot(50)
        draw.penup()
        draw.forward(100)
        draw.pendown()
        if draw.xcor() >= 300:
            draw.penup()
            draw.goto(-200, draw.ycor() + 100)
            draw.pendown()

    screen.exitonclick()


if __name__ == '__main__':
    main()

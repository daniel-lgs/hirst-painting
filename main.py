from data import rgb_colors
from turtle import Turtle, Screen, colormode
import random

my_arrow = Turtle()
my_arrow.hideturtle()
my_arrow.penup()
my_arrow.speed("fastest")
colormode(255)
step = 50
start_position = (-225, -225)
my_arrow.setposition(start_position)

for column in range(10):
    for row in range(10):
        my_arrow.dot(20, random.choice(rgb_colors))
        my_arrow.forward(step)
    my_arrow.setposition(start_position[0], my_arrow.position()[1] + step)

my_screen = Screen()
my_screen.exitonclick()

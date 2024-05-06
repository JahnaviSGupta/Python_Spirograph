import turtle
from turtle import Turtle,Screen
import random

def color():
    r= random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
turtle.colormode(255)
tim = Turtle()
screen = Screen()
tim.speed(0)
def gap(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

gap(10)
screen.exitonclick()
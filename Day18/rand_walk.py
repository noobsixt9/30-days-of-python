from turtle import Turtle,Screen, color
import random

from scipy import rand
colors = ("red","green","blue","yellow","blue","black","pink",)
direction = (0, 90, 180, 270)
my_turtle = Turtle()
my_turtle.pensize(15)
my_turtle.speed("fast")

def rand_walk():
    for _ in range(150):
        my_turtle.color(random.choice(colors))
        my_turtle.setheading(random.choice(direction))
        my_turtle.forward(50)
rand_walk()




screen = Screen()
screen.exitonclick()

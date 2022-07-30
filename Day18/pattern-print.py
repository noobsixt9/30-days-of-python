from turtle import Turtle,Screen
import random
colors = ("red","green","blue","yellow","blue","black","pink",)

my_turtle = Turtle()
my_turtle.pensize(3)

def draw(num_sides):
    angle = (360 / num_sides)
    for _ in range(num_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)
for side in range(3, 10):
    draw(side)
    my_turtle.color(random.choice(colors))




screen = Screen()
screen.exitonclick()

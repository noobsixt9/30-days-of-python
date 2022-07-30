import random
from turtle import Turtle,Screen
import turtle

color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
dot_num = 100

turtle.colormode(255)
my_turtle = Turtle()
my_turtle.hideturtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(350)
my_turtle.setheading(0)

for dot in range(1, dot_num+1):
    my_turtle.dot(20,random.choice(color_list))
    my_turtle.forward(50)
    if dot % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

screen = Screen()
screen.exitonclick()

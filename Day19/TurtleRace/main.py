from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
colors = ("red","yellow","green","pink","blue","black",)
y_position = [-100,-60,-20,20, 60, 100]

user_guess = screen.textinput(title="choose your turtle", prompt="Which turtle will win the race? make your bet: ")
all_turtles = []
screen.setup(width=500, height=400)
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("slow")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You have won! {winning_color} turtle won the race.")
            else:
                print(f"You have lost! {winning_color} turtle won the race.")

        rand_speed = random.randint(0, 10)
        turtle.forward(rand_speed)


screen.exitonclick()

from pickle import FALSE
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time


#creating background
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game V1.0")
screen.bgcolor("black")
screen.tracer(0)
is_game_on = True
#creating snake
snake = Snake()
food = Food()
score = Score()

#detecting key strokes
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh() 
        score.increase_score()
    if snake.head.xcor() > 297 or snake.head.xcor() < -297 or snake.head.ycor() > 297 or snake.head.ycor() < -297:
        score.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()

from turtle import Screen
from snake import Snake 
from food import Food
from scoreboard import scoreboard
import time
#creating background
screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(n=0)
is_game_on = True

#creating food and snake
snake = Snake() 
food = Food()
score_board = scoreboard()

#detecting keys
screen.listen()
screen.onkey(fun=snake.Up, key="Up")
screen.onkey(fun=snake.Down, key="Down")
screen.onkey(fun=snake.Left, key="Left")
screen.onkey(fun=snake.Right, key="Right")
while is_game_on: 
    screen.update()       
    time.sleep(0.1)
    #moving snake
    snake.MoveSnake()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
        #detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()
        is_game_on = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()
            is_game_on = False

        

screen.exitonclick()
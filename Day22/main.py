from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
game_on = True      
left = (-383, 0)
right = (383, 0)
screen.tracer(0)


paddle1 = Paddle(right)
paddle2 = Paddle(left)
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

while game_on:
    time.sleep(ball.fast)
    screen.update()
    ball.MoveBall()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.Bounce_y()
    if ball.distance(paddle1) < 50 and ball.xcor() > 365 or ball.distance(paddle2) < 50 and ball.xcor() < -365:
        ball.Bounce_x()
    elif ball.xcor() > 400:
        score.paddleOne_score()
        ball.Reset()
    elif ball.xcor() < -400:
        score.paddleTwo_score()
        ball.Reset()

screen.exitonclick()
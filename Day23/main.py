import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
game_is_on = True

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(fun=player.MoveTurtle, key="Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

        if player.is_finised():
            player.goto_start()
            car_manager.level_up()
            score_board.increase_level()

screen.exitonclick()
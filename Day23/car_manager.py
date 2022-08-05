from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
X_COR = 320

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_choice = random.randint(1, 6)
        if rand_choice == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            rand_y = random.randint(-250, 250)
            new_car.goto(x=X_COR, y=rand_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
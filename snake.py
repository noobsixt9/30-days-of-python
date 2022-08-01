from turtle import Screen, Turtle, shape
import time
is_game_on = True
POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE = 20   
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.CreateSnake()
        self.head = self.segments[0]

    def CreateSnake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def MoveSnake(self):
            for seg in range(len(self.segments)-1, 0, -1):
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(x=new_x, y=new_y)
            self.head.forward(MOVE)

    def add_segment(self, position):
            square = Turtle(shape="square")
            square.speed("slowest")
            square.color("white")
            square.penup()
            square.goto(position)
            self.segments.append(square)

    def extend(self):
        self.add_segment(self.segments[-1].position())
            
    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
 
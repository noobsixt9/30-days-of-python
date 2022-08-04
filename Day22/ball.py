from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        self.fast = 0.1

    def MoveBall(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.penup()
        self.goto(new_x, new_y)

    def Bounce_y(self):
        self.y_move *= -1
    
    def Bounce_x(self):
        self.x_move *= -1
        self.fast *= 0.9

    def Reset(self):
        self.goto(x=0, y=0)
        self.fast = 0.1
        self.x_move *= -1
        
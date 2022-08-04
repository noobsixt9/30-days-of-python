from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white") 
        self.penup()
        self.hideturtle()
        self.paddle1_score = 0
        self.paddle2_score = 0
        self.UpdateScore()
        
    def UpdateScore(self):
        self.goto(x=-100, y=230)
        self.write(self.paddle1_score, align="left",font=("courier",40,"normal"))
        self.goto(x=100, y=230)
        self.write(self.paddle2_score, align="left",font=("courier",40,"normal"))

    def paddleOne_score(self):
        self.clear()
        self.paddle1_score += 1
        self.UpdateScore()
    def paddleTwo_score(self):
        self.clear()
        self.paddle2_score += 1
        self.UpdateScore()
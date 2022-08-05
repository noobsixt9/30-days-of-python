from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=260)
        self.upadte_level()
       
    def upadte_level(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.upadte_level()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER",align="center", font=FONT)
    
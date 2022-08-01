from turtle import Turtle, goto
ALIGN = "center"
FONT = ('courier',15,'normal')
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score: {self.score}",align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(f"GAME OVER",align=ALIGN, font=FONT)
        self.goto(x=0, y= -30)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
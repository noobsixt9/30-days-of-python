import turtle
import pandas
FONT = ('',10,'normal')

screen = turtle.Screen()
screen.title("Nepal Province Quiz")
image = "nepal.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("province.csv")
province_name = data["province"].to_list()
guessed_province = []

while len(guessed_province) < 7:
    answer = screen.textinput(title=f"{len(guessed_province)}/7 Province Correct", prompt="What's another province name?").title()
    if answer == "Exit":
        missing_province = []
        for province in province_name:
            if province not in guessed_province:
                missing_province.append(province)
        new_data = pandas.DataFrame(missing_province)
        new_data.to_csv("province_to_learn.csv")
        break
    if answer in province_name:
        t = turtle.Turtle()
        guessed_province.append(answer)
        t.hideturtle()
        t.penup()
        state_data = data[data.province == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer, font=FONT)

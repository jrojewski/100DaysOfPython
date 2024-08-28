print("---POLAND VOIVODESHIPS GAME---")

import turtle
import pandas
from tkinter import messagebox

screen = turtle.Screen()
screen.title("Poland Voivodeships Game")
image = "blank_voivodeships_img.gif"
#source: https://simplemaps.com/static/svg/country/pl/admin1/pl.svg
screen.addshape(image)
turtle.shape(image)

###
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
###

data = pandas.read_csv("16_voivodeships.csv")
all_voivodeships = data.voivodeship.to_list()
guessed_voivodeships = []

while len(guessed_voivodeships) < 16:
    answer_voivodeship = screen.textinput(title=f"{len(guessed_voivodeships)}/{len(all_voivodeships)} voivodeships Correct",
                                    prompt="What's another voivodeship's name?").title()
    if answer_voivodeship == "Exit":
        missing_voivodeships = []
        for voivodeship in all_voivodeships:
            if voivodeship not in guessed_voivodeships:
                missing_voivodeships.append(voivodeship)
        new_data = pandas.DataFrame(missing_voivodeships)
        new_data.to_csv("voivodeships_to_learn.csv")
        break
    if answer_voivodeship in all_voivodeships and answer_voivodeship not in guessed_voivodeships:
        guessed_voivodeships.append(answer_voivodeship)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        voivodeship_data = data[data.voivodeship == answer_voivodeship]
        t.goto(voivodeship_data.x.item(), voivodeship_data.y.item())
        t.write(answer_voivodeship)

if len(guessed_voivodeships) == len(all_voivodeships):
    messagebox.showinfo("Info", "Congratulations!")
else:
    messagebox.showinfo("Info", "Keep learning!")

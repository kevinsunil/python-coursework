import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
correct_guesses = 0
wrong_answer = 0
already_guessed_state = []
state_to_learn = []

data = pandas.read_csv("50_states.csv")
all_state_list = data.state.to_list()
game_over = False

while not game_over:
    answer_state = screen.textinput(title=f'{correct_guesses}/50 Guess the state', prompt='Write your answer')
    answer_state = answer_state.title()
    if answer_state in all_state_list:
        if answer_state in already_guessed_state:
            pass
        else:
            temp = turtle.Turtle()
            temp.hideturtle()
            temp.penup()
            correct_guesses += 1
            state_data = data[data["state"] == answer_state]
            x_corr = state_data["x"].to_list()
            y_corr = state_data["y"].to_list()
            temp.goto(x_corr[0], y_corr[0])
            temp.write(answer_state, align='center', font=("Courier", 10, "normal"))
            already_guessed_state.append(answer_state)
    else:
        wrong_answer += 1
    if wrong_answer == 3:
        game_over = True

for state in all_state_list:
    if state in already_guessed_state:
        pass
    else:
        state_to_learn.append(state)
df = pandas.DataFrame(state_to_learn)
df.to_csv("States_toLearn.csv")
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
screen.exitonclick()

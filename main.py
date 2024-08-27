import turtle
import pandas
import answer
import scoreboard

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
answer = answer.Answer()
scoreboard = scoreboard.Scoreboard()
is_game_on = True
answered = []

# while is_game_on:
#     answer_state = screen.textinput(f"{scoreboard.score}/50 States Correct", "What's another state's name?")
#     data = pandas.read_csv("50_states.csv")
#     exist = answer_state in data["state"].values
#     if answer_state in answered:
#         pass
#
#     elif exist:
#         answer_xco = int(data.iloc[data[data["state"] == answer_state].index, 1])
#         answer_yco = int(data.iloc[data[data["state"] == answer_state].index, 2])
#         answer.answer_write(answer_state, answer_xco, answer_yco)
#         scoreboard.score_check()
#         answered.append(answer_state)
#
#     elif scoreboard.score == 50:
#         is_game_on = False

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state =[]

while len(guessed_state) < 50:
    answer_state = screen.textinput(f"{len(guessed_state)}/50 States Correct",
                                    "What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in guessed_state:
        pass
    elif answer_state in all_state:
        guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        answer.answer_write(answer_state, state_data.x.item(), state_data.y.item())


turtle.mainloop()

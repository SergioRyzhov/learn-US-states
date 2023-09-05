import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(height=491, width=725)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()


def draw(answer):
    row = states_data[states_data.state == answer.capitalize()]
    cor_x = row.x.item()
    cor_y = row.y.item()
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(cor_x, cor_y)
    turtle.write(answer_state.capitalize(), move=False, align='left', font=('Arial', 8, 'normal'))
    turtle.goto(0, 0)


game_is_on = True
guess_count = 0
list_of_guesses = []
while game_is_on:
    answer_state = screen.textinput(title=f"{guess_count}/50 States Correct", prompt="What's another state's name?")
    if answer_state.lower() == "exit":
        break
    if answer_state and answer_state.capitalize() in states_list:
        guess_count += 1
        draw(answer_state)
        list_of_guesses.append(answer_state.capitalize())
    if len(list_of_guesses) >= 50:
        game_is_on = False

# states to learn.csv
learn_list = list(set(states_list) - set(list_of_guesses))
file = pandas.DataFrame(learn_list)
file.to_csv("states_to_learn.csv")


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.color('black')
tim.speed('fastest')

# como ao clicar em um ponto do mapa, definir as coordenadas daquele ponto
# base para gerar o arquivo 50_states.csv

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv('50_states.csv')
states_list = data['state'].to_list()
correct_guesses = []

while True:
    answer_state = screen.textinput(title=f'{len(correct_guesses)}/50 States Correct',
                                    prompt="What's another State's name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in states_list if state not in correct_guesses]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv('states_to_learn.csv')
        break
    if answer_state in states_list:
        state_info = data[data.state == answer_state]
        state_xcor = int(state_info['x'].iloc[0])
        state_ycor = int(state_info['y'].iloc[0])
        tim.goto(state_xcor, state_ycor)
        tim.write(f'{answer_state}', align='center', font=('courier', 10, 'normal'))
        correct_guesses.append(answer_state)
    if len(correct_guesses) == 50:
        break

# screen.exitonclick()

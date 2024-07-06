import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv('50_states.csv')
guessed_states = []
all_states = data['state'].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv('states_to_learn.csv')
        
        break

    
    if data['state'].isin([answer_state]).any():
        state_data = data[data['state'] == answer_state]
        guessed_states.append(answer_state)
        
        x_coor = int(state_data['x'])
        y_coor = int(state_data['y'])
        print(f'{x_coor}, {y_coor}')

        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state.goto(x_coor, y_coor)
        state.write(answer_state)
    else:
        pass


if len(guessed_states) == 50:
    state.goto(0, 0)
    state.write('You win!')

  
screen.exitonclick()
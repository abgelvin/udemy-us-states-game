import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

correct = 0

while correct < 50:
    answer_state = screen.textinput(title=f'{correct}/50 States Correct', prompt="What's another state's name?").title()

    data = pandas.read_csv('50_states.csv')
    if data['state'].isin([answer_state]).any():
        answer = data[data['state'] == answer_state]
        x_coor = int(answer['x'])
        y_coor = int(answer['y'])
        print(f'{x_coor}, {y_coor}')

        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state.goto(x_coor, y_coor)
        state.write(answer_state)
        correct += 1
    else:
        pass

state.goto(0, 0)
state.write('You win!')

# turtle.mainloop()



screen.exitonclick()
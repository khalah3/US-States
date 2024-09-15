import turtle
import pandas

screen = turtle.Screen()
screen.title("US. States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    input_state_data = screen.textinput(title=f"{len(guessed_states)}/"
                                              f"50 States guessed",prompt="Guess a state in US").title()

    if input_state_data == "Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        unguessed_state = pandas.DataFrame(missing_states)
        unguessed_state.to_csv("non-guessed-states.csv")
        break

    if input_state_data in all_states:
        guessed_states.append(input_state_data)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == input_state_data]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(input_state_data)








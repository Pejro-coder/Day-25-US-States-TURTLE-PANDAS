import turtle
import pandas as pd
from state import StateName

# Load states data
states_data = pd.read_csv("50_states.csv")

# Get the states into a list
states = states_data["state"].to_list()
print(states)

# Initialize the Turtle screen
screen = turtle.Screen()

# Position the Turtle screen using `setup()`
screen.setup(width=745, height=511, startx=2500, starty=-200)

# Add background image
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

guesses = 0
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{guesses}/50", "Your guess:").title()

    if answer_state in states and answer_state not in guessed_states:
        state_data = states_data[states_data.state == answer_state]
        print(state_data)
        state_x = state_data.x.item()
        state_y = state_data.y.item()

        state = StateName(answer_state)
        state.add_state(state_x, state_y)
        guessed_states.append(answer_state)
        guesses += 1

    # screen.exitonclick()
# turtle.mainloop()

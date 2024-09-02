from turtle import Turtle


class StateName:
    def __init__(self, state):
        self.state = state

    def add_state(self, x, y):
        new_state = Turtle()
        new_state.penup()
        new_state.hideturtle()
        # new_state.color("yellow")
        new_state.goto(x, y)
        new_state.write(arg=self.state, move=False, align="center", font=("Arial", 10, "bold"))

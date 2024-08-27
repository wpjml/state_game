import turtle


class Answer(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def answer_write(self, answer_state, x, y):
        self.goto(x, y)
        self.write(answer_state, align="center", font=("Courier", 10, "normal"))

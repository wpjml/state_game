import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()

    def score_check(self):
        self.score += 1



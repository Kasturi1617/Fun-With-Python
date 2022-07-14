from turtle import Turtle
FONT = ("Courier", 25, "normal")


class Score(Turtle):

    def __init__(self, new_x, new_y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(new_x, new_y)
        self.write(self.score, align="center", font=FONT)

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=FONT)
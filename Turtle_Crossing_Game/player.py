from turtle import Turtle
STARTING_POS = (0,-250)
FORWARD = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POS)
        self.setheading(90)

    def go_up(self):
        self.forward(FORWARD)

    def isAtFinishLine(self):
        if self.ycor() >= 280:
            return True
        else:
            return False

    def gotoStart(self):
        self.goto(STARTING_POS)

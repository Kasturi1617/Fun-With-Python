from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("blue")
        self.goto(0, 250)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
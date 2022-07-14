from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-150, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")

        self.goto(200, 270)
        self.write(f"High score: {self.high_score}", align="right", font=FONT)

    def increase_score(self):
        self.score += 5
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 24, "normal"))

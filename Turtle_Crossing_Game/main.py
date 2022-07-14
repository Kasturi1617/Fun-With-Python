from turtle import Turtle, Screen
from player import Player
from car import Car
from score import Score
import time

screen = Screen()
screen.setup(width=700, height=600)
screen.tracer(0)

timmy = Player()
myCar = Car()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=timmy.go_up)

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    myCar.create_car()
    myCar.move_car()

    # Detect collision with car:
    for car in myCar.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            score.game_over()

    # Detect player successful crossing
    if timmy.isAtFinishLine():
        timmy.gotoStart()
        myCar.level_up()
        score.increase_level()

screen.exitonclick()